# 从init 文件中导入模块
from . import db, Base


class Camera(Base):
    """摄像头机器表"""
    __tablename__ = 'camera'
    name = db.Column(db.String(255), comment="摄像头备注名称")
    address = db.Column(db.String(255), comment="ip地址")
    port = db.Column(db.String(50), comment="连接端口")
    username = db.Column(db.String(255), comment="连接用户名")
    password = db.Column(db.Text, default=None, comment="连接用户密码")
    serial_number = db.Column(db.String(255), comment="序列号")
    network_state = db.Column(db.String(255), default="良好", comment="网络状态")
    location = db.Column(db.String(255), comment="部署地点")
    longitude = db.Column(db.String(255), comment="部署地点坐标经度")
    latitude = db.Column(db.String(255), comment="部署地点坐标纬度")

    def toDict(self):
        dic = {}
        for column in self.__table__.columns:
                dic[column.name] = str(getattr(self, column.name))
        return dic


