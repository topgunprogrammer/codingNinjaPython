
s = "this is a word string having many many words"
k = 2

dict={}

for word in s.split() :
   dict[word] = dict.get(word,0) +1

for key,value in dict.items():
    if value == k :
        print(key)