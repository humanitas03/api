from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from product import views
from util.common import API_COMMON_PATH

urlpatterns = [
    path(API_COMMON_PATH+'products/', views.product_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
