from application.usecases.router_view_usecase import RouterViewUseCase
from application.ports.output.router_view_outputport import RouterViewOutputPort
from domain.value_objects.router_type import RouterType
from typing import List, Callable
from domain.entities.router import Router

class RouterViewInputPort(RouterViewUseCase):
    def __init__(self, output_port: RouterViewOutputPort):
        self.output_port = output_port

    def get_routers(self, filter_func: Callable[[Router], bool]) -> List[Router]:
        routers = self.output_port.fetch_routers()
        return list(filter(filter_func, routers))

    def add_router(self, router_id: str, router_type: RouterType):
        router = Router(id=router_id, type=router_type)
        self.output_port.add_router(router)