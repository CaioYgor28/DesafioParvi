"""Analyze the CSV file containing scraped quotes."""

import ast
import os

import pandas as pd


def processando_dados(
    nome_pasta: str = "data",
    nome_arquivo: str = "citacoes.csv",
    busca_1: str = "Texto",
    busca_2: str = "Autor",
    busca_3: str = "Tags",
) -> dict:
    """Summarize quote counts, the most frequent author, and the most common tag.

    :param str nome_pasta: CSV directory.
    :param str nome_arquivo: CSV file name.
    :param str busca_1: Column containing the quote text.
    :param str busca_2: Column containing the author.
    :param str busca_3: Column containing tags.
    :return dict: Values keyed by Citacoes, Autor, and Tag.
    """
    caminho = os.path.join(nome_pasta, nome_arquivo)
    df = pd.read_csv(caminho)
    if df.empty:
        raise ValueError("O arquivo CSV não contém citações.")

    total_quotes = len(df)
    autor_mais_frequente = df[busca_2].value_counts().idxmax()
    tags = df[busca_3].apply(ast.literal_eval).explode().dropna()
    tag_mais_frequente = (
        tags.astype(str).str.capitalize().value_counts().idxmax()
        if not tags.empty
        else "Sem tags"
    )

    print(f"\nQuantidade total de citações: {total_quotes}")
    print(f"Autor mais recorrente: {autor_mais_frequente}")
    print(f"Tag mais utilizada: {tag_mais_frequente}\n")

    return {
        "Citacoes": int(total_quotes),
        "Autor": autor_mais_frequente,
        "Tag": tag_mais_frequente,
    }
