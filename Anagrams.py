from collections import Counter
def anagrams(str1,str2):
    if len(str1)!= len(str2):
        return False
    return Counter(str1)==Counter(str2)
string1="silent"
string2="listen"
print(anagrams(string1,string2))
