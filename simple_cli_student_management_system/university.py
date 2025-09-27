import sqlite3


class University:
    
  #database and table create area start here
    db_name = "university.db"

    def __init__(self, versityName):
        self.versityName = versityName
        # self.students = []
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
          CREATE TABLE IF NOT EXISTS students(
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      studentId INTEGER NOT NULL UNIQUE,
                      name TEXT NOT NULL,
                      age INTEGER NOT NULL

                      )
"""
        )
#database and table create area end here


  #data insert area start here
    def addStudent(self, student):
        try:
            cursor = self.conn.cursor()

            cursor.execute(
                "SELECT * FROM students WHERE studentId = ?", (student.studentId,)
            )
            existing = cursor.fetchone()

            if existing:
                print(
                    f"Student with ID {student.studentId} already exists. Not inserting again."
                )
            else:
                cursor.execute(
                    "INSERT INTO students(studentId, name, age) VALUES (?, ?, ?)",
                    (student.studentId, student.name, student.age),
                )
                self.conn.commit()
                print(f"Student '{student.name}' added successfully.")
        except Exception as e:
            print("Error while adding student:", e)
    #data insert area end here




  #data update area start here
    def updateStudentData(self):
      cursor = self.conn.cursor()
      try:
          studentId = int(input("Enter Student ID to update: ").strip())
          
          # Check if student exists
          cursor.execute("SELECT * FROM students WHERE studentId = ?", (studentId,))
          existing = cursor.fetchone()

          if not existing:
              print(f"No student found with ID {studentId}.")
              return  # Function exit

          # if student exists
          new_name = input("Enter new name: ").strip()
          new_age = int(input("Enter new age: ").strip())

          # Update query
          cursor.execute(
              "UPDATE students SET name = ?, age = ? WHERE studentId = ?",
              (new_name, new_age, studentId)
          )
          self.conn.commit()
          print(f"Student with ID {studentId} updated successfully.")

      except Exception as e:
          print("Error while updating student data:", e)    

    #data update area end here



    # data delete area start here
    def deleteStudentData(self):
        cursor = self.conn.cursor()
        try:
            studentId = int(input("Enter Student ID to delete: ").strip())
            cursor.execute("DELETE FROM students WHERE studentId = ?", (studentId,))
            self.conn.commit()

            if cursor.rowcount > 0:
                print(f"Student with ID {studentId} deleted successfully.")
            else:
                print(f"No student found with ID {studentId}.")
        except ValueError:
            print("Please enter a valid number as Student ID.")

    # data delete area end here

    

  # data retrieve area start here
    def displayInfo(self):
        print("Universiyt Name: ", self.versityName)
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for student in rows:
            print(
                " DB id:",
                student[0],
                "\n" " Student Id : ",
                student[1],
                "\n",
                "Name:",
                student[2],
                "\n",
                "Age:",
                student[3],
            )
  # data retrieve area end here