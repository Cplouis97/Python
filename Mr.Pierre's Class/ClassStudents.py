
class my_Class:
    ID = 2334756

    def __init__(self, fname, lname, sAge, sGPA, sEmail):
        self.sID = my_Class.ID
        self.fname = fname
        self.lname = lname
        self.sAge = sAge
        self.sGPA = sGPA
        self.sEmail = sEmail
        my_Class.ID += 1

    def full_name(self):
        return self.fname + " " + self.lname

    def print_info(self):
        print("Student Name: {} {}".format(self.fname, self.lname))
        print("Age: {}".format(self.sAge))
        print("GPA: {}".format(self.sGPA))


def remove_student(ArrayList):
    stuID = int(input("Enter your Student ID: "))
    foundStu = False
    for i in range(len(ArrayList)):
        if  stuID == ArrayList[i].sID:
            print("{} you have been removed from the class".format(ArrayList[i].full_name()))
            foundStu = True
            del ArrayList[i]
            break


    if foundStu != True:
        print("Sorry that Student ID was not found")

    pass


def main():
    ArrayList = []
    f = open('Students')

    while True:
        contents = f.readline()
        if not contents:
            break
        contents = contents.split(";")
        c1 = my_Class(contents[0],contents[1],int(contents[2]),float(contents[3]),contents[4])
        ArrayList.append(c1)

    f.close()

    print("Welcome to Mr. Pierre's Programming Class!")
    print("Here are the students in my class: \n")

    for i in range(len(ArrayList)):
        print(ArrayList[i].full_name())

    print(len(ArrayList))
    ans = input("\nIf there was a mistake and you need to be removed please enter 'y': ")

    if ans.lower() == 'y':
        remove_student(ArrayList)
        print("OK")

    print(len(ArrayList))



if __name__ == '__main__':
    main()