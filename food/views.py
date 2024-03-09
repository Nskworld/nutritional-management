from django.shortcuts import render
from django.views.generic import ListView
from .models import Food

class FoodListView(ListView):
    model = Food
    template_name = 'food/food_list.html'
    context_object_name = 'food_list'
    paginate_by = 20

    def get_queryset(self):
        return Food.objects.filter(delete_flg=False).order_by('-created_datetime')

