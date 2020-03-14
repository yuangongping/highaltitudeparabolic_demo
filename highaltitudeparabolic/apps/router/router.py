from ...apps import restful_api
from ..controller.cameractrl import CameraCtrl
from ..controller.videoctrl import VideoCtrl
from ..controller.eventctrl import EventCtrl
from ..controller.videostreamctrl import VideoStreamCtrl


def regist_router():
    restful_api.add_resource(CameraCtrl, '/camera')
    restful_api.add_resource(VideoCtrl, '/video')
    restful_api.add_resource(EventCtrl, '/event')
    restful_api.add_resource(VideoStreamCtrl, '/videofile')



