# #check which attributes have which priority


# #check which is the minority case for each attribute # do we need this for STEMdegrees?? More helpful for gender?
# # # priorProgExpAdvanced = 0
# # priorProgExpSome = 0
# # priorProgExpNone = 0
# # priorSTEMDegreeStudents = 0

# # for student in StudentList:
# #     if student.priorSTEMDegree == True:
# #         priorSTEMDegreeStudents += 1
# #     if student.priorProgExp = 3:
# #         priorProgExpAdvanced += 1
# #     elif student.priorProgExp = 2:
# #         priorProgExpSome += 1
# #     elif student.priorProgExp = 1:
# #         priorProgExpNone += 1
# # 
# # STEMDegreeIsMinority = True
# # if priorSTEMDegreeStudents < (numberOfStudents/2):
# #     STEMDegreeIsMinority = True
# # else:
# #     STEMDegreeIsMinority = False
# #what about attributes that have multiple possibilites eg prior prog exp
# # if student is minprity case for all priority attributes, allocate these students to groups
# # if student is minority case for priority1 but not priority2, allocate these students next
# # if student is minority case for priority2 but not priority1, allocate these students next
# # allocate all other students

# class Student:
#     def __init__(self, name, priorProgExp, priorSTEMDegree):
#         self.name = name
#         self.priorProgExp = priorProgExp
#         self.priorSTEMDegree = priorSTEMDegree

#     def __str__(self):
#         return self.name
#     def __repr__(self):
#         return self.name

# helen = Student("helen", 1, False)
# jiachen = Student("jiachen", 0, False)
# hawwa = Student("hawwa", 2, True)
# bob = Student("bob", 0, True)
# steve = Student("steve", 0, False)
# jen = Student("jen", 1, False)
# ben = Student("ben", 1, True)
# nina = Student("nina", 2, True)
# sarah = Student("sarah", 2, False)
# tim = Student("tim", 1, False)
# charlie = Student("charlie", 0, False)
# ellie = Student("ellie", 2, True)

# #give score based on priority and characteristics
# #change form to store 3 for 1 and 1 for 3?? for priorities

# # if STEM degree = 1 
# # for student in students: multiply if STEM degree = True, score = STEM priority?
# # take prior prog score * by exp priority (highest = 6, lowest = 0)

# if stem priority = 3 and prior prog = 2
# Exp2STEM = 3+4=10
# Exp1STEM = 3+2=8
# Exp0STEM = 3
# Exp2NoSTEM = 4
# Exp1NoSTEM = 2
# Exp0NoSTEM = 0

# if priorprog = 3 and stem = 2
# Exp2STEM = 6+2=10
# Exp1STEM = 3+2=7
# Exp0STEM = 2
# Exp2NoSTEM = 6+0=6
# Exp1NoSTEM = 3
# Exp0NoSTEM = 0

# #store score in databasE? or put in lists? separate by gender?
# #put in two lists for men and women, ordered by score (also 'prefer not to say' - or add to men?)

# StudentList = [helen,jiachen,hawwa,bob,steve,jen,ben,nina,sarah,tim,charlie,ellie]

# Exp2STEM = []
# Exp1STEM = []
# Exp0STEM = []
# Exp2NoSTEM = []
# Exp1NoSTEM = []
# Exp0NoSTEM = []

# for student in StudentList:

#     if student.priorProgExp == 2 and student.priorSTEMDegree == True:
#         Exp2STEM.append(student)
#     elif student.priorProgExp == 1 and student.priorSTEMDegree == True:
#         Exp1STEM.append(student)
#     elif student.priorProgExp == 0 and student.priorSTEMDegree == True:
#         Exp0STEM.append(student)
#     elif student.priorProgExp == 2 and student.priorSTEMDegree == False:
#         Exp2NoSTEM.append(student)
#     elif student.priorProgExp == 1 and student.priorSTEMDegree == False:
#         Exp1NoSTEM.append(student)
#     elif student.priorProgExp == 0 and student.priorSTEMDegree == False:
#         Exp0NoSTEM.append(student)

# print("Exp2STEM = ", Exp2STEM,"Exp1STEM = ",  Exp1STEM, "Exp0STEM = ", Exp0STEM, "Exp2NoSTEM = ", Exp2NoSTEM, "Exp1NoSTEM = ", Exp1NoSTEM, "Exp0NoSTEM = ", Exp0NoSTEM)

# #check group size needed

# # maxGroupSize = lecturerSpec

# #create groups

# # numberOfGroups = (numberOfStudents / maxGroupSize)
# #rounded down but add remaining students to groups

# # class Group:
# #     def __init__(self, groupId, students):
# #         self.groupId = groupId
# #         self.students = students

# numberOfGroups = 10

# listOfGroups = []
# for x in range(numberOfGroups):
#     listOfGroups.append([x+1])


# def allocateCategoryOfStudents(category, startingGroupNumber):
#     print(category)
#     print("len(cat)=", len(category))
#     if len(category) == 0:
#         return startingGroupNumber
#     for x in range(startingGroupNumber, len(listOfGroups)):
#         print(startingGroupNumber, len(listOfGroups))
#         if len(category) > 0:
#             listOfGroups[x].append(category.pop())
#         else:
#             return listOfGroups[x][0]-1
#     while len(category) > 0:
#         for group in listOfGroups:
#             if len(category) > 0:
#                 group.append(category.pop())
#             else:
#                 return group[0]-1

# # print("output=", allocateCategoryOfStudents(Exp2STEM, 0))
# # print("output=", allocateCategoryOfStudents(Exp1STEM, 1))

# x = allocateCategoryOfStudents(Exp2STEM, 0)
# y = allocateCategoryOfStudents(Exp1STEM, x)
# z = allocateCategoryOfStudents(Exp0STEM, y)
# a = allocateCategoryOfStudents(Exp2NoSTEM, z)
# b = allocateCategoryOfStudents(Exp1NoSTEM, a)
# c = allocateCategoryOfStudents(Exp0NoSTEM, b)

# print("finalgrouplist=", listOfGroups)
# print("final categories=", Exp2STEM, Exp1STEM, Exp0STEM, Exp2NoSTEM, Exp1NoSTEM, Exp0NoSTEM)


@app.route("/groupallocations",methods=['GET','POST'])
@login_required
def groupallocations():
    intialStudents=User.query.filter(User.isLecturer==False)
    STEM = Option.query.filter(Option.optionID==2).first()
    STEMpriority = STEM.priority
    PriorExp = Option.query.filter(Option.optionID==1).first()
    PriorExpPriority = PriorExp.priority
    gender = Option.query.filter(Option.optionID==3).first()
    genderPairs = gender.priority
    numberPerGroup = Option.query.filter(Option.optionID==3).first()
    numberOfStudentsPerGroup = numberPerGroup.priority
    totalNumberOfStudents = User.query.filter(User.isLecturer==False).count()
    print("type numberOfStudentsPerGroup", type(numberOfStudentsPerGroup))
    print("type totalNumberOfStudents", type(totalNumberOfStudents))
    numberOfGroups = round(totalNumberOfStudents/numberOfStudentsPerGroup)
    totalFemale = User.query.filter(and_(User.isLecturer==False, User.gender=="F"))
    totalMale = User.query.filter(and_(User.isLecturer==False, User.gender=="M"))
    if totalMale >= totalFemale:
        majorityGender = "M"
    else:
        majorityGender = "F"

    studentScoresMajGender = []
    studentScoresMinGender = []
    allStudentScores = []
    for student in initialStudents:
        gender = student.gender
        STEM = student.priorSTEMDegree
        if STEM == True:
            STEMscore = STEMpriority
        else:
            STEMscore = 0
        PriorExp = student.priorProgExp
        PriorExpScore = PriorExp * PriorExpPriority
        score = STEMscore + PriorExpScore
        if genderPairs == True:
            if gender == majorityGender or gender == "O":
                studentScoresMajGender.append(student, score)
            else:
                studentScoresMinGender.append(student, score)
        else:
            allStudentScores.append(student, score)
    print(studentScoresMajGender)
    print(studentScoresMinGender)
    print(allStudentScores)
    #NEED TO SORT LISTS BY SCORE BEFORE ALLOCATION
    studentScoresMajGender = sorted(studentScoresMajGender, key = lambda x:x[1])
    studentScoresMinGender = sorted(studentScoresMinGender, key = lambda x:x[1])
    allStudentScores = sorted(allStudentScores, key = lambda x:x[1])

    print(studentScoresMajGender)
    print(studentScoresMinGender)
    print(allStudentScores)

    listOfGroups = []
    for x in range(numberOfGroups):
        listOfGroups.append([x+1])

    if genderPairs == False:
        while len(allStudentScores) > 0:
            for group in listOfGroups:
                if len(allStudentScores) > 0:
                    group.append(allStudentScores.pop(0)) #does pop go from start? need to pop highest score

    else:
        while len(studentScoresMinGender) > 0:
            for group in listOfGroups:
                if len(studentScoresMinGender) > 1:
                    group.append(studentScoresMinGender,pop(0)) #add minorityGender with highest score
                    group.append(studentScoresMinGender.pop(-1)) #add minorityGender with lowest score
                if len(studentScoresMinGender) == 1:
                    group.append(studentScoresMinGender.pop())
                else:
                    group.append(studentScoresMaxGender,pop(0)) #add majGender with highest score
                    group.append(studentScoresMaxGender.pop(-1))#add majGender with lowest score
        while len(studentScoresMajGender) > 0:
            for group in listOfGroups:
                if len(studentScoresMajGender) > 0:
                    group.append(studentScoresMajGender.pop(0))
                else:
                    break

    for group in listOfGroups:
        for x in range(1,len(group)):
            group[x][0].group = group[0]

    db.session.commit()

    students=User.query.filter(User.isLecturer==False)

    return render_template('groupallocations.html',title='Groupallocations',students=students, numberOfGroups = numberOfGroups)

    #give score based on priority and characteristics
    #change form to store 3 for 1 and 1 for 3?? for priorities

    # if STEM degree = 1 
    # for student in students: multiply if STEM degree = True, score = STEM priority?
    # take prior prog score * by exp priority (highest = 6, lowest = 0)

    # if stem priority = 3 and prior prog = 2
    # Exp2STEM = 3+4=10
    # Exp1STEM = 3+2=8
    # Exp0STEM = 3
    # Exp2NoSTEM = 4
    # Exp1NoSTEM = 2
    # Exp0NoSTEM = 0

    # if priorprog = 3 and stem = 2
    # Exp2STEM = 6+2=10
    # Exp1STEM = 3+2=7
    # Exp0STEM = 2
    # Exp2NoSTEM = 6+0=6
    # Exp1NoSTEM = 3
    # Exp0NoSTEM = 0

    #store score in databasE? or put in lists? separate by gender?
    #  put in two lists for men and women, ordered by score (also 'prefer not to say' - or add to men?)

    # for student in intialStudents:
    #     if student.priorProgExp == 2 and student.priorSTEMDegree == True:
    #         Exp2STEM.append(student)
    #     elif student.priorProgExp == 1 and student.priorSTEMDegree == True:
    #         Exp1STEM.append(student)
    #     elif student.priorProgExp == 0 and student.priorSTEMDegree == True:
    #         Exp0STEM.append(student)
    #     elif student.priorProgExp == 2 and student.priorSTEMDegree == False:
    #         Exp2NoSTEM.append(student)
    #     elif student.priorProgExp == 1 and student.priorSTEMDegree == False:
    #         Exp1NoSTEM.append(student)
    #     elif student.priorProgExp == 0 and student.priorSTEMDegree == False:
    #         Exp0NoSTEM.append(student)

    # numberOfGroups = 10

    # listOfGroups = []
    # for x in range(numberOfGroups):
    #     listOfGroups.append([x+1])


    # def allocateCategoryOfStudents(category, startingGroupNumber):
    #     if len(category) == 0:
    #         return startingGroupNumber
    #     for x in range(startingGroupNumber, len(listOfGroups)):
    #         if len(category) > 0:
    #             listOfGroups[x].append(category.pop())
    #         else:
    #             return listOfGroups[x][0]-1
    #     while len(category) > 0:
    #         for group in listOfGroups:
    #             if len(category) > 0:
    #                 group.append(category.pop())
    #             else:
    #                 return group[0]-1

    # x = allocateCategoryOfStudents(Exp2STEM, 0)
    # y = allocateCategoryOfStudents(Exp1STEM, x)
    # z = allocateCategoryOfStudents(Exp0STEM, y)
    # a = allocateCategoryOfStudents(Exp2NoSTEM, z)
    # b = allocateCategoryOfStudents(Exp1NoSTEM, a)
    # c = allocateCategoryOfStudents(Exp0NoSTEM, b)

    