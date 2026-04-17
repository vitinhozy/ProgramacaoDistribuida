📊 Sistema de Metas Jurisdicionais

Este projeto em Python tem como objetivo processar arquivos CSV contendo dados jurisdicionais, permitindo análises como consolidação, cálculo de metas, ranking de tribunais e filtragem por município.

🚀 Funcionalidades

O sistema oferece um menu interativo com as seguintes opções:

1. 📁 Concatenar arquivos
Junta múltiplos arquivos CSV (teste_TRE*.csv) em um único arquivo
Gera o arquivo:
concatenado.csv
2. 🏙️ Resumo por Municípios
Agrupa os dados por município (municipio_oj)
Calcula métricas e metas jurisdicionais
Gera o arquivo:
resumo_municipios.csv
3. 🏛️ Top 10 Tribunais
Agrupa por tribunal (sigla_tribunal)
Calcula as metas
Ordena pelo melhor desempenho na Meta 1
Gera o arquivo:
top_10_tribunais.csv
4. 🔍 Filtro por Município
Permite buscar dados de um município específico
Possui sistema de sugestão inteligente (busca parcial)
Gera um arquivo com o nome do município:
Exemplo: BRASILIA.csv
⚙️ Tecnologias Utilizadas
Python 3
Pandas
Glob
Concurrent Futures (ThreadPool e ProcessPool)
🧠 Lógica das Metas

As metas são calculadas com base em fórmulas específicas:

Meta 1
Meta 2A
Meta 2 Antigas
Meta 4A
Meta 4B

O sistema utiliza uma função de divisão segura para evitar erro de divisão por zero:

def divisao_segura(numerador, denominador, multiplicador=100):
    if denominador != 0:
        return (numerador / denominador) * multiplicador
    return 0
⚡ Processamento Paralelo

O sistema permite execução em dois modos:

Serial → processamento normal
Paralelo → usando:
ThreadPoolExecutor (I/O – leitura de arquivos)
ProcessPoolExecutor (CPU – cálculos e agrupamentos)

Ao final de cada operação, é exibido o ganho de performance (speedup).

📂 Estrutura Esperada

Coloque os arquivos CSV na mesma pasta do script com o seguinte padrão:

teste_TRE1.csv
teste_TRE2.csv
teste_TRE3.csv
...
▶️ Como Executar
Instale as dependências:
pip install pandas
Execute o script:
python nome_do_script.py
Escolha uma opção no menu:
1 - Concatenar arquivos
2 - Resumo por municípios
3 - Top 10 tribunais
4 - Filtrar município
0 - Sair
⚠️ Observações Importantes
Os nomes dos municípios são normalizados para maiúsculo e sem espaços extras
A busca por município exige correspondência exata, mas oferece sugestões
Apenas arquivos com padrão teste_TRE*.csv são considerados
Certifique-se de que os CSVs possuem as colunas esperadas
🛠️ Possíveis Melhorias
Substituir .apply() por operações vetorizadas (melhor performance)
Interface gráfica (GUI)
Exportação para Excel
Logs de execução
Testes automatizados
👨‍💻 Autor

Desenvolvido para processamento e análise de metas jurisdicionais com foco em desempenho e paralelismo.
