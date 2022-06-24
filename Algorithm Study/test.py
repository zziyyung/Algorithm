# a = [1 ,2]
# print(len(a))


s = "id,name,age,score\nNULL,NULL\n1,Jack,NULL,12\ncountry,population,arear\nUK,67m,242000km2\nANNUL,ANNULLED\nnull,NILL"
slist= s.split("\n")
print(slist)
for i in slist[:]:
    if (',NULL,' in i) or (',NULL' in i) or ('NULL,' in i) or ('NULL,NULL' in i) : # 널값이 있다면
    #if (',NULL,' or ',NULL' or 'NULL,' or 'NULL,NULL') in i:  # 널값이 있다면
        slist.remove(i)
        print(slist)
str = '\\n'.join(slist)
print(str)
