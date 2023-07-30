from django.shortcuts import render, redirect
import os
from twilio.rest import Client
from django.http import HttpResponse
from .forms import UserCreationForm, VerifyForm
from django.contrib.auth.decorators import login_required
from . import verify
from .decorators import verification_required


@login_required
@verification_required
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            verify.send(form.cleaned_data['phone'])
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def verify_code(request):
    if request.method == 'POST':
        form = VerifyForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            if verify.check(request.user.phone, code):
                request.user.is_verified = True
                request.user.save()
                return redirect('index')
    else:
        form = VerifyForm()
    return render(request, 'verify.html', {'form': form})


def send_otp(request):
    # Download the helper library from https://www.twilio.com/docs/python/install
    import os
    from twilio.rest import Client

    # Set environment variables for your credentials
    # Read more at http://twil.io/secure
    account_sid = "AC127adafcc4914a2ec70e8f3c142d2f7d"
    auth_token = "15c345c0dfe2f31f4447fdfd94db9ca6"
    verify_sid = "VA48af433d25aaefd01a0af7c18425c110"
    verified_number = "+905380586316"

    client = Client(account_sid, auth_token)

    verification = client.verify.v2.services(verify_sid) \
        .verifications \
        .create(to=verified_number, channel="sms")
    print(verification.status)

    otp_code = input("Please enter the OTP:")

    verification_check = client.verify.v2.services(verify_sid) \
        .verification_checks \
        .create(to=verified_number, code=otp_code)
    print(verification_check.status)


def home(request):
    account_sid = 'YOUR_ACCOUNT_SID'
    auth_token = 'YOUR_AUTH_TOKEN'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Hi there..',
        from_='YOUR_TRIAL_NUMBER',
        to='VERIFIED_NUMBER'
    )

    return HttpResponse('Message Sent Successfully..')
