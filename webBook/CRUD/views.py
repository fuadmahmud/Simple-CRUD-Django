from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Books
from .forms import BookForm

# Create your views here.
def update(request,update_id):
    book_update = Books.objects.get(id=update_id)
    data = {
        'author': book_update.author,
        'title': book_update.title,
        'pages': book_update.pages,
        'types': book_update.types,
        'pub_date': book_update.pub_date,
    }
    book_form = BookForm(request.POST or None, initial=data,instance=book_update)
    if request.method == 'POST':
        if book_form.is_valid():
            book_form.save()
        return redirect('CRUD:list')

    context = {
        'page_title': 'Update Book',
        'book_form': book_form,
    }

    return render(request,'book/create.html',context)    

def delete(request,delete_id):
    Books.objects.filter(id=delete_id).delete()
    return redirect('CRUD:list')

def create(request):
    book_form = BookForm(request.POST or None)
    if request.method == 'POST':
        if book_form.is_valid():
            book_form.save()
        return redirect('CRUD:list')

    context = {
        'page_title': 'Adding Book',
        'book_form': book_form,
    }

    return render(request,'book/create.html',context)

def list(request):
    bookList = Books.objects.all()

    context = {
        'page_title': 'Book List',
        'Book_List': bookList,
    }

    return render(request,'book/list.html',context)