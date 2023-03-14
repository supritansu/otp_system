from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
import random
from . import serializers, models
from rest_framework.decorators import api_view


@api_view(["POST"])
def sendOtp(request):
    # dict = {"result": "success"}
    #

    if request.method == "POST":
        mobile_number = request.data.get("mobile_number")
        if not mobile_number:
            return JsonResponse({"error": "Mobile number is required."}, status=400)
        elif len(mobile_number) < 10:
            return JsonResponse(
                {"error": "Please enter a valid mobile number."}, status=400
            )
        otp = random.randint(100000, 999999)

        newuser = models.Customer(mobile_number=mobile_number, otp=otp)
        newuser.save()

        return JsonResponse(
            {
                "result": True,
                "message": f"Otp sent sucessfully to {mobile_number}",
                "otp": otp,
            }
        )


@api_view(["POST"])
def verifyOtp(request):
    if request.method == "POST":
        mobile_number = request.data.get("mobile_number")

        if not mobile_number:
            return JsonResponse({"error": "Mobile number is required."}, status=400)
        elif len(mobile_number) < 10:
            return JsonResponse(
                {"error": "Please enter a valid mobile number."}, status=400
            )
        otp = request.data.get("otp")

        if not otp:
            return JsonResponse({"error": "OTP is required."}, status=400)
        elif len(otp) != 6:
            return JsonResponse({"error": "Please enter a valid otp."}, status=400)
        exisuser = models.Customer.objects.filter(
            mobile_number=mobile_number, otp=otp
        ).first()
        if exisuser == None:
            return JsonResponse({"error": "Invalid otp/mobile number."}, status=400)
        dict = {"id": exisuser.id, "mobile_number": exisuser.mobile_number}

        return JsonResponse(dict, status=200)
