from django.urls import path
from .views import (
    show_main, create_product, show_product,
    show_xml, show_json, show_xml_by_id, show_json_by_id,
    register, login_user, logout_user, edit_product, delete_product,
    add_to_cart,
    # AJAX endpoints
    get_products_json, create_product_ajax, update_product_ajax, 
    delete_product_ajax, login_ajax, register_ajax,
    get_product_detail_json,  
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("create-product/", create_product, name="create_product"),
    path("product/<int:id>/", show_product, name="show_product"),
    path("product/<int:id>/edit", edit_product, name="edit_product"),  
    path("product/<int:id>/delete", delete_product, name="delete_product"), 
    path("xml/", show_xml, name="show_xml"),
    path("json/", show_json, name="show_json"),
    path("xml/<int:id>/", show_xml_by_id, name="show_xml_by_id"),
    path("json/<int:id>/", show_json_by_id, name="show_json_by_id"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("product/<int:id>/add-to-cart/", add_to_cart, name="add_to_cart"),
    
    # AJAX API endpoints
    path("api/products/", get_products_json, name="get_products_json"),
    path("api/products/create/", create_product_ajax, name="create_product_ajax"),
    path("api/products/<int:id>/", get_product_detail_json, name="get_product_detail_json"),  
    path("api/products/<int:id>/update/", update_product_ajax, name="update_product_ajax"),
    path("api/products/<int:id>/delete/", delete_product_ajax, name="delete_product_ajax"),
    path("api/login/", login_ajax, name="login_ajax"),
    path("api/register/", register_ajax, name="register_ajax"),
]