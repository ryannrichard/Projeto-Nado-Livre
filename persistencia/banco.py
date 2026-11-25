
from sqlalchemy import create_engine, URL

from modelos.base import Base

# Importar os modelos registra as tabelas em Base.metadata
import modelos.nadador
import modelos.atendente
import modelos.toalha
import modelos.utilizacao


# Dados de conexão com o MySQL
URL_BANCO = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="",
    host="localhost",
    port=3306,
    database="nado_livre"
)

# Criar conexão com o banco de dados
engine = create_engine(URL_BANCO, echo=False)


def criar_tabelas() -> None:
    """Cria as tabelas a partir dos modelos, caso ainda não existam."""
    Base.metadata.create_all(engine)
