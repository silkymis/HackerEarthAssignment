from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt


from .views import ApplyFilterView



urlpatterns = [
				url(r'^v1/applyfilter/$', csrf_exempt(ApplyFilterView.as_view())),
			]