# 从init 文件中导入模块
from . import db, Base


class Video(Base):
    """摄像头下的所有原始视频表"""
    __tablename__ = 'video'
    camera_name = db.Column(db.String(255), comment="时间对应的摄像头名称")
    name = db.Column(db.String(255), comment="文件名")
    start_date = db.Column(db.DateTime, comment="视频的起始时间")
    end_date = db.Column(db.DateTime, comment="视频的结束时间")

    def toDict(self):
        dic = {}
        for column in self.__table__.columns:
            dic[column.name] = str(getattr(self, column.name))
        return dic
