# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:29:48 2019

@author: rknudsen
"""

import datetime
import pandas as pd
import spacy

import import_news

nlp = spacy.load('en_core_web_sm')

def extract_fields(articles):
    ids_ = list()
    sources = list()
    titles = list()
    publishedAts = list()

    i = 0
    for article in articles:
        source = article['source']['name']
        title = article['title']
        publishedAt = datetime.datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')

        ids_.append(i)
        sources.append(source)
        titles.append(title)
        publishedAts.append(publishedAt)
        i += 1
    
    return ids_, sources, titles, publishedAts

def get_labels(titles, publishedAts, ids_):
    labels = list()

    for title, publishedAt, id_ in zip(titles, publishedAts, ids_):
        if title is not None:
            doc = nlp(title)
            for ent in doc.ents:
                labels.append([id_, publishedAt, ent.text, ent.label_])

    labels = pd.DataFrame(labels, columns=['id', 'publishedAt', 'label', 'class'])
    return labels

def main_topics():
    articles = import_news.get_news()
    ids_, sources, titles, publishedAts = extract_fields(articles)
    labels = get_labels(titles, publishedAts, ids_)
    return(labels)

if __name__ == '__main__':
    labels = main_topics()
    print(labels.head(10))