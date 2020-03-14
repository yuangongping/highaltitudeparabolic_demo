from flask import Response


class VideoStreamSrv(object):
    @classmethod
    def getFileStream(cls, filename: str):
        if filename:
            path = r"D:\pythonWorkSpace\highaltitudeparabolic_demo\highaltitudeparabolic\apps\vidoes\{}.mp4".format(filename)
        else:
            path = r"D:\pythonWorkSpace\highaltitudeparabolic_demo\highaltitudeparabolic\apps\vidoes\1.mp4"

        def chunck(filename):
            with open(filename, 'rb') as target_file:
                while True:
                    chunk = target_file.read(512)
                    if chunk:
                        yield chunk
                    else:
                        break
        response = Response(chunck(path))
        response.headers['Content-Type'] = 'video/mp4'
        return response
