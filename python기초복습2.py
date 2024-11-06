# a = 'hello'
# b = {'young' : 100, 'jun' : 200}
# print( list(a), list(b.keys()), list(b.values()), list(b.items()) )
# print( list(a[1]) )

# print( 3.14 )
# print( str(3.14) , type(str(3.14)) )

# a = [1,2,3]
# b = [4,5,6]
# print( a+b )
# print( a*2 )
# b[0:2] = [8,9]
# print( b )
# del b[0:2]
# print( b )
# a.append( 10 )
# print( a )
# print( a.index(10) )
# a.insert( 1, 20 )
# print(a)

# name = [ '홍', '영', '준' ]
# name.pop()
# print( name )
# # del name[0]
# print( name )
# name.remove( '영' )
# print( name )
# b = [ 1,2,3 ]
# b.extend( [4,5,6,7] )
# print( b )
# name.extend( ['hong', 'young'] )
# print(name)

# a = (1,2,3)
# print( a * 2 )

# dict = { 'name' : '홍영준', 'age' : 19 }
# print( dict )
# dict[ 'name' ] = '홍길동'
# print( dict )
# dict[ 'city' ] = 'Seoul'
# print( dict )
# del dict[ 'name' ]
# print( dict )
# dict.clear() # clear는 데이터 전체 삭제 del은 리스트 자체를 삭제
# print( dict )
# print( dict.get('age') )
# print( dict.get('addr', '없음'))

# a = set( [ 1, 2, 3, 1, 1, 3, 2, 3, 4 ] ) # 중복 제거
# print( a )
# b = { 1, 2, 3 }
# print( b )

# a = set( 'hello' ) # 순서가 없음
# print( a )

# name1 = { '홍', '영', '준' }
# name2 = {'홍', '길', '영'}
# print( set( name1 & name2 ) )
# print( name1.intersection( name2 ) )
# print( name1 | name2)
# print( name1.union(name2) )

# a = set( [1,2,3,4,5,6,7] )
# b = set( [6,7,8] )
# print( a - b )
# print( b - a )
# a.add( 10 )
# print( a )
# a.remove( 6 )
# print( a )

# from random import *

# people = range( 1, 21 )
# people = list( people )
# print( people )
# shuffle( people )
# print( people )
# one = sample( people, 3 )
# print( one )
# print( f'1등 : {one[0]}' )
# print( f'2등 : {one[1]}' )
# print( f'3등 : {one[2]}' )
# print( '1등 : {}'.format( one[0] ) )
# print( '2등 : {}'.format( one[1] ) )
# print( '3등 : {}'.format( one[2] ) )


# name = ['홍', '영', '준']
# i = 0
# while True:
#     print( name[i] )
#     i += 1
#     if i == 3:
#         break

# a = [ 1,2,3 ]
# b = a      # 주소와 값을 복사
# a[1] = 7
# print( b[1] )
# print( id(a), id(b) )

# a = [ 1,2,3 ]
# b = a[ : ]   # 값만 복사
# a[ 1 ] = 9
# print( a is b )
# print( id(a), id(b) )
# print(a, b)

# a, b = ( '홍', '이' )
# print(a)
# print(b)

# ( a, b ) = [ '홍', '이' ]
# print(a)
# print(b)

# a= b= '홍'
# print(a)
# print(b)

# a = 10
# b = 20
# c = 0
# c = a
# a = b
# b = c
# print( 'a = ', a, ',', 'b = ', b )

# x = 10
# y = 20
# x, y = y, x
# print( 'x = ', x, ',', 'y = ', y )

# money = True
# if money == True:
#     print( '택시 타' )
# else:
#     print( '버스 타' )

# math_score = 60
# eng_score = 35
# if math_score >= 20 or eng_score >= 60:
#      print( '잘했다' )
# else:
#     print( '열심히 하자' )

# name = [ '홍', '영', '준' ]
# if '영' in name:
#      print( '"영"은', name.index('영'), '번째 인덱스에 있습니다!' )

# i = 0
# while i < 100 :
#     if i % 2 == 1 :
#          print( i, end=' ' )
#     i += 1

# i = 1
# while True:
#     print(f'{i}번 손님 커피 나왔습니다!')
#     i += 1
#     if i > 5:
#         break

# bbackdabang = { 734:'제로콜라', 254:'닥터페퍼', 351:'뜨거운우유' }
# while True:
#     print( f'메뉴판 : 0 = 없음   734번 = 제로콜라   254번 = 닥터페퍼   351번 = 뜨거운우유' )
#     menu = int( input( '음료의 번호를 눌러주세요! : ' ) )
#     if menu == 0:
#         print( '이용해 주셔서 감사합니다~!' )
#         break
#     elif menu == 734:
#         print( f'{bbackdabang[734]} 나왔습니다 맛있게 드세요~')
#     elif menu == 254:
#         print( f'{bbackdabang[254]} 나왔습니다 맛있게 드세요~')
#     elif menu == 351:
#         print( f'{bbackdabang[351]} 나왔습니다 맛있게 드세요~')
#     else:
#         print('메뉴에 없는 번호입니다. 다시 입력해 주세요!')
