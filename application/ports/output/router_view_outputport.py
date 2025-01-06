from abc import ABC, abstractmethod
from typing import List
from domain.entities.router import Router

class RouterViewOutputPort(ABC):
    
    @abstractmethod
    def fetch_routers(self) -> List[Router]:
       pass 
        # raise NotImplementedError

    @abstractmethod
    def save_routers(self, router: Router) -> None:
       pass 