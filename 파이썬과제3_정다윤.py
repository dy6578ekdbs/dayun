"""클래스와... 객체 """
class What :
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __str__(self):
        return "{}는 {}세이고, {}입니다.".format(self.name, self.age, self.sex)

what1 = What('짱구', 5, "여자")
what2 = What('도라에몽', 14, "남자")
what3 = What('코난', 8, "남자")
what4 = What('쇼콜라', 15, "여자")
what5 = What('아무', 12, "여자")
what6 = What('가영', 16, "여자")

print(what1)
print(what2)
print(what3)
print(what4)
print(what5)
print(what6)


