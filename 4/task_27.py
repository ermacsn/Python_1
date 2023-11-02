# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
input_text = ('She sells sea shells on the sea shore. The shells '
              'that she sells are sea shells I\'m sure. So if she sells sea '
              'shells on the sea shore. I\'m sure that the shells are sea shore shells.')
# Output: 13

text_list = ((input_text.replace('.',' ')).lower()).split()
text_set = set(text_list)
print(text_list)
print(text_set)
print(len(text_set))