from django.urls import path
from todo_app.views import itemCreateView, itemUpdateView, itemListView, itemDeleteView

app_name = "todo_app"
urlpatterns = [
    path('', itemListView.as_view(), name='home'),
    path('add/', itemCreateView.as_view(), name='add'),
    path('<int:pk>', itemUpdateView.as_view(), name='detail'),
    path('<int:pk>/delete', itemDeleteView.as_view(), name='delete')

]
