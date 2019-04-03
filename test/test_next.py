
# items = [{'name':'chair'},{'name':'table'}]
# # 循环:
# while True:
#     try:
#         # 获得下一个值:
#         x = next(filter(lambda x: x['name']=='table', items), None)
#         print(x)
#     except StopIteration:
#         # 遇到StopIteration就退出循环
#         break
# def is_odd(n):
#     return n % 2 == 1
 
# tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# print(tmplist)



# items = ['a','b','c']
# # 循环:
# while True:
#     try:
#         # 获得下一个值:
#         x = next(filter(lambda x: x=='c', items), None)
#         print(x)
#     except StopIteration:
#         # 遇到StopIteration就退出循环
#         break


class User:
    def __init__(self, _id, username, password):
        self._id=_id
        self.username=username
        self.password=password

users=[User(1, 'bob', '123'),User(2, 'ddd', '123')]
user_mapping={u.username: u for u in users}
print(user_mapping)