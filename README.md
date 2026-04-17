📊 Sistema de Metas Jurisdicionais

Este projeto em Python tem como objetivo processar arquivos CSV contendo dados jurisdicionais, permitindo análises como consolidação, cálculo de metas, ranking de tribunais e filtragem por município.

🚀 Funcionalidades
📁 1. Concatenar arquivos
Junta múltiplos arquivos CSV (teste_TRE*.csv)
Gera:
concatenado.csv
🏙️ 2. Resumo por Municípios
Agrupa por municipio_oj
Calcula metas jurisdicionais
Gera:
resumo_municipios.csv
🏛️ 3. Top 10 Tribunais
Agrupa por sigla_tribunal
Ordena pela Meta 1
Gera:
top_10_tribunais.csv
🔍 4. Filtro por Município
Filtra dados de um município específico
Possui sugestão inteligente (busca parcial)
Gera:
NOME_DO_MUNICIPIO.csv
⚙️ Tecnologias Utilizadas
Python 3
Pandas
Glob
Concurrent Futures (ThreadPoolExecutor e ProcessPoolExecutor)
🧠 Lógica das Metas

O sistema utiliza divisão segura para evitar erros:

def divisao_segura(numerador, denominador, multiplicador=100):
    if denominador != 0:
        return (numerador / denominador) * multiplicador
    return 0

Metas calculadas:

Meta1
Meta2A
Meta2Ant
Meta4A
Meta4B
⚡ Processamento Paralelo

O sistema pode executar em dois modos:

Serial → execução padrão
Paralelo → utilizando:
ThreadPoolExecutor (leitura de arquivos)
ProcessPoolExecutor (processamento de dados)

O ganho de desempenho (speedup) é exibido ao final de cada operação.

📂 Estrutura Esperada

Os arquivos devem estar na mesma pasta do script:

teste_TRE1.csv
teste_TRE2.csv
teste_TRE3.csv
▶️ Como Executar
1. Instalar dependências
pip install pandas
2. Executar o projeto
python nome_do_script.py
3. Menu do sistema
1 - Concatenar arquivos
2 - Resumo por municípios
3 - Top 10 tribunais
4 - Filtrar município
0 - Sair
⚠️ Observações
Os municípios são normalizados (maiúsculo e sem espaços extras)
A busca exige correspondência exata, mas sugere resultados similares
Apenas arquivos teste_TRE*.csv são processados
Certifique-se de que os CSVs possuem as colunas esperadas
🛠️ Melhorias Futuras
Otimização (remoção de .apply() → uso vetorizado)
Interface gráfica (GUI)
Exportação para Excel
Sistema de logs
Testes automatizados
👨‍💻 Autor

Projeto desenvolvido para análise de metas jurisdicionais com foco em performance e paralelismo.

Se quiser dar um nível a mais (estilo GitHub top), posso incluir:

badges (Python, status, etc.)
GIF de demonstração
exemplos reais de entrada/saída
ou até estruturar como projeto open source 👍
