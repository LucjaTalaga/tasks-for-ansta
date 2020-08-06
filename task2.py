
def get_list(data):
    input_list = data[0]
    n = data[1]
    output_list = []
    for i in range(1, n + 1):
        if i not in input_list:
            output_list.append(i)
    return output_list

user_data = input("[list], n: ")
print(get_list(user_data))