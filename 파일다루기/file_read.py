# 1. r : 전체 읽기
f = open('test.txt','r')
print(f.read())

# f.read()를 추가로 실행하면 읽지 못함! -> 끝까지 읽은 상태라서 다음 읽기 불가..
# seek을 통해 어디를 읽는지 초기화 가능
f.seek(0)
print(f.read())
