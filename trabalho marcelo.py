import pandas as pd
import glob
import time
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def ler_csv(caminho):
    return pd.read_csv(caminho)

def divisao_segura(numerador, denominador, multiplicador=100):
    if denominador != 0:
        return (numerador / denominador) * multiplicador
    return 0

def calcular_metas_finais(df):
    df = df.copy()

    df["Meta1"] = df.apply(lambda r: divisao_segura(r["julgados_2026"], r["casos_novos_2026"] + r["dessobrestados_2026"] - r["suspensos_2026"]), axis=1)
    df["Meta2A"] = df.apply(lambda r: divisao_segura(r["julgm2_a"], r["distm2_a"] - r["suspm2_a"], 1000 / 7), axis=1)
    df["Meta2Ant"] = df.apply(lambda r: divisao_segura(r["julgm2_ant"], r["distm2_ant"] - r["suspm2_ant"] - r["desom2_ant"]), axis=1)
    df["Meta4A"] = df.apply(lambda r: divisao_segura(r["julgm4_a"], r["distm4_a"] - r["suspm4_a"]), axis=1)
    df["Meta4B"] = df.apply(lambda r: divisao_segura(r["julgm4_b"], r["distm4_b"] - r["suspm4_b"]), axis=1)

    return df

def map_municipio(chunk):
    return chunk.groupby("municipio_oj").sum(numeric_only=True)

def map_tribunal(chunk):
    return chunk.groupby("sigla_tribunal").sum(numeric_only=True)

def map_filtro(args):
    chunk, municipio = args
    return chunk[chunk["municipio_oj"] == municipio]

def concatenar_arquivos(arquivos, modo="serial"):
    if modo == "serial":
        dfs = [ler_csv(a) for a in arquivos]
    else:
        with ThreadPoolExecutor() as executor:
            dfs = list(executor.map(ler_csv, arquivos))

    df = pd.concat(dfs, ignore_index=True)
    df.to_csv("concatenado.csv", index=False, encoding='utf-8-sig')
    return df

def resumo_municipios(df, modo="serial", workers=4):
    if modo == "serial":
        bruto = df.groupby("municipio_oj").sum(numeric_only=True).reset_index()
    else:
        chunks = [df.iloc[i::workers] for i in range(workers)]
        with ProcessPoolExecutor(workers) as executor:
            partes = list(executor.map(map_municipio, chunks))
        bruto = pd.concat(partes).groupby("municipio_oj").sum().reset_index()

    final = calcular_metas_finais(bruto)
    colunas = ["municipio_oj", "julgados_2026", "Meta1", "Meta2A", "Meta2Ant", "Meta4A", "Meta4B"]
    final = final[colunas]
    final.to_csv("resumo_municipios.csv", index=False, encoding='utf-8-sig')
    return final

def top_10_tribunais(df, modo="serial", workers=4):
    if modo == "serial":
        bruto = df.groupby("sigla_tribunal").sum(numeric_only=True).reset_index()
    else:
        chunks = [df.iloc[i::workers] for i in range(workers)]
        with ProcessPoolExecutor(workers) as executor:
            partes = list(executor.map(map_tribunal, chunks))
        bruto = pd.concat(partes).groupby("sigla_tribunal").sum().reset_index()

    final = calcular_metas_finais(bruto)
    top10 = final.sort_values("Meta1", ascending=False).head(10)
    colunas = ["sigla_tribunal", "Meta1", "Meta2A", "Meta2Ant", "Meta4A", "Meta4B"]
    top10 = top10[colunas]
    top10.to_csv("top_10_tribunais.csv", index=False, encoding='utf-8-sig')
    return top10

def filtrar_municipio(df, municipio, modo="serial", workers=4):
    if modo == "serial":
        resultado = df[df["municipio_oj"] == municipio]
    else:
        chunks = [df.iloc[i::workers] for i in range(workers)]
        args = [(c, municipio) for c in chunks]
        with ProcessPoolExecutor(workers) as executor:
            partes = list(executor.map(map_filtro, args))
        resultado = pd.concat(partes)

    resultado.to_csv(f"{municipio}.csv", index=False, encoding='utf-8-sig')
    return resultado

