from flask import request
from flask_restful import Resource
from demo1.api.services.deepface import represent, verify, analyze
from base64 import b64decode
import uuid

from demo1.config import DEEPFACE_TEMP_IMAGE_PATH

class DeepfaceResource(Resource):

    def get(self):
        return "Deepface api."


class RepresentResource(Resource):
    """Deepface resource

    ---
    post:
      tags:
        - deepface
      summary: represent
      description: represent
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
        404:
          description: 404
    """
    def post(self):
        input_args = request.get_json()

        if input_args is None:
            return {"message": "empty input set passed"}

        img_path = input_args.get("img")
        if img_path is None:
            return {"message": "you must pass img_path input"}

        model_name = input_args.get("model_name", "VGG-Face")
        detector_backend = input_args.get("detector_backend", "opencv")
        enforce_detection = input_args.get("enforce_detection", True)
        align = input_args.get("align", True)

        obj = represent(
            img_path=img_path,
            model_name=model_name,
            detector_backend=detector_backend,
            enforce_detection=enforce_detection,
            align=align,
        )

        return obj

class VerifyResource(Resource):
    def post(self):
        input_args = request.get_json()

        if input_args is None:
            return {"message": "empty input set passed"}

        img1_path = input_args.get("img1_path")
        img2_path = input_args.get("img2_path")

        if img1_path is None:
            return {"message": "you must pass img1_path input"}

        if img2_path is None:
            return {"message": "you must pass img2_path input"}

        model_name = input_args.get("model_name", "VGG-Face")
        detector_backend = input_args.get("detector_backend", "opencv")
        enforce_detection = input_args.get("enforce_detection", True)
        distance_metric = input_args.get("distance_metric", "cosine")
        align = input_args.get("align", True)

        verification = verify(
            img1_path=img1_path,
            img2_path=img2_path,
            model_name=model_name,
            detector_backend=detector_backend,
            distance_metric=distance_metric,
            align=align,
            enforce_detection=enforce_detection,
        )

        verification["verified"] = str(verification["verified"])

        return verification

class AnalyzeResource(Resource):
    def post(self):
        input_args = request.get_json()

        if input_args is None:
            return {"message": "empty input set passed"}

        img_path = input_args.get("img_path")
        if img_path is None:
            return {"message": "you must pass img_path input"}

        detector_backend = input_args.get("detector_backend", "opencv")
        enforce_detection = input_args.get("enforce_detection", True)
        align = input_args.get("align", True)
        actions = input_args.get("actions", ["age", "gender", "emotion", "race"])

        demographies = analyze(
            img_path=img_path,
            actions=actions,
            detector_backend=detector_backend,
            enforce_detection=enforce_detection,
            align=align,
        )

        return demographies

class ImageResource(Resource):
     def post(self):
        input_args = request.get_json()
        header, encoded = input_args.get('imageDate').split(",", 1)
        fileName = str(uuid.uuid4())
        fh = open(DEEPFACE_TEMP_IMAGE_PATH + fileName, "wb")
        fh.write(b64decode(encoded))
        fh.close()

        return {
            'fileName' : DEEPFACE_TEMP_IMAGE_PATH + fileName
        }