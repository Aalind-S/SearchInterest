from django.shortcuts import render
from .models import Person, Bank
import pyrebase
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BankSerializer, PersonSerializer
from rest_framework import generics
from rest_framework.views import APIView


config = {

    'apiKey': "AIzaSyD53J1lsvTz7FL8e7PUJkvB33LJ_rJp2Oc",

    'authDomain': "auth-portal-83536.firebaseapp.com",

    'projectId': "auth-portal-83536",

    'storageBucket': "auth-portal-83536.appspot.com",

    'messagingSenderId': "834294599954",

    'appId': "1:834294599954:web:858cd6201669edc9fda3cb",

    'measurementId': "G-TJQXW048K7",

    'databaseURL': "",

}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()


def signIn(request):

    return render(request, "signIn.html")


def postsignIn(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user = auth.sign_in_with_email_and_password(email, passw)
        return render(request, "welcome.html")

    except:
        return render()


def signUp(request):
    if request.method == "POST":
        email = request.POST.get('email')
        passw = request.POST.get('pass')
        name = request.POST.get('name')  # for the input with name = "name"
        age = request.POST.get('age')
        salary = request.POST.get('salary')
        info = Person.objects.create(Name=name, Age=age, Salary=salary, Email=email)

        info.save()
        user = auth.create_user_with_email_and_password(email, passw)

        return render(request, "signUp.html")


def reset(request):
    return render(request, "reset.html")


def postReset(request):

    email = request.POST.get('email')
    try:
        auth.send_password_reset_email(email)
        message = "An email to reset password is successfully sent"
        return render(request, "reset.html", {"msg": message})
    except email.DoesNotExist:
        message = "Something went wrong! Please Check the email you provided"
        return render(request, "reset.html", {"msg": message})


def comp_interest(request):
    principal = request.POST.get('principal')
    rate = request.POST.get('rate')
    compounding = request.POST.get('compounding')
    years = request.POST.get('years')
    amount = principal*((1+rate/compounding)**(compounding*years))
    interest = amount - principal
    context = {
        "amount": amount,
        "interest": interest
    }
    return render(request, "base.html", context)


'''



    writing              api                  views                   now


from rest_framework.generics import ListAPIView


'''


# @csrf_exempt
# @api_view(['GET', 'POST'])
# def getbank(request):
#    if request.method == "GET":
#    name = request.GET.get("name")
#        banker = Bank.objects.all()
#        serializer_class = BankSerializer(banker)
#        return Response(serializer_class.data)

class GetBank(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class getbank(generics.RetrieveAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class bankdetail(APIView):
    def get_object(self, pk, format=None):
        try:
            return Bank.objects.get(pk=pk)
        except Bank.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bank = self.get_object(pk)
        serializer = BankSerializer(bank)
        return Response(serializer.data)
