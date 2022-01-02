from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.AddInstituteView.as_view(),name='add_institute'),
    path('show/',views.InstituteListView.as_view(),name='show_list'),
    path('update/<int:i>/',views.UpdateView.as_view(),name='update'),
    path('delete/<int:i>/',views.DeleteView.as_view(),name='delete'),

]