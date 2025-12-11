from django.shortcuts import render

# Create your views here.
from django.views import View


class SubscriptionsView(View):

    template='subscriptions/subscription-list.html'

    def get(self,request,*args,**kwargs):

        return render(request,self.template)