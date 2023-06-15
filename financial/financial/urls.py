"""financial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout, password_change

admin.site.index_template = 'admin/index.html'
admin.autodiscover()

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index2/', views.index2, name='index2'),
    url(r'^admin/', admin.site.urls),

    # Apps URLS
    url(r'^mainproduct/', include('mainproduct.urls', app_name='mainproduct', namespace='mainproduct')),
    url(r'^product/', include('product.urls', app_name='product', namespace='product')),
    url(r'^adtype/', include('adtype.urls', app_name='adtype', namespace='adtype')),
    url(r'^journalvoucher/', include('journalvoucher.urls', app_name='journalvoucher', namespace='journalvoucher')),
    url(r'^acctentry/', include('acctentry.urls', app_name='acctentry', namespace='acctentry')),
    url(r'^inventoryitemtype/', include('inventoryitemtype.urls', app_name='inventoryitemtype', namespace='inventoryitemtype')),
    url(r'^inventoryitemclass/', include('inventoryitemclass.urls', app_name='inventoryitemclass', namespace='inventoryitemclass')),
    url(r'^inventoryitem/', include('inventoryitem.urls', app_name='inventoryitem', namespace='inventoryitem')),

    # Apps Grace
    url(r'^vat/', include('vat.urls', app_name='vat', namespace='vat')),
    url(r'^wtax/', include('wtax.urls', app_name='wtax', namespace='wtax')),
    url(r'^mainunit/', include('mainunit.urls', app_name='mainunit', namespace='mainunit')),
    url(r'^unit/', include('unit.urls', app_name='unit', namespace='unit')),
    url(r'^typeofexpense/', include('typeofexpense.urls', app_name='typeofexpense', namespace='typeofexpense')),
    url(r'^currency/', include('currency.urls', app_name='currency', namespace='currency')),
    url(r'^industry/', include('industry.urls', app_name='industry', namespace='industry')),
    url(r'^bankaccounttype/', include('bankaccounttype.urls', app_name='bankaccounttype', namespace='bankaccounttype')),
    url(r'^cvtype/', include('cvtype.urls', app_name='cvtype', namespace='cvtype')),
    url(r'^aptype/', include('aptype.urls', app_name='aptype', namespace='aptype')),
    url(r'^bankaccount/', include('bankaccount.urls', app_name='bankaccount', namespace='bankaccount')),
    url(r'^customertype/', include('customertype.urls', app_name='customertype', namespace='customertype')),
    url(r'^creditterm/', include('creditterm.urls', app_name='creditterm', namespace='creditterm')),
    url(r'^customer/', include('customer.urls', app_name='customer', namespace='customer')),
    url(r'^mainsupplier/', include('mainsupplier.urls', app_name='mainsupplier', namespace='mainsupplier')),
    url(r'^collector/', include('collector.urls', app_name='collector', namespace='collector')),
    url(r'^maininventory/', include('maininventory.urls', app_name='maininventory', namespace='maininventory')),
    url(r'^serviceinformation/', include('serviceinformation.urls', app_name='serviceinformation', namespace='serviceinformation')),
    url(r'^outputvat/', include('outputvat.urls', app_name='outputvat', namespace='outputvat')),
    url(r'^supplier/', include('supplier.urls', app_name='supplier', namespace='supplier')),
    url(r'^mainsupplier_supplier/', include('mainsupplier_supplier.urls', app_name='mainsupplier_supplier', namespace='mainsupplier_supplier')),
    url(r'^companyparameter/', include('companyparameter.urls', app_name='companyparameter', namespace='companyparameter')),
    url(r'^employee/', include('employee.urls', app_name='employee', namespace='employee')),
    url(r'^debitcreditmemosubtype/', include('debitcreditmemosubtype.urls', app_name='debitcreditmemosubtype', namespace='debitcreditmemosubtype')),
    url(r'^purchaseorder/', include('purchaseorder.urls', app_name='purchaseorder', namespace='purchaseorder')),
    url(r'^requisitionform/', include('requisitionform.urls', app_name='requisitionform', namespace='requisitionform')),
    url(r'^rfprfapproval/', include('rfprfapproval.urls', app_name='rfprfapproval', namespace='rfprfapproval')),
    url(r'^operationalfund/', include('operationalfund.urls', app_name='operationalfund', namespace='operationalfund')),
    url(r'^checkvoucher/', include('checkvoucher.urls', app_name='checkvoucher', namespace='checkvoucher')),
    url(r'^debitcreditmemo/', include('debitcreditmemo.urls', app_name='debitcreditmemo', namespace='debitcreditmemo')),
    url(r'^agenttype/', include('agenttype.urls', app_name='agenttype', namespace='agenttype')),
    url(r'^agent/', include('agent.urls', app_name='agent', namespace='agent')),
    url(r'^replenish_pcv/', include('replenish_pcv.urls', app_name='replenish_pcv', namespace='replenish_pcv')),
    url(r'^cvsubtype/', include('cvsubtype.urls', app_name='cvsubtype', namespace='cvsubtype')),
    url(r'^replenish_rfv/', include('replenish_rfv.urls', app_name='replenish_rfv', namespace='replenish_rfv')),
    url(r'^apsubtype/', include('apsubtype.urls', app_name='apsubtype', namespace='apsubtype')),
    url(r'^jvsubtype/', include('jvsubtype.urls', app_name='jvsubtype', namespace='jvsubtype')),
    url(r'^officialreceipt/', include('officialreceipt.urls', app_name='officialreceipt', namespace='officialreceipt')),
    url(r'^acknowledgementreceipt/', include('acknowledgementreceipt.urls', app_name='acknowledgementreceipt', namespace='acknowledgementreceipt')),
    url(r'^arsubtype/', include('arsubtype.urls', app_name='arsubtype', namespace='arsubtype')),
    url(r'^dcartype/', include('dcartype.urls', app_name='dcartype', namespace='dcartype')),
    url(r'^cmsadjustment/', include('cmsadjustment.urls', app_name='cmsadjustment', namespace='cmsadjustment')),
    url(r'^processing_transaction/', include('processing_transaction.urls', app_name='processing_transaction', namespace='processing_transaction')),
    url(r'^processing_jv/', include('processing_jv.urls', app_name='processing_jv', namespace='processing_jv')),
    url(r'^chartofaccountmainsubgroup/', include('chartofaccountmainsubgroup.urls', app_name='chartofaccountmainsubgroup', namespace='chartofaccountmainsubgroup')),
    url(r'^chartofaccountmaingroup/', include('chartofaccountmaingroup.urls', app_name='chartofaccountmaingroup', namespace='chartofaccountmaingroup')),
    url(r'^chartofaccountsubgroup/', include('chartofaccountsubgroup.urls', app_name='chartofaccountsubgroup', namespace='chartofaccountsubgroup')),
    url(r'^transactionposting/', include('transactionposting.urls', app_name='transactionposting', namespace='transactionposting')),
    url(r'^transactionclosing/', include('transactionclosing.urls', app_name='transactionclosing', namespace='transactionclosing')),
    url(r'^rep_booksofaccounts/', include('rep_booksofaccounts.urls', app_name='rep_booksofaccounts', namespace='rep_booksofaccounts')),

    # Apps Kelvin
    url(r'^ataxcode/', include('ataxcode.urls', app_name='ataxcode', namespace='ataxcode')),
    url(r'^inputvat/', include('inputvat.urls', app_name='inputvat', namespace='inputvat')),
    url(r'^inputvattype/', include('inputvattype.urls', app_name='inputvattype', namespace='inputvattype')),
    url(r'^kindofexpense/', include('kindofexpense.urls', app_name='kindofexpense', namespace='kindofexpense')),
    url(r'^mistype/', include('mistype.urls', app_name='mistype', namespace='mistype')),
    url(r'^bank/', include('bank.urls', app_name='bank', namespace='bank')),
    url(r'^bankbranch/', include('bankbranch.urls', app_name='bankbranch', namespace='bankbranch')),
    url(r'^branch/', include('branch.urls', app_name='branch', namespace='branch')),
    url(r'^mainmodule/', include('mainmodule.urls', app_name='mainmodule', namespace='mainmodule')),
    url(r'^module/', include('module.urls', app_name='module', namespace='module')),
    url(r'^chartofaccount/', include('chartofaccount.urls', app_name='chartofaccount', namespace='chartofaccount')),
    url(r'^ofsubtype/', include('ofsubtype.urls', app_name='ofsubtype', namespace='ofsubtype')),
    url(r'^oftype/', include('oftype.urls', app_name='oftype', namespace='oftype')),
    url(r'^ortype/', include('ortype.urls', app_name='ortype', namespace='ortype')),
    url(r'^paytype/', include('paytype.urls', app_name='paytype', namespace='paytype')),
    url(r'^potype/', include('potype.urls', app_name='potype', namespace='potype')),
    url(r'^serviceclassification/', include('serviceclassification.urls', app_name='serviceclassification', namespace='serviceclassification')),
    url(r'^productgroup/', include('productgroup.urls', app_name='productgroup', namespace='productgroup')),
    url(r'^unitofmeasure/', include('unitofmeasure.urls', app_name='unitofmeasure', namespace='unitofmeasure')),
    url(r'^suppliertype/', include('suppliertype.urls', app_name='suppliertype', namespace='suppliertype')),
    url(r'^advertisingcategory/', include('advertisingcategory.urls', app_name='advertisingcategory', namespace='advertisingcategory')),
    url(r'^artype/', include('artype.urls', app_name='artype', namespace='artype')),
    url(r'^fxtype/', include('fxtype.urls', app_name='fxtype', namespace='fxtype')),
    url(r'^companyproduct/', include('companyproduct.urls', app_name='companyproduct', namespace='companyproduct')),
    url(r'^circulationproduct/', include('circulationproduct.urls', app_name='circulationproduct', namespace='circulationproduct')),
    url(r'^circulationcategory/', include('circulationcategory.urls', app_name='circulationcategory', namespace='circulationcategory')),
    url(r'^maingroupproduct/', include('maingroupproduct.urls', app_name='maingroupproduct', namespace='maingroupproduct')),
    url(r'^mrstype/', include('mrstype.urls', app_name='mrstype', namespace='mrstype')),
    url(r'^company/', include('company.urls', app_name='company', namespace='company')),
    url(r'^productbudget/', include('productbudget.urls', app_name='productbudget', namespace='productbudget')),
    url(r'^department/', include('department.urls', app_name='department', namespace='department')),
    url(r'^departmentbudget/', include('departmentbudget.urls', app_name='departmentbudget', namespace='departmentbudget')),
    url(r'^jvtype/', include('jvtype.urls', app_name='jvtype', namespace='jvtype')),
    url(r'^rep_chartofaccount/', include('rep_chartofaccount.urls', app_name='rep_chartofaccount', namespace='rep_chartofaccount')),
    url(r'^rep_department/', include('rep_department.urls', app_name='rep_department', namespace='rep_department')),
    url(r'^rep_supplier/', include('rep_supplier.urls', app_name='rep_supplier', namespace='rep_supplier')),
    url(r'^rep_customer/', include('rep_customer.urls', app_name='rep_customer', namespace='rep_customer')),
    url(r'^purchaserequisitionform/', include('purchaserequisitionform.urls', app_name='purchaserequisitionform', namespace='purchaserequisitionform')),
    url(r'^canvasssheet/', include('canvasssheet.urls', app_name='canvasssheet', namespace='canvasssheet')),
    url(r'^accountspayable/', include('accountspayable.urls', app_name='accountspayable', namespace='accountspayable')),
    url(r'^bankbranchdisburse/', include('bankbranchdisburse.urls', app_name='bankbranchdisburse', namespace='bankbranchdisburse')),
    url(r'^utils/', include('utils.urls', app_name='utils', namespace='utils')),
    url(r'^cashdisbursement/', include('cashdisbursement.urls', app_name='cashdisbursement', namespace='cashdisbursement')),
    url(r'^outputvattype/', include('outputvattype.urls', app_name='outputvattype', namespace='outputvattype')),
    url(r'^orsubtype/', include('orsubtype.urls', app_name='orsubtype', namespace='orsubtype')),
    url(r'^creditcard/', include('creditcard.urls', app_name='creditcard', namespace='creditcard')),
    url(r'^user_employee/', include('user_employee.urls', app_name='user_employee', namespace='user_employee')),
    url(r'^processing_or/', include('processing_or.urls', app_name='processing_or', namespace='processing_or')),
    url(r'^processing_data/', include('processing_data.urls', app_name='processing_data', namespace='processing_data')),
    url(r'^locationcategory/', include('locationcategory.urls', app_name='locationcategory', namespace='locationcategory')),
    url(r'^productgroupcategory/', include('productgroupcategory.urls', app_name='productgroupcategory', namespace='productgroupcategory')),
    url(r'^circulationpaytype/', include('circulationpaytype.urls', app_name='circulationpaytype', namespace='circulationpaytype')),
    url(r'^filemanagement/', include('filemanagement.urls', app_name='filemanagement', namespace='filemanagement')),
    url(r'^dcclasstype/', include('dcclasstype.urls', app_name='dcclasstype', namespace='dcclasstype')),
    url(r'^budgetapproverlevels/', include('budgetapproverlevels.urls', app_name='budgetapproverlevels', namespace='budgetapproverlevels')),
    url(r'^generaljournalbook/', include('generaljournalbook.urls', app_name='generaljournalbook', namespace='generaljournalbook')),
    url(r'^rep_generalledger/', include('rep_generalledger.urls', app_name='rep_generalledger', namespace='rep_generalledger')),
    url(r'^reportdashboard/', include('reportdashboard.urls', app_name='reportdashboard', namespace='reportdashboard')),
    url(r'^rep_bir/', include('rep_bir.urls', app_name='rep_bir', namespace='rep_bir')),
    url(r'^rep_master/', include('rep_master.urls', app_name='rep_master', namespace='rep_master')),
    url(r'^generalledgerbook/', include('generalledgerbook.urls', app_name='generalledgerbook', namespace='generalledgerbook')),

    # New Module
    url(r'^orinquiry/', include('orinquiry.urls', app_name='orinquiry', namespace='orinquiry')),
    url(r'^cvinquiry/', include('cvinquiry.urls', app_name='cvinquiry', namespace='cvinquiry')),
    url(r'^jvinquiry/', include('jvinquiry.urls', app_name='jvinquiry', namespace='jvinquiry')),
    url(r'^apinquiry/', include('apinquiry.urls', app_name='apinquiry', namespace='apinquiry')),
    url(r'^budgetreport/', include('budgetreport.urls', app_name='budgetreport', namespace='budgetreport')),

    # Aileen
    url(r'^rftype/', include('rftype.urls', app_name='rftype', namespace='rftype')),
    url(r'^prftype/', include('prftype.urls', app_name='prftype', namespace='prftype')),
    url(r'^cstype/', include('cstype.urls', app_name='cstype', namespace='cstype')),
    url(r'^supplieraccount/', include('supplieraccount.urls', app_name='supplieraccount', namespace='supplieraccount')),
    url(r'^categorymaingroup/', include('categorymaingroup.urls', app_name='categorymaingroup', namespace='categorymaingroup')),
    url(r'^categorymainsubgroup/', include('categorymainsubgroup.urls', app_name='categorymainsubgroup', namespace='categorymainsubgroup')),
    url(r'^fxrate/', include('fxrate.urls', app_name='fxrate', namespace='fxrate')),
    url(r'^rep_contributionmargin/', include('rep_contributionmargin.urls', app_name='rep_contributionmargin', namespace='rep_contributionmargin')),

    # Part 2
    url(r'^nontrade/', include('nontrade.urls', app_name='nontrade', namespace='nontrade')),

    # Jek
    url(r'^bankrecon/', include('bankrecon.urls', app_name='bankrecon', namespace='bankrecon')),
    url(r'^checkvoucher/batchprinting/', include('batchprinting_checkvoucher.urls', app_name='batchprinting_checkvoucher', namespace='batchprinting_checkvoucher')),
    url(r'^journalvoucher/batchprinting/', include('batchprinting_journalvoucher.urls', app_name='batchprinting_journalvoucher', namespace='batchprinting_journalvoucher')),
    url(r'^accountspayable/batchprinting/', include('batchprinting_accountspayable.urls', app_name='batchprinting_accountspayable', namespace='batchprinting_accountspayable')),
    url(r'^triplec/', include('triplec.urls', app_name='triplec', namespace='triplec')),
    url(r'^triplecbureau/', include('triplecbureau.urls', app_name='triplecbureau', namespace='triplecbureau')),
    url(r'^triplectype/', include('triplecsubtype.urls', app_name='triplecsubtype', namespace='triplecsubtype')),
    url(r'^triplecsection/', include('triplecsection.urls', app_name='triplecsection', namespace='triplecsection')),
    url(r'^triplecpublication/', include('triplecpublication.urls', app_name='triplecpublication', namespace='triplecpublication')),
    url(r'^triplecpage/', include('triplecpage.urls', app_name='triplecpage', namespace='triplecpage')),
    url(r'^triplecclassification/', include('triplecclassification.urls', app_name='triplecclassification', namespace='triplecclassification')),
    url(r'^triplecsupplier/', include('triplecsupplier.urls', app_name='triplecsupplier', namespace='triplecsupplier')),
    url(r'^triplecrate/', include('triplecrate.urls', app_name='triplecrate', namespace='triplecrate')),
    url(r'^triplecvariousaccount/', include('triplecvariousaccount.urls', app_name='triplecvariousaccount', namespace='triplecvariousaccount')),
    
    # Login/Logout URLs
    url(r'^login/$', login, {'template_name': 'login.html'}),
    url(r'^logout/$', views.logout),
    url(r'^logout/$', logout, {'next_page': '/login/'}),
    url(r'^admin/password_change/$', password_change, {'template_name': 'admin/password_change_form.html'},name='password_change'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

