📘 Multi-Agent Data Assistant

Um projeto em Python utilizando agentes especializados para buscar, limpar e analisar dados reais de uma API pública.
O sistema é composto por três agentes independentes que trabalham juntos:

🔍 SearchAgent — Busca dados em uma API pública

🧹 ProcessingAgent — Limpa e normaliza os dados

🧠 SummaryAgent — Gera um resumo inteligente usando OpenAI

📌 Objetivo do Projeto

Demonstrar como criar um pipeline multi-agente simples, modular e extensível, capaz de:

Buscar informações reais da web

Processá-las e padronizá-las

Gerar análises com IA (OpenAI)

Esse projeto é ideal para quem está estudando:

Agentes inteligentes

Arquitetura multi-agente

Integração com APIs

Uso do OpenAI API em Python

Processamento de dados

Análises automáticas

📂 Estrutura do Projeto
examples/
  └── multi_agent_data_assistant/
      ├── agents.py
      ├── main.py
      └── README.md
      └── tools.py
    

🚀 Como Executar
1) Clone o repositório
git clone https://github.com/SEU_USUARIO/openai-agents-python
cd openai-agents-python

2) Crie e ative o ambiente virtual
python -m venv venv
.\venv\Scripts\activate    # Windows

3) Instale as dependências
pip install -r requirements.txt

4) Configure a chave da OpenAI

Crie um arquivo .env:

OPENAI_API_KEY=sua_chave_aqui


E carregue a variável:

setx OPENAI_API_KEY "sua_chave_aqui"

5) Execute o projeto
python examples/multi_agent_data_assistant/main.py

🧠 Como o Pipeline Funciona
✔️ 1. SearchAgent

Faz a busca real em:
https://dummyjson.com/products/search?q=termo

Retorna produtos encontrados.

✔️ 2. ProcessingAgent

Padroniza cada item para um formato organizado:

{
  "title": "...",
  "price": 99.99,
  "rating": 4.5,
  "category": "accessories",
  "description": "..."
}

✔️ 3. SummaryAgent

Gera um resumo inteligente usando o modelo:

gpt-4o-mini


Analisa:

categorias

preços

padrões

insights

✨ Exemplo de Saída
Digite um termo para buscar: iphone

======== SearchAgent ========
Encontrados: 8 produtos

======== ProcessingAgent ========
Itens limpos: 8

======== SummaryAgent ========
Resumo de análise:
- Acessórios e smartphones foram encontrados
- Faixa de preço entre $14 e $299
- Itens com maior nota tendem a ser acessórios

🛠️ Tecnologias

Python 3.10+

Biblioteca oficial OpenAI

Requests

Dotenv

📌 Melhorias Futuras (Roadmap)

Gráficos de distribuição de preços

Interface Web com Streamlit

Novo agente para comparar produtos

Logs mais detalhados

Testes unitários

Integração com bancos de dados reais

📄 Licença

MIT License