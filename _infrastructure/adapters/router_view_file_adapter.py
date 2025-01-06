from application.ports.output.router_view_outputport import RouterViewOutputPort
from domain.entities.router import Router
from domain.value_objects.router_type import RouterType
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RouterModel(db.Model):
    __tablename__ = 'routers'
    id = db.Column(db.String, primary_key=True)
    type = db.Column(db.String, nullable=False)

    def to_domain(self):
        return Router(id=self.id, type=RouterType(self.type))

class RouterViewFileAdapter(RouterViewOutputPort):
    def fetch_routers(self):
        router_models = RouterModel.query.all()
        return [model.to_domain() for model in router_models]

    def add_router(self, router: Router):
        db.session.add(RouterModel(id=router.id, type=router.type.value))
        db.session.commit()