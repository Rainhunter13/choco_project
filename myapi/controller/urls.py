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


class CategoryRouter(routers.DefaultRouter):
    routes = [
        routers.Route(
            url=r'^{prefix}/$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': ''}
        ),
        routers.DynamicRoute(
            url=r'^{prefix}/{url_path}/$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        ),
    ]


product_list_router = ProductListRouter()
product_list_router.register('product', views.ProductListViewSet)

product_router = ProductRouter(trailing_slash=False)
product_router.register('product', views.ProductViewSet)

category_router = CategoryRouter()
category_router.register('laptop', views.LaptopViewSet)
category_router.register('tablet', views.TabletViewSet)
category_router.register('monitor', views.MonitorViewSet)
category_router.register('eBook', views.EBookViewSet)

urlpatterns = [
    path('', include(product_router.urls), name="Product"),
    path('', include(product_list_router.urls), name="Product List"),
    path('', include(category_router.urls), name="Product List by Category"),
]
