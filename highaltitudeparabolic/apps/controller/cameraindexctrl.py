from flask_restful import Resource, reqparse
from ..service.camerasrv import cameraSrv
from ..uitls import success_res, error_res


class CameraCtrl(Resource):
    def get(self) -> object:
        parser = reqparse.RequestParser()
        parser.add_argument('location', type=str)
        args = parser.parse_args(strict=True)
        dataset = cameraSrv.search(name=args.name, page=args.pageIndex, num=args.pageSize)
        return success_res(dataset)