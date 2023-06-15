import datetime
from datetime import datetime as dt, timedelta
import hashlib
import json
import pandas
from django.http import JsonResponse, Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string, get_template
from django.views.generic import ListView, View, DetailView
from django.db.models import Q, Sum, Count
from django.db import connection
from collections import namedtuple
from annoying.functions import get_object_or_None
from endless_pagination.views import AjaxListView
from collections import defaultdict
from chartofaccount.models import Chartofaccount
from department.models import Department
from triplecvariousaccount.models import Triplecvariousaccount
from .models import TripleC
from .models import Triplecquota
from companyparameter.models import Companyparameter
from supplier.models import Supplier
from ataxcode.models import Ataxcode
from accountspayable.models import Apmain, Apdetail
from financial.utils import Render
from django.utils import timezone
from triplecbureau.models import Triplecbureau as Bureau
from triplecsection.models import Triplecsection as Section
from triplecsubtype.models import Triplecsubtype as Subtype
from triplecpublication.models import Triplecpublication as Publication
from triplecpage.models import Triplecpage as Page
from triplecrate.models import Triplecrate as Rate
from triplecclassification.models import Triplecclassification as Classification
from triplecsupplier.models import Triplecsupplier


upload_size = 3
textsuccess = "text-success"
textwarning = "text-warning"
dataexists = " Data exists"
errorsavingdata = " Error saving data"

@method_decorator(login_required, name='dispatch')
class IndexView(AjaxListView):
    model = TripleC
    template_name = 'triplec/index.html'
    context_object_name = 'data_list'

    # page_template = 'triplec/index_list.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['authors'] = Supplier.objects.all().filter(isdeleted=0, triplec=1).order_by('code')
        context['bureaus'] = Bureau.objects.all().filter(isdeleted=0).order_by('code')
        context['sections'] = Section.objects.all().filter(isdeleted=0).order_by('code')
        context['publications'] = Publication.objects.all().filter(isdeleted=0).order_by('code')
        context['pages'] = Page.objects.all().filter(isdeleted=0).order_by('code')
        context['classifications'] = Classification.objects.all().filter(isdeleted=0).order_by('code')
        
        return context


def generate_hash_key(issue_date,article_id,numofwords,numofcharacters):
    hash = hashlib.md5(str(issue_date) + str(article_id) + str(numofwords) + str(numofcharacters))
    return hash.hexdigest()


