from django.urls import include, path

from .views import FoodListView

urlpatterns = [
    path('food_list/', FoodListView.as_view(), name='food_list'),
]