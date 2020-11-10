# 1. w : 쓰기 , r : 읽기
f = open("test.txt","w", encoding="utf8")

# 같은 폴더 안에 파일 생성
#f.write("test")

# 컴 설정이 utf8 이외면 글자 깨짐 현상 발생 -> open에 utf8 / utf-8 설정하기!
f.write("안녕")

# 2. w는 덮어쓰기 -> 끝줄에 추가 : a
f2 = open("test1.txt","a", encoding="utf-8")
# 개행문자 (\n) 추가하여 줄 나뉘기 가능
f2.write("append test\n")

f.close()
f2.close()

