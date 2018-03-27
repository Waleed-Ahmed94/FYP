from django.shortcuts import render
from django.shortcuts import redirect
import predict_pickle
from newspaper import Article

# Create your views here.
def home(request):
    return render(request, 'fakenews/home.html' , {})

def classify(request):
    if request.method== "POST":
        result,features=predict_pickle.classify(request.POST['title'],request.POST['article'])

        print(result)
        print(features[0])

    return render(request, "fakenews/classify.html", {'result' : result, 'wordcount': features[0][0], 'titlecount':features[0][1], 'punccount': features[0][2], 'gunningfog': features[0][4], 'readability':features[0][5]})

def classify_url(request):
    if request.method=="POST":
        newsurl=request.POST['newsurl']
        article=Article(newsurl)
        article.download()
        article.parse()

        print(article.title)
        print(article.text)
        result, features = predict_pickle.classify(article.title, article.text)
        return render(request, "fakenews/classify.html", {'articletitle': article.title, 'articletext': article.text,'result': result, 'wordcount': features[0][0], 'titlecount':features[0][1], 'punccount': features[0][2], 'gunningfog': features[0][4], 'readability':features[0][5]})