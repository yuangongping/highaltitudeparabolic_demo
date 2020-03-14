from ..model import db
from ..model.video import Video
from flask import abort
from sqlalchemy import and_
from sqlalchemy import func

class VideoSrv(object):
    @classmethod
    def getAllVideo(cls, page: int, num: int, camera_name: str,
            start_date:str, end_date: str):
        try:
            exp_list = []
            if camera_name is not None:
                exp_list.append(Video.camera_name == camera_name)
            if start_date is not None:
                exp_list.append(
                    func.date_format(Video.start_date, '%Y-%m-%d %H:%i:%S') >= start_date)
            if end_date is not None:
                exp_list.append(func.date_format(Video.start_date, '%Y-%m-%d %H:%i:%S') < end_date)
            order_exp = Video.start_date.desc()
            if len(exp_list) > 0:
                filter_exp = and_(*exp_list)
                pagination = Video.query.filter(filter_exp).order_by(order_exp).paginate(page, num, error_out=False)
            else:
                pagination = Video.query.order_by(order_exp).paginate(page, num, error_out=False)
            return {
                'total': pagination.total,
                'pages': pagination.pages,
                'has_prev': pagination.has_prev,
                'has_next': pagination.has_next,
                'data': [video.toDict() for video in pagination.items]
            }
        except Exception as e:
            abort(500, "数据出错！")