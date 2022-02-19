# Count the frequency of words appearing in a string Using Python
def freq_words():
    s1 = input("Enter string of words: ")
    li = s1.split()
    d={}
    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)
freq_words()