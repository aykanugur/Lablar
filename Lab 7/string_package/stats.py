
def  count_characters(s):
    return len(s)
def count_words(s):
    return len(s.split())
def average_word_length(s):
    newword = s
    words = newword.split()
    count = 0
    for x in words:
        count += len(x)
    return count / count_words(newword)
        
    
        
    
        