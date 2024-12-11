#
#              # 0          1         2       3   4   5
# names_list = ["akash", "paresh", "rakesh", 33, 24, 89.6]
# print(names_list)
#
# print(type(names_list))
# print(names_list[2])
# print(names_list[-2])
# print(names_list[1:4])
# # print(names_list[-1:-4])
#
# names_list[3]= "walzade"
# print(names_list)

# String = "akash"
#
# for char in String :
#     if char == "k":
#         print("k is present in the string")
#
#         continue
#     else:
#
#         print(f'{char} is not u')
#
#     print("checking the nxt character")
# else:
#     print("k is not present")

print(234)
def check_even_or_odd(number_take):
    if number_take % 2 == 0:
        print(f'{number_take} is even number')

    else:
        print(f'{number_take} is odd number')



def multiply_two_numbers(number2 = 3, numbers1 = 5):
    print(f'numbers2 is {number2}')
    print(f'number1 is {numbers1}')

    numtiply_result = number2 * numbers1

    print(numtiply_result)
    return numtiply_result


multiply_two_numbers()



check_even_or_odd(9)


