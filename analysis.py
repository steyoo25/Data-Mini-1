import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('texasdata.csv')

df_hispanic = df[(df['race'] == 'Hispanic') & (df['grade_lo'] >= -1) & (df['grade_hi'] <= 9)].copy()

df_hispanic['rep_gap'] = df_hispanic['student_frac'] - df_hispanic['teacher_frac']

relevant_locations = ['City-Large', 'Suburb-Large', 'Rural-Remote']
df_filtered = df_hispanic[df_hispanic['locationType'].isin(relevant_locations)]

plt.figure(figsize=(12, 7))
sns.scatterplot(
    data=df_filtered, 
    x='s_econ_disadv_prop', 
    y='rep_gap', 
    hue='locationType',     # Colors by City/Suburb/Rural
    style='locationType',   # Different shapes for accessibility
    alpha=0.6,
    palette='deep'
)

sns.lmplot(
    data=df_filtered, 
    x='s_econ_disadv_prop', 
    y='rep_gap', 
    hue='locationType', 
    scatter=False,
    legend=False,
    palette='deep',
    height=6, aspect=1.5
)

plt.title('Poverty vs. Hispanic Representation Gap (City vs. Suburban vs. Rural)', fontsize=12)
plt.xlabel('Proportion of Economically Disadvantaged Students', fontsize=12)
plt.ylabel('Representation Gap (Student % - Teacher %)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)

print("--- Correlation by Location Type ---")
for loc in relevant_locations:
    subset = df_filtered[df_filtered['locationType'] == loc]
    corr = subset['s_econ_disadv_prop'].corr(subset['rep_gap'])
    print(f"{loc}: {corr:.3f}")

plt.show()