from StackClass import Stack

def dec_2_bin(dec_number):
    stack=Stack()

    while dec_number > 0:
        result=dec_number % 2
        # print(result)
        stack.push(result)

        dec_number=dec_number // 2
        # print(dec_number)

    bin_string=""
    while stack.size() !=0:
        bin_string += str(stack.pop())

    return bin_string


print(dec_2_bin(108))
print(dec_2_bin(63))