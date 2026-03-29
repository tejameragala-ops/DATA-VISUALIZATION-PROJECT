import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# Calculate average
df['Average'] = df[['Maths','Science','English']].mean(axis=1)

# Find topper
topper = df.loc[df['Average'].idxmax()]

# Pass/Fail
df['Result'] = df['Average'].apply(lambda x: 'Pass' if x >= 50 else 'Fail')

# Subject average
subject_avg = df[['Maths','Science','English']].mean()

# Print outputs
print("Student Data:\n", df)
print("\nTopper:\n", topper)
print("\nSubject Average:\n", subject_avg)

# Plot graph
plt.bar(df['Name'], df['Average'])
plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Save output
df.to_csv("output.csv", index=False)