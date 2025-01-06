from typing import List
from domain.entities.router import Router

class RouterViewOutputPort:
    def fetch_routers(self) -> List[Router]:
        raise NotImplementedError
