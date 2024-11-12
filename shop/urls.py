from django.urls import path, re_path
from . import views

urlpatterns = [
    # path("<str:shop_page>" , views.page , name="shop_pages"),
    path("<page>", views.redirect_pages, name="redirect_pages"),
    path("products/<str:product_page>", views.product_pages, name="productpages"),
    path("products/<str:product_page>/<int:product>", views.specific_productint),
    # path("products/<str:product_page>/<str:product>", views.specific_productint),
    path("", views.shop_page, name="shop_main"),
    path("products/", views.product_list_page, name="product_page"),
    # path("products", views.redirect_slash_product,),
    # re_path(r'^products/?$', views.product_list_page, name="product_page"),
]