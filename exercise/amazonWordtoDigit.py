#write a function to convert a word into digit.
dict1={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10}
dict2={"hundred":100,"thousand":1000,"million":1000000,"billion":10000000}
def WordToDigit(s):
    a=s.split(" ")
    i=len(a)-1
    while(i>=0):
        ans=1
        for k in dict1.keys():
            if k==a[i]:
                out=dict1[a[i]]
                ans+=out
                i=i-1
        for j in dict2.keys():
            if j==a[i]:
                if i>0:
                    out=dict2[a[i]]*dict1[a[i-1]]
                else:
                    out=dict2[a[i]]*1
                ans+=out
                i-=2
                if i<0:
                    break
        
    return ans-1

print(WordToDigit("four hundred one"))
print(WordToDigit("four hundred"))
