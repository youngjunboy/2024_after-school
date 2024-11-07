# class Jun :
#     def __init__(self, name) :
#         self.name = name
#         print(self.name + '은 초기화 이름')
#         print(name + '은 초기화 이름')
#     def work(self, it) :
#         print(self.name + "은 it" + it)

# obj = Jun('홍영준')    # obj = instance(실제 값 = 만들어진 값)
# obj.work('회사에 출근 합니다.')



# class Per:
#     def __init__(self, name) :
#         self.name = name
#         print(self.name + '님 안녕하세요~!')
#         print(name + '님 안녕하세요~!')
#     def work(self, high) :
#         print(self.name + '은 고등학교에 ' + high)

#     def what(self) :
#         print(self.name + '은 복싱을 하고 있습니다.')

#     age = 19
#     name = '홍영준'
#     @classmethod
#     def getAge(cls) :
#         return cls.age
#     @classmethod
#     def getName(cls) :
#         return cls.name
    
# obj = Per('홍영준')
# obj.work('등교합니다.')
# obj.what()
# print('나의 이름은', obj.name)

# print('클래스 변수 age : ', Per.getAge(), '클래스 변수 name : ', Per.getName())
# print('클래스 이름으로 출력 : ', Per.age, '클래스 변수 name : ', Per.name)
# print('클래스 인스턴스로 출력 : ', obj.age, '클래스 변수 name : ', obj.name)
