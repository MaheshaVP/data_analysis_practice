
# ================================
# NUMPY PRACTICE QUESTIONS
# ================================
import numpy as np

# dataset
age = np.array([22, 25, np.nan, 35, 28, 40, 30, np.nan, 27, 32])
salary = np.array([20000, 25000, 30000, np.nan, 28000, 35000, 40000, 22000, np.nan, 32000])
experience = np.array([1, 3, 5, 7, 2, 10, 8, 4, 2, 6])

# ================================
# LEVEL 1: BASICS
# ================================

# 1. Print all arrays
print("Age :",age)
print("Salary : ",salary)
print("Experience : ",experience)

# 2. Find length of age array
print(len(age))

# 3. Find shape of salary array
print(salary.shape)

# 4. Get first value of age
print(age[0])

# 5. Get last value of salary
print(salary[-1])



# ================================
# LEVEL 2: MISSING VALUES
# ================================

# 6. Count number of NaN values in age
print(np.isnan(age).sum())

# 7. Replace NaN in age with mean
age_mean=(np.nanmean(age))
age_filled = np.where(np.isnan(age),age_mean,age)
print(age_filled)


# 8. Replace NaN in salary with median
salary_median = np.nanmedian(salary)
salary_filled = np.where(np.isnan(salary),salary_median,salary)
print(salary_filled)

# ================================
# LEVEL 3: MATH OPERATIONS
# ================================

# 9. Find mean of age
print(np.nanmean(age))

# 10. Find median of salary
print(np.nanmedian(salary))

# 11. Find max experience
print(np.max(experience))

# 12. Find min salary
print(np.nanmin(salary))

# 13. Increase all salaries by 10%
salary_increased = salary*1.10
print(salary_increased)


# ================================
# LEVEL 4: FILTERING
# ================================

# 14. Get all ages greater than 30
print(age[age>30])

# 15. Get all salaries greater than 30000
print(salary[salary>30000])

# 16. Get indices where salary is NaN
print(np.where(np.isnan(salary)))


# ================================
# LEVEL 5: ADVANCED NUMPY
# ================================

# 17. Combine age and salary into 2D array
combine = np.column_stack((age,salary))
print(combine)

# 18. Reshape experience into (5,2)
reshaped_exp = experience.reshape(5,2)
print(reshaped_exp)

# 19. Stack arrays horizontally
h_stack = np.hstack((age.reshape(-1,1), salary.reshape(-1,1)))
print(h_stack)

# 20. Stack arrays vertically
v_stack = np.vstack((age,salary))
print(v_stack)


# ================================
# LEVEL 6: LOGICAL OPERATIONS
# ================================

# 21. Get values where age > 25 AND salary > 25000
result = (age>25) & (salary>25000)
print(age[result],salary[result])

# 22. Replace salary < 25000 with 25000
salary_updated = np.where(salary<25000,25000,salary)
print(salary_updated)


# ================================
# BONUS (OPTIONAL)
# ================================

# 23. Normalize salary (0 to 1 scale)
salary_norm = (salary - np.nanmin(salary)) / (np.nanmax(salary) - np.nanmin(salary))
print(salary_norm)

# 24. Find standard deviation of age
print(np.nanstd(age))

# 25. Sort salary array
print(np.sort(salary))