if __name__ == "__main__":
    pasta_script = os.path.dirname(os.path.abspath(__file__))
    os.chdir(pasta_script)
    
    padrao = os.path.join(pasta_script, "teste_TRE*.csv")
    arquivos = glob.glob(padrao)

    if not arquivos:
        print(f"\n[!] Erro: Nenhum ficheiro original 'teste_TRE' encontrado em: {pasta_script}")
        exit()

    print(f"[+] Foram encontrados {len(arquivos)} ficheiros originais. A carregar base...")
    df_base = concatenar_arquivos(arquivos, "serial") 

    df_base["municipio_oj"] = df_base["municipio_oj"].astype(str).str.strip().str.upper()

    while True:
        print("\n" + "="*40)
        print(" SISTEMA DE METAS JURISDICIONAIS ")
        print("="*40)
        print("1 - Gerar Ficheiro Concatenado (.csv)")
        print("2 - Gerar Resumo por Municípios")
        print("3 - Gerar Top 10 Tribunais")
        print("4 - Filtrar por Município Específico")
        print("0 - Sair")
        print("="*40)
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nProcessando...")
            t0 = time.time(); concatenar_arquivos(arquivos, "serial"); t1 = time.time() - t0
            t0 = time.time(); concatenar_arquivos(arquivos, "paralelo"); t2 = time.time() - t0

            speedup = t1/t2 if t2 > 0 else 0
            print(f"> Tempo Serial: {t1:.4f}s")
            print(f"> Tempo Paralelo: {t2:.4f}s")
            print(f"> Speedup: {speedup:.2f}x")

        elif opcao == "2":
            print("\nProcessando...")
            t0 = time.time(); resumo_municipios(df_base, "serial"); t1 = time.time() - t0
            t0 = time.time(); resumo_municipios(df_base, "paralelo"); t2 = time.time() - t0

            speedup = t1/t2 if t2 > 0 else 0
            print(f"> Tempo Serial: {t1:.4f}s")
            print(f"> Tempo Paralelo: {t2:.4f}s")
            print(f"> Speedup: {speedup:.2f}x")

        elif opcao == "3":
            print("\nProcessando...")
            t0 = time.time(); top_10_tribunais(df_base, "serial"); t1 = time.time() - t0
            t0 = time.time(); top_10_tribunais(df_base, "paralelo"); t2 = time.time() - t0

            speedup = t1/t2 if t2 > 0 else 0
            print(f"> Tempo Serial: {t1:.4f}s")
            print(f"> Tempo Paralelo: {t2:.4f}s")
            print(f"> Speedup: {speedup:.2f}x")

        elif opcao == "4":
            cidade = input("\nDigite o nome do município: ").strip().upper()
            
            if cidade not in df_base["municipio_oj"].values:
                sugestoes = df_base.loc[df_base["municipio_oj"].str.contains(cidade, na=False), "municipio_oj"].unique()
                
                if len(sugestoes) > 0:
                    print(f"\n[!] O município '{cidade}' não foi encontrado. Você quis dizer algum destes?")
                    for s in sugestoes[:5]: 
                        print(f" -> {s}")
                    print("Dica: Copie o nome exatamente como aparece acima (com acentos) e tente novamente.")
                else:
                    print(f"\n[!] Aviso: Nenhuma cidade foi encontrada com '{cidade}'.")
                continue 
                
            print(f"A filtrar por '{cidade}'...")
            t0 = time.time(); filtrar_municipio(df_base, cidade, "serial"); t1 = time.time() - t0
            t0 = time.time(); filtrar_municipio(df_base, cidade, "paralelo"); t2 = time.time() - t0

            speedup = t1/t2 if t2 > 0 else 0
            print(f"> Tempo Serial: {t1:.4f}s")
            print(f"> Tempo Paralelo: {t2:.4f}s")
            print(f"> Speedup: {speedup:.2f}x")

        elif opcao == "0":
            print("\nA encerrar o sistema...")
            break
        else:
            print("\n[!] Opção inválida.")