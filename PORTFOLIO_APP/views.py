
from django.shortcuts import render, redirect, get_object_or_404
from .models import Video, Article,Contact
from .forms import ArticleForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
def article_list(request):
    articles = Article.objects.all()  # Retrieve all articles
    return render(request, 'article_list.html', {'articles': articles})
def food(request):
    return render(request,'food.html')

def e_shop(request):
    return render(request,'e_shop.html')

def index(request):
    return render(request,'index.html')

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()  # Save the article
            return redirect('article_list')  # Redirect to the article list
    else:
        form = ArticleForm()
    return render(request, 'article_create.html', {'form': form})

def article_details(request, article_id):
    article = get_object_or_404(Article, id=article_id)  # Retrieve the specific article
    return render(request, 'article_details.html', {'article': article})

def another_home(request):
    return render(request, 'another_home.html')

from django.conf import settings
from django.core.mail import send_mail

def home(request):
    videos = Video.objects.all() 
    if request.method == 'POST':
        # Extract data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')  # This should be a valid email address
        message = request.POST.get('message')

        # Ensure the email is valid before sending
        if email:
            try:
                send_mail(
                    name,  # Subject
                    message,  # Message
                    settings.EMAIL_HOST_USER,  # Sender email (from settings)
                    [email],  # Recipient email (from form)
                    fail_silently=False,
                )
                # Notify success
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                # Notify failure
                messages.error(request, f'Failed to send the message. Error: {str(e)}')
        else:
            # Notify invalid email
            messages.error(request, 'Invalid email address provided.')
            
    return render(request, 'home.html', {'videos': videos})
