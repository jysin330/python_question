# a = input("enter a  number : ")
# print(f"the multiplication table of {a} is : ")
# try:
#     for i in range(1,11):
#         print(f"{int(a)}*{i} = {int(a)*i}")
# except Exception as e:
#     print(e)
#     print("invalid input")
# print("some imp code")
# print("end of program")



# try:
#     num= int(input("enter an integer: "))
#     a=[6,3]
#     print(a[num])
# except ValueError:
#     print("number entered is not an integer")
# except IndexError:
#     print("index error")



def fun1():
    try:
        l=[1,2,3,4]
        i= int(input("enter index: "))
        return 1
    except:
        print("some error occurred")
        return 0
    finally:
        print("i am always executed") # i will executed after returning the value
        
        
    # print("i am always executed") # this will not executed after returning the value
x= fun1()
print(x)