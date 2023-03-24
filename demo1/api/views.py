from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from demo1.extensions import apispec
from demo1.api.resources import UserResource, UserList, DemoResource, DeepfaceResource, RepresentResource, AnalyzeResource, VerifyResource, ImageResource
from demo1.api.schemas import UserSchema


blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)


api.add_resource(UserResource, "/users/<int:user_id>", endpoint="user_by_id")
api.add_resource(UserList, "/users", endpoint="users")
api.add_resource(DemoResource, "/demo", endpoint="demo")
api.add_resource(DeepfaceResource, "/deepface", endpoint="deepface")
api.add_resource(RepresentResource, "/deepface/represent", endpoint="deepface_represent")
api.add_resource(AnalyzeResource, "/deepface/analyze", endpoint="deepface_analyze")
api.add_resource(VerifyResource, "/deepface/verify", endpoint="deepface_verify")
api.add_resource(ImageResource, "/deepface/image", endpoint="deepface_image")


@blueprint.before_app_first_request
def register_views():
    apispec.spec.components.schema("UserSchema", schema=UserSchema)
    apispec.spec.path(view=UserResource, app=current_app)
    apispec.spec.path(view=UserList, app=current_app)
    apispec.spec.path(view=DemoResource, app=current_app)
    apispec.spec.path(view=RepresentResource, app=current_app)
    apispec.spec.path(view=VerifyResource, app=current_app)



@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    """Return json error for marshmallow validation errors.

    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400
