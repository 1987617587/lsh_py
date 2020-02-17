from django.conf.urls import url
from django.http import FileResponse

from . import views

app_name = "download"


def load(request, filename):
    return FileResponse(open(filename, "rb"), content_type='application/msword', filename=filename, as_attachment=True)


urlpatterns = [
    # 直接调用上面的下载函数，下载文件 文件名=filename(可以加路径)
    url(r'^(.*?)/$', load),

]
