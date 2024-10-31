#Extract the word starting with a specific letter 
def extract(arr,letter):
    res=[]
    for i in arr:
        words=i.split()
        for j in words:
            if j[0].lower()==letter.lower():
                res.append(j)
    return res
li=['i am','strong','stable','self motivated','also serious']
nl=extract(li,'s')
for i in nl:
    print(i)