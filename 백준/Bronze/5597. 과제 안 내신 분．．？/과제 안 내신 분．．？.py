students = [i for i in range(1, 31)]

for j in range(28):
    submit = int(input())
    students.remove(submit)

print(min(students))
print(max(students))