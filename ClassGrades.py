
class my_Class:
    def __init__(self, fname, lname, grade1, grade2, grade3):
        #'Construct' if you are use to java or C++
        self.fname = fname
        self.lname = lname
        self.grade1 = float(grade1)
        self.grade2 = float(grade2)
        self.grade3 = float(grade3)

    #Concatenates the first and last name to create the student's full name
    def full_name(self):
        return self.fname + " " + self.lname

    #calculates the student's average test grade
    def avg_grade(self):
        avgGrade= (self.grade1 + self.grade2 + self.grade3)/3
        return avgGrade

def main():
    #print("Hey YOU there, hey, hey, YOU There")
    ArrayList = [] #array placeholder
    f = open("Students.txt", "r") #file pointer

    #loop through the file
    while True:
        contents = f.readline()
        if not contents: #breaks the loop if there is no other line to read in file
            break
        contents = contents.split(";")
       #print(contents)
        c1 = my_Class(contents[0], contents[1], contents[2], contents[3], contents[4]) #my_Class object
        ArrayList.append(c1) #addthe object to the array
    f.close()

    cAvg = 0
    #This array prints the Average grade for each individual student
    for i in range(len(ArrayList)):
        cAvg += ArrayList[i].avg_grade()
        print(ArrayList[i].full_name() + "'s Average Test Grade is: ", end=" ")
        print("{0:.2f}".format(ArrayList[i].avg_grade()))

    cAvg = cAvg/len(ArrayList) # Avg of each individual average gives i=you the class average
    print("\nThe Average class test grade is : {0:.2f}".format(cAvg))


if __name__ == '__main__':
    main()
