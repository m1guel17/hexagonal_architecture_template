from dataclasses import dataclass
from domain.value_objects.router_type import RouterType

@dataclass(frozen=True)
class Router:
    router_id: str
    router_type: RouterType

    def to_dict(self):
        return {
            "router_id": self.router_id,
            "router_type": self.router_type.value  # Convert Enum to string
        }