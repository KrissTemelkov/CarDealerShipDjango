from django.shortcuts import render


def profile_info(request):
    return render(request, 'accounts/accountInfo.html')
