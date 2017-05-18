from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
#     这个是请求详情id
    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
]