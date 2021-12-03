from django.shortcuts import redirect, render, HttpResponse
def root(request):
    return redirect('/blogs')
def index(request):
    return render(request, 'index.html')
def new(request):
    return HttpResponse('placeholder para mostrar un nuevo formulario para crear un nuevo blog')
def create(request):
    return redirect('/')
def show(request, number):
    return HttpResponse( f'placeholder para mostrar el blog numero: {number}')
def edit(request, number):
    return HttpResponse( f"placeholder to edit blog {number}")
def destroy(request, number):
    return redirect( '/blogs' )


# Create your views here.
