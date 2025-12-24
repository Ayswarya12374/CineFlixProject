from django.shortcuts import render,redirect

# Create your views here.
from django.views import View
from .models import SubscriptionPlans
from django.utils.decorators import method_decorator

from authentication.permissions import permitted_user_roles
from .forms import SubscriptionForm

class SubscriptionsView(View):

    template='subscriptions/subscription-list.html'

    def get(self,request,*args,**kwargs):

        plans=SubscriptionPlans.objects.all()

        data={'plans':plans}

        return render(request,self.template,context=data)
    
@method_decorator(permitted_user_roles(['Admin']),name='dispatch')
class SubscriptionCreateView(View):

    form_class=SubscriptionForm

    template= 'subscriptions/subscription-create.html'

    def get(self,request,*args,**kwargs):

        
        form=self.form_class()

        data= {'page':'Create subscription',
               'form':form
              }

        return render(request,self.template,context=data)
    
    def post(self,request,*args,**kwargs):

       

        form=self.form_class(request.POST)

        if form.is_valid() :

            form.save()                    
            
            return redirect('subscription-list')
      
        
        data={'form':form,'page':'Create subscription'}
        
        return render(request,self.template,context=data)
    
class SubscriptionDeleteView(View):

    def get(self,*args,**kwargs):

         uuid=kwargs.get('uuid')

         subscription=SubscriptionPlans.objects.get(uuid=uuid)

        #  movie.delete()--hard delete
        
        #soft delete
         subscription.active_status=False

         subscription.save()

         return redirect('subscription-list')        