# 20. Write a Python class to find the three elements that sum to zero from
# a list of n real numbers.
# Input input_listay : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]

input_list=[-25, -10, -7, -3, 2, 4, 8, 10]


def sum_zero(input_list, n):
    output_list=[]
    list=[]
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if (input_list[i] + input_list[j] + input_list[k] == 0):
                    list.append(input_list[i])
                    list.append(input_list[j])
                    list.append(input_list[k])
                    output_list.append(list)
                    list=[]
    print(output_list)

sum_zero(input_list,len(input_list))

