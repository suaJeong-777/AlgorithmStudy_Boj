Hnames=input() #한수의 영어이름
alpha_cnt=[0 for _ in range(26)]  #0으로 초기화된 26칸짜리 리스트 생성
for name in Hnames:
    alpha_cnt[ord(name)-65]+=1  #해당 문자에 대한 유니코드 정수 반환 ex.A-> 65

odd=0
odd_alpha=''
alpha=''
for i in range(26): #이때 i는 0부터 시작
    if alpha_cnt[i]%2 ==1: 
        odd+=1
        odd_alpha +=chr(i+65) #chr는 숫자를 해당하는 유니코드 문자로 
    alpha +=chr(i+65)*(alpha_cnt[i]//2)
    
if odd>1:
    print("I'm Sorry Hansoo")
else: 
    print(alpha+odd_alpha+alpha[::-1])