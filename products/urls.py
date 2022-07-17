from .views import products, basket_add,basket_delete
from django.urls import path

app_name = 'products'
urlpatterns = [
    path('', products, name='index'),
    path('<int:category_id>/', products, name='category'),
    path('page/<int:page>/', products, name='page'),
    path('basket-add/<int:product_id>/', basket_add, name='basket-add'),
    path('basket-delete/<int:id>/', basket_delete, name='basket-delete'),

]
