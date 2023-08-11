from django.urls import path 
from .views import registration_view,login_view,logout_view,home_view,booking_view,agency_view,route_view,booking_list_view

urlpatterns=[
    path('',home_view),
    path('agencies/',agency_view),
    path('booking/',booking_view),
    path('route/<int:id>',route_view),
    path('booking_list/',booking_list_view),
    path('register/',registration_view),
    path('login/',login_view),
    path('logout/',logout_view),
]