# Create a spreadsheet pivot table as a DataFrame

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": ["foo", "foo", "foo", "foo", "foo","bar", "bar", "bar", "bar"],
    "B": ["one", "one", "one", "two", "two","one", "one", "two", "two"],
    "C": ["small", "large", "large", "small","small", "large", "small", "small","large"],
    "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
    "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]
    })

print(df)

# This first example aggregates values by taking the sum.
table = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc=np.sum)


# We can also fill missing values using the fill_value parameter.
table = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc=np.sum, fill_value=0)

print("\nPivot Table\n")
print(table)