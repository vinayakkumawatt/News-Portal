from django.shortcuts import render
from main.models import Categories,News,Comment
from .forms import CommentForm

def search(request):
    query = request.GET.get('search')
    search = News.objects.filter(heading__icontains = query)
    category = Categories.objects.all()
    data = {
        'category':category,
        'search':search,   
    }
    return render(request,'search.html', data)
    
def details(request, a): 
    news_data = News.objects.get(pk = a)
    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            name = commentForm.cleaned_data['name']
            cm = commentForm.cleaned_data['comment']
            commentM = Comment(news = news_data, name = name, comment = cm)
            commentM.save()
    commentForm = CommentForm()
    commentData = Comment.objects.filter(news = news_data)


    category = Categories.objects.all() 
    # jaha pr bhi id 'a' se match hogi like jaha pr bhi id 2 se match hogi wo fetch hokr news wale var mai jayegi
    #  get yaha pr jo bhi single record match horha h wohi lekr arha hai 
    data = {
        'category':category,
        'news' : news_data,
        'form':commentForm, 
        'comments':commentData,
    }
    return render(request,'details.html',data)

def home(request):
    category =  Categories.objects.all()
    news = News.objects.all()
    bolly = News.objects.filter(category__title = "Bollywood News")
    india = News.objects.filter(category__title = "India News")
    data = {
            'category':category,
            'news':news,
            'bolly':bolly,
            'india':india,
        }
    return render(request,'index.html',data)

def india(request):
    category = Categories.objects.all()
    india = News.objects.filter(category__title = "India News")
    return render(request,'india.html',{'india':india, 'category':category})

def bollywood(request):
    category = Categories.objects.all()
    bolly = News.objects.filter(category__title = "Bollywood News")
    data= {
        'category':category,
        'bolly':bolly,
        }
    return render(request,'bollywood.html',data)