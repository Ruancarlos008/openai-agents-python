import os
import requests
from openai import OpenAI


# =========================
# BaseAgent — classe pai
# =========================

class BaseAgent:
    def __init__(self, name, description):
        self.name = name.upper()
        self.description = description

    def log(self, message: str):
        print(f"[{self.name}] {message}")

    def run(self, *args, **kwargs):
        raise NotImplementedError("Subclasses devem implementar o método run().")


# =========================
# SearchAgent — busca em API pública
# =========================

class SearchAgent(BaseAgent):
    """Agente responsável por buscar dados reais em API pública."""

    def __init__(self):
        super().__init__("SearchAgent", "Busca dados em uma API pública usando um termo informando.")

    def run(self, query: str):
        print("\n======== SearchAgent: BUSCA ========\n")

        url = f"https://dummyjson.com/products/search?q={query}"

        try:
            response = requests.get(url, timeout=8)
            response.raise_for_status()
            data = response.json()

            results = data.get("products", [])

            print(f"[SearchAgent] query='{query}' | encontrados: {len(results)}")

            return {"raw_data": results}

        except Exception as e:
            print(f"[SearchAgent] erro ao buscar API: {e}")
            return {"raw_data": []}


# =========================
# ProcessingAgent — limpeza dos dados
# =========================

class ProcessingAgent(BaseAgent):
    """Limpa e organiza os dados retornados pela busca."""

    def __init__(self):
        super().__init__("ProcessingAgent", "Filtra e normaliza os dados coletados.")

    def run(self, data: dict):
        print("\n======== ProcessingAgent: LIMPEZA ========\n")

        items = data.get("raw_data", [])

        cleaned = [
            {
                "title": item.get("title"),
                "price": item.get("price"),
                "category": item.get("category"),
                "rating": item.get("rating"),
                "description": item.get("description"),
            }
            for item in items
        ]

        print(f"[ProcessingAgent] cleaned items: {len(cleaned)}")

        return {"cleaned": cleaned}


# =========================
# SummaryAgent — usa OpenAI para resumir
# =========================

class SummaryAgent(BaseAgent):
    """Gera um resumo inteligente dos dados usando um modelo da OpenAI."""

    def __init__(self):
        super().__init__("SummaryAgent", "Resume os dados processados usando IA.")
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def run(self, processed: dict):
        print("\n======== SummaryAgent: RESUMO ========\n")

        items = processed.get("cleaned", [])

        if not items:
            return {"summary": "Nenhum item encontrado para resumir."}

        text_for_llm = "\n".join(
            [
                f"- {item['title']} | preço: {item['price']} | categoria: {item['category']} | avaliação: {item['rating']}"
                for item in items
            ]
        )

        prompt = f"""
Você é um assistente especialista em análise de dados. Com base nos itens abaixo,
gere um resumo conciso destacando padrões, categorias e preços relevantes.

Itens:
{text_for_llm}

Resumo:
"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=180
            )
        
            resumo = response.choices[0].message.content

            print(resumo)
            return {"summary": resumo}

        except Exception as e:
            print(f"[SummaryAgent] erro ao gerar resumo: {e}")
            return {"summary": "Erro ao gerar resumo."}