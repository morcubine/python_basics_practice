##### DONT UNCOMMENT THE CODE OTHERWISE YOU MIGHT
# KNOW THE ANSWER  #####

# x = 10
#
# def test():
#     x = 20
#     print(x)    #   --> 20
#
# test()
# print(x)    #   --> 10




# count = 10
#
# def increase():
#     count = count + 1
#     print(count)
#
# increase()


# count = 10
#
# def increase():
#     global count
#     count = count + 1
#     print(count)      #   --> 11  /   --> 10
#
# increase()
# increase()
# # print(count)    #   --> 12


# count = 10
#
# def increase(n):
#     return n + 1
#
#
# count = increase(count)
# print(count)      #   --> 11




# name = "Python"
#
# def change():
#     name = "Java"
#     print(name)     #   --> 'Java'
#
# change()
# print(name)     #   --> 'Python'



# x = 100
#
# def first():
#     x = 50
#     print(x)    #   --> 50
#
# def second():
#     print(x)    #   --> 100
#
# first()
# second()



# a = 10
#
# def test():
#     b = 20
#     print(a + b)    #   --> 20
#
# test()
# print(a)    #   --> 10




# x = 5
#
# def test():
#     x = 10
#
#     if x > 5:
#         x = 20
#
#     print(x)    #   --> 20
#
# test()
# print(x)    #   --> 5





# x = 10
#
# def test():
#     for x in range(3):
#         pass
#
#     print(x)    #   --> 10
#
# test()
# print(x)    #   --> 10




# value = 100
#
# def calculate(value):
#     value *= 2
#     return value
#
# result = calculate(value)
# # value = calculate(value)
#
# print(result)   #   --> 200
# print(value)    #   --> 200




# x = 10
#
# def test():
#     print(x)    #   --> error (not associated)
#     x = 20
#
# test()





# x = 10
#
# def test():
#
#     if False:
#         x = 20
#
#     print(x)    #   --> 10
#
# test()





# x = 5
#
# def one():
#     x = 10      #   --> error
#     two()
#
# def two():
#     print(x)    #   --> 5
#
# one()