library(tidyverse)
library(patchwork)

df = read_csv("texasdata.csv")

str(df)

unique(df$campusName)
unique(df$region)
unique(df$grade_hi)
unique(df$grade_lo)

a = df |>
  group_by(region, race) |>
  summarise(
    teach = mean(teacher_frac),
    stud = mean(student_frac)
  ) |>
  mutate(diff = teach - stud)

p1 = ggplot(data = a, aes(region, teach, fill = race)) + 
  geom_col(position = "dodge")

p2 = ggplot(data = a, aes(region, stud, fill = race)) + 
  geom_col(position = "dodge")

p3 = ggplot(data = a, aes(region, diff, fill = race)) + 
  geom_col(position = "dodge")

p1/p2/p3



b = df |>
  group_by(schoolLevel, race) |>
  summarise(
    teach = mean(teacher_frac),
    stud = mean(student_frac)
  ) |>
  mutate(diff = teach - stud)

p1 = ggplot(data = b, aes(schoolLevel, teach, fill = race)) + 
  geom_col(position = "dodge")

p2 = ggplot(data = b, aes(schoolLevel, stud, fill = race)) + 
  geom_col(position = "dodge")

p3 = ggplot(data = b, aes(schoolLevel, diff, fill = race)) + 
  geom_col(position = "dodge")

p1/p2/p3



c = df |>
  group_by(locationType, race) |>
  summarise(
    teach = mean(teacher_frac),
    stud = mean(student_frac)
  ) |>
  mutate(diff = teach - stud)

p1 = ggplot(data = c, aes(locationType, teach, fill = race)) + 
  geom_col(position = "dodge")

p2 = ggplot(data = c, aes(locationType, stud, fill = race)) + 
  geom_col(position = "dodge")

p3 = ggplot(data = c, aes(locationType, diff, fill = race)) + 
  geom_col(position = "dodge")

p1/p2/p3


d = df |>
  group_by(charterSchool, race) |>
  summarise(
    teach = mean(teacher_frac),
    stud = mean(student_frac)
  ) |>
  mutate(diff = teach - stud)

p1 = ggplot(data = d, aes(charterSchool, teach, fill = race)) + 
  geom_col(position = "dodge")

p2 = ggplot(data = d, aes(charterSchool, stud, fill = race)) + 
  geom_col(position = "dodge")

p3 = ggplot(data = d, aes(charterSchool, diff, fill = race)) + 
  geom_col(position = "dodge")

p1/p2/p3

e = filter(df, race == "Hispanic")

f = filter(df, race == "Black")

g = filter(df, race == "white")

h = filter(df, race == "white" | race == "Hispanic")

ggplot(data = e, aes(s_econ_disadv_prop, student_frac, color = race)) + 
  geom_point(alpha = 0.1)

ggplot(data = f, aes(s_econ_disadv_prop, student_frac, color = race)) + 
  geom_point(alpha = 0.1)

ggplot(data = g, aes(s_econ_disadv_prop, student_frac, color = race)) + 
  geom_point(alpha = 0.1)

ggplot(data = h, aes(s_econ_disadv_prop, student_frac, color = race)) + 
  geom_point(alpha = 0.1)

ggplot(data = df, aes(s_econ_disadv_prop, student_frac, color = race)) + 
  geom_point()

df <- mutate(
  df,
  quartile = ntile(s_econ_disadv_prop, 4)
)

j = df |>
  group_by(quartile, race) |>
  summarise(
    teach = mean(teacher_frac),
    stud = mean(student_frac)
  ) |>
  mutate(diff = teach - stud)

p1 = ggplot(data = j, aes(quartile, teach, fill = race)) + 
  geom_col(position = "dodge")

p2 = ggplot(data = j, aes(quartile, stud, fill = race)) + 
  geom_col(position = "dodge")

p3 = ggplot(data = j, aes(quartile, diff, fill = race)) + 
  geom_col(position = "dodge")

p1/p2/p3

i = filter(df, region == "01")

i

