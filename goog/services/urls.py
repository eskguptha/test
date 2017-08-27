from django.conf.urls import url
from services import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^stock$', views.stock_rest, name='stock_rest'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
