from pathlib import Path

from sqlalchemy import create_engine, event

from modelos.base import Base

# Importar os modelos registra as tabelas em Base.metadata
import modelos.nadador  # noqa: F401
import modelos.atendente  # noqa: F401
import modelos.toalha  # noqa: F401
import modelos.utilizacao  # noqa: F401

CAMINHO_BANCO = (
    Path(__file__).resolve().parent.parent / "dados" / "nado_livre.db"
)
CAMINHO_BANCO.parent.mkdir(exist_ok=True)

engine = create_engine(f"sqlite:///{CAMINHO_BANCO}")


@event.listens_for(engine, "connect")
def _ativar_chaves_estrangeiras(conexao, _registro) -> None:
    """O SQLite ignora chaves estrangeiras por padrão; isso as ativa."""
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


def criar_tabelas() -> None:
    """Cria as tabelas a partir dos modelos, caso ainda não existam."""
    Base.metadata.create_all(engine)