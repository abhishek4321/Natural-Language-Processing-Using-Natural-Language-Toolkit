import nltk
import random
#import statistics
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier,PassiveAggressiveClassifier
from sklearn.svm import LinearSVC, NuSVC
from nltk.classify import ClassifierI 
#from statistics import mode as m
import pickle

class VoteClassifier(ClassifierI):

    def __init__(self,*classifiers):
       self._classifiers=classifiers

    def classify(self,features):
      votes=[]
      for i in self._classifiers:
         v=i.classify(features)
         votes.append(v)
      #return m(votes)

    def confidence(self,features):
       votes=[]
       for i in self._classifiers:
          v=i.classify(features)
          votes.append(v)
          choiceofvotes=votes.count(m(votes))
          cf=float(choiceofvotes)/len(votes)
          return cf
   
'''
documents=[]
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append(list(movie_reviews.words(fileid).category)
        documents.append(list(movie_reviews.words(fileid).category
'''

documents=[(list(movie_reviews.words(fileid)),category)
           for category in movie_reviews.categories()
           for fileid in movie_reviews.fileids(category)]
        
random.shuffle(documents)

save_classifier = open("c:/users/user/desktop/project/documents.pickle","wb")
pickle.dump(documents,save_classifier)
save_classifier.close()

#print(documents[0])
all_words=[]
for i in movie_reviews.words():
   all_words.append(i.lower())
all_words=nltk.FreqDist(all_words)
#print(all_words.most_common(15))
#print(all_words["cheerleader"])
word_features=list(all_words.keys())[:4000]#keys
#print word_features

save_word_features = open("c:/users/user/desktop/project/word_features.pickle","wb")
pickle.dump(word_features, save_word_features)
save_word_features.close()

def find_feature(document):
   words=set(document)
   features={}
   for i in word_features:
      features[i]=(i in words)
   return features

#print((find_feature(movie_reviews.words("pos/cv010_29198.txt"))))
featuresets=[(find_feature(rev),category) for(rev,category) in documents]

#Naive Bayes Classifier
#likelihood=(prior occurance*likelihood)/evidence

training_set = featuresets[:1560]
testing_set = featuresets[1560:]
classifier = nltk.NaiveBayesClassifier.train(training_set)
print('Original Naive bayes algo accuracy percent:',(nltk.classify.accuracy(classifier,testing_set))*100)
classifier.show_most_informative_features(15)


save_classifier = open("c:/users/user/desktop/project/originalnaivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

#MNB_classifier
MNB_classifier=SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print('Original MNB classifier algo accuracy percent:',(nltk.classify.accuracy(MNB_classifier,testing_set))*100)

save_classifier = open("c:/users/user/desktop/project/MNBclassifier.pickle","wb")
pickle.dump(MNB_classifier,save_classifier)
save_classifier.close()

#Bern_classifier
Bern_classifier=SklearnClassifier(BernoulliNB())
Bern_classifier.train(training_set)
print('Original Bernoulli Classifier algo accuracy percent:',(nltk.classify.accuracy(Bern_classifier,testing_set))*100)

save_classifier = open("c:/users/user/desktop/project/Bern_classifier.pickle","wb")
pickle.dump(Bern_classifier,save_classifier)
save_classifier.close()

#logisticRegression_classifier
logistics_classifier=SklearnClassifier(LogisticRegression())
logistics_classifier.train(training_set)
print('Original Logistics classifier algo accuracy percent:',(nltk.classify.accuracy(logistics_classifier,testing_set))*100)

save_classifier = open("c:/users/user/desktop/project/logistics_classifier.pickle","wb")
pickle.dump(logistics_classifier,save_classifier)
save_classifier.close()

#SGDClassifier
SGDClassifier_classifier=SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print('Original SGDC Classifier algo accuracy percent:',(nltk.classify.accuracy(SGDClassifier_classifier,testing_set))*100)

save_classifier = open("c:/users/user/desktop/project/SGDClassifier_classifier.pickle","wb")
pickle.dump(SGDClassifier_classifier,save_classifier)
save_classifier.close()

#PassiveAgressiveClassifier
PassiveAggressiveClassifier_classifier=SklearnClassifier(PassiveAggressiveClassifier())
PassiveAggressiveClassifier_classifier.train(training_set)
print('Original Passive Aggressive Classifier algo accuracy percent:',(nltk.classify.accuracy(PassiveAggressiveClassifier_classifier,testing_set))*100)

save_classifier = open("c:/users/user/desktop/project/PassiveAggressiveClassifier_classifier.pickle","wb")
pickle.dump(PassiveAggressiveClassifier_classifier,save_classifier)
save_classifier.close()

#LinearSVC_classifier
LinearSVC_classifier=SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print('Original Linear SVC_classifier algo accuracy percent:',(nltk.classify.accuracy(LinearSVC_classifier,testing_set))*100)

save_classifier = open("c:/users/user/desktop/project/LinearSVC_classifier.pickle","wb")
pickle.dump(LinearSVC_classifier,save_classifier)
save_classifier.close()

#NuSVC_classifier
NuSVC_classifier=SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print('Original NuSVC_classifier algo accuracy percent:',(nltk.classify.accuracy(NuSVC_classifier,testing_set))*100)

save_classifier = open("c:/users/user/desktop/project/NuSVC_classifier.pickle","wb")
pickle.dump(NuSVC_classifier,save_classifier)
save_classifier.close()

voted_classifier=VoteClassifier(classifier,
                            MNB_classifier,
                            Bern_classifier,
                            logistics_classifier,
                            SGDClassifier_classifier,
                            PassiveAggressiveClassifier_classifier,
                            LinearSVC_classifier
                           )

print("voted classifier accuracy percent",(nltk.classify.accuracy(voted_classifier,testing_set))*100)

print("Classification:", voted_classifier.classify(testing_set[0][0]), "Confidence %:",voted_classifier.confidence(testing_set[0][0])*100)
print("Classification:", voted_classifier.classify(testing_set[1][0]), "Confidence %:",voted_classifier.confidence(testing_set[1][0])*100)
print("Classification:", voted_classifier.classify(testing_set[2][0]), "Confidence %:",voted_classifier.confidence(testing_set[2][0])*100)
print("Classification:", voted_classifier.classify(testing_set[3][0]), "Confidence %:",voted_classifier.confidence(testing_set[3][0])*100)
print("Classification:", voted_classifier.classify(testing_set[4][0]), "Confidence %:",voted_classifier.confidence(testing_set[4][0])*100)
print("Classification:", voted_classifier.classify(testing_set[5][0]), "Confidence %:",voted_classifier.confidence(testing_set[5][0])*100)

def sentiment(text):
    op=find_feature(text)
    return voted_classifier.classify(op).voted_classifier.confidence(op)
    