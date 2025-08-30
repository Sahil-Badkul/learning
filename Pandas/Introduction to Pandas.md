# Introduction to Pandas

*-Learn Basic Pandas with Leetcode 15 question*

## **Pandas Data Structures**

### **2877. Create a DataFrame from List**

```python
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns = ["student_id", "age"])
    return df
```

## **Data Inspection**

### **2878. Get the Size of a DataFrame**

```python
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    # print(len(players), len(players[0])) # This will raise an error as [0] not exist
    
    # Approach 1
    return [len(players), len(players.columns)]
    
    # Approach 2
    return list(players.shape)
```

### **2879. Display the First Three Rows**

```python
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
```

Some alternatives:

| **Method** | **Description** | **Recommended?** |
| --- | --- | --- |
| **`.head(3)`** | Clear and intuitive | ✅ Best practice |
| **`.iloc[:3]`** | Explicit positional slicing | ✅ Very good alternative |
| **`[:3]`** | Slicing shorthand | ✅ Works, simple |
| **`.loc[0:2]`** | Label slicing by index values | ⚠️ Only if index is as expected |

## **Data Selecting**

### **2880. Select Data**

```python
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    filtered_students = students[students['student_id'] == 101]
    return filtered_students[["name", "age"]]

# Alternatives
def selectDataloc(students: pd.DataFrame) -> pd.DataFrame:
	return students.loc[students["student_id"] == 101, ["name", "age"]]

# Chaining
def selectDataChaining(students: pd.DataFrame) -> pd.DataFrame:
    return (
        students[students['student_id'] == 101]
        .loc[:, ['name', 'age']]
    )
```

df.loc[…]

- **`.loc`** is an **attribute/property** of the DataFrame (not a method).
- You index with **`.loc[]`** using labels (row and column names).
- It allows powerful and flexible label-based selection and filtering.

| **Property** | **Selection Type** |
| --- | --- |
| **`.loc[]`** | Label-based indexing (by names) |
| **`.iloc[]`** | Integer position-based indexing |

> Trying to use an integer position in **`.loc[]`** that is not a label will raise a KeyError if the label doesn't exist.
> 

### **2881. Create a New Column**

In pandas, to create a new column, you simply assign to a new column name using **`df[new_column] = <values>`**

```python
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"]*2
    return employees
```

Alternatives:

| **Method** | **Modifies Original?** | **Functional / Chainable** | **Notes** |
| --- | --- | --- | --- |
| **`df['bonus'] = ...`** | Yes | No | Simple and most used |
| **`employees.assign(bonus=employees['salary'] * 2)`** | No | Yes | Best for chaining |
| **`df.insert(loc=len(df.columns), column='bonus', value=employees['salary'] * 2)`** | Depends if copied | No | Controls column order |
| **`employees.loc[:, 'bonus'] = employees['salary'] * 2`** | Yes | No | Same as simple assign |

## **Data Cleaning**

### **2882. Drop Duplicate Rows**

```python
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset = ['email'])
```

> **DataFrame.drop_duplicates(*subset=None*, ***, *keep='first'*, *inplace=False*, *ignore_index=False*)**
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html
> 

```python
df.drop_duplicates(subset=["name"], keep='last')
```

### **2883. Drop Missing Data**

```python
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset = ["name"])
```

> **DataFrame.dropna(***, *axis=0*, *how=<no_default>*, *thresh=<no_default>*, *subset=None*, *inplace=False*, *ignore_index=False*)[[source]](https://github.com/pandas-dev/pandas/blob/v2.3.1/pandas/core/frame.py#L6545-L6703)**

https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html
> 

### **2884. Modify Columns**

```python
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] *= 2
    return employees
```

### **2885. Rename Columns**

```python
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(
        columns={
            'id': 'student_id',
            'first': 'first_name',
            'last': 'last_name',
            'age': 'age_in_years'
        }
    )
```

### **2886. Change Data Type**

```python
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
		# Both methods will work
    # students['grade'] = students['grade'].astype(int)
    students = students.astype({'grade': int})
    return student
```

### **2887. Fill Missing Data**

```python
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    return products.fillna({'quantity': 0})
```

## **Table Reshaping**

### **2888. Reshape Data: Concatenate**

```python
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    result = pd.concat([df1, df2])
    return result
```

> https://pandas.pydata.org/docs/user_guide/merging.html
> 

### **2889. Reshape Data: Pivot**

```python
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(
        index = "month", 
        columns = "city", 
        values = "temperature"
    )
```

### **2890. Reshape Data: Melt**

```python
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(
        id_vars = 'product', 
        value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],
        var_name='quarter',
        value_name='sales'
    )
```

## **Advanced Techniques**

### **2891. Method Chaining**

```python
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values(by='weight', ascending = False)[['name']]
```