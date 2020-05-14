from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lines', views.lines, name='lines'),
    path('timetable', views.timetable, name='timetable'),
    path('info', views.info, name='info'),
    path('getLineType', views.get_line_type, name='getLineType'),
    path('getVariantStops', views.get_variant_stops, name='getVariantStops')
]
