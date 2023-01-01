#Qu 1
id = {("name" ,"last_name") : 'Malak Mahameed','age':28,'phone num':505588006}
print(id)

#Qu2
list = ["a",2,"&","a",5,6]
def func(list):
    try:
        list[5] = "@"
        print(list)
    except IndexError:
        print("relevant exception")
    return list
func(list)


#qu 3
list1 = ["a",2,"&","a",5]
def funct(list1):
    assert len(list1) >=6 ,"relevant assertion"
    list[5] = "@"
    print(list)
    return list1
funct(list1)

#Qu4
dict = {"name":"Malak"}
newdict = {}
def func1(dict):
    dict.update({"age":"28"})
    return dict
print(func1(dict))

#Qu6
n = int(5)
dict = {}
for x in range(1,n+1):
    dict[n]=n+3
print(dict)

#qu7
dict1 = {1:10,2:20}
dict2 = {3:30,4:40}
dict3 = {5:50,6:60}
dict4 = {}
for dict in (dict1 , dict2 ,dict3):
    dict4.update(dict)
print(dict4)

#qu7
str1 = "HANNA"
cdict = {}
def func(str1):
    for char in str1:
        count = cdict.get(char,0)
        count += 1
        cdict[char] = count
    return cdict
print(func(str1))

#qu7    #A second solution
str1 = "HANNA"
ccdict = {}
def func(str1):
    for char in str1:
        c = str1.count(char)
        ccdict[char] = c
    return ccdict
print(func(str1))


#qu 8
d1 = {"a":100 , "b":200 , "c":300}
d2 = {"a":300 , "b":200 , "d":400}
new_dict = d2
for i,j in d1.items():
    if i in d2:
        new_dict[i] = j + d2[i]
    else:
        new_dict[i] = j
print(new_dict)


