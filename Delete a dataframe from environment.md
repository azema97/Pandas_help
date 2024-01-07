# 🚮 Delete a dataframe from environment

In Python, if you want to delete a DataFrame from your environment, you can use the `del` statement followed by the DataFrame's name. Here's an example:

```python
import pandas as pd

# Creating a DataFrame
data = {'Column1': [1, 2, 3], 'Column2': ['A', 'B', 'C']}
df = pd.DataFrame(data)

# Displaying the DataFrame
print("Original DataFrame:")
print(df)

# Deleting the DataFrame
del df

# Attempting to print the DataFrame after deletion will result in an error
# Uncommenting the following line will raise an error since the DataFrame is deleted
# print(df)
```

In this example, the `del df` statement is used to delete the DataFrame. After deletion, any attempt to use the DataFrame will result in an error. Be cautious when using `del` because it removes the reference to the DataFrame, and if there are other references to the same DataFrame, they will still exist. If you want to clear all variables from the environment, you can use the `%reset` magic command in IPython or Jupyter Notebooks.

```python
%reset -f
```

This command will remove all variables from the environment, including DataFrames. Use it carefully, as it will clear all variables, not just the DataFrames.