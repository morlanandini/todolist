from django.urls import path, include
from app import views
app_name='app'
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('reg/',views.registration_page, name='registration_page'),
    path('login_page/',views.login_page,name='login_page'),
    path('todo_page/',views.todo_page,name='todo_page'),
    path('see/',views.see,name='see'),
    # path('otp_page/',views.otp_page,name='otp_page'),
    # path('opt_verification_function/',views.opt_verification_function,name='opt_verification_function'),

]
