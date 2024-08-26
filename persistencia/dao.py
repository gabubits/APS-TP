from modelo.entidade import Entidade
from abc import ABC, abstractmethod
from typing import List
from persistencia.singleton import Singleton

class DAO(ABC, Singleton):

    @abstractmethod
    def carregar_dados(self) -> None: ...

    @abstractmethod
    def atualizar_dados(self) -> None: ...

    @abstractmethod
    def inserir(self, objeto: Entidade) -> None: ...

    @abstractmethod
    def remover(self, objeto_id: int) -> None: ...

    @abstractmethod
    def pesquisar(self, atributo: str, valor: str) -> List[Entidade]: ...

    @abstractmethod
    def obter_tudo(self) -> List[Entidade]: ...