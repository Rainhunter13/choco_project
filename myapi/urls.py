from django.urls import include, path
from rest_framework import routers
from myapi import views


class ProductListRouter(routers.DefaultRouter):
    routers = [
        routers.Route(
            url=r'^{prefix}/$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': ''}
        ),
    ]


class ProductRouter(routers.DefaultRouter):
    routes = [
        routers.Route(
            url=r'^{prefix}/{lookup}/$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': ''}
        ),
    ]


product_list_router = ProductListRouter()
product_list_router.register('product', views.ProductListViewSet)

product_router = ProductRouter()
product_router.register('product', views.ProductViewSet)

urlpatterns = [
    path('', include(product_list_router.urls), name="Product List"),
    path('', include(product_router.urls), name="Product"),
    path('<str:seller>/', views.seller_product_list, name="Seller Product List"),
    path('<str:seller>/<int:id>/', views.seller_product, name="Seller Product"),
    path('category/<str:ctg>/', views.category, name="Category"),
    path('category/<str:ctg>/min_price/', views.category_min_price, name="Category Min Price"),
    path('category/<str:ctg>/max_price/', views.category_max_price, name="Category Max Price"),
]
