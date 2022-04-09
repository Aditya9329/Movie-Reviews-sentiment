import nltk
from nltk.corpus import stopwords
import re
class TextPreparation:
    def __init__(self):
        pass
    
    # remove html tags
    def remove_tags(self,data):
        self.pattern='<.*?>'
        self.clean_data = re.sub(self.pattern,r'',data)
        return self.clean_data
        
    # all words will be in a lowercase
    def lower_casing(self,data):
        self.cleaned_data = data.lower()
        # print(self.cleaned_data)
        return self.cleaned_data

    #remove stopwords 
    def remove_stopwords(self,data):
        self.x = []
        self.data = data
        for e in self.data.split():
            if e not in stopwords.words('english'):
                    self.x.append(e)
        
        self.cleaned_data = self.x[:]
        # print(self.cleaned_data)
        self.x.clear()
        return self.cleaned_data

    def join_words(self,data):
        self.cleaned_data = " ".join(data)
        return self.cleaned_data


