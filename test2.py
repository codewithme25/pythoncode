s='AABCCDEEA'
s=s.lower()
k=3
for i in range(0,len(s),k):
    #list1=list(s)
    #print(s[i:i+k])
    t=(s[i:i+k])
    m=set(t)
    x=list(m)
    finalJoin=''.join(x).upper()
    print(finalJoin)
