import re
# 정규식 
p = re.compile("ca.e") 
# . :한글자  ^ : 문자열의 시작  (^de) -> desk, destimna | fade(x)
# $ : 문자열의 끝 (se$) -> case, base | face(x)

#m = p.match("case") # 매칭 안되면 에러

# if m:
#     print(m.group())
# else:
#     print("매칭 되지 않음")

def print_match(m):
    if m:
        print("m.group() :",m.group()) # 일치하는 문자열 반환
        print("m.string :",m.string) # 입력받은 문자열
        print("m.start() :",m.start()) # 일치하는 문자열의 시작 INDEX
        print("m.end() :",m.end()) # 일치하는 문자열의 끝 index
        print("m.span() :",m.span()) # 일치하는 문자열의 시작 /띁 인덱스
    else:
        print("매칭 되지 않음")

#m = p.match("good")
#m = p.match("careless") # match : 주어진 문자열의 처음부터 일치 확인
# m = p.search("careless") # match : 주어진 문자열의 중에 일치 확인
# print_match(m)
#print(m.group()) # 매치 안되면 에러가 발생

#lst = p.findall("careless") # findall : 일치하는 모든 것을 리스트
# lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트
# print(lst)

# 1. re.compile("원하는 형태")
# 2. m=p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m=p.search("비교할 문자열"): 주어진 문자열 중에 일치 하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환
