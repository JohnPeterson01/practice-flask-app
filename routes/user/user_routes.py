from flask import request, Response
import json


class UserRoutes:
    def __init__(self, user_store):
        self.user_store = user_store

    def register(self, blueprint):
        @blueprint.route('', methods=['GET'])
        def hi():
            response_data = ''
            status_code = 200
            headers = {"Content-Type": "application/json"}
            return Response(
                response=response_data,
                status=status_code,
                headers=headers
            )

        @blueprint.route('/new', methods=['POST'])
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

        @blueprint.route('/all', methods=['GET'])
        def fetch_all_users():
            print(self)
            db_result = self.user_store.search_all()

            response_data = json.dumps({"results": db_result})
            status_code = 200
            headers = {"Content-Type": "application/json"}
            return Response(
                response=response_data,
                status=status_code,
                headers=headers
            )

        return blueprint
