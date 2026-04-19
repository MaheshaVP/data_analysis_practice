#pandas real ex using in code

import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E", "F"],
    "sales": [100, 200, None, 400, 500, 600]
}

df = pd.DataFrame(data)
print(df)

# print(df.dropna())

df['sales'] = df["sales"].fillna(df["sales"].mean())
print(df)

high = df[df["sales"] > 400]
print(high)

df["bonus"] = df["sales"] * 0.1
df["tax"] = df["sales"] * 0.05
print(df)

print("Average sales : ",df["sales"].mean())