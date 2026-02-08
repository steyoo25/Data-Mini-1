import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Grade': [
        'Grade 3', 'Grade 4', 'Grade 5',  # Elementary
        'Grade 6', 'Grade 7', 'Grade 8',  # Middle
        'English I', 'English II'         # High School
    ],
    'School Level': [
        'Elementary', 'Elementary', 'Elementary',
        'Middle', 'Middle', 'Middle',
        'High School', 'High School'
    ],
    'Region 1 (Edinburg)': [50, 56, 59, 54, 53, 56, 47, 52],
    'Region 19 (El Paso)': [51, 57, 60, 54, 53, 57, 45, 52],
    'State Average':       [44, 48, 52, 48, 46, 51, 42, 47]
}

df_scores = pd.DataFrame(data)

df_scores.to_csv('reading_outcomes_2025.csv', index=False)
print("✅ Saved 'reading_outcomes_2025.csv' for GitHub.")

df_long = df_scores.melt(
    id_vars=['Grade', 'School Level'], 
    var_name='Region', 
    value_name='Score'
)

plt.figure(figsize=(12, 6))

sns.lineplot(
    data=df_long, 
    x='Grade', 
    y='Score', 
    hue='Region', 
    style='Region', 
    markers=True, 
    dashes=False, 
    linewidth=2.5,
    palette=['#1f77b4', '#2ca02c', 'grey'] # Blue (R1), Green (R19), Grey (State)
)

plt.axvspan(-0.5, 2.5, color='orange', alpha=0.1, label='Elementary')
plt.axvspan(2.5, 5.5, color='purple', alpha=0.1, label='Middle')
plt.axvspan(5.5, 7.5, color='red', alpha=0.1, label='High School')

plt.title('The Representation Dividend: Hispanic Reading Outcomes (2025)', fontsize=14, fontweight='bold')
plt.ylabel('% Meets Grade Level (Reading)', fontsize=12)
plt.xlabel('Grade Level', fontsize=12)
plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig('reading_outcomes_chart.png') # Saves the image for your slides
plt.show()