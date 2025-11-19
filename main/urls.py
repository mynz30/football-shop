from django.urls import path
from .views import (
    show_main, create_product, show_product,
    show_xml, show_json, show_xml_by_id, show_json_by_id,
    register, login_user, logout_user, edit_product, delete_product,
    add_to_cart, create_product_flutter,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("create-product/", create_product, name="create_product"),
    path("create-flutter/", create_product_flutter, name="create_product_flutter"),  # TAMBAHAN
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
]