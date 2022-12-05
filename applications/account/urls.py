from django.urls import path

from applications.account.views import RegisterApiView, LoginApiView, LogoutApiView, ChangePasswordApiView, \
    send_hello_api_view, CreateBookAPIView

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login/', LoginApiView.as_view()),
    path('logout/', LogoutApiView.as_view()),
    path('change_password/', ChangePasswordApiView.as_view()),
    path('send_mail/', send_hello_api_view),
    path('createbook/', CreateBookAPIView.as_view()),
]