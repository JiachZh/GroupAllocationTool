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

helen = Student("helen", 2, False)
jiachen = Student("jiachen", 1, False)
hawwa = Student("hawwa", 3, True)

StudentList = [helen,jiachen,hawwa]
print(StudentList)

Exp3STEM = []
Exp2STEM = []
Exp1STEM = []
Exp3NoSTEM = []
Exp2NoSTEM = []
Exp1NoSTEM = []

for student in StudentList:

    if student.priorProgExp == 3 and student.priorSTEMDegree == True:
        Exp3STEM.append(student)
    elif student.priorProgExp == 2 and student.priorSTEMDegree == True:
        Exp2STEM.append(student)
    elif student.priorProgExp == 1 and student.priorSTEMDegree == True:
        Exp1STEM.append(student)
    elif student.priorProgExp == 3 and student.priorSTEMDegree == False:
        Exp3NoSTEM.append(student)
    elif student.priorProgExp == 2 and student.priorSTEMDegree == False:
        Exp2NoSTEM.append(student)
    elif student.priorProgExp == 1 and student.priorSTEMDegree == False:
        Exp1NoSTEM.append(student)

print(Exp3STEM, Exp2STEM, Exp1STEM, Exp3NoSTEM, Exp2NoSTEM, Exp1NoSTEM)

#check group size needed

maxGroupSize = lecturerSpec

#create groups

numberOfGroups = (numberOfStudents / maxGroupSize)#rounded up

class Group:
    def __init__(self, groupId, students):
        self.groupId = groupId
        self.students = students
    