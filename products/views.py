from multiprocessing import AuthenticationError
from telnetlib import LOGOUT
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from products.forms import UserCreateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from products.models import Category, Product

from .models import ProductReview
from .forms import ProductForm, CreateProductForm


# Create your views here.
def home_page(request):
    product_list = Product.objects.all()
    categories = Category.objects.all()
    selected_category_id = request.GET.get('category')
    search_query = request.GET.get('qidiruv', '')
    if search_query:
        product_list = product_list.filter(name__icontains=search_query)
    elif selected_category_id:
        product_list = Product.objects.filter(category_id=selected_category_id)
    else:
        product_list = Product.objects.all()
    context = {'product_list': product_list, 'categories': categories}

    return render(request, 'index.html', context)


def detail_page(request, slug):
    if request.method == "POST":
        product = get_object_or_404(Product, slug=slug)
        review = request.POST.get('review')
        user = request.user
        ProductReview.objects.create(user=user, product=product, review=review)

    product = get_object_or_404(Product, slug=slug)
    product_reviews = ProductReview.objects.all().order_by('-created_at').filter(product=product)
    context = {'product': product, 'product_reviews': product_reviews}
    return render(request, 'detail.html', context)
     

def login_page(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect(home_page)
    else:
        login_form = AuthenticationError()
    return render(request, 'login.html', {'form': login_form})


def user_create(request):
    if request.method == 'POST':
        create_form = UserCreateForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect(login_page)
    else:
        create_form = UserCreateForm()
        context = {'create_form': create_form}
    return render(request, 'create_user.html', context)


def logout_page(request):
    logout(request)
    return redirect(home_page)


def edit_comment(request, id, slug):
    if request.method == "POST":
        comment = ProductReview.objects.get(id=id)
        form = ProductForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(detail_page, slug=slug)
    else:
        comment = ProductReview.objects.get(id=id)
        form = ProductForm(instance=comment)
        context = {'comment': comment, 'form': form}
    return render(request, 'edit_comment.html', context=context)


def delete_comment(request, id, slug):
    comment = ProductReview.objects.get(id=id)
    comment.delete()
    return redirect(detail_page, slug=slug)


def create_post(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(home_page)
    else:
        form = CreateProductForm()
    return render(request, 'create.html', {'form': form})












