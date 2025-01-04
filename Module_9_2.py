first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Если длина строк не менее 5 символов.
first_result = [x for x in first_strings if len(x) >= 5]

# Если длина слов равна
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]

sum_strings = first_strings + second_strings

# Запись в словарь при условии четность строк
third_result = {x: len(x) for x in sum_strings if len(x) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)