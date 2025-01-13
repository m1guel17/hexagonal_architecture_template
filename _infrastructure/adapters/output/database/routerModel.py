from domain.entities.router import Router
from domain.value_objects.router_type import RouterType
from driver.flask_app import db


class RouterModel(db.Model):
    __tablename__ = 'routers'
    id = db.Column(db.Integer, primary_key=True)
    router_id = db.Column(db.String, nullable=False)
    router_type = db.Column(db.String, nullable=True)
    
    def to_domain(self) -> Router:
        return Router(router_id=self.router_id, router_type=RouterType(self.router_type))

    @classmethod
    def from_domain(cls, router: Router) -> "RouterModel":
        return cls(router_id=router.router_id,router_type=router.router_type.value)