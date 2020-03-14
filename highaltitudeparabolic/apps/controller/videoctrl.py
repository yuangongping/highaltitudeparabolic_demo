from flask_restful import Resource, reqparse
from ..service.videosrv import VideoSrv
from ..uitls import success_res, error_res


class VideoCtrl(Resource):
    def get(self) -> object:
        parser = reqparse.RequestParser()
        parser.add_argument('pageIndex', required=True, type=int)
        parser.add_argument('pageSize', required=True, type=int)
        parser.add_argument('cameraName', required=True, type=str)
        parser.add_argument('startDate', default=None)
        parser.add_argument('endDate', default=None)
        args = parser.parse_args(strict=True)
        dataset = VideoSrv.getAllVideo(
            page=args.pageIndex,
            num=args.pageSize,
            camera_name=args.cameraName,
            start_date=args.startDate,
            end_date=args.endDate
        )
        return success_res(dataset)
