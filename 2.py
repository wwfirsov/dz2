s = list(input('Введите элементы списка: '))

result_list =[]
result_end =[]

var_1 = 0
var_2 = 2

for el in s:
    result_list = s[var_1:var_2]
    result_list.reverse()
    result_end = result_end + result_list
    var_1 = var_1 + 2
    var_2 = var_2 + 2
print('Результат:', ''.join(result_end))







