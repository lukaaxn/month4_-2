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

import food.views
from users.views import register_view, login_view, logout_view
user_patterns = [
    path('register/', register_view),
    path('login/', login_view),
    path('logout/', logout_view)
]


urlpatterns = (
    user_patterns
    + [
        path('admin/', admin.site.urls),
        path('', food.views.home),
        path('foods/', food.views.food_list),
        path('foods/<int:food_id>/', food.views.food_detail),
        path('foods/create/', food.views.food_create_view),
        path('foods/<int:food_id>/delete/', food.views.food_delete_view),
        path('foods/<int:food_id>/add-to-cart/', food.views.add_to_cart_view),
    ] 
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)


