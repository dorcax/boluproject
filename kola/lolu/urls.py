from django.urls import path
from . import views
urlpatterns=[
    path('lolu/',views.index,name='lolu-index'),
    path('order/',views.order,name='lolu-order'),
    path('product/',views.product,name='lolu-product'),
    path('staff/',views.staff,name='lolu-staff'),
    

    
]