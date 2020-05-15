def longestWord(string_list):
    longest_word = None
    longest_size=0
    for x in string_list:
        if len(x)>longest_size:
            longest_word = x
    return x

longestWord(["hi","hello","awesome"])
