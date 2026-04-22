#chatgpt simple ex

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Dept": ["IT", "HR", "IT", "Sales"],
    "Salary": [20000, 30000, 25000, 40000]
})

grouped = df.groupby('Dept')['Salary'].mean()

grouped.plot(kind='line')

plt.title("average sales by dept")
plt.ylabel("Salary")
plt.show()