import json
from django.contrib.auth.views import LoginView, LogoutView

from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from .models import Post, Category, Comment, CommentLike

from blog.forms import CommentForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView
from django.views.generic import DetailView


class PostArchive(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'blog/posts.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_single.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        post = context['post']
        context['form'] = CommentForm()
        context['comments'] = post.comments.filter(is_confirmed=True)
        context['settings'] = post.post_setting
        context['category'] = post.category
        context['author'] = 'post.author'
        context['categories'] = Category.objects.all()
        return context


class CategoryDetail(DetailView):
    model = Category
    template_name = 'blog/category_detail.html'


class CategoryArchive(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'blog/category_archive.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data()
    #     context['categories'] = Category.objects.all()
    #     return context


class SignInView(LoginView):
    # authentication_form = UserLoginForm
    template_name = 'blog/login.html'
    # redirect_authenticated_user = '/'


class LogoutView(LogoutView):
    template_name = 'blog/login.html'
    # redirect_field_name = 'login/'


class SignUpView(CreateView):
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegistrationForm


@csrf_exempt
def create_comment(request):
    data = json.loads(request.body)
    user = request.user
    try:
        comment = Comment.objects.create(post_id=data['post_id'], content=data['content'], author=user)
        response = {"comment_id": comment.id, "content": comment.content, 'dislike_count': 0, 'like_count': 0,
                    'full_name': user.get_full_name()}
        return HttpResponse(json.dumps(response), status=201)
    except:
        response = {"error": 'error'}
        return HttpResponse(json.dumps(response), status=400)


@csrf_exempt
def like_comment(request):
    data = json.loads(request.body)
    print(data)
    user = request.user
    try:
        comment = Comment.objects.get(id=data['comment_id'])
    except Comment.DoesNotExist():
        return HttpResponse("comment does not exit", status=404)
    comment_like = CommentLike.objects.filter(author=user, comment=comment).first()
    if comment_like:
        comment_like.condition = data['condition']
        comment_like.save()
    else:
        CommentLike.objects.create(condition=data['condition'], author=user, comment=comment)
    response = {"like_count": comment.like_count, "dislike_count": comment.dislike_count}
    return HttpResponse(json.dumps(response), status=201)

# def home(request):
#     author = request.GET.get('author', None)
#     category = request.GET.get('category', None)
#     posts = Post.objects.all()
#     if author:
#         posts = posts.filter(author__username=author)
#     if category:
#         posts = posts.filter(category__slug=category)
#     categories = Category.objects.all()
#     context = {
#         "posts": posts,
#         "categories": categories,
#     }
#     return render(request, 'blog/posts.html', context)

# def post_single(request, pk):
#     try:
#         post = Post.objects.select_related('post_setting', 'category', 'author').get(slug=pk)
#         categories = Category.objects.all()
#     except Post.DoesNotExist:
#         raise Http404('post not found')
#     context = {
#         'form': CommentForm(),
#         "post": post,
#         'settings': post.post_setting,
#         'category': post.category,
#         'author': post.author,
#         'comments': post.comments.filter(is_confirmed=True),
#         "categories": categories,
#     }
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.post = post
#             comment.save()
#         else:
#             context['form'] = form
#
#     return render(request, 'blog/post_single.html', context)
#
# def get_context_data(self, **kwargs):
#     # Call the base implementation first to get a context
#     context = super(CategoryList, self).get_context_data(**kwargs)
#     # Add in the category
#     context['category'] = self.category
#     return context

# def get_context_data(self, **kwargs):
#     context = super(CategoryDetail, self).get_context_data(**kwargs)
#     # category = context['category']
#     # context['categories'] = category.post.all()
#     context['categories'] = self.category
#     return context


# def category_single(request, pk):
#     try:
#         category = Category.objects.get(slug=pk)
#     except Category.DoesNotExist:
#         raise Http404('Category not found')
#     posts = Post.objects.filter(category=category)
#     links = ''.join(
#         '<li><a href={}>{}</a></li>'.format(reverse('post_single', args=[post.slug]), post.title) for post in posts)
#     blog = '<html><head><title>post archive</title></head>{}<a href={}>all categories</a></body></html>'.format(
#         '<ul>{}</ul>'.format(links), reverse('categories_archive'))
#     return HttpResponse(blog)

# def categories_archive(request):
#     categories = Category.objects.all()
#     links = ''.join(
#         '<li><a href={}>{}</a></li>'.format(reverse('category_single', args=[category.slug]), category.title) for
#         category in categories)
#     blog = '<html><head><title>post archive</title></head>{}</body></html>'.format(
#         '<ul>{}</ul>'.format(links))
#     return HttpResponse(blog)

# def login_view(request):
#     form = UserLoginForm(request.POST)
#     if form.is_valid():
#         username = form.cleaned_data.get('username', None)
#         password = form.cleaned_data.get('password', None)
#         user = authenticate(request, username=username, password=password)
#         if user and user.is_active:
#             login(request, user)
#             return redirect('posts_archive')
#         else:
#             context = {'form': form}
#             return render(request, 'blog/login.html', context)
#     else:
#         context = {'form': form}
#     return render(request, 'blog/login.html', context)
#

# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('posts_archive')
#
#     if request.method == 'POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         user = authenticate(request, username=username, password=password)
#         if user and user.is_active:
#             login(request, user)
#             return redirect('posts_archive')
#         else:
#             return redirect('login')
#
#     return render(request, 'blog/login.html', context={})

# def logout_view(request):
#     logout(request)
#     return redirect('posts_archive')


# def register_view(request):
#     form = UserRegistrationForm(request.POST)
#     if form.is_valid():
#         register_form = form.save(commit=False)
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         password2 = form.cleaned_data['password2']
#         email = form.cleaned_data['email']
#         first_name = form.cleaned_data['first_name']
#         last_name = form.cleaned_data['last_name']
#         if password == password2:
#             try:
#                 user = User.objects.get(username=username)
#                 context = {'form': form}
#                 # return redirect('login')
#                 return render(request, 'blog/register.html', context)
#             except User.DoesNotExist:
#                 user = User.objects.create(username=username, password=password, first_name=first_name,
#                                            last_name=last_name, email=email)
#                 user.save()
#                 register_form.user = request.user
#                 register_form.save()
#                 context = {'form': form}
#                 return redirect('login')
#                 # return render(request, 'blog/register.html', context)
#         else:
#             context = {'form': form}
#             # return redirect('login')
#             return render(request, 'blog/register.html', context)
#     else:
#         context = {'form': form}
#         return render(request, 'blog/register.html', context)

# =================================================================================
# class SignUpView(SuccessMessageMixin, CreateView):
#     template_name = 'blog/register.html'
#     success_url = reverse_lazy('login')
#     form_class = UserRegistrationForm
#     success_message = "Your profile was created successfully"

# def register_view(request):
#     form = UserRegistrationForm(request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save(commit=True)
#             return redirect('login')
#         else:
#             context = {'form': form}
#             return render(request, 'blog/register.html', context)
#     else:
#         context = {'form': form}
#     return render(request, 'blog/register.html', context)

# def register_view(request):
#     context = {'form': UserRegistrationForm()}
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             register_form = form.save(commit=True)
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             password2 = form.cleaned_data['password2']
#             email = form.cleaned_data['email']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             user = User.objects.create(username=username, password=password, first_name=first_name,
#                                        last_name=last_name,
#                                        email=email)
#             user.set_password(password)
#             user.save()
#             register_form.user = request.user
#             register_form.save()
#             print(password)
#             print(password2)
#             return redirect('login')
#         else:
#             context = {'form': form}
#     else:
#         form = UserRegistrationForm()
#         context = {'form': form}
#     return render(request, 'blog/register.html', context)

# ====================================================================================

# def register_view(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             email = form.cleaned_data['email']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             user = User.objects.create(username=username, password=password, first_name=first_name, last_name=last_name,
#                                        email=email)
#             user.set_password(password)
#             return redirect('login')
#         else:
#             context = {'form': form}
#     else:
#         form = UserRegistrationForm()
#         context = {'form': form}
#     return render(request, 'blog/register.html', context)
