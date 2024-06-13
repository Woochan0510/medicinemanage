import time
from datetime import datetime

current_date = datetime.now().date() # 현재 날짜 기록

capacity = 20 # 용량 지정
array_s = [None] * capacity # 스택 요소 배열
array_q = [None] * capacity # 큐 요소 배열
top = -1 # 공백상태로 초기화
front = 0 # 삭제하는 부분 인덱스
rear = 0 # 추가하는 부분 인덱스

def daily_task():
    global top 
    global front
    global rear
    print("날이 변경되어 약 복용 리스트를 초기화 합니다.")
    top = -1
    front, rear = 0
    for i in range(20):
        array_s[i] = None
        array_q[i] = None
    
def isEmpty_s():
    if top == -1: # 공백이면
        return True
    else:         # 공백아니면
        return False
    
def isFull_s():
    return top == capacity # 스택이 가득차있으면 True 반환

def push(e):
    global top
    if not isFull_s(): # 포화 상태가 아닌 경우
        top += 1
        array_s[top] = e
    else:
        print("stack overflow") # 포화 상태
        exit()
        
def pop():
    global top
    if not isEmpty_s(): # 공백 상태가 아닌 경우
        de = array_s[top]
        array_s.remove(de) # 스택 마지막 항목 제거
        array_s.append(None)
        top -= 1
        return de
        
    else:
        print("stack underflow") # 공백 상태
        exit()
        
def peek_s():
    if not isEmpty_s(): # 공백 상태가 아닌 경우
        return array_s[top]
    else: pass # underflow 예외는 처리 하지 않음

def size_s():
    print(top+1) # 현재 스택에 있는 요소의 수 반환

def isEmpty_q():
    return front == rear

def isFull_q():
    return front == (rear+1) % capacity
    
def enqueue(item):
    global rear
    if not isFull_q():
        array_q[rear] = item
        rear += 1

def dequeue():
    global front
    global rear
    if not isEmpty_q():
        fr = array_q[front]
        array_q.remove(fr) # 큐에서 삭제
        array_q.append(None) # 목록 공간 일정하게 유지
        rear -= 1
        push(fr) # 스택에 추가
        return fr
    else: 
        print("목록이 비어있음")

def peek_q():
    global front
    if not isEmpty_q():
        return array_q[front]
    else:
        print("목록이 꽉참")
    
def size_q():
    global rear
    global front
    print(rear - front)

def __str__():
    if front < rear:
        return str(array_q[front+1:rear+1])
    else:
        return str(array_q[front+1:capacity] + array_q[0:rear+1])

def print_array_without_none(array): # 리스트 출력시 None요소는 제외하고 출력
    filtered_array = list(filter(lambda x: x is not None, array))
    print(filtered_array)

while True:
    now = datetime.now()
    
    if now.date() != current_date:
        daily_task()
        current_date = now.date()
        
    print("<<약물 복용 관리 시스템>>")
    print("필요한 서비스를 입력하세요.")
    print("1: 복용한 약 추가")
    print("2: 최근 복용한 약 제거")
    print("3: 복용한 약 목록")
    print("4: 복용한 약 개수")
    
    print("-----------------------------")
    
    print("5: 복용할 약 추가")
    print("6: 복용할 약을 섭취했다면 입력")
    print("7: 복용할 약 목록")
    print("8: 복용할 약 개수")
    
    print("0: 프로그램 종료")
    
    n = int(input())
    
    if n == 1:
        med = input()
        push(med)
        print("")
    elif n == 2:
        print(pop())
        print("")
    elif n == 3:
        print(array_s)
        print("")
    elif n == 4:
        size_s()
        print("")
    
    elif n == 5:
        med = input()
        enqueue(med)
        print("")
    elif n == 6:
        dequeue()
        print("")
    elif n == 7:
        print_array_without_none(array_q)
        print("")
    elif n == 8:
        size_q()
        print("")
    
    elif n == 0:
        break
   
    else:
        print("올바른 번호를 입력해주세요.")
        print("")
        