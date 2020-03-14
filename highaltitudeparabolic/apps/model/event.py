# 从init 文件中导入模块
from . import db, Base


class Event(Base):
    """摄像头时间表"""
    __tablename__ = 'event'
    camera_name = db.Column(db.String(255), comment="时间对应的摄像头名称")
    name = db.Column(db.String(500), comment="事件名称")
    address = db.Column(db.Text, comment="事件的详细地点")
    object_name = db.Column(db.String(255), comment="抛出物体的名称")
    occurrence_time = db.Column(db.DateTime, comment="事件的发生时间")

    fall_time = db.Column(db.String(255), comment="物体下路时间")
    casualties = db.Column(db.String(50), comment="是否造成人员伤亡")
    communicate_residents = db.Column(db.String(50), comment="是否与住户进行沟通")
    security_level = db.Column(db.String(50), default="轻度危害", comment="是否与住户进行沟通")
    notes = db.Column(db.Text, comment="事件备注")
    video_name = db.Column(db.Text, comment="事件的视频文件名称")

    def toDict(self):
        dic = {}
        for column in self.__table__.columns:
                dic[column.name] = str(getattr(self, column.name))
        return dic
