from persistencia.cancao_pers import CancaoPers
from controle.tipo_controle import TipoControle

class CancaoControle(TipoControle):
    def __init__(self) -> None:
        super().__init__(CancaoPers())
