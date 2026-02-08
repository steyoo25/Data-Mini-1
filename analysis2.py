import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load Data
df = pd.read_csv('texasdata.csv')

# 2. Filter for Hispanic (Largest demographic)
df_hisp = df[df['race'] == 'Hispanic'].copy()

# 3. Calculate the Representation Gap
# Gap = Student % - Teacher %
df_hisp['rep_gap'] = df_hisp['student_frac'] - df_hisp['teacher_frac']

# 4. Calculate Average Gap by School Level
# We use these averages to populate the specific grades
level_means = df_hisp.groupby('schoolLevel')['rep_gap'].mean()
elem_gap = level_means['Elementary']
mid_gap = level_means['Middle']
high_gap = level_means['High School']

# 5. Create a New Dataset for Grades 3-8 & English I/II
# This maps the School Level data to the User's desired Grade Level format
grade_data = pd.DataFrame({
    'Grade': [
        'Grade 3', 'Grade 4', 'Grade 5',  # Elementary
        'Grade 6', 'Grade 7', 'Grade 8',  # Middle
        'English I', 'English II'         # High School
    ],
    'Representation Gap': [
        elem_gap, elem_gap, elem_gap, 
        mid_gap, mid_gap, mid_gap, 
        high_gap, high_gap
    ],
    'School Level': [
        'Elementary', 'Elementary', 'Elementary',
        'Middle', 'Middle', 'Middle',
        'High School', 'High School'
    ]
})

# 6. The "Step Function" Visualization
plt.figure(figsize=(12, 6))

# Bar Plot with Hue to show the "Jumps" between levels
ax = sns.barplot(
    data=grade_data, 
    x='Grade', 
    y='Representation Gap', 
    hue='School Level', 
    palette=['#ff9999', '#cc0000', '#660000'], # Light Red -> Dark Red (Danger increases)
    dodge=False,    # Keeps bars centered
    edgecolor='black'
)

# Formatting
plt.title('The Leaky Pipeline: Representation Gap Across Grades 3–12', fontsize=16, fontweight='bold')
plt.xlabel('Student Grade Level', fontsize=12)
plt.ylabel('Representation Gap (Higher is Worse)', fontsize=12)
plt.ylim(0, 0.35) 
plt.legend(title='School Level', bbox_to_anchor=(1.02, 1), loc='upper left')

# Add Labels on top of bars
for i in ax.containers:
    ax.bar_label(i, fmt='%.1f%%', fontsize=11, padding=3)

plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()

# Save specifically for your report
plt.savefig('leaky_pipeline_by_grade.png')
plt.show()
