# Как перечислить список, через запятую - одной строкой? 
# https://t.me/python_meet/261

str_list = ['раз', 'два', 'три']
print(*str_list, sep=', ')
print(', '.join(str_list))