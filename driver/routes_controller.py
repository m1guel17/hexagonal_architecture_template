from flask import request, jsonify
from _infrastructure.adapters.output.router_view_file_adapter import RouterViewFileAdapter
from application.ports.input.router_view_inputport import RouterViewInputPort
from domain.entities.router import Router
from domain.value_objects.router_type import RouterType


def Routes(app):
    # Create instances of our hexagonal components
    router_output_port = RouterViewFileAdapter()
    router_input_port = RouterViewInputPort(router_output_port)

    @app.route("/routers", methods=["GET"])
    def get_routers():
        """
        Example endpoint to retrieve routers. 
        Optionally, filter by query parameter ?type=EDGE or ?type=CORE
        """
        router_type_filter = request.args.get("type")

        def filter_fn(r: Router):
            if router_type_filter:
                return r.router_type.value == router_type_filter
            return True

        routers = router_input_port.get_routers(filter_fn)
        response = [{"router_id": r.router_id, "router_type": r.router_type.value} for r in routers]
        return jsonify(response), 200

    @app.route("/routers", methods=["POST"])
    def add_router():
        """
        Example endpoint to add a new router.
        Expects JSON with {"router_id": "...", "router_type": "..."}
        """
        data = request.json
        if not data or "router_id" not in data or "router_type" not in data:
            return jsonify({"error": "Invalid payload"}), 400

        try:
            router_type = RouterType(data["router_type"])
        except ValueError:
            return jsonify({"error": "Invalid router_type"}), 400

        new_router = Router(router_id=data["router_id"], router_type=router_type)
        router_input_port.add_router(new_router)
        return jsonify({"message": "Router added successfully"}), 201