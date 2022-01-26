import logging as logger

from flask_restful import Resource

from redis_service import redis_config

logger.basicConfig(level=logger.DEBUG)


class Task(Resource):
    def __init__(self):
        self.logger = logger
        self.redis_cli = redis_config.RedisCache(logger, 1)

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
        # if task not completed in 3600 seconds then remove from cache
        self.task_expire_time = 3600
        self.redis_cli = redis_config.RedisCache(logger, 1)

    def get(self, task_id):
        self.logger.info("inside get task")
        task_info = self.redis_cli.get(task_id)
        if task_info:
            return {"message": "Task found with task_id: {}".format(task_id), "task_info": task_info.decode()}, 200
        else:
            return {"message": "No task found with task_id: {}".format(task_id)}, 401

    def post(self, task_id):
        self.logger.info("inside post task")
        task_info = self.redis_cli.get(task_id)
        if task_info:
            return {"message": "Task already exists with task_id: {}".format(task_id)}, 400
        task_info = "Task attached to task_id {}".format(task_id)
        self.redis_cli.set(task_id, task_info, self.task_expire_time)
        return {"message": "task added with task_id: {}".format(task_id)}, 201

    def put(self, task_id):
        self.logger.info("inside put task")
        task_info = self.redis_cli.get(task_id)
        if task_info:
            task_info = "Updated task for task_id {}".format(task_id)
            self.redis_cli.set(task_id, task_info, self.task_expire_time)
            return {"message": "Task updated with task_id: {}".format(task_id)}, 200
        else:
            return {"message": "No task found with task_id: {}".format(task_id)}, 401

    def delete(self, task_id):
        self.logger.info("inside delete task")
        task_info = self.redis_cli.get(task_id)
        if not task_info:
            return {"message": "No task found with task_id: {}".format(task_id)}, 401
        self.redis_cli.delete(task_id)
        return {"message": "Task deleted with task_id: {}".format(task_id)}, 200
