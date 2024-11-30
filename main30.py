x={'Id1':{'name':'khanak','school':'xxx','subject':['math,english,science,art']},'Id2':{'name':'khanak','school':'xxx','subject':['math,english,science,art']},'Id3':{'name':'khanak1','school':'kkk','subject':['math,english,science,art']}}
result={}
for key,value in x.items():
    if value not in result.values():
        result[key]=value

print(result)

for i in range(1,2,3,4,5):
    print(i)
