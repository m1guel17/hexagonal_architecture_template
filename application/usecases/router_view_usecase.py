from typing import List, Callable
from domain.entities.router import Router

class RouterViewUseCase:
    def get_routers(self, filter_func: Callable[[Router], bool]) -> List[Router]:
        raise NotImplementedError
