from django.shortcuts import render


class Sitedown():
    def __init__(self,get_response) :
        self.get_response= get_response

    def __call__(self, request) :
        return render(request,'siteuc.html')