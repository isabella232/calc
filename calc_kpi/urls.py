from django.conf.urls import include, url

from .views import price_compare

urlpatterns = [
    url(r'^percentage_compare',price_compare.percentage_compare,name="percentage_compare")
    #I don't remember if this is right...following https://docs.djangoproject.com/en/1.10/intro/tutorial01/
]
