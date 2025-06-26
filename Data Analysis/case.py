#write your code here
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Load the dataset
file_path = "StudentsPerformance .csv"
df = pd.read_csv(file_path)

# Rename columns for easier access
df.columns = ['gender', 'race', 'parent_education', 'lunch', 'prep_course', 'math_score', 'reading_score', 'writing_score']

# Display basic info
print("Dataset Info:")
print(df.info())

# Display first few rows
print("\nDataset Preview:")
print(df.head())

# Check for missing values
print("\nMissing values in Each Column:")
print(df.isnull().sum())

# Filter students whose parents have no higher education
non_higher_edu = df[df["parent_education"].isin(["some high school", "high school"])]

# Calculate the average exam scores for students with/without preparatory courses
prep_course_results = non_higher_edu.groupby("prep_course")[["math_score", "reading_score", "writing_score"]].mean()

# Display average scores
print("\nAverage Exam Scores Based on Test Preparation Enrollment:")
print(prep_course_results)

# Visualize: Math Score Impact
plt.figure(figsize = (12, 6))
sns.boxplot(x="prep_course", y="math_score", data=non_higher_edu, palette="Set2")
plt.title("Impact of Test Preparation on Math Scores (No Higher Education Parents)")
plt.xlabel("completed Test Prep Course")
plt.ylabel("Math Score")
plt.show()
plt.figure(figsize = (7, 5))

sns.barplot(x="prep_course", y="math_score", data=non_higher_edu, palette="Greens_d")
plt.title("Impact of Test Prep (Low Parental Education)")
plt.xlabel("Test Preparation Course")
plt.ylabel("Average Score")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()
# Perform T-test: Math Scores
prep_scores = non_higher_edu[non_higher_edu["prep_course"] == "completed"]["math_score"]
no_prep_scores = non_higher_edu[non_higher_edu["prep_course"] == "none"]["math_score"]
t_stat, p_value = ttest_ind(prep_scores, no_prep_scores, equal_var=False)

# Display test results
print("\nStatistical Test (T-test) Rsults for Math Scores:")
print(f"T-Statistic: {t_stat:.2f}, P-Value: {p_value:.4f}")

# Interpretation
if p_value < 0.05:
    print("✅ Statistically significant: Preparatory courses likely improve exam scores.")
else:
    print("❌ Not statistically significant: No strong evidence that preparatory courses improve exam scores.")