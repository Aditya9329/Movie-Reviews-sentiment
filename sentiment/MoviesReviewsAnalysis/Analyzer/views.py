from django.shortcuts import render
from django.http import HttpResponse
from . import forms
import pickle
from TextPreparation import preparation
# # loading model file 
# mdl  = pickle.load('./Model/sentiment_analysis_model.pickle','rb')


# load machine learning model 
model =  pickle.load(open('./model/sentiment_analysis_model4.pickle','rb'))
# load the vectorization file
vect  =  pickle.load(open('./vectorizer/vectorize.pickle', 'rb'))


# Create your views here
def analyzer(request):
    ans=None
    if request.method =='POST':
        form = forms.GetText(request.POST)
        text = form.data['text']
        #      module name classObject.calling function  for html text removal
        text = preparation.TextPreparation().remove_tags(text)
        print(text)

        # creating  a object of a class and calling a function  for lowercase the text
        lower_cased_text = preparation.TextPreparation().lower_casing(text)
        # Testing
        
        # remove stopwords from the text
        prepared_text = preparation.TextPreparation().remove_stopwords(lower_cased_text)
        # Testing
        
        # prepared_text is a list of words so covert into string form
        user_text = preparation.TextPreparation().join_words(prepared_text)
        print(user_text)
        t=model.predict(vect.transform([user_text]))
        if t==1:
            ans = "<h1>Positive</h1>"
        elif t==0:
            ans = "<h1>Negative</h1> <br> <a href="">Go Back</a>"
        return HttpResponse(ans)
        
    form = forms.GetText()
    res  = render(request,'index.html',{'form':form})
    return res 