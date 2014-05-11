
from django.conf.urls import patterns, include, url
from hazard import views


urlpatterns = patterns('',
    url(
        r'^flood-warning/create/$',
        views.FloodingWarningCreateView.as_view(),
        name='view',
    ),
)
