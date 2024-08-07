grades = [[5, 3, 3, 5, 4],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 3],
          [5, 5, 5, 4, 5]]
students ={'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students=list(students) #преобразуем множество в список
list_students.sort() #сортируем список по алфавиту
print (list_students) #проверка
# вычисляем средней балл, присвоив каждому элементу списка переменную
ave_1 = (grades[0])
ave_1 = sum(ave_1)/len(ave_1)
ave_2 = (grades[1])
ave_2 = sum(ave_2)/len(ave_2)
ave_3 = (grades[2])
ave_3 = sum(ave_3)/len(ave_3)
ave_4 = (grades[3])
ave_4 = sum(ave_4)/len(ave_4)
ave_5 = (grades[4])
ave_5 = sum(ave_5)/len(ave_5)
#повторяем фокус с присвоением для списка учеников
stu_1 = list_students[0]
stu_2 = list_students[1]
stu_3 = list_students[2]
stu_4 = list_students[3]
stu_5 = list_students[4]
#формируем словарь
average_match = {stu_1: ave_1, stu_2: ave_2, stu_3: ave_3, stu_4: ave_4, stu_5: ave_5 }
print (average_match)
#Задача выполнена для неизменного количества учеников.
