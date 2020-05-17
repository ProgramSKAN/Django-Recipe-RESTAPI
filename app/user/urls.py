from django.urls import path
from user import views

app_name='user'
urlpatterns = [
    path('create/',views.CreateUserView.as_view(),name='create'), #name is useful in reverse lookup unction
    path('token/',views.CreateTokenView.as_view(),name='token'), #name matches with test file 'TOKEN_URL=reverse('user:token')'
    path('me/',views.ManageUserView.as_view(),name='me'),
]
