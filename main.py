__author__ = "Tochi Bedford" 
__email__ = "tochibedford.work@gmail.com" 

import sys
import string
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from numpy import exp

def softmax(array):
    return exp(array)/sum(exp(array))

def main(text, tokenenizer, model):
    raw_text = open(text, encoding="utf-8").read().casefold() #lower case raw text

    cleaned_text = raw_text.translate(str.maketrans("", "", string.punctuation))

    encoded_text = tokenenizer(cleaned_text, return_tensors='pt')
    output = model(**encoded_text)
    return softmax(output[0][0].detach().numpy())
    
if __name__ == '__main__':
    arguments = sys.argv[1:]
    model_path = 'cardiffnlp/twitter-roberta-base-sentiment'
    tokenenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    if(arguments):
        for path in arguments:
            print(f'{path}: {main(path, tokenenizer, model)}')