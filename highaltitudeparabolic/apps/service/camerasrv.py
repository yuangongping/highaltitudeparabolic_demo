from ..model import db
from ..model.camera import Camera
from flask import abort
from sqlalchemy import and_


class cameraSrv(object):
    @classmethod
    def add(cls, name: str, address: str, port: str, username: str,
            password: str, serial_number: str, location: str,  longitude: str, latitude:str,
            network_state=None):
        try:
            obj = Camera(
                name=name,
                address=address,
                port=port,
                username=username,
                password=password,
                serial_number=serial_number,
                network_state=network_state,
                location=location,
                longitude=longitude,
                latitude=latitude
            )
            db.session.add(obj)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return abort(500, '新增数据出错')

    @classmethod
    def delete(cls, id: int):
        try:
            obj =  Camera.query.filter_by(id=id).first()
            db.session.delete(obj)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            abort(500, '删除数据出错')

    @classmethod
    def search(cls, page: int, num: int,  name=None):
        exp_list = []
        if name:
            words = name.split(' ')
            for word in words:
                exp_list.append(Camera.name.like('%{}%'.format(word)))
        order_exp = Camera.date_created.desc()
        if len(exp_list) > 0:
            filter_exp = and_(*exp_list)
            pagination = Camera.query.filter(filter_exp).order_by(order_exp).paginate(page, num, error_out=False)
        else:
            pagination = Camera.query.order_by(order_exp).paginate(page, num, error_out=False)

        return {
                'total': pagination.total,
                'data': [camera.toDict() for camera in pagination.items]
        }