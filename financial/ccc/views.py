from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from endless_pagination.views import AjaxListView

@method_decorator(login_required, name='dispatch')
class IndexView(AjaxListView):
    model = Ccc
    template_name = 'ccc/index.html'
    context_object_name = 'data_list'

    page_template = 'ccc/index_list.html'

    def get_context_data(self, **kwargs):
       context = super(IndexView, self).get_context_data(**kwargs)
    #    context['bankaccount'] = Bankaccount.objects.all().filter(isdeleted=0).order_by('code')
       
       return context


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        return True
    else:
        context = {
            # "banks": Bank.objects.all().order_by('description'),
            # "bankaccount": Bankaccount.objects.all().filter(isdeleted=0).order_by('code'),
            # "username": request.user,
        }
        return render(request, 'ccc/upload.html', context)