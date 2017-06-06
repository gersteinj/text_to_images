from django.conf.urls import url

from . import views

app_name = 'webtool'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^image/$', views.image, name='image'),
	url(r'^wordimage/$', views.word_image, name='word_image'),
	url(r'^chooseword/(?P<sent_word>[a-zZ-Z0-9]+)/$', views.selected_word, name='selected_word'),
	url(r'^tti/$', views.tti, name='tti'),
]