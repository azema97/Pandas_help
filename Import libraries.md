# Python Libraries: Quick import

---

### Basic libraries
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as skl
```

### Preprocessing libraries

```python
# Preprocessing libraries
from sklearn import preprocessing
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
```

### Machine Learning models
```python
# machine learning models
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold # Cross validation for Classification
from sklearn.model_selection import RepeatedKFold # Cross validation for Regression
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC # Kernelized support vector machines
from sklearn.neural_network import MLPClassifier # neural network
from sklearn.ensamble import RandomForestClassifier
from sklearn.ensamble import GradientBoostingClassifier

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensamble import RandomForestRegressor
from sklearn.ensamble import GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
```

### Metrics
```python
# metrics
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
```