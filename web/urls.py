from django.urls import path
from .views import overview, product, location, movement, delete

urlpatterns = [
    path('', overview.as_view(), name='overview'),
    path('location', location.as_view(), name='location'),
    path('product', product.as_view(), name='product'),
    path('movement', movement.as_view(), name='movement'),
    path('delete', delete.as_view(), name='delete')
]
