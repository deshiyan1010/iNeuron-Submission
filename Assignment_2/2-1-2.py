def  filter_long_words(string_list,n):
    long_word = []
    for x in string_list:
        if len(x)>n:
            long_word.append(x)
    return long_word
    
 filter_long_words(["hi","hello","howareoyu"],4)
