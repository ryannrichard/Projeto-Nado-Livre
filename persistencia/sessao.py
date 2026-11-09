from sqlalchemy.orm import Session, sessionmaker

from persistencia.banco import engine

_fabrica_sessoes = sessionmaker(bind=engine, expire_on_commit=False)


def obter_sessao() -> Session:
    """Retorna uma nova sessão para uso nos serviços (use com 'with')."""
    return _fabrica_sessoes()