from sqlalchemy import create_engine

from modelos.base import Base

# Importar os modelos registra as tabelas em Base.metadata
import modelos.nadador  # noqa: F401
import modelos.atendente  # noqa: F401
import modelos.toalha  # noqa: F401
import modelos.utilizacao  # noqa: F401

URL_BANCO = "mysql+pymysql://root:@localhost:3306/nado_livre"

engine = create_engine(URL_BANCO, echo=False)


def criar_tabelas() -> None:
    """Cria as tabelas a partir dos modelos, caso ainda não existam."""
    Base.metadata.create_all(engine)