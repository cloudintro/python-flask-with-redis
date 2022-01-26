from flask_restful import Resource
import logging as logger

logger.basicConfig(level=logger.DEBUG)


class Task(Resource):
    def __init__(self):
        self.logger = logger

    def get(self):
        self.logger.info("inside get task")
        return {"message": "task found"}, 200

    def post(self):
        self.logger.info("inside post task")
        return {"message": "task added"}, 201

    def put(self):
        self.logger.info("inside put task")
        return {"message": "task updated"}, 200

    def delete(self):
        self.logger.info("inside delete task")
        return {"message": "task deleted"}, 200


class TaskById(Resource):
    def __init__(self):
        self.logger = logger

    def get(self, task_id):
        self.logger.info("inside get task")
        return {"message": "task found with task_id: {}".format(task_id)}, 200

    def post(self, task_id):
        self.logger.info("inside post task")
        return {"message": "task added with task_id: {}".format(task_id)}, 201

    def put(self, task_id):
        self.logger.info("inside put task")
        return {"message": "task updated with task_id: {}".format(task_id)}, 200

    def delete(self, task_id):
        self.logger.info("inside delete task")
        return {"message": "task deleted with task_id: {}".format(task_id)}, 200
