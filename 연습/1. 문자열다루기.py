[문자열 다루기]
함수 solution은 정수 x와 자연수 n을 입력 받아, 
x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 
다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.




답

def solution(x, n):
    ans=0
    answer =[]
    for i in range(n):
        ans+=x
        answer.append(ans)
        print(ans)
    return answer
  
  
  출처: https://programmers.co.kr/learn/courses/30/lessons/12954

