from ..model.event import Event
from ...apps import app
import os
from flask import abort


class eventSrv(object):
    @classmethod
    def getEvent(cls, cameraName: str, page: int, num: int) -> object:
        pagination = Event.query.filter_by(camera_name=cameraName).paginate(page, num, error_out=False)
        return {
            'total': pagination.total,
            'pages': pagination.pages,
            'has_prev': pagination.has_prev,
            'has_next': pagination.has_next,
            'data': [event.toDict() for event in pagination.items]
        }

