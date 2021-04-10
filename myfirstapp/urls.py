from django.urls import path
from myfirstapp import views

urlpatterns = [
    path("", views.render_index),
    path("render_delete/<str:main_id>", views.render_delete, name = "delete_render"),
    path("perform_insertion", views.insert_portfolio, name="stock"),
    path("perform_delete/<str:main_id>", views.remove_portfolio, name="stock_remove"),
    path(r"^perform_edit/(?P<pk>[0-9]+)/$", views.edit_portfolio, name="stock_edit")
]