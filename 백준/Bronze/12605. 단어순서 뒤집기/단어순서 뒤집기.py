n=int(input())
for i in range(1,n+1):
    sentence=list(input().rstrip().split())
    print('Case #%d: %s' %(i, ' '.join(sentence[::-1])))
