from application.ports.output.router_view_outputport import RouterViewOutputPort
from domain.entities.router import Router
from domain.value_objects.router_type import RouterType
from flask_sqlalchemy import SQLAlchemy
from typing import List

db = SQLAlchemy()

class RouterModel(db.Model):
    __tablename__ = 'routers'
    id = db.Column(db.Integer, primary_key=True)
    router_id = db.Column(db.String, nullable=False)
    router_type = db.Column(db.String, nullable=False)
    
    def to_domain(self) -> Router:
        return Router(router_id=self.router_id, router_type=RouterType(self.router_type))

    @classmethod
    def from_domain(cls, router: Router) -> "RouterModel":
        return cls(router_id=router.router_id,router_type=router.router_type.value)
    
class RouterViewFileAdapter(RouterViewOutputPort):
    def fetch_routers(self) -> List[Router]:
        router_models = RouterModel.query.all()
        return [model.to_domain() for model in router_models]

    def save_routers(self, router: Router) -> None:
        router_model = RouterModel.from_domain(router)
        db.session.add(router_model)
        db.session.commit()
        
    # def add_router(self, router: Router):
    #     db.session.add(RouterModel(id=router.id, type=router.type.value))
    #     db.session.commit()