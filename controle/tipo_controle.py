# Classe que representa a parte Strategy
# do Strategy

from abc import ABC
from persistencia.dao import DAO

class TipoControle(ABC):

    def __init__(self, persistencia: DAO) -> None:
        self.persistencia = persistencia
