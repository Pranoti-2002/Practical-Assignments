import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
stop_words = set(stopwords.words('english'))  

ps=stemmer = PorterStemmer() 
lemmatizer = WordNetLemmatizer()
tfidf = TfidfVectorizer()

text = 'Data science is the study of data to extract meaningful insights for business. It is a multidisciplinary approach that combines principles and practices from the fields of mathematics, statistics, artificial intelligence, and computer engineering to analyze large amounts of data.' 

print(word_tokenize(text)) 

print(sent_tokenize(text)) 

#print(stop_words) # it prints all stopwords 

# stopwords 

tokenized = word_tokenize(text) 

filtered_sentence = [w for w in tokenized if not w.lower() in stop_words] 
#with no lower case conversion
filtered_sentence = []
  
for w in tokenized:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)  

#parts of speech tagging

tagged = nltk.pos_tag(tokenized)
print(tagged)  

#stemming 

for w in tokenized:
    print(w ,":" , ps.stem(w)) 

#Lemmatization  

for w in tokenized:
    print(w , ":" , lemmatizer.lemmatize(w))  

#tf-idf 

d0="Hello World" 
d1="Hello Pranoti" 
d2="Hello Pranoti and Priti" 
 
string = [d0 , d1 , d2]  

result = tfidf.fit_transform(string) 
# get idf values
print('\nidf values:')
for ele1, ele2 in zip(tfidf.get_feature_names_out(), tfidf.idf_):
    print(ele1, ':', ele2) 


