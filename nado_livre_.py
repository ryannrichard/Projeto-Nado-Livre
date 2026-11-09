from persistencia.banco import criar_tabelas


class NadoLivre:
    """
    Ponto de entrada da aplicação. Garante que o banco de dados
    e suas tabelas existam antes do uso dos serviços.
    """

    def __init__(self) -> None:
        criar_tabelas()