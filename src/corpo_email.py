"""Email body formatting for the collected quotes report."""


def msg_corpo_email(
    total_dicionario: dict,
    busca_1: str = "Citacoes",
    busca_2: str = "Autor",
    busca_3: str = "Tag",
) -> str:
    """Create a summary of the collected quote statistics.

    :param dict total_dicionario: Aggregated quote statistics.
    :param str busca_1: Key containing the number of quotes.
    :param str busca_2: Key containing the most frequent author.
    :param str busca_3: Key containing the most frequent tag.
    :return str: Text suitable for an email body.
    """
    return (
        "Olá, seguem os dados da análise de citações:\n\n"
        f"Total de citações: {total_dicionario[busca_1]}\n"
        f"Autor mais recorrente: {total_dicionario[busca_2]}\n"
        f"Tag mais frequente: {total_dicionario[busca_3]}"
    )
