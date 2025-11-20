"""
tools.py
Funções utilitárias simples (validação, formatação).
"""

def validate_query(query: str) -> str:
    if not query or not isinstance(query, str):
        return "data"
    q = query.strip()
    if len(q) < 2:
        return "data"
    return q

def pretty_print_section(title: str):
    print("\n" + "=" * 8 + " " + title + " " + "=" * 8 + "\n")