# 📊 SalesTrack | Sistema de Análise de Vendas


\


**SalesTrack** é uma aplicação desenvolvida em Python para registrar vendas, calcular indicadores comerciais e apresentar informações relevantes sobre o desempenho de vendas por meio de uma interface interativa no terminal.

O projeto foi criado com o objetivo de aplicar fundamentos de programação na resolução de um problema prático, explorando conceitos essenciais para o desenvolvimento de software e a análise de dados.

---

## 🎯 Objetivo do projeto

Pequenos negócios precisam acompanhar seus resultados comerciais para compreender o desempenho de suas operações.

O SalesTrack apresenta uma solução inicial para esse cenário, permitindo registrar valores de vendas e obter indicadores como faturamento acumulado, ticket médio e identificação de vendas acima da média.

Além da aplicação prática, o projeto faz parte de uma jornada de desenvolvimento de competências em **Python, lógica de programação e análise de dados**.

## 🚀 Funcionalidades

| Funcionalidade            | Descrição                                         |
| ------------------------- | ------------------------------------------------- |
| 🛒 Registro de vendas     | Cadastro de valores de vendas pelo usuário        |
| 🛡️ Validação de dados    | Impede o cadastro de valores negativos            |
| 💰 Faturamento total      | Calcula o valor acumulado das vendas              |
| 📊 Média de vendas        | Calcula o valor médio das vendas registradas      |
| 📈 Maior e menor venda    | Identifica os valores extremos                    |
| 🔎 Análise acima da média | Identifica vendas superiores à média geral        |
| 🖥️ Menu interativo       | Permite acessar as funcionalidades pelo terminal  |
| 🔄 Cadastro acumulativo   | Permite adicionar novas vendas durante a execução |

## 🖥️ Demonstração

Exemplo ilustrativo de utilização do sistema:

```text
========== SALESTRACK ==========

Sistema de Análise de Vendas

========== MENU PRINCIPAL ==========

1 - Registrar vendas
2 - Consultar faturamento
3 - Consultar média de vendas
4 - Consultar maior e menor venda
5 - Consultar vendas acima da média
6 - Sair

Digite a opção desejada: 1

Digite o valor da venda: 150
Digite o valor da venda: 350
Digite o valor da venda: 500
Digite o valor da venda: 200
Digite o valor da venda: 800

Vendas registradas com sucesso!
```

Exemplo de indicadores calculados:

```text
Faturamento total: R$ 2000.00
Média de vendas: R$ 400.00
Maior venda: R$ 800.00
Menor venda: R$ 150.00

Vendas acima da média: [500.0, 800.0]
```

*Os valores apresentados são fictícios e demonstram os cálculos realizados pela aplicação.*

## 🛠️ Tecnologias utilizadas

**Python 3** — linguagem utilizada para implementar as funcionalidades e realizar os cálculos.

**Visual Studio Code** — ambiente de desenvolvimento utilizado na construção do projeto.

**Git e GitHub** — ferramentas utilizadas para versionamento e publicação do código-fonte.

### Conceitos aplicados

- Estruturas condicionais (`if`, `elif`, `else`)
- Estruturas de repetição (`for`, `while`)
- Listas e manipulação de elementos
- List comprehension
- Entrada e validação de dados
- Funções nativas (`sum`, `len`, `max`, `min`)
- Operações matemáticas e cálculos de indicadores
- Formatação de saídas com f-strings

## 📁 Estrutura do projeto

```text
salestrack-python/
│
├── main.py
└── README.md
```

O arquivo `main.py` contém a implementação do sistema, enquanto o `README.md` apresenta sua documentação.

## ⚙️ Como executar

### Pré-requisitos

- Python 3 instalado
- Terminal ou editor de código

### Execução

**1.** Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/salestrack-python.git
```

**2.** Acesse a pasta do projeto:

```bash
cd salestrack-python
```

**3.** Execute o programa:

```bash
python main.py
```

No Windows, dependendo da configuração, também é possível executar utilizando `py main.py`.

O sistema será iniciado no terminal, exibindo o menu principal.

## 📐 Indicadores analisados

**Faturamento total**

Representa a soma dos valores de todas as vendas cadastradas.

**Ticket médio**

Representa o faturamento total dividido pela quantidade de vendas registradas.

**Maior e menor venda**

Permitem identificar os valores extremos do conjunto de vendas.

**Vendas acima da média**

Permitem identificar transações com valores superiores ao ticket médio, oferecendo uma visão inicial da distribuição dos valores comerciais.

## 🧠 Aprendizados

O desenvolvimento do SalesTrack proporcionou a aplicação prática de fundamentos de Python, especialmente na construção de fluxos interativos e na manipulação de dados.

Entre os principais aprendizados estão:

- Estruturar um programa a partir de requisitos funcionais.
- Utilizar estruturas de repetição para automatizar tarefas.
- Validar entradas para evitar dados inconsistentes.
- Transformar valores armazenados em indicadores.
- Identificar e corrigir erros durante o desenvolvimento.
- Organizar funcionalidades por meio de um menu interativo.

## 🗺️ Roadmap — Próximas evoluções

O SalesTrack é um projeto em evolução. Algumas melhorias planejadas incluem:

- [ ] Refatoração do código utilizando funções.
- [ ] Tratamento de entradas não numéricas.
- [ ] Cadastro de produtos e categorias.
- [ ] Registro de datas das vendas.
- [ ] Persistência de dados com SQLite.
- [ ] Consultas e análises utilizando SQL.
- [ ] Exportação de relatórios em CSV.
- [ ] Visualização de indicadores com Power BI.

Essas funcionalidades representam possibilidades de evolução e ainda não fazem parte da versão inicial.

## 📌 Limitações da versão atual

A aplicação funciona localmente no terminal e mantém os registros em memória durante sua execução.

Por enquanto, os dados não são preservados após o encerramento do programa, e os cadastros são realizados em grupos de cinco vendas.

O projeto não utiliza banco de dados ou interface gráfica nesta versão.

## 👨‍💻 Sobre o desenvolvimento

Projeto desenvolvido como parte dos estudos em **Análise e Desenvolvimento de Sistemas**, com foco no aprendizado de Python e na construção progressiva de um portfólio voltado à área de Tecnologia e Dados.

O SalesTrack representa uma primeira aplicação prática dos conhecimentos adquiridos, com a proposta de evoluir conforme novos conceitos e tecnologias forem estudados.
