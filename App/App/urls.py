from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('lists/', views.list_view, name='list_view'),
 #   path('list/<int:list_id>/item/<int:item_id>/', views.item_detail_view, name='item_detail_view'),
    path('list/<int:list_id>/', views.list_detail_view, name='list_detail_view'),
    path('list/create/', views.create_list_view, name='create_list_view'),
  #  path('list/<int:list_id>/update/', views.update_list_view, name='update_list_view'),
   # path('list/<int:list_id>/item/<int:item_id>/edit/', views.item_edit_view, name='item_edit_view'),
    path('list/<int:list_id>/item/create/', views.create_item_view, name='create_item_view'),
    path('list/<int:list_id>/item/<int:item_id>/complete/', views.mark_item_complete_view, name='mark_item_complete_view'),
    path('lists/<int:list_id>/delete/', views.delete_list_view, name='delete_list'),
]
