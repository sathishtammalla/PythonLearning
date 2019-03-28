with open('john17.txt','r') as jn:
    data = jn.readline()
    word_dict = {}
    for l in data.strip().split():
        if l.lower() in word_dict:
            word_dict[l.lower()] += 1
        else:
            word_dict[l] = 1

for i in word_dict.items():
    print(i)




