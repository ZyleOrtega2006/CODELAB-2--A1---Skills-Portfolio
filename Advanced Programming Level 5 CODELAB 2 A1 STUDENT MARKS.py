import tkinter as tk
from tkinter import ttk, messagebox

# Makes the main application window
root = tk.Tk()
root.title("Student Manager")
root.geometry("600x400")
root.config(bg="#e9f2f4") # CHanges the color of the background

def load_data(): # Loads the data from the file and also returns the list of student record with the grades calculated
    student_list = []  # Fixed: Changed from students to student_list for consistency
    try:
        with open("studentMarks.txt", "r") as file:
            # Skip header line and process each student record

             lines = file.readlines()[1:]
             for line in lines:
                        # Splits the CSV data into individual fileds 
                        num, name, m1, m2, m3, exam = line.strip().split(",")
                        # Converts the string value to integers
                        m1=int(m1)
                        m2=int(m2)
                        m3-int(m3) # Fixed: Changed from m3-int(m3) to m3 = int(m3)
                        exam=int(exam)
                        
                        # Calculates the totla coursework and overall percentage 
                        mark_total = m1+m2+m3
                        overall = ((mark_total+exam) / 100)* 100 # Calculate percentage  
                        
                        # Determines grade based on overall percentage
                        if overall >= 70: grade= "Grade: A"
                        elif overall >= 60: grade = "Grade: B"
                        elif overall >= 50: grade = "Grade: C"
                        elif overall >= 40: grade = "Grade: D"
                        else: grade = "Grade: F"
                        
                        # Adds the student record to the list 
                        students.append([num, name, mark_total, exam, overall, grade])                        
        return student_list
    except FileNotFoundError:
        messagebox.showerror("Sorry, studentMarks.txt not found")

def view_data(): # Displays all the studetns record with a summary statistic
    text.delete(1.0,tk.END) # Clears the widget of the text
    total = 0  # Inititalizes total for average calculation

    # Loop through each student and display their details
    for s in students:
        text.insert(tk.END, f"{s[1]} ({s[0]})\nCoursework: {s[2]}\nExam: {s[3]}\nOverall: {s[4]:.1f}% Grade: {s[5]}\n\n") # Adds the students overall mark to the total
        total += s[4] # Adds to the running total
    
    # Calculate and display the average score     
    avg = total /len (students)
    text.insert(tk.END, f"Total Students: {len(students)}\nAverage: {avg:.1f}%")
    
def view_one():  # Displays the selected student's details from the dropdown
    name = combo.get() # Get selected student name from dropdown 
    text.delete(1.0, tk.END) # Clear text box
    
    # Search for the student by their name 
    for s in students: 
        if s[1] == name:
            text.insert(tk.END, f"Name: {s[1]}\nNumber: {s[0]}\nCoursework: {s[2]}\nExam: {s[3]}\nOverall: {s[4]:.1f}%\nGrade: {s[5]}")
            return
    # If the students arent found then it shows an error message     
    messagebox.showinfo("Not found", "Student Record not found")

def highest():
    # Finds and displays the student with the highest overall percentage 
    top = max(students, key=lambda s: s[4]) # Gets the student with the max overall %
    text.delete(1.0, tk.END)
    text.insert(tk.END, f"Highest: {top[1]} ({top[0]})\nOverall: {top[4]:.1f}% Grade: {top[5]}")
    
def lowest(): # Finds display the student with the lowest overall percentage
    low = min(students, key=lambda s: s[4]) # Now it finds the student with the min overall %
    text.delete(1.0, tk.END)
    text.insert( tk.END,  f"Lowest: {low[1]} ({low[0]})\nOverall: {low[4]:.1f}% Grade: {low[5]}")                            


# Load data from the text file 
students = load_data()

# Title Label
tk.Label(root, text="Student Manager", font=("Arial", 16, "bold"), bg="#e9f2f4").pack(pady=5)

# The frame to hold the buttons 
frame = tk.Frame(root, bg="#e9f2f4")
frame.pack()

# The buttons for viewing the data and stats in the Students CSV
tk.Button(frame, text="View All", width=15, command=view_data).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="Highest", width=15, command=highest).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame, text="Lowest", width=15, command=lowest).grid(row=0, column=2, padx=5, pady=5)

# Dropdown to select the individual students 
tk.Label(root, text="Select Student:", bg="#e9f2f4").pack(pady=5)
combo = ttk.Combobox(root, values=[s[1] for s in students], width=25)
combo.pack()

# The button to view individual students
tk.Button(root, text="View Individual", command=view_one).pack(pady=5)

# Text widget to display output 
text = tk.Text(root, height=10, width=65)
text.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
    