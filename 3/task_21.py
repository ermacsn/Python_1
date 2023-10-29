# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

list_ = [{"V": "S001", "1": "12"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "}, {" VIII ": " S007 "}]

list_new = []
for dict in list_:
    for key in dict:
        list_new.append(dict[key].strip())
list_new = set(list_new)
print(list_new)
result_set = set()
for dict in list_:
        result_set.add(dict.values())
print(result_set)
result = set(v.strip() for i in list_ for v in i.values())
print(result)