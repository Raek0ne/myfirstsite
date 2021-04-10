from django.urls import path
from myfirstapp import views

urlpatterns = [
    path("", views.render_index),
    path("perform_insertion", views.insert_portfolio, name="stock"),
    path(r"^perform_delete/(?P<pk>[0-9]+)/$", views.remove_portfolio, name="stock_remove"),
    path(r"^perform_edit/(?P<pk>[0-9]+)/$", views.edit_portfolio, name="stock_edit")
]