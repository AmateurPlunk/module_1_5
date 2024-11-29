immutable_var = 1, 2, 3, 'слово', False
print(immutable_var)
#immutable_var.remove('слово') Значения элементов кортежа нельзя изменить, потому что кортежи неизменяемы.Это означает, что после создания кортежа его элементы нельзя изменить, добавить или удалить
mutable_list = [4, 5, 6,]
mutable_list.append(True)
mutable_list.remove(4)
print(mutable_list)