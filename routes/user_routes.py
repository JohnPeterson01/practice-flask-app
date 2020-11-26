from flask.blueprints import Blueprint
from flask import request, Response
import json

from stores.user_store import UserStore


user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/<name>', methods=['GET'])
def hi_there(name):
    response_data = json.dumps({ "name": name })
    status_code = 200
    headers = { "Content-Type": "application/json" }
    return Response(
        response=response_data,
        status=status_code,
        headers=headers
    )

@user_blueprint.route('/new', methods=['POST'])
def add_user():
    request_body = json.loads(request.data)

    # Validate the request here...

    # request body validated
    user_store = UserStore()
    user_store.create(request_body)
    
    response_data = ''
    status_code = 200
    headers = {"Content-Type": "application/json"}
    return Response(
        response=response_data,
        status=status_code,
        headers=headers
    )


@user_blueprint.route('/all', methods=['GET'])
def fetch_all_users():
    user_store = UserStore()
    users = user_store.search_all()
    results = []
    for user in users:
        user_obj = {
            "name": user.name,
            "email": user.email
        }
        results.append(user_obj)

    response_data = json.dumps({"results": results })
    status_code = 200
    headers = {"Content-Type": "application/json"}
    return Response(
        response=response_data,
        status=status_code,
        headers=headers
    )