from django.urls import include, path
from rest_framework import routers
from myapi.controller import views


class ProductListRouter(routers.DefaultRouter):
    routers = [
        routers.Route(
            url=r'^{prefix}$',
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
            initkwargs={'suffix': 'Detail'}
        ),
    ]


class SellerRouter(routers.DefaultRouter):
    routers = [
        routers.Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': ''}
        ),
        routers.Route(
            url=r'^{prefix}/{lookup}/$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
    ]


product_list_router = ProductListRouter()
product_list_router.register('product', views.ProductListViewSet)

product_router = ProductRouter()
product_router.register('product', views.ProductViewSet)

seller_router = SellerRouter()
seller_router.register('sulpak', views.SulpakViewSet)
seller_router.register('technodom', views.TechnodomViewSet)
seller_router.register('mechta', views.MechtaViewSet)
seller_router.register('veter', views.VeterViewSet)

urlpatterns = [
    path('', include(seller_router.urls), name="Seller"),
    path('', include(product_list_router.urls), name="Product List"),
    path('', include(product_router.urls), name="Product"),
    path('<str:cat>/', views.category, name="Category"),
    path('<str:cat>/min_price', views.category_min_price, name="Category Min Price"),
    path('<str:cat>/max_price', views.category_max_price, name="Category Max Price"),
]
