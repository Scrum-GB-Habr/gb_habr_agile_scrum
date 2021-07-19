from . import views
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post'),
    path('success/', views.PostSuccessMessageView.as_view(), name='success'),
    path('dashboard/', views.PostDashboardView.as_view(), name='dashboard'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
    path('help/', views.HelpView.as_view(), name='help'),
]
