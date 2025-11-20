import sys
from agents import SearchAgent, ProcessingAgent, SummaryAgent


# Instanciando os agentes
search_agent = SearchAgent()
processing_agent = ProcessingAgent()
summary_agent = SummaryAgent()


def run_pipeline(query: str):
    print("\n======== SearchAgent: BUSCA ========\n")

    # 1) Busca
    raw = search_agent.run(query)

    # Garante que a estrutura está correta
    raw_entries = raw.get("raw_data", [])

    print(f"[SearchAgent] query='{query}' | encontrados: {len(raw_entries)}")

    if len(raw_entries) == 0:
        print("[WARN] Nenhum resultado encontrado. Finalizando pipeline.\n")
        return

    print("\n======== ProcessingAgent: LIMPEZA ========\n")

    # 2) Processamento
    cleaned = processing_agent.run(raw)
    cleaned_entries = cleaned.get("cleaned_data", [])

    print("\n======== SummaryAgent: RESUMO ========\n")

    # 3) Resumo com LLM
    summary = summary_agent.run(cleaned)

    final_text = summary.get("summary", "(Sem resumo gerado.)")

    print("======== RESULTADO FINAL ========\n")
    print(final_text)
    print("\n=================================\n")


def main():
    print("🔎 Multi-Agent Data Assistant — exemplo")

    while True:
        try:
            query = input("Digite um produto ou marca para busca (ex: Iphone): ").strip()

            if not query:
                print("Digite algo válido!\n")
                continue

            run_pipeline(query)

            again = input("Pesquisar novamente? (s/n): ").strip().lower()
            if again != "s":
                print("Encerrando...")
                break

        except KeyboardInterrupt:
            print("\nEncerrado pelo usuário.")
            sys.exit(0)
        except Exception as e:
            print("\n❌ ERRO NO PIPELINE")
            print(str(e))
            print("Continuando...\n")


if __name__ == "__main__":
    main()