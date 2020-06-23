import pandas as pd
import numpy as np
import re
from bs4 import BeautifulSoup
import html
import contractions
import emoji
from emoji import UNICODE_EMOJI
import unicodedata
import num2words
import string
import nltk
from nltk.tokenize import WhitespaceTokenizer
from nltk.corpus import stopwords
from spellchecker import SpellChecker
spell = SpellChecker()
from nltk.stem import LancasterStemmer
lancaster=LancasterStemmer()
from textblob import TextBlob, Word
from operator import add
from itertools import starmap



def remove_url(text):
    return re.sub(r"http\S+|www\S+", "", text)

def remove_html(text):
    soup = BeautifulSoup(text, 'lxml')
    text = soup.get_text()
    return text

def remove_line_break(text):
    return text.replace('\r', ' ').replace('\n', ' ')

def remove_mention(text):
    return ' '.join(re.sub("([@][A-Za-z0-9._:-]+)"," ",text).split())

def map_contraction(text):
    return contractions.fix(text)

def lower_case(text):
    return text.lower()

def is_emoji(s):
    return s in UNICODE_EMOJI

def space_out_emoji(text):
    spaced = ''
    for char in text:
        if is_emoji(char):
            spaced += ' '
        spaced += char
    return spaced

def replace_emoji(text):
    return emoji.demojize(text, delimiters=("", " "))

def remove_emoji(text):
    allchars = [str for str in text]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    text = ' '.join([str for str in text.split() if not any(j in str for j in emoji_list)])
    return text

def remove_accented_char(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')

def remove_non_ascii(text):
    return re.sub(r'[^\x00-\x7F]+',' ',text)

def extract_hashtag(text):
    return re.findall('#\w+', text)

def remove_hashtag(text):
    return ' '.join(re.sub("([#][A-Za-z0-9._:-]+)"," ",text).split())

def remove_punctuation(text):
    return text.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation))).replace(' '*4, ' ').replace(' '*3, ' ').replace(' '*2, ' ').strip()

def keep_alphabet(text):
    return re.sub(r"[^a-zA-Z]", " ", text, 0)

word = WhitespaceTokenizer()
def tokenize_text(text):
    return word.tokenize(text)

stopWords = set(stopwords.words('english'))
def remove_stopword(tokens):
    nword = []
    for word in tokens:
        if word not in stopWords:
            nword.append(word)
    return nword

def spell_correct(text):
    misspelled = spell.unknown(text)
    print(text)
    print(misspelled)
    for word in misspelled:
        correct = []
        correct.append(spell.correction(word))
        text[text.index(word)] = correct[0]
        #[correct if x==word else x for x in text]
    return text

def join_words(text):
    return ' '.join(text)

def stemming(text):
    nword=[]
    for word in text:
        nword.append(lancaster.stem(word))
    return nword

def lemmatize_with_postag(text):
    sent = TextBlob(text)
    tag_dict = {"J": 'a', 
                "N": 'n', 
                "V": 'v', 
                "R": 'r'}
    words_and_tags = [(w, tag_dict.get(pos[0], 'n')) for w, pos in sent.tags]    
    lemmatized_list = [wd.lemmatize(tag) for wd, tag in words_and_tags]
    return " ".join(lemmatized_list)

def add_hashtags(text, hashtags):
    token = tokenize_text(text)
    token = token + hashtags
    text = join_words(token)
    return text


def clean(toggle):

    char_exceed = False
    if toggle['clean_input']!=['']:
        ogtext = text = toggle['clean_input'][0]
        char_exceed = True
        if len(text) <= 400:
            char_exceed = False

            hashtags = extract_hashtag(text) #Extract Hashtags
            text = remove_hashtag(text)
            text = lower_case(text) #Lower Case
            
            
            if 'html' in toggle:
                text = remove_url(text) #URL
                text = remove_html(text) #HTML
                text = remove_line_break(text) #Line Break
                
            if 'mention' in toggle:
                text = remove_mention(text) #Mention Handling
                
            if 'contraction' in toggle:
                text = map_contraction(text) #Contraction Mapping
            
            if 'spelling' in toggle:
                text = tokenize_text(text) #Tokenize
                text = spell_correct(text)
                text = join_words(text)
            
            if 'emoji' in toggle:
                text = space_out_emoji(text) #Space out emoji
                text = replace_emoji(text) #Replace Emoji
                
            if 'punctuation' in toggle:
                text = remove_punctuation(text) #Punctuation Handling
                text = remove_accented_char(text)
                text = remove_non_ascii(text)
                text = keep_alphabet(text)
            
            if 'tokenisation' in toggle:
                text = tokenize_text(text) #Tokenize
                
            if 'stopword' in toggle:
                if 'tokenisation' in toggle:
                    text = remove_stopword(text)
                else:
                    text = tokenize_text(text) #Tokenize
                    text = remove_stopword(text)
                    text = join_words(text)
                
            if 'stemming' in toggle:
                if 'tokenisation' in toggle:
                    text = stemming(text)
                else:
                    text = tokenize_text(text) #Tokenize
                    text = stemming(text)
                    text = join_words(text)
                    
            if 'lemmatization' in toggle:
                if 'tokenisation' in toggle:
                    text = join_words(text)
                    text = lemmatize_with_postag(text)
                    text = tokenize_text(text) #Tokenize
                else:
                    text = lemmatize_with_postag(text)
            
            if 'tokenisation' in toggle:
                text = text  + hashtags
            else:
                text = add_hashtags(text, hashtags)
            
    else:
        text = 'Text to be Cleaned Area cannot be left blank, please enter some text or copy sample text from Learn Area'
        ogtext = text
    
    if char_exceed:
        text = ogtext = 'Keeping in mind processor constraints, maximum character limit for Text to be Cleaned is 400 characters. Reduce the size of text and try again.'
    return text, ogtext
