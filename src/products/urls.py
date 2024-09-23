from django.urls import path
from . import views 

urlpatterns = [
    path("sales", views.sales, name = "sales_route"),
    path("", views.list, name = "products_route"),
    path("details/<int:id>", views.details, name = "details_route"),
    path("category", views.categories, name = "categories_route"),
    path("new", views.insert, name = "insert_route"),
    path("newCategory", views.insertCategory, name = "insertCategory_route"),
    path("edit/<int:id>", views.edit, name = "edit_route"),
    path("editCategory/<int:id>", views.editCategory, name = "editCategory_route"),
    path("delete/<int:id>", views.delete, name = "delete_route"),
    path("deleteCategory/<int:id>", views.deleteCategory, name = "deleteCategory_route"),

]
