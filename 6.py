sois=['ewt','se','vlsi']


sois.append('vr')
sois.insert(3,'big data')


print("Here is the list after sorting:")
for student in sorted(sois):
    print(student.title())

print("here is the list after reverse sorting")
for student in sorted(sois, reverse=True):
    print(student.title())