import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  
student_scores = np.random.randint(0, 101, size=(32, 4))  

mask = np.random.rand(*student_scores.shape) < 0.1
student_scores[mask] = 0

subjects = ['Math', 'Science', 'English', 'History']

students_attended = np.count_nonzero(student_scores, axis=0)

subject_averages = []
for col in range(student_scores.shape[1]):
    valid_scores = student_scores[:, col][student_scores[:, col] > 0]
    avg = np.mean(valid_scores) if len(valid_scores) > 0 else 0
    subject_averages.append(avg)

max_index = np.argmax(subject_averages)
highest_subject = subjects[max_index]
highest_score = subject_averages[max_index]

print(f"Total Students: {student_scores.shape[0]}\n")
print("Students Attended per Subject:")
for subject, count in zip(subjects, students_attended):
    print(f"{subject}: {count} students")

print("\nAverage Score per Subject:")
for subject, avg in zip(subjects, subject_averages):
    print(f"{subject}: {avg:.2f}")

print(f"\nSubject with highest average: {highest_subject} ({highest_score:.2f})")

fig, ax1 = plt.subplots(figsize=(9, 5))

bars = ax1.bar(subjects, subject_averages, color='skyblue', label='Average Score')
bars[max_index].set_color('orange')  # Highlight top subject

for i, avg in enumerate(subject_averages):
    ax1.text(i, avg + 1, f"{avg:.1f}", ha='center', fontsize=10)

ax1.set_ylabel('Average Score', color='blue')
ax1.set_ylim(0, 100)

ax2 = ax1.twinx()
ax2.plot(subjects, students_attended, color='green', marker='o', linestyle='--', label='Students Attended')
ax2.set_ylabel('Number of Students', color='green')
ax2.set_ylim(0, 35)

plt.title(f'Subject-wise Performance (Total Students: {student_scores.shape[0]})')
fig.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()
