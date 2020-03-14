from flask_restful import Resource, reqparse
from ..service.camerasrv import cameraSrv
from ..uitls import success_res, error_res


class CameraCtrl(Resource):
    def get(self) -> object:
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('pageIndex', required=True, type=int)
        parser.add_argument('pageSize', required=True, type=int)
        args = parser.parse_args(strict=True)
        dataset = cameraSrv.search(name=args.name, page=args.pageIndex, num=args.pageSize)
        return success_res(dataset)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, type=str)
        parser.add_argument('address', required=True, type=str)
        parser.add_argument('port', required=True, type=str)
        parser.add_argument('username', required=True, type=str)
        parser.add_argument('password', required=False, type=str)
        parser.add_argument('serial_number', required=True, type=str)
        parser.add_argument('network_state', type=str)
        parser.add_argument('location', required=True, type=str)
        parser.add_argument('longitude', required=True, type=str)
        parser.add_argument('latitude', required=True, type=str)
        args = parser.parse_args(strict=True)
        data = cameraSrv.add(
            name=args.get("name"),
            address=args.get("address"),
            port=args.get("port"),
            username=args.get("username"),
            password=args.get("password"),
            serial_number=args.get("serial_number"),
            network_state=args.get("network_state"),
            location=args.get("location"),
            longitude=args.get("longitude"),
            latitude=args.get("latitude")
        )
        return success_res(data)

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True, type=int)
        args = parser.parse_args(strict=True)
        data = cameraSrv.delete(id=args.get("id"))
        return success_res(data)