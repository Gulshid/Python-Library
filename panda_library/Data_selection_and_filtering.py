import pandas as pd

data = {
    "Student": ["Charlie", "Bob", "Frank", "ALice", "Diana"],
    "Math" : [89, 80, 67, 56, 70],
    "Science": [78, 69, 89, 66, 78],
    "English" : [89, 56, 88, 69, 90],
    "Grade": ["A+", "A", "B+", "B", "A"]
}

df = pd.DataFrame(data)

print("DataFrame of data :\n", df)

print("===========================")
# Data Selection and Filtering
print("Data Selection and Filtering :")
print("Student + Grade :\n", df[["Student", "Grade"]])
print("===========================")
print("Math + Science + English :\n", df[["Math", "Science", "English"]])


print("===========================")
print("Math > 80 :\n", df[df["Math"] > 70])

print("===========================")
print("Math > 70 and Science > 75 :\n", df[(df["Math"] > 70) & (df["Science"] > 75)])

print("===========================")
print("Student with Grade A+: \n", df.query("Grade == 'A+'"))