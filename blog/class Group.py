class Group:
    def __init__(self,groupId, students):
        self.groupId = groupId
        self.students = students

#e.g. students list -- [name, id, .....]
#can Group class access User/Student 

    def addStudent(student, groupId):
        #to avoid adding same student in one group
        for student in groupId.students:
            if student not in group:
                students.append(student)
                print("Student added") 


    def removeStudent():

    def setGroupId():
    
    def getGroupId():

    def setSize():

    def getSize(groupId):
        num = 0
        for student in Group.students:
            while num < len(Group.studnets):
                num += 1
            return num
        print("There are" + str(num) + "students in Group" + str(groupId))

    def setStudents():

    def getStudents():

    def printGroupDetails(groupId):
        print 
        

   
#create some group instances 
groupA = Group("groupA", size, students)
groupB = Group("groupB", size, students)
   
groupA.getStudents()
groupA.printGroupDetails()
