from flask import request
from flask_restful import Resource


class DemoResource(Resource):
    """Demo resource

    ---
    get:
      tags:
        - demo
      summary: check health
      description: check health
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
        404:
          description: check health
    """
    def get(self):
        return {"info": "ok"}