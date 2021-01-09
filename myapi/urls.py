from django.urls import include, path
from rest_framework import routers
from . import views


class ProductListRouter(routers.DefaultRouter):
    routers = [
        routers.Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}  # suffix change does not make sense for some reason
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


product_list_router = ProductListRouter()
product_list_router.register('product', views.ProductListViewSet)

product_router = ProductRouter(trailing_slash=False)
product_router.register('product', views.ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(product_router.urls), name="Product"),
    path('', include(product_list_router.urls), name="Product List"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
