eq = input().split('-') 
result=0

for i in eq[0].split("+"):
  result+=int(i)
  #이때 i는 첫번째 -가 나오기 전까지의 숫자와 +를 포함한다
  #이 과정을 통해 첫번째 초기값을 구하게 됨

for i in eq[1:]:
  for j in i.split('+'):
    result-=int(j)
#이 부분은 -이후에 나타나는 값으로 이 값이 클수록 최소값이 가까워진다
# - 이후에 나타난 숫자 와 + 들 역시 다 합쳐주고
#첫번째 for문에서 나타난 초기값에서 빼주면 된다

print(result)
