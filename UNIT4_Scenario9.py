import numpy as np
import pandas as pd

course_names = [
    "Python Programming",
    "Full Stack Web Development",
    "Data Science & AI",
    "Cloud Computing",
    "Cyber Security",
    "UI/UX Design"
]
course_fees = np.array([15000, 32000, 45000, 28000, 35000, 18000])

avg_fee = np.mean(course_fees)
max_fee = np.max(course_fees)
min_fee = np.min(course_fees)

print("=== Course Fee Summary (NumPy) ===")
print(f"Average Course Fee: ₹{avg_fee:,.2f}")
print(f"Maximum Course Fee: ₹{max_fee:,}")
print(f"Minimum Course Fee: ₹{min_fee:,}\n")

df = pd.DataFrame({
    "Course Name": course_names,
    "Fee (₹)": course_fees
})

print("=== All Courses (Pandas DataFrame) ===")
print(df.to_string(index=False))
print()

high_fee_courses = df[df["Fee (₹)"] > 25000]

print("=== Courses with Fee Greater Than ₹25,000 ===")
print(high_fee_courses.to_string(index=False))