def fileprocess(request):
    df = pandas.read_excel(request.FILES['data_file'])

    # filter article status as 'Archived' only
    filtered = df[df['article status'] == 'Archived']
    records = filtered.to_json(orient='records')
    records = json.loads(records)

    return records


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        if request.FILES['data_file'] \
                and request.FILES['data_file'].name.endswith('.xls') \
                    or request.FILES['data_file'].name.endswith('.xlsx'):
            if request.FILES['data_file']._size < float(upload_size) * 1024 * 1024:
                
                try:
                    records = fileprocess(request)
                    records_count = len(records)
                    
                    successcount = 0
                    existscount = 0
                    failedcount = 0
                    faileddata = []
                    successrecords = []
                    
                    for record in records:
                        generated_key = generate_hash_key(record['Issue Date'], record['Article ID'], record['Number Of words'], record['NumberofCharacters'])
                        issue_date = pandas.to_datetime(record['Issue Date'], unit='ms')
                        
                        if TripleC.objects.filter(generated_key=generated_key).exists():
                            existscount += 1
                            faileddata.append([issue_date, record['Article ID'], record['Article Title'], record['Number Of words'], record['NumberofCharacters'], dataexists, textsuccess])
                        else:
                            save = savedata(record,generated_key,issue_date)
                            if save:
                                successrecords.append([record])
                                successcount += 1
                            else:
                                failedcount += 1
                                faileddata.append([issue_date, record['Article ID'], record['Article Title'], record['Number Of words'], record['NumberofCharacters'], errorsavingdata, textwarning])
                    
                    if successcount == records_count:
                        result = 1 
                    elif records_count == existscount:
                        result = 2
                    elif records_count == failedcount:
                        result = 3
                    else:
                        result = 4
                    
                    return JsonResponse({
                        'result': result,
                        'success_count': successcount,
                        'records_count': records_count,
                        'failed_data': faileddata,
                        'successrecords': successrecords
                    })
                
                except:
                    return JsonResponse({
                        'result': 3
                    })
    else:
        context = {
            # "banks": Bank.objects.all().order_by('description'),
            # "bankaccount": Bankaccount.objects.all().filter(isdeleted=0).order_by('code'),
            # "username": request.user,
        }
        return render(request, 'triplec/upload.html', context)
    

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters '''
    if string == '' or string is None:
        return str('')
    
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def savedata(record,generated_key,issue_date):
    try:
        article_title = strip_non_ascii(record['Article Title'])
        byline = strip_non_ascii(record['Byline'])
        created_by = strip_non_ascii(record['Created by'])
       
        TripleC.objects.create(
            generated_key=generated_key,
            cms_issue_date=issue_date,
            cms_article_status='A',
            cms_publication=str(record['Publication']),
            cms_section=str(record['Section']),
            cms_page=str(record['Page']),
            cms_article_id=str(record['Article ID']),
            cms_article_title=article_title,
            cms_byline=byline,
            cms_author_name=str(record['Author name']),
            cms_created_by=created_by,
            cms_no_of_words=int(record['Number Of words']),
            cms_no_of_characters=int(record['NumberofCharacters'])
        )
        return True
    except:
        return False
    
# optimize the speed of this function - ok in RetrieveView
# def retrieve(request):
#     print 'start'
#     dfrom = request.GET["dfrom"]
#     dto = request.GET["dto"]
#     type = request.GET["type"]
#     author_name = request.GET["author_name"]
#     status = request.GET["status"]
#     bureau = request.GET["bureau"]
#     # publication = request.GET["publication"]
#     section = request.GET["section"]
#     page = request.GET["page"]

#     triplec_data = TripleC.objects.filter(cms_issue_date__range=[dfrom, dto], isdeleted=0).order_by('pk')

#     if type != '':
#         triplec_data = triplec_data.filter(type=type)

#     if author_name != '':
#         triplec_data = triplec_data.filter(author_name__icontains=author_name)

#     if status != '':
#         if status == 'O_APV':
#             triplec_data = triplec_data.filter(status__icontains='O', apv_no__isnull=False).exclude(apv_no__exact='')
#         elif status == 'O':
#             triplec_data = triplec_data.filter(status__icontains=status).exclude(confirmation__exact='').exclude(apv_no__isnull=False)
#         else:
#             triplec_data = triplec_data.filter(status__icontains=status)

#     if bureau != '':
#         triplec_data = triplec_data.filter(bureau=bureau)

#     # if publication != '':
#     #     triplec_data = triplec_data.filter(publication=publication)

#     if section != '':
#         triplec_data = triplec_data.filter(section=section)

#     if page != '':
#         triplec_data = triplec_data.filter(page=page)
    
#     viewhtml = ''
#     context = {}
#     context['triplec_data'] = triplec_data
#     context['authors'] = Supplier.objects.filter(isdeleted=0, triplec=1).order_by('code')
#     context['bureaus'] = Bureau.objects.filter(isdeleted=0).order_by('code')
#     context['pages'] = Page.objects.filter(isdeleted=0).order_by('code')
#     context['publications'] = Publication.objects.filter(isdeleted=0).order_by('code')
#     context['sections'] = Section.objects.filter(isdeleted=0).order_by('code')
#     context['subtypes'] = Subtype.objects.filter(isdeleted=0).order_by('code')
#     context['rates'] = Rate.objects.filter(isdeleted=0).order_by('code')
#     context['classifications'] = Classification.objects.filter(isdeleted=0).order_by('code')
#     context['dfrom'] = dfrom
#     context['dto'] = dto

#     print 'render_to_string'
#     present_time = dt.now()
#     viewhtml = render_to_string('triplec/transaction_result.html', context)
#     end_time = dt.now()
#     time_difference = end_time - present_time
#     print 'endrender_to_string'
#     print 'time', time_difference.total_seconds()
    
#     data = {
#         'status': 'success',
#         'viewhtml': viewhtml
#     }
#     print 'end'
#     return JsonResponse(data)


class RetrieveView(DetailView):
    model = TripleC
    template_name = 'triplec/transaction_result.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            dfrom = request.GET.get('dfrom')
            dto = request.GET.get('dto')
            type = request.GET["type"]
            author_name = request.GET["author_name"]
            status = request.GET["status"]
            bureau = request.GET["bureau"]
            section = request.GET["section"]
            page = request.GET["page"]

            triplec_data = TripleC.objects.filter(cms_issue_date__range=[dfrom, dto], isdeleted=0).order_by('pk')

            if type != '':
                triplec_data = triplec_data.filter(type=type)

            if author_name != '':
                triplec_data = triplec_data.filter(author_name__icontains=author_name)

            if status != '':
                if status == 'O_APV':
                    triplec_data = triplec_data.filter(status__icontains='O', apv_no__isnull=False).exclude(apv_no__exact='')
                elif status == 'O':
                    triplec_data = triplec_data.filter(status__icontains=status).exclude(confirmation__exact='').exclude(apv_no__isnull=False)
                else:
                    triplec_data = triplec_data.filter(status__icontains=status)

            if bureau != '':
                triplec_data = triplec_data.filter(bureau=bureau)

            if section != '':
                triplec_data = triplec_data.filter(section=section)

            if page != '':
                triplec_data = triplec_data.filter(page=page)

            context = {}
            context['triplec_data'] = triplec_data
            context['authors'] = Supplier.objects.filter(isdeleted=0, triplec=1).order_by('code')
            context['bureaus'] = Bureau.objects.filter(isdeleted=0).order_by('code')
            context['pages'] = Page.objects.filter(isdeleted=0).order_by('code')
            context['sections'] = Section.objects.filter(isdeleted=0).order_by('code')
            context['subtypes'] = Subtype.objects.filter(isdeleted=0).order_by('code')
            context['rates'] = Rate.objects.filter(isdeleted=0).order_by('code')
            context['classifications'] = Classification.objects.filter(isdeleted=0).order_by('code')
            context['dfrom'] = dfrom
            context['dto'] = dto
            # start_time = dt.now()
            
            template = get_template(self.get_template_names()[0])
            html_content = template.render(context, request)
            
            # end_time = dt.now()
            # time_difference = end_time - start_time
            # print 'time', time_difference.total_seconds()
            return HttpResponse(html_content, content_type='text/html')
        else:
            return super().get(request, *args, **kwargs)

@csrf_exempt
def save_batch_tagging(request):
    form_data = json.loads(request.POST.getlist('data')[0])
    result = 'success'
    for data in form_data:
        try:
            triplec = TripleC.objects.filter(pk=data['id'])
            if triplec[0].code != data['code'] or triplec[0].type != data['type']:
                triplec.update(code=data['code'], author_name=data['author'], type=data['type'], \
                    modifyby_id=request.user.id, modifydate=datetime.datetime.now())
        except:
            result = 'failed'

    return JsonResponse({
        'result': result
    })


@csrf_exempt
def get_supplier_by_type(request):
    if request.is_ajax and request.method == 'GET':
        ccc = request.GET['ccc']
        try:
            if ccc != '':
                data = Supplier.objects.filter(isdeleted=0, triplec=1, ccc=ccc) \
                    .values('id', 'code', 'name').order_by('code')
            else:
                data = Supplier.objects.filter(isdeleted=0, triplec=1) \
                    .values('id', 'code', 'name').order_by('code')

            return JsonResponse({
                    'data': list(data), 
                    'result': 'success'
                })
        except:
            return JsonResponse({'result': 'Get supplier by type call failed'})
    else:
        return JsonResponse({'result': 'Get supplier by type call failed'})
     

@csrf_exempt
def get_supplier_by_code(request):
    data = {}
    if request.is_ajax and request.method == 'GET':
        code = request.GET['code']
        try:
            if code != '':
                supplier = Supplier.objects.values('id', 'name', 'ccc').filter(code=code)
                
                data={'result': True, 'supplier': list(supplier)}
            else:
                data={'result': False, 'message': 'Code is required'}    
        except:
           data={'result': False, 'message': 'Get supplier by code call failed'}
    else:
        data={'result': False, 'message': 'Method not allowed'}

    return JsonResponse(data)

@csrf_exempt
def get_supplier_by_name(request):
    data = {}
    if request.is_ajax and request.method == 'GET':
        name = request.GET['name']
        try:
            if name != '':
                supplier = Supplier.objects.filter(isdeleted=0, triplec=1, name=name).values('code', 'ccc')
                data={'result': True, 'supplier': list(supplier)}
            else:
                data={'result': False, 'message': 'Code is required'}
        except:
            data={'result': False, 'message': 'Get supplier by name call failed'}
    else:
        data={'result': False, 'message': 'Method not allowed'}
    return JsonResponse(data)
    

@csrf_exempt
def supplier_suggestion(request):
    data = {}
    if request.is_ajax and request.method == 'GET':
        code = request.GET['code']
        try:
            if code != '':
                supplier = Supplier.objects.get(code=code).pk
                triplecsupplier = Triplecsupplier.objects.values('bureau', 'section').filter(supplier=supplier)
                
                data={'result': True, 'triplecsupplier': list(triplecsupplier)}
            else:
                data={'result': False, 'message': 'Code is required'}    
        except Exception as e:
           print e
           data={'result': False, 'message': 'Supplier suggestion call failed'}
    else:
        data={'result': False, 'message': 'Method not allowed'}

    return JsonResponse(data)


# add validation here
# validate lahat ng butas or disable fields na malaki epekto kung i-update like name
@csrf_exempt
def save_transaction_entry(request):
    if request.is_ajax and request.method == 'POST':
        try:

            triplec = TripleC.objects.filter(pk=request.POST['id'])
            
            status = 'E'
            if triplec[0].apv_no:
                return JsonResponse({
                    'result': False,
                    'message': 'Could not be saved. This transaction is already Posted to AP - #'+ str(triplec[0].apv_no)
                })
            elif triplec[0].status == 'O':
                status = 'O'
                
            triplec.update(
                issue_date=request.POST['issue_date'],
                supplier_id=request.POST['supplier_id'],
                code=request.POST['code'],
                author_name=request.POST['author_name'],
                type=request.POST['type'],
                subtype=request.POST['subtype'],
                bureau=request.POST['bureau'],
                section=request.POST['section'],
                article_title=request.POST['article_title'],
                no_ccc=request.POST['no_of_ccc'],
                no_items=request.POST['no_of_items'],
                page=request.POST['page_no'],
                no_of_words=request.POST['no_of_words'],
                no_of_characters=request.POST['no_of_characters'],
                length1=request.POST['length1'],
                length2=request.POST['length2'],
                length3=request.POST['length3'],
                length4=request.POST['length4'],
                width1=request.POST['width1'],
                width2=request.POST['width2'],
                width3=request.POST['width3'],
                width4=request.POST['width4'],
                total_size=request.POST['total_size'],
                rate_code=request.POST['rate_code'],
                amount=request.POST['amount'],
                status=status,
                modifyby_id=request.user.id, 
                modifydate=datetime.datetime.now()
            )
            data = {'result': True}
            # else:
            #     data = {
            #         'result': False,
            #         'message': 'Updating is not allowed with this status'
            #     }
        except Exception as e:
            print e, type(e)
            data = {
                    'result': False,
                    'message': 'Unable to save this transaction'
                }
    else:
        data = {
                'result': False,
                'message': 'Method not allowed'
            }
        
    return JsonResponse(data)


# revert transaction status as Ready for Posting
@csrf_exempt
def revert_transaction(request):
    if request.is_ajax and request.method == 'POST':
        try:

            triplec = TripleC.objects.filter(pk=request.POST['id'])

            if triplec[0].status == 'O' and (triplec[0].apv_no == None or triplec[0].apv_no == ''):

                confirmation = triplec[0].confirmation

                Triplecquota.objects.filter(confirmation=confirmation).update(
                    isdeleted=1,
                    modifyby_id=request.user.id,
                    modifydate=datetime.datetime.now()
                )

                triplec.update(
                    confirmation='',
                    status='E',
                    modifyby_id=request.user.id,
                    modifydate=datetime.datetime.now()
                )
                data = {
                    'result': True,
                    'message': 'Revert transaction successful.'
                }
            elif triplec[0].status == 'E' and triplec[0].confirmation == '':
                data = {
                    'result': False,
                    'message': 'This transaction is Ready for Posting or has been reverted already.'
                }
            else:
                data = {
                    'result': False,
                    'message': 'The transaction is already posted to APV: AP#'+ str(triplec[0].apv_no)
                }
        except Exception as e:
            data = {
                'result': False,
                'message': 'An error occured: '+ str(e)
            }
    else:
        data = {
                'result': False,
                'message': 'Method not allowed'
            }
        
    return JsonResponse(data)


@csrf_exempt
def count_csno(request):
    if request.is_ajax and request.method == 'POST':
        try:
            count = TripleC.objects.filter(confirmation=request.POST['csno']).count()
            print 'countcs', count
            data = {
                    'result': True,
                    'message': 'Success',
                    'count': count
                }
        except Exception as e:
            data = {
                'result': False,
                'message': 'An error occured: '+ str(e)
            }
    else:
        data = {
                'result': False,
                'message': 'Method not allowed'
            }
        
    return JsonResponse(data)


# change year into year of transaction date and add validation for uniqueness
def get_confirmation():
    try:
        triplec = TripleC.objects.latest()

        if triplec.confirmation:
            last_cs = triplec.confirmation
        else:
            year = datetime.date.today().year
            last_cs = str(year) + '000000'

        return last_cs
        
    except Exception:
        # fault tolerance - for fixing
        return '0000000000'


@method_decorator(login_required, name='dispatch')
class ProcessTransactionView(ListView):
    model = TripleC
    template_name = 'triplec/process_transaction/index.html'
    context_object_name = 'data_list'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('triplec.process_transaction_triplec'):
            raise Http404
        return super(ListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
       context = super(ProcessTransactionView, self).get_context_data(**kwargs)
       context['triplec'] = TripleC.objects.all().filter(isdeleted=0).order_by('code')
       context['authors'] = Supplier.objects.all().filter(isdeleted=0, triplec=1)
       
       return context


@method_decorator(login_required, name='dispatch')
class GenerateProcessTransaction(View):
    def get(self, request):
        try:
            dfrom = request.GET['dfrom']
            dto = request.GET['dto']
            author_name = request.GET['author_name']
            code = request.GET['code']
            classification = request.GET['classification']

            if dfrom != '' and dto != '':
                triplec_data = TripleC.objects.filter(issue_date__range=[dfrom, dto], status='E', isdeleted=0)\
                    .values('code', 'type')
                
            elif dfrom != '' and dto == '':
                triplec_data = TripleC.objects.filter(issue_date=dfrom, status='E', isdeleted=0)\
                    .values('code', 'type')
                
            elif dfrom == '' and dto != '':
                triplec_data = TripleC.objects.filter(issue_date=dto, status='E', isdeleted=0)\
                    .values('code', 'type')
            else:
                return JsonResponse({
                    'status': 'failed',
                    'message': 'Transaction date is required'
                })
            
            triplec_data = triplec_data.annotate(total=Sum('amount'), transactions=Count('pk')).order_by('code')
            
            if author_name != '':
                triplec_data = triplec_data.filter(author_name=author_name)
            # print triplec_data[0]['code'], triplec_data[0]['total']
            
            param = {}
            for key in range(len(triplec_data)):
                
                if dfrom != '' and dto != '':
                    param[key] = TripleC.objects.filter(issue_date__range=[dfrom, dto], status='E', isdeleted=0, code=triplec_data[key]['code'], type=triplec_data[key]['type'])
                elif dfrom != '' and dto == '':
                    param[key] = TripleC.objects.filter(issue_date=dfrom, status='E', isdeleted=0, code=triplec_data[key]['code'], type=triplec_data[key]['type'])
                elif dfrom == '' and dto != '':
                    param[key] = TripleC.objects.filter(issue_date=dto, status='E', isdeleted=0, code=triplec_data[key]['code'], type=triplec_data[key]['type'])
            
            data = {
                'status': 'success',
                'viewhtml': render_to_string('triplec/process_transaction/generate.html', {"triplec_data": param})
            }

            return JsonResponse(data)
        except:
            return JsonResponse({
                'status': 'failed',
                'message': 'An error occured'
            })
        

@csrf_exempt
def transaction_posting(request):
    if request.method == 'POST':
        try:
            transactions = json.loads(request.POST.getlist('data')[0])
            
            olditem = ''
            newitem = ''
            existing = []
            csnums = []

            for item in transactions:

                newitem = item['code']+'sep'+item['type']
                csno = get_confirmation()
                
                try:
                    triplec = TripleC.objects.filter(pk=item['pk'])
                    
                    if triplec[0].status != 'O':
                        if newitem != olditem:
                            new_csno = int(csno) + 1
                            triplec.update(
                                confirmation=new_csno, 
                                date_posted= datetime.datetime.now(), 
                                status='O', 
                                modifyby_id=request.user.id,
                                modifydate=datetime.datetime.now()
                            )
                            olditem = newitem
                            csnums.append(new_csno)

                        else:
                            triplec.update(
                                confirmation=csno, 
                                date_posted= datetime.datetime.now(), 
                                status='O', 
                                modifyby_id=request.user.id,
                                modifydate=datetime.datetime.now()
                            )
                    else:
                        existing.append([triplec[0].confirmation, newitem])

                except:
                    response = {
                        'result': False,
                        'message': 'Unable to save transaction for '+ item['code'] + '. Processing stopped, please retry.'
                    }

            if not existing:
                success_quota = process_quota(request, csnums)
                if success_quota == True:
                    response = {'result': True}
                else:
                    response = {
                        'result': False,
                        'message': 'An internal error: ' + str(success_quota)
                    }
            else:   
                response = {
                    'result': 'existing',
                    'message': 'Already posted transaction(s) has been detected.',
                    'existing': existing
                }
            
        except:
            response = {
                'result': False,
                'message': 'An internal error occured while processing your transaction.'
            }
    else:
        response = {
            'result': False,
            'message': 'Method not allowed'
        }

    return JsonResponse(response)


def process_quota(request, csnums):
    if csnums:
        try:
            for i in range(len(csnums)):
                transactions = TripleC.objects.filter(confirmation=csnums[i], type='COR')

                if transactions:

                    num_items = transactions.aggregate(num_items=Sum('no_items'))
                    total_size = transactions.aggregate(size=Sum('total_size'))
                    num_photos = transactions.filter(subtype__description__icontains='PHOTO').count()
                    num_articles = transactions.filter(subtype__description__icontains='ARTICLE').count()

                    additional = Triplecvariousaccount.objects.filter(isdeleted=0, type='addtl')
                    
                    if (num_photos > 0 and (num_photos >= 8 or num_items['num_items'] >= 8)) and (num_articles > 0 and total_size >= 50):
                        
                        transpo = additional.get(code='TRANSPO').amount 
                        transpo2 = additional.get(code='TRANSPO2').amount 

                        trans = transpo + transpo2
                        cellcard = additional.get(code='TEL').amount

                        Triplecquota.objects.create(
                            confirmation = csnums[i],
                            no_item = max(num_articles, num_items['num_items']),
                            type = 'A',
                            transportation_amount = trans,
                            cellcard_amount = cellcard,
                            enterby_id = request.user.id,
                            enterdate = datetime.datetime.now(),
                            modifyby_id = request.user.id,
                            modifydate = datetime.datetime.now()
                        )

                    elif num_photos > 0 and (num_photos >= 8 or num_items['num_items'] >= 8):

                        transpo2 = additional.get(code='TRANSPO2').amount
                        Triplecquota.objects.create(
                            confirmation=csnums[i],
                            no_item = max(num_photos, num_items['num_items']),
                            type = 'P',
                            transportation_amount = transpo2,
                            enterby_id = request.user.id,
                            enterdate = datetime.datetime.now(),
                            modifyby_id = request.user.id,
                            modifydate = datetime.datetime.now()
                        )
                    elif num_articles > 0 and total_size >= 50:

                        transpo = additional.get(code='TRANSPO').amount 
                        cellcard = additional.get(code='TEL').amount

                        Triplecquota.objects.create(
                            confirmation = csnums[i],
                            no_item = max(num_articles, num_items['num_items']),
                            type = 'A',
                            transportation_amount = transpo,
                            cellcard_amount = cellcard,
                            enterby_id = request.user.id,
                            enterdate = datetime.datetime.now(),
                            modifyby_id = request.user.id,
                            modifydate = datetime.datetime.now()
                        )
            return True
        except Exception as e:
            return e
          

def print_cs(request):

    triplec_ids = json.loads(request.GET['q'])
    parameter = {}
    info = {}

    data_list = []

    for triplec_id in triplec_ids:
        try:
            data_list.append(TripleC.objects.values('pk', 'code', 'author_name', 'confirmation', 'date_posted').get(pk=triplec_id, status='O', isdeleted=0))
        except Exception as e:
            print e

    grouped_list = defaultdict(list)

    for item in data_list:
        grouped_list[
            item['confirmation']
        ].append(
            [item['pk']]
        )

    for csno, ids in grouped_list.items():

        csno = str(csno)
        parameter[csno] = {}
        details = {}
        batch_cs = TripleC.objects.filter(confirmation=csno, status='O', isdeleted=0)

        parameter[csno]['main'] = batch_cs.first()

        has_quota = get_object_or_None(Triplecquota, confirmation=csno, status='A', isdeleted=0)
        
        quota_amount = 0
        with_additional = False
        if has_quota:
            transpo = has_quota.transportation_amount
            cellcard = has_quota.cellcard_amount

            quota_amount = transpo + cellcard
            with_additional = True

            parameter[csno]['transportation_amount'] = transpo
            parameter[csno]['cellcard_amount'] = cellcard
        
        atc_id = Supplier.objects.get(code=parameter[csno]['main'].code).atc_id
        rate = Ataxcode.objects.get(pk=atc_id).rate

        subtotal = batch_cs.aggregate(subtotal=Sum('amount'))
        subtotal = float(subtotal['subtotal'])
        total = subtotal + float(quota_amount)
        ewt = percentage(float(rate), total)
        net = total - ewt

        parameter[csno]['size'] = batch_cs.aggregate(total_size=Sum('total_size'))
        parameter[csno]['with_additional'] = with_additional
        parameter[csno]['ataxrate'] = rate
        parameter[csno]['subtotal'] = subtotal
        parameter[csno]['total'] = total
        parameter[csno]['ewt'] = ewt
        parameter[csno]['net'] = net
        
        for id in ids:
            index = str(id[0])
            details[index] = TripleC.objects.get(pk=id[0])

        parameter[csno]['details'] = details
    
    info['logo'] = request.build_absolute_uri('/static/images/pdi.jpg')
    info['parameter'] = Companyparameter.objects.get(code='PDI', isdeleted=0, status='A')
    
    return render(request, 'triplec/process_transaction/print_cs.html', {'info': info, 'parameter': parameter})


def percentage(percent, whole):
    if whole:
        return (percent * whole) / 100.0
    
    return 0.00


@method_decorator(login_required, name='dispatch')
class ReportView(ListView):
    model = TripleC
    template_name = 'triplec/report/index.html'
    context_object_name = 'data_list'

    def dispatch(self, request, *args, **kwargs):
        return super(ListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        context['triplec'] = TripleC.objects.all().filter(isdeleted=0).order_by('code')
        context['authors'] = Supplier.objects.all().filter(isdeleted=0, triplec=1)
        context['bureaus'] = Bureau.objects.all().filter(isdeleted=0).order_by('code')
        context['sections'] = Section.objects.all().filter(isdeleted=0).order_by('code')
       
        return context
    

@method_decorator(login_required, name='dispatch')
class GeneratePDF(View):
    def get(self, request):

        company = Companyparameter.objects.all().first()
        datalist = []
        parameter = {}

        if request.method == 'GET' and request.GET['blank'] != '1':
            dfrom = request.GET['from']
            dto = request.GET['to']
            type = request.GET['type']
            bureau = request.GET['bureau']
            section = request.GET['section']

            q = TripleC.objects.filter(issue_date__range=[dfrom, dto], status='O', isdeleted=0)\
                .values('pk', 'code', 'author_name', 'subtype_id', 'amount').annotate(totalamount=Sum('amount')).order_by('code')
            
            has_bureau = False
            has_section = False
            has_type = False
            summary_by = 'CCC Summary Report'
            ccc_type = ''

            if type:
                has_type = True
                summary_by = 'Summary Report by CCC'
                if type == 'CON':
                    ccc_type = 'CONTRIBUTOR'
                elif type == 'COL':
                    ccc_type = 'COLUMNIST'
                elif type == 'COR':
                    ccc_type = 'CORRESPONDENT'

            if bureau:
                has_bureau = True
                summary_by = 'Summary Report by Bureau'

                q.filter(bureau=bureau)

            if section: 
                has_section = True
                summary_by = 'Summary Report by Section'
            q.annotate(totalamount=Sum('amount')).order_by('code')
            print 'Whole', q
            # stopped here, do the computation of amount and quantity
            # grouped_list = defaultdict(list)
            # for item in q: 
            #     grouped_list[
            #         item['code']
            #     ].append(
            #         [item['pk']]
            #     )
            
            # print grouped_list

            # for code, ids in grouped_list.items():
            #     parameter[code] = {}
            #     amount = 0
            #     photos = 0
            #     articles = 0
            #     for id in ids:
            #         # print id[0]
            #         row = TripleC.objects.filter(id=id[0]).values('subtype', 'amount').get()
            #         print row
            #         print row['subtype'], row['amount']
            datalist = q
            dates = 'AS OF ' + datetime.datetime.strptime(dfrom, '%Y-%m-%d').strftime('%b. %d, %Y')\
                + ' TO ' + datetime.datetime.strptime(dto, '%Y-%m-%d').strftime('%b. %d, %Y')
            
            context = {
                "today": timezone.now(),
                "company": company,
                "list": datalist,
                "username": request.user,
                "heading": {
                    'dates': dates,
                    'bureau':bureau,
                    'section': section, 
                    'ccc_type': ccc_type,
                    'has_bureau': has_bureau, 
                    'has_section': has_section, 
                    'has_type':has_type,
                    'summary_by': summary_by,
                    'logo': request.build_absolute_uri('/static/images/pdi.jpg'),
                }
            }
        else:
             context = {
                "today": timezone.now(),
                "company": company,
                "list": list,
                "username": request.user,
                "heading": {
                    'logo': request.build_absolute_uri('/static/images/pdi.jpg'),
                }
            }
             
        return Render.render('triplec/report/pdf.html', context)
        

def get_apnum(pdate):
    apnumlast = lastAPNumber('true')
    latestapnum = str(apnumlast[0])
    apnum = pdate[:4]
    last = str(int(latestapnum) + 1)
    zero_addon = 6 - len(last)
    for num in range(0, zero_addon):
        apnum += '0'
    apnum += last

    return apnum
    

@csrf_exempt
def goposttriplec(request):

    if request.method == 'POST':

        pkslist = request.POST.getlist('ids[]')
        postdate = request.POST['postdate']
        pdate = datetime.datetime.strptime(postdate, '%m/%d/%Y').strftime('%Y-%m-%d')

        data_list = TripleC.objects.filter(pk__in=pkslist,isdeleted=0,status='O').values('pk', 'confirmation')
        
        grouped_list = defaultdict(list)

        for item in data_list:
            grouped_list[
                item['confirmation']
            ].append(
                [item['pk']]
            )
        
        if grouped_list:
            already_posted = 0
            total_trans = 0
            successful_trans = 0

            for csno, ids in grouped_list.items():
                
                apnum = get_apnum(pdate)
                billingremarks = 'Test'
                
                try:
                    total_trans += 1
                    triplec = TripleC.objects.filter(confirmation=csno,status='O').first()

                    if triplec.apv_no:
                        already_posted += 1
                    else:
                        supplier = Supplier.objects.get(pk=triplec.supplier_id)
                        various_account = Triplecvariousaccount.objects

                        main = Apmain.objects.create(
                            apnum = apnum,
                            apdate = pdate,
                            aptype_id = 14, # Non-UB
                            apsubtype_id = 16, # Triple C
                            branch_id = 5, # Head Office
                            inputvattype_id = 3, # Service
                            creditterm_id = 2, # 90 Days 2
                            payee_id= supplier.id,
                            payeecode= supplier.code,
                            payeename= supplier.name,
                            vat_id = 8, # NA 8
                            vatcode = 'VATNA', # NA 8
                            vatrate = 0,
                            atax_id = 66, # NO ATC 66
                            ataxcode = 'WX000', # NO ATC 66
                            ataxrate = 0,
                            duedate = pdate,
                            refno = triplec.confirmation,
                            particulars = str(triplec.type)+' '+str(billingremarks),
                            currency_id = 1,
                            fxrate = 1,
                            designatedapprover_id = 225, # Arlene Astapan
                            approverremarks = 'For approval from Triple C Posting',
                            responsedate = datetime.datetime.now(),
                            apstatus = 'F',
                            enterby_id = request.user.id,
                            enterdate = datetime.datetime.now(),
                            modifyby_id = request.user.id,
                            modifydate = datetime.datetime.now()
                        )

                        counter = 1
                        amount = 0
                        entries = []

                        triplec_supplier = Triplecsupplier.objects.filter(supplier=supplier.id).first()
                        department = Department.objects.get(pk=triplec_supplier.department_id)
                        expchart = Chartofaccount.objects.get(pk=department.expchartofaccount_id)

                        # identify chartofaccount of each transaction
                        for id in ids:
                            expc = get_expc(expchart, id)
                            entries.append({'id':id, 'expc':expc})

                        grouped_entries = defaultdict(list)

                        for item in entries:
                            grouped_entries[
                                item['expc']
                            ].append(
                                item['id']
                            )
                        
                        for coa, entry_ids in grouped_entries.items():
                            # sort transactions by similar chartofaccount
                            idlist = []
                            for i in entry_ids:
                                idlist.append(i[0])
                            
                            tc = TripleC.objects.filter(pk__in=idlist).aggregate(sum_amount=Sum('amount'))

                            TripleC.objects.filter(pk__in=idlist).update(
                                apv_no = main.apnum,
                                date_apv = main.apdate,
                            )

                            Apdetail.objects.create(
                                apmain_id = main.id,
                                ap_num = main.apnum,
                                ap_date = main.apdate,
                                item_counter = counter,
                                debitamount = tc['sum_amount'],
                                creditamount = '0.00',
                                balancecode = 'D',
                                amount = tc['sum_amount'],
                                chartofaccount_id = coa,
                                department_id = department.id,
                                status='A',
                                enterby_id = request.user.id,
                                enterdate = datetime.datetime.now(),
                                modifyby_id = request.user.id,
                                modifydate = datetime.datetime.now()
                            )
                            amount += tc['sum_amount']
                            counter += 1

                        has_quota = get_object_or_None(Triplecquota, confirmation=csno)

                        if has_quota:
                            # quota - transpo
                            transpo = various_account.get(code='TRANSPO', type='addtl', isdeleted=0)
                            if transpo:
                                
                                if expchart.accountcode == '5100000000':
                                    transpoexpc = transpo.chartexpcostofsale_id
                                elif expchart.accountcode == '5200000000':
                                    transpoexpc = transpo.chartexpgenandadmin_id
                                else:
                                    transpoexpc = transpo.chartexpsellexp_id

                                counter += 1
                                Apdetail.objects.create(
                                    apmain_id = main.id,
                                    ap_num = main.apnum,
                                    ap_date = main.apdate,
                                    item_counter = counter,
                                    debitamount = has_quota.transportation_amount,
                                    creditamount = '0.00',
                                    balancecode = 'D',
                                    amount = has_quota.transportation_amount,
                                    chartofaccount_id = transpoexpc,
                                    department_id = department.id,
                                    status='A',
                                    enterby_id = request.user.id,
                                    enterdate = datetime.datetime.now(),
                                    modifyby_id = request.user.id,
                                    modifydate = datetime.datetime.now()
                                )
                                amount += has_quota.transportation_amount

                            # quota - cellcard
                            cellcard = various_account.get(code='TEL', type='addtl', isdeleted=0)
                            if cellcard:

                                if expchart.accountcode == '5100000000':
                                    cellcardexpc = cellcard.chartexpcostofsale_id
                                elif expchart.accountcode == '5200000000':
                                    cellcardexpc = cellcard.chartexpgenandadmin_id
                                else:
                                    cellcardexpc = cellcard.chartexpsellexp_id

                                counter += 1
                                Apdetail.objects.create(
                                    apmain_id = main.id,
                                    ap_num = main.apnum,
                                    ap_date = main.apdate,
                                    item_counter = counter,
                                    debitamount = has_quota.cellcard_amount,
                                    creditamount = '0.00',
                                    balancecode = 'D',
                                    amount = has_quota.cellcard_amount,
                                    chartofaccount_id = cellcardexpc,
                                    department_id = department.id,
                                    status='A',
                                    enterby_id = request.user.id,
                                    enterdate = datetime.datetime.now(),
                                    modifyby_id = request.user.id,
                                    modifydate = datetime.datetime.now()
                                )
                                amount += has_quota.cellcard_amount

                        companyparameter = Companyparameter.objects.get(code='PDI', isdeleted=0, status='A')
                        atc_id = Supplier.objects.get(pk=supplier.id).atc_id
                        rate = Ataxcode.objects.get(pk=atc_id).rate
                        
                        ewt = percentage(float(rate), float(amount))
                        aptrade_amount = float(amount) - float(ewt)
                        counter += 1

                        # EWT
                        Apdetail.objects.create(
                            apmain_id = main.id,
                            ap_num = main.apnum,
                            ap_date = main.apdate,
                            item_counter = counter,
                            debitamount = '0.00',
                            creditamount = ewt,
                            balancecode = 'C',
                            ataxcode_id = atc_id,
                            chartofaccount_id = companyparameter.coa_ewtax_id,
                            supplier_id = supplier.id,      
                            status='A',
                            enterby_id = request.user.id,
                            enterdate = datetime.datetime.now(),
                            modifyby_id = request.user.id,
                            modifydate = datetime.datetime.now()
                        )
                        
                        counter += 1
                        # AP TRADE
                        Apdetail.objects.create(
                            apmain_id = main.id,
                            ap_num = main.apnum,
                            ap_date = main.apdate,
                            item_counter = counter,
                            debitamount = '0.00',
                            creditamount = aptrade_amount,
                            balancecode = 'C',
                            chartofaccount_id = companyparameter.coa_aptrade_id,
                            supplier_id = supplier.id,      
                            status='A',
                            enterby_id = request.user.id,
                            enterdate = datetime.datetime.now(),
                            modifyby_id = request.user.id,
                            modifydate = datetime.datetime.now()
                        )

                        main.amount = amount
                        main.save()

                        successful_trans += 1

                except Exception as e:
                    print 'errorrr', e
                    response = {'status': 'error', 'message': 'Internal error occured'}
            if already_posted > 0 and successful_trans > 0:
                response = {'status': 'error', 'message': 'Successfully posted '+str(successful_trans)+' transactions. However, there are '+ str(already_posted)+ ' transactions have been already posted'}
            elif successful_trans == 0 or already_posted == total_trans:
                response = {'status': 'error', 'message': 'All transactions have been posted and are not allowed for reposting.'}
            else:
                response = {'status': 'success'}
        else:
            response = {'status': 'error', 'message': 'Transactions for posting to AP could not be found. No CS#'}
    else:
        response = {'status': 'error', 'message': 'Method not allowed'}
    
    return JsonResponse(response)


def get_expc(expchart, id):
    entry = TripleC.objects.get(pk=id[0])
    various_account = Triplecvariousaccount.objects
    expc = 0
    priorities = Subtype.objects.exclude(various_account__isnull=True)

    # spcecial cases only e.g. type is Photo as CF-PHOTO
    if priorities:
        for priority in priorities:

            if entry.subtype_id == priority.id:
                expc = various_account.get(pk=priority.various_account_id).chartexpcostofsale_id
                return expc

    account_id = Classification.objects.get(code=entry.type)    

    if entry.type == 'COL':
        expc = various_account.get(pk=account_id.various_account_id).chartexpcostofsale_id

    elif entry.type == 'CON':
        if expchart.accountcode == '5100000000':
            expc = various_account.get(pk=account_id.various_account_id).chartexpcostofsale_id
        elif expchart.accountcode == '5200000000':
            expc = various_account.get(pk=account_id.various_account_id).chartexpgenandadmin_id
        else:
            expc = various_account.get(pk=account_id.various_account_id).chartexpsellexp_id

    elif entry.type == 'COR':
        supplier_id = Supplier.objects.get(code=entry.code).id
        various_account_id = Triplecsupplier.objects.get(supplier_id=supplier_id).various_account_id
        
        if various_account_id:
            expc = various_account.get(pk=various_account_id).chartexpcostofsale_id
        else:
            # city corres
            expc = 614

    return expc
    

def lastAPNumber(param):
    # print "Summary"
    ''' Create query '''
    cursor = connection.cursor()

    query = "SELECT  SUBSTRING(apnum, 5) AS num FROM apmain ORDER BY id DESC LIMIT 1"

    cursor.execute(query)
    result = namedtuplefetchall(cursor)

    return result[0]


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]
