from flask import Response
from ..uitls import file_iterator


class VideoStreamSrv(object):
    @classmethod
    def getFileStream(cls, file_path: str):
        video_dir = 'highaltitudeparabolic/apps/videos/{}'
        video_path = video_dir.format(file_path)

        response = Response(file_iterator(video_path))
        response.headers['Content-Type'] = 'video/mp4'
        return response
