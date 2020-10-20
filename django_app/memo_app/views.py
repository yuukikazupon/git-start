from django.shortcuts import render,redirect
from django.core.paginator import Paginator
# from django.views.generic import TemplateView
from .forms import PostForm,RecordNumberForm,NewOldForm
from .models import *

def set_record_number(request):
    request.session['record_number']=request.POST['record_number']
    return redirect(to='/')

def set_order_option(request):
    request.session['new_old']=request.POST['new_old']
    return redirect('index')


def index(request,now_page=1):
    # import pdb; pdb.set_trace()
    if 'record_number' in request.session:
        record_number=request.session['record_number']
    else:
        record_number=10

    if 'new_old' in request.session:
        new_old=request.session['new_old']
    else:
        new_old=1

    record_number_form=RecordNumberForm()
    record_number_form.initial={'record_number':str(record_number)}


    new_old_form=NewOldForm()
    new_old_form.initial={'new_old':str(new_old)}


    if new_old=="1":
        memos=Memo.objects.all().order_by("update_datetime").reverse()
    else:
        memos=Memo.objects.all()
    # page=Paginator(memos,15)
    page=Paginator(memos,record_number)
    # print(page.page_range)
    # print(dir(page))

    params={
    #     # "memos":memos,
        "page":page.get_page(now_page),
        "form":PostForm(),
        'record_number_form':record_number_form,
        'new_old_form':new_old_form
    }

    return render(request,"index.html",params)

def post(request):
    form=PostForm(request.POST,instance=Memo())
    if form.is_valid():
        form.save()
    else:
        print(form.errors)
    return redirect(to="/")
