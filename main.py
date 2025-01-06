from flask import Flask, request, jsonify
from _infrastructure.adapters.router_view_file_adapter import db, RouterViewFileAdapter
from application.ports.input.router_view_inputport import RouterViewInputPort
from domain.value_objects.router_type import RouterType

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///routers.db'
db.init_app(app)

with app.app_context():
    db.create_all()

adapter = RouterViewFileAdapter()
input_port = RouterViewInputPort(adapter)

@app.route('/routers', methods=['GET'])
def get_routers():
    type_filter = request.args.get('type', None)
    if type_filter:
        router_type = RouterType[type_filter.upper()]
        filtered_routers = input_port.get_routers(lambda r: r.type == router_type)
    else:
        filtered_routers = input_port.get_routers(lambda r: True)

    return jsonify([router.to_dict() for router in filtered_routers])
    

@app.route('/routers', methods=['POST'])
def add_router():
    data = request.json
    router_id = data['id']
    router_type = RouterType[data['type'].upper()]

    # Pass the request data to the application layer
    input_port.add_router(router_id, router_type)
    return jsonify({'message': 'Router added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
