from typing import List, Callable
from abc import ABC, abstractmethod
from domain.entities.router import Router

class RouterViewUseCase(ABC):
    @abstractmethod
    def get_routers(self, filter_func: Callable[[Router], bool]) -> List[Router]:
        pass
        # raise NotImplementedError
    @abstractmethod
    def add_router(self, router: Router):
        pass
    