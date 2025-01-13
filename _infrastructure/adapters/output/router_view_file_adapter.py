from application.ports.output.router_view_outputport import RouterViewOutputPort
from domain.entities.router import Router
from driver.flask_app import db
from _infrastructure.adapters.output.database.routerModel import RouterModel

from typing import List
    
class RouterViewFileAdapter(RouterViewOutputPort):
    def fetch_routers(self) -> List[Router]:
        router_models = RouterModel.query.all()
        return [model.to_domain() for model in router_models]

    def save_routers(self, router: Router) -> None:
        router_model = RouterModel.from_domain(router)
        db.session.add(router_model)
        db.session.commit()
        