# print(message)      #   --> error
# def greet():
#     message = [2, 3, 4]
#     print(message)      #   --> [2, 3, 4]
#
# message = [4, 5, 6]
# print(message)      #   --> [4, 5, 6]
# greet()
# print(message)      #   --> [4, 5, 6]






# def greet(message):
#     message = [2, 3, 4]
#     print(message)      #   --> [2, 3, 4]
#
# message = [4, 5, 6]
# print(message)      #   --> [4, 5, 6]
# greet(message)
# print(message)      #   --> [4, 5, 6]




# def greet(message):
#     message.append(2)
#     print(message)      #   --> [4, 5, 6, 2]
#
# message = [4, 5, 6]
# print(message)      #   --> [4, 5, 6]
# greet(message)
# print(message)      #   --> [4, 5, 6]




# def greet(message):
#     message[0] = 14
#     print(message)      #   --> [14, 5, 6]
#
# message = [4, 5, 6]
# print(message)      #   --> [4, 5, 6]
# greet(message)
# print(message)      #   --> [14, 5, 6]




# def greet(message):
#     message += "world"
#     print(message)      #   --> "helloworld"
#
# message = "hello"
# print(message)      #   --> "hello"
# greet(message)
# print(message)      #   --> "helloworld"




# def greet(message):
#     message = message + [3, 4, 5]
#     print(message, id(message))     #   --> [2, 1, 3, 4, 3, 4, 5]  rebinding and different id
#
# message = [2, 1, 3, 4]
# print(message, id(message))     #   --> [2, 1, 3, 4]
# greet(message)
# print(message, id(message))     #   --> [2, 1, 3, 4]  not mutating



# def greet(message):
#     message += [3, 4, 5]        #   --> [2, 1, 3, 4, 3, 4, 5]   mutating
#     print(message, id(message))
#
# message = [2, 1, 3, 4]
# print(message, id(message))     #   --> [2, 1, 3, 4]
# greet(message)
# print(message, id(message))     #   --> [2, 1, 3, 4, 3, 4, 5]




# def greet(message):
#     message += 3
#     print(message)      #   --> 5
#
# message = 2
# print(message)      #   --> 2
# greet(message)
# print(message)      #   --> 5

