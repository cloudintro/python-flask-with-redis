import logging as logger

from flask import Flask
from flask_restful import Api

from api.rest_api import Task, TaskById

logger.basicConfig(level=logger.DEBUG)

flask_instance = Flask(__name__)
rest_server = Api(flask_instance)
rest_server.add_resource(Task, "/v1/task")
rest_server.add_resource(TaskById, "/v1/task/<string:task_id>")


def hello_world():
    return {"msg": "Hello World!!", "code": 0}


if __name__ == "__main__":
    logger.info(f"starting application {hello_world()}")
    flask_instance.run(host="0.0.0.0", port=8081, use_reloader=True, debug=True)
