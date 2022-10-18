def solution(s):
    a_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    n_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    zip_dict = dict(zip(a_list, n_list))

    for i in zip_dict.keys():
        if i in s:
            s = s.split(i)
            s.insert(s[1], zip_dict[i])
            s = ''.join(s)

    answer = int(s)

    return answer
print(solution('one4seveneight'))


# def solution(s):
#     a_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     n_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#
#     zip_dict = dict(zip(a_list, n_list))
#
#     for i in zip_dict.keys():
#         if i in s:
#             s = s.replace(i, zip_dict[i])
#     answer = int(s)
#
#     return answer
# print(solution("23four5six7"))

