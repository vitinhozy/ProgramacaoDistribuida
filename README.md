<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Sistema de Metas Jurisdicionais</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            line-height: 1.6;
            background-color: #f8f9fa;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        code {
            background-color: #eaeaea;
            padding: 3px 6px;
            border-radius: 4px;
        }
        pre {
            background-color: #eaeaea;
            padding: 10px;
            border-radius: 6px;
            overflow-x: auto;
        }
        .container {
            max-width: 900px;
            margin: auto;
            background: #fff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
        }
        ul {
            margin-left: 20px;
        }
        .tag {
            display: inline-block;
            background: #3498db;
            color: white;
            padding: 3px 8px;
            border-radius: 5px;
            font-size: 12px;
        }
    </style>
</head>
<body>

<div class="container">

    <h1>📊 Sistema de Metas Jurisdicionais</h1>

    <p>
        Este projeto em Python tem como objetivo processar arquivos CSV contendo dados jurisdicionais,
        permitindo análises como consolidação, cálculo de metas, ranking de tribunais e filtragem por município.
    </p>

    <h2>🚀 Funcionalidades</h2>

    <h3>1. 📁 Concatenar arquivos</h3>
    <ul>
        <li>Junta múltiplos arquivos CSV (<code>teste_TRE*.csv</code>)</li>
        <li>Gera: <code>concatenado.csv</code></li>
    </ul>

    <h3>2. 🏙️ Resumo por Municípios</h3>
    <ul>
        <li>Agrupa por <code>municipio_oj</code></li>
        <li>Calcula metas jurisdicionais</li>
        <li>Gera: <code>resumo_municipios.csv</code></li>
    </ul>

    <h3>3. 🏛️ Top 10 Tribunais</h3>
    <ul>
        <li>Agrupa por <code>sigla_tribunal</code></li>
        <li>Ordena pela Meta 1</li>
        <li>Gera: <code>top_10_tribunais.csv</code></li>
    </ul>

    <h3>4. 🔍 Filtro por Município</h3>
    <ul>
        <li>Busca município específico</li>
        <li>Inclui sugestões inteligentes</li>
        <li>Gera arquivo com nome do município</li>
    </ul>

    <h2>⚙️ Tecnologias</h2>
    <ul>
        <li><span class="tag">Python 3</span></li>
        <li><span class="tag">Pandas</span></li>
        <li><span class="tag">Glob</span></li>
        <li><span class="tag">Concurrent Futures</span></li>
    </ul>

    <h2>🧠 Lógica das Metas</h2>
    <p>O sistema utiliza divisão segura para evitar erro de divisão por zero:</p>

    <pre><code>
def divisao_segura(numerador, denominador, multiplicador=100):
    if denominador != 0:
        return (numerador / denominador) * multiplicador
    return 0
    </code></pre>

    <h2>⚡ Processamento Paralelo</h2>
    <p>O sistema pode rodar em dois modos:</p>
    <ul>
        <li><b>Serial</b> → execução normal</li>
        <li><b>Paralelo</b> → usando threads e processos</li>
    </ul>

    <h2>📂 Estrutura Esperada</h2>
    <pre><code>
teste_TRE1.csv
teste_TRE2.csv
teste_TRE3.csv
    </code></pre>

    <h2>▶️ Como Executar</h2>
    <pre><code>
pip install pandas
python nome_do_script.py
    </code></pre>

    <h2>⚠️ Observações</h2>
    <ul>
        <li>Os municípios são convertidos para maiúsculo</li>
        <li>Busca com sugestões inteligentes</li>
        <li>Apenas arquivos <code>teste_TRE*.csv</code> são usados</li>
    </ul>

    <h2>🛠️ Melhorias Futuras</h2>
    <ul>
        <li>Otimização de performance</li>
        <li>Interface gráfica</li>
        <li>Exportação para Excel</li>
        <li>Logs</li>
    </ul>

    <h2>👨‍💻 Autor</h2>
    <p>Projeto desenvolvido para análise de metas jurisdicionais com foco em desempenho.</p>

</div>

</body>
</html>
