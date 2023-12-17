from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from . import models
from django.db.models import Q
from orders.forms import CartAddForm
from django.contrib import messages
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from utils import IsAdminUserMixin
from django.utils.decorators import method_decorator
# Create your views here.

class HomeView(View):
    templates_class='home/main.html'

    def get(self,request,category_slug=None):
        products =models.Book.objects.filter(is_printed_available=True)
        book=products
        top_like=products.order_by('uvote')[0]

        return render(request,self.templates_class,{'products':products ,'top':top_like,'book':products})


# def get(self, request, category_slug=None):
#     products = models.Book.objects.filter(Q(is_printed_available=True) | Q(is_electric_available=True))
#     categories = models.Category.objects.filter(is_sub=False)
#     if category_slug:
#         category = models.Category.objects.get(slug=category_slug)
#         products = products.filter(category=category)
#     return render(request, 'home/home.html', {'products': products})


class ProductDetailView(View):

   form_class = forms.CommentCreateForm
   form_class_reply = forms.CommentReplyForm


   def setup(self, request, *args, **kwargs):
    self.product = get_object_or_404(models.Book, slug=kwargs['slug'])
    return super().setup(self, request, *args, **kwargs)


   def get(self, request, slug):
    comments = self.product.bcommmnt.filter(is_replay=False)
    form = CartAddForm()
    can_like = False
    if request.user.is_authenticated:
        can_like = True
    return render(request, 'home/detils_book.html', {'book': self.product,'a':form,
                                                           'comments': comments, 'form': self.form_class,
                                                           'reply_form': self.form_class_reply, 'can_like': can_like})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
     form = self.form_class(request.POST)
     if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.user = request.user
        new_comment.Product = self.product
        new_comment.save()
        messages.success(request, 'your comment submitted successfully', 'success')
        return redirect('home:post_detail', self.product.id, self.product.slug)


class PostAddReplyView(LoginRequiredMixin, View):
	form_class = forms.CommentReplyForm

	def post(self, request, post_id, comment_id):
		post = get_object_or_404(forms.Post, id=post_id)
		comment = get_object_or_404(forms.Comment, id=comment_id)
		form = self.form_class(request.POST)
		if form.is_valid():
			reply = form.save(commit=False)
			reply.user = request.user
			reply.Product= models.Book
			reply.reply = comment
			reply.is_reply = True
			reply.save()
			messages.success(request, 'your reply submitted successfully', 'success')
		return redirect('home:post_detail', models.Book.id, models.Book.slug)


class PostLikeView(LoginRequiredMixin, View):
	def get(self, request, Product_id):
		product= get_object_or_404(models.Post, id=Product_id)
		like = models.Vote.objects.filter(Product=product, user=request.user)
		if like.exists():
			messages.error(request, 'you have already liked this post', 'danger')
		else:
			forms.Vote.objects.create(Product=product, user=request.user)
			messages.success(request, 'you liked this post', 'success')
		return redirect('home:post_detail', product.id, product.slug)

