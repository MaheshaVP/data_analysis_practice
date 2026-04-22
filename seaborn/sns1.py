#seaborn

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

names = sns.get_dataset_names()
# print(names)

penguins = sns.load_dataset('penguins')
# print(penguins)

c = penguins['species'].value_counts()
d = penguins['island'].value_counts()
# print(c)
# print(d)

# sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g',hue='island', palette='Dark2')
# sns.despine()

# sns.set_context('notebook')
# sns.stripplot(data=penguins, x='species', y='body_mass_g', hue='island', jitter=True)

# sns.set_context('talk')
# sns.swarmplot(data=penguins, x='species', y='body_mass_g', hue='island')
# sns.despine()

# sns.set_context('notebook')
# sns.histplot(data=penguins, x='body_mass_g', hue='sex', multiple='stack')

# sns.set_style('whitegrid')
# sns.lineplot(data=penguins, x='body_mass_g', y='flipper_length_mm',hue='sex')

sns.countplot(data=penguins, x='species', hue='island')

plt.show()

