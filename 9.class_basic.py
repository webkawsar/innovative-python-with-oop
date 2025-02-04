# class Student:
#     name = 'Kawsar Ahmed'

# student = Student()
# print(student.name)


class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def info(self):
        print(self)
        return self.id, self.name


id_no = 101
name = "Kawsar"
student1 = Student(id_no, name)
st_id, st_name = student1.info()
print(st_id, 'st_id')
print(st_name, 'st_name')












