# from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    # path("admin/", admin.site.urls),
    path("send_otp/", csrf_exempt(views.sendOtp), name="Send_otp"),
    path("verify_otp/", csrf_exempt(views.verifyOtp), name="Verify_otp"),
]
