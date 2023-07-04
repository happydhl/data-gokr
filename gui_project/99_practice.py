# lst = [1,2,3,4,5]
# print(lst)
# lst.reverse()
# print(lst)

# lst2 = [1,2,3,4,5]
# print("리스트 2  뒤집기 전:", lst2)

# lst3 = reversed(lst2)
# print("리스트 2  뒤집은 후:", lst2)
# print("리스트 3  :", list(lst3))

kor = ["사과", "오렌지", "바나나"]
eng = ["apple", "orage","banana"]

print(list(zip(kor,eng)))

mixed = [('사과', 'apple'), ('오렌지', 'orage'), ('바나나', 'banana')]
print(list(zip(*mixed)))

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)