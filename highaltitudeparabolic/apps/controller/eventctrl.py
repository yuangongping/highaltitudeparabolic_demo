from flask_restful import Resource, reqparse
from ..service.eventsrv import eventSrv
from ..uitls import success_res, error_res


class EventCtrl(Resource):
    def get(self)-> object:
        # 查询事件
        parser = reqparse.RequestParser()
        parser.add_argument('cameraName', required=True, type=str)
        parser.add_argument('pageIndex', required=True, type=int)
        parser.add_argument('pageSize', required=True, type=int)
        args = parser.parse_args(strict=True)
        dataset = eventSrv.getEvent(cameraName=args.cameraName, page=args.pageIndex, num=args.pageSize)
        return success_res(dataset)

    def put(self):
        # 编辑事件
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True, type=str)
        parser.add_argument('region', required=True, type=str)
        parser.add_argument('dir_path', required=True, type=str)
        parser.add_argument('file_num', required=True, type=int)
        parser.add_argument('file_size', required=True, type=int)
        parser.add_argument('dataset_num', required=True, type=int)
        parser.add_argument('acquire_date', required=True, type=str)
        args = parser.parse_args(strict=True)
        data = eventSrv.update(
            province=args.get("province"),
            region=args.get("region"),
            dir_path=args.get("dir_path"),
            file_num=args.get("file_num"),
            file_size=args.get("file_size"),
            dataset_num=args.get("dataset_num"),
            acquire_date=args.get("acquire_date")
        )
        return success_res(data)