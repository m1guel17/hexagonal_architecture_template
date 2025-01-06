from dataclasses import dataclass
from domain.value_objects.router_type import RouterType

@dataclass
class Router:
    id: str
    type: RouterType

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type.value  # Convert Enum to string
        }