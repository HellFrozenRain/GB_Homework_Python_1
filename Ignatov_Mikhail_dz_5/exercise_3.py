from itertools import zip_longest
# норм решение
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']



result = zip_longest(tutors, klasses[:len(tutors)])
print(type(result))
print(*list(result), sep='\n')


#так себе решение

# for el in range(len(tutors)):
#     if len(tutors) <= len(klasses):
#         result = (tup for tup in zip(tutors, klasses))
#     else:
#         for i in range(len(tutors) - len(klasses)):
#             klasses.append(None)
#         result = (tup for tup in zip(tutors, klasses))
# print(type(result))

print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))