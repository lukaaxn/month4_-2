"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

import cinema.views
from users.views import register_view, login_view, logout_view
user_patterns = [
    path('register/', register_view),
    path('login/', login_view),
    path('logout/', logout_view),
]


urlpatterns = (
    user_patterns
    + [
        path('admin/', admin.site.urls),
        path('', cinema.views.home),
        path('movies/', cinema.views.movie_list),
        path('movies/<int:movie_id>/', cinema.views.movie_detail),
        path('movies/create/', cinema.views.movie_create_view),
        path('movies/<int:movie_id>/delete/', cinema.views.movie_delete_view),
    ] 
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)


