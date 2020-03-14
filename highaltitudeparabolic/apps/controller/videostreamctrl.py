from flask_restful import reqparse, Resource
from ..service.videostreamsrv import VideoStreamSrv
from ..uitls import success_res


class VideoStreamCtrl(Resource):
    @classmethod
    def get(cls):
        parser = reqparse.RequestParser()
        parser.add_argument('filename', type=str)
        args = parser.parse_args(strict=True)
        data = VideoStreamSrv.getFileStream(file_path=args.filename)
        return data

