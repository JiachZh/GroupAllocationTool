#check which attributes have which priority


#check which is the minority case for each attribute # do we need this for STEMdegrees?? More helpful for gender?
# # priorProgExpAdvanced = 0
# priorProgExpSome = 0
# priorProgExpNone = 0
# priorSTEMDegreeStudents = 0

# for student in StudentList:
#     if student.priorSTEMDegree == True:
#         priorSTEMDegreeStudents += 1
#     if student.priorProgExp = 3:
#         priorProgExpAdvanced += 1
#     elif student.priorProgExp = 2:
#         priorProgExpSome += 1
#     elif student.priorProgExp = 1:
#         priorProgExpNone += 1
# 
# STEMDegreeIsMinority = True
# if priorSTEMDegreeStudents < (numberOfStudents/2):
#     STEMDegreeIsMinority = True
# else:
#     STEMDegreeIsMinority = False
#what about attributes that have multiple possibilites eg prior prog exp
# if student is minprity case for all priority attributes, allocate these students to groups
# if student is minority case for priority1 but not priority2, allocate these students next
# if student is minority case for priority2 but not priority1, allocate these students next
# allocate all other students

class Student:
    def __init__(self, name, priorProgExp, priorSTEMDegree):
        self.name = name
        self.priorProgExp = priorProgExp
        self.priorSTEMDegree = priorSTEMDegree

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

helen = Student("helen", 1, False)
jiachen = Student("jiachen", 0, False)
hawwa = Student("hawwa", 2, True)
bob = Student("bob", 0, True)
steve = Student("steve", 0, False)
jen = Student("jen", 1, False)
ben = Student("ben", 1, True)
nina = Student("nina", 2, True)
sarah = Student("sarah", 2, False)
tim = Student("tim", 1, False)

StudentList = [helen,jiachen,hawwa,bob,steve,jen,ben,nina,sarah,tim]

Exp2STEM = []
Exp1STEM = []
Exp0STEM = []
Exp2NoSTEM = []
Exp1NoSTEM = []
Exp0NoSTEM = []

for student in StudentList:

    if student.priorProgExp == 2 and student.priorSTEMDegree == True:
        Exp2STEM.append(student)
    elif student.priorProgExp == 1 and student.priorSTEMDegree == True:
        Exp1STEM.append(student)
    elif student.priorProgExp == 0 and student.priorSTEMDegree == True:
        Exp0STEM.append(student)
    elif student.priorProgExp == 2 and student.priorSTEMDegree == False:
        Exp2NoSTEM.append(student)
    elif student.priorProgExp == 1 and student.priorSTEMDegree == False:
        Exp1NoSTEM.append(student)
    elif student.priorProgExp == 0 and student.priorSTEMDegree == False:
        Exp0NoSTEM.append(student)

print("Exp2STEM = ", Exp2STEM,"Exp1STEM = ",  Exp1STEM, "Exp0STEM = ", Exp0STEM, "Exp2NoSTEM = ", Exp2NoSTEM, "Exp1NoSTEM = ", Exp1NoSTEM, "Exp0NoSTEM = ", Exp0NoSTEM)

#check group size needed

# maxGroupSize = lecturerSpec

#create groups

# numberOfGroups = (numberOfStudents / maxGroupSize)
#rounded down but add remaining students to groups

# class Group:
#     def __init__(self, groupId, students):
#         self.groupId = groupId
#         self.students = students

numberOfGroups = 10

listOfGroups = []
for x in range(numberOfGroups):
    listOfGroups.append([x+1])


def allocateCategoryOfStudents(category, startingGroupNumber):
    print(category)
    print("len(cat)=", len(category))
    if len(category) == 0:
        return startingGroupNumber
    for x in range(startingGroupNumber, len(listOfGroups)):
        print(startingGroupNumber, len(listOfGroups))
        if len(category) > 0:
            listOfGroups[x].append(category.pop())
        else:
            return listOfGroups[x][0]-1
    while len(category) > 0:
        for group in listOfGroups:
            if len(category) > 0:
                group.append(category.pop())
            else:
                return group[0]-1



# print("output=", allocateCategoryOfStudents(Exp2STEM, 0))
# print("output=", allocateCategoryOfStudents(Exp1STEM, 1))


x = allocateCategoryOfStudents(Exp2STEM, 0)
y = allocateCategoryOfStudents(Exp1STEM, x)
z = allocateCategoryOfStudents(Exp0STEM, y)
a = allocateCategoryOfStudents(Exp2NoSTEM, z)
b = allocateCategoryOfStudents(Exp1NoSTEM, a)
c = allocateCategoryOfStudents(Exp0NoSTEM, b)

print("finalgrouplist=", listOfGroups)
print("final categories=", Exp2STEM, Exp1STEM, Exp0STEM, Exp2NoSTEM, Exp1NoSTEM, Exp0NoSTEM)