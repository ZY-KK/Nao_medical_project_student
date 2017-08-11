def find_keyword(test_string='I have a cold and fever and my breast has some problem'):
    key_file=open('keywords.txt')
    data=key_file.read()

    words=data.split()

    word_freq={}
    for word in words:
        if word in word_freq:
            word_freq[word]+=1
        else:
            word_freq[word]=1
    word_prob_dict={}
    size_corpus=len(words)
    for word in word_freq:
        word_prob_dict[word]=float(word_freq[word])/size_corpus
    prob_list=[]
    print word_prob_dict
    for word , prob in word_prob_dict.items():
        prob_list.append(prob)
    non_exist_prob=min(prob_list)/2

    words=test_string.split()
    test_word_freq={}
    for word in words:
        if word in test_word_freq:
            test_word_freq[word]+=1
        else:
            test_word_freq[word]=1

    test_word_ba={}
    word_match=[]
    for word , freq in test_word_freq.items():
        if word in word_prob_dict:
            test_word_ba[word]=freq/word_prob_dict[word]
            word_match.append(word)
        else:
            test_word_ba[word]=freq/non_exist_prob
            #test_word_ba[word]=10000000
    test_word_ba_list=[]
    for word , ba in test_word_ba.items():
        test_word_ba_list.append((word,ba))

    def sort_func(a,b):
        if a[1]>b[1]:
            return -1
        elif a[1]<b[1]:
            return 1
        return 0
    test_word_ba_list.sort(sort_func)
    return word_match


print find_keyword()

