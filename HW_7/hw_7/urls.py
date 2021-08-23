"""hw_7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
import hw_7_app.views as v
from hw_7_app.models import Post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.create_user, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user='post/'), name='login'),
    path('post/', v.PostList.as_view(), name='home'),
	path('post/<int:pk>/', v.PostDetail.as_view(), name='post_detail'),
    path('post/create/', v.PostCreate.as_view(), name='create'),
    path('post/update/<int:pk>/', v.PostUpdate.as_view(), name='update'),
]
