from flask import request, Response
import json


class UserRoutes:
    def __init__(self, user_store, user_blueprint):
        self.user_store = user_store
        self.user_blueprint = user_blueprint
        self._register()

    def _register(self):

        @self.user_blueprint.route('/new', methods=['POST'])
        def add_user():
            request_body = json.loads(request.data)

            # Validate the request here...

            # request body validated
            user_store = self.user_store
            user_store.create(request_body)

            response_data = ''
            status_code = 200
            headers = {"Content-Type": "application/json"}
            return Response(
                response=response_data,
                status=status_code,
                headers=headers
            )

        @self.user_blueprint.route('/all', methods = ['GET'])
        def fetch_all_users():
            users = self.user_store.search_all()

            results = []
            for user in users:
                user_obj = {
                    "name": user.name,
                    "email": user.email
                }
                results.append(user_obj)

            response_data = json.dumps({"results": results})
            status_code = 200
            headers = {"Content-Type": "application/json"}
            return Response(
                response=response_data,
                status=status_code,
                headers=headers
            )
