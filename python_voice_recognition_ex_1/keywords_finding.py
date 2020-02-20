#!/usr/bin/env python
# -*-coding:utf-8 -*-

class keywords_finding:
    # def __init__(self):



    def find_keyword(self, recognitionText):
        key_file = open('keywords.txt')
        keyData = key_file.read()

        keyWords = keyData.split(' ')

        word_freq = {}
        for word in keyWords:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
        word_prob_dict = {}
        size_corpus = len(keyWords)
        for word in word_freq:
            word_prob_dict[word] = float(word_freq[word]) / size_corpus
        prob_list = []

        for word, prob in word_prob_dict.items():
            prob_list.append(prob)
        non_exist_prob = min(prob_list) / 2

        words = recognitionText.split()
        test_word_freq = {}
        for word in words:
            if word in test_word_freq:
                test_word_freq[word] += 1
            else:
                test_word_freq[word] = 1

        test_word_ba = {}
        word_match = []
        for word, freq in test_word_freq.items():
            if word in word_prob_dict:
                #test_word_ba[word] = freq / word_prob_dict[word]
                word_match.append(word)
            else:
                test_word_ba[word] = freq / non_exist_prob
        """
        test_word_ba_list = []
        for word, ba in test_word_ba.items():
            test_word_ba_list.append((word, ba))
        test_word_ba_list.sort()
        """
        return word_match

#
# key= keywords_finding()
#
# print key.find_keyword()
