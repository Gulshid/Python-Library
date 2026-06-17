import matplotlib.pyplot as plt

# Bar Chart of Students and Their Marks 
students = ["Ali", "Ahmad", "Umar", "Hamza"]
marks = [88, 60, 57, 48]

# Create a Bar chart on the basis of Students Data
plt.bar(students, marks)

plt.title("*** Students Marks *** ")

plt.xlabel("Students")

plt.ylabel("Marks")

plt.show()