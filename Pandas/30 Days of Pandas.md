# 30 Days of Pandas

## **Data Filtering**

### **183. Customers Who Never Order**

```python
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    transactionDF = pd.merge(customers, orders, left_on = 'id', right_on = 'customerId', how = 'left')
    filteredDF = transactionDF[transactionDF['customerId'].isna()][["name"]]
    return filteredDF.rename(columns = {"name":"Customers"})
```

### **1148. Article Views I**

```python
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views["author_id"] == views["viewer_id"]][["author_id"]] \
         .drop_duplicates() \
         .sort_values(by = "author_id") \
         .rename(columns = {"author_id" : "id"})
    return df
```

## **String Methods**

### **1683. Invalid Tweets**

```python
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets[tweets["content"].str.len() > 15][["tweet_id"]]
    return df
```

### **1873. Calculate Special Bonus**

```python
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Initialize bonus column with 0
    employees["bonus"] = 0

    # Assign salary where employee_id is even
    employees.loc[(employees["employee_id"] % 2 != 0) & (~employees["name"].str.startswith("M")), "bonus"] = employees["salary"]

    return employees[["employee_id", "bonus"]].sort_values(by = "employee_id")
```

```python
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(
        bonus=employees.apply(lambda x: x['salary'] if int(x['employee_id']) % 2 != 0 and not x['name'].startswith('M') else 0, axis=1)
    )[['employee_id', 'bonus']].sort_values(
        by='employee_id',
    )
```

Let’s comparing two valid and commonly used Pandas techniques: **`.apply()` with lambda** vs **vectorized `.loc[]` assignment**. Let's break both down from a **technical, performance, and best-practice** perspective, including **time and space complexity**.

---

### 🧪 First: The Problem

> Assign bonus = salary if:
> 
> - `employee_id` is **odd**, and
> - `name` does **not** start with `"M"`
>     
>     Else, `bonus = 0`
>     

---

## ✅ Approach 1: `apply()` with lambda

```python
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(
        bonus=employees.apply(lambda x: x['salary'] if int(x['employee_id']) % 2 != 0 and not x['name'].startswith('M') else 0, axis=1)
    )[['employee_id', 'bonus']].sort_values(by='employee_id')

```

### 🔹 How it works:

- `.apply()` iterates **row by row**.
- Lambda function checks condition, assigns `salary` or `0`.
- `assign()` adds a new column without modifying the original DataFrame.

### ⏱️ Time Complexity:

- `O(n)` linear traversal of rows
- **But** `.apply(axis=1)` is **slower than vectorized operations** due to internal Python loops.

> ⚠️ Not efficient for large datasets.
> 

### 📦 Space Complexity:

- `O(n)` extra space for the new `bonus` column
- No copy of the full DataFrame unless chained

### ✅ Pros:

- Flexible, can handle complex row-wise logic
- Readable for small datasets

### ❌ Cons:

- **Slow** for large DataFrames (`n > 10^5`)
- Doesn’t leverage NumPy vectorization

---

## ✅ Approach 2: Vectorized `.loc[]` assignment

```python
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = 0
    employees.loc[
        (employees["employee_id"] % 2 != 0) & (~employees["name"].str.startswith("M")),
        "bonus"
    ] = employees["salary"]
    return employees[["employee_id", "bonus"]].sort_values(by="employee_id")

```

### 🔹 How it works:

- Creates a Boolean mask using vectorized conditions (efficient).
- Uses `.loc[]` to assign salary where mask is True.
- Directly modifies the DataFrame.

### ⏱️ Time Complexity:

- `O(n)` for vectorized condition evaluation
- **Much faster** than `.apply()` due to use of **NumPy-level operations**

### 📦 Space Complexity:

- `O(n)` for the new `bonus` column
- More memory efficient — no Python-level loop

### ✅ Pros:

- **Fast and scalable** (preferred for large data)
- Clean and concise logic
- Uses native Pandas/NumPy broadcasting

### ❌ Cons:

- Slightly less flexible than `.apply()` for row-specific complex operations

---

## 🔁 Side-by-Side Comparison

| Feature | `.apply()` Approach | Vectorized `.loc[]` Approach |
| --- | --- | --- |
| Performance | Slower (Python loop) | **Faster (NumPy vectorized)** |
| Readability | Good for small, complex logic | Clean and expressive |
| Flexibility | More flexible for arbitrary row logic | Limited to column-level operations |
| Best for large datasets | ❌ | ✅ |
| Time Complexity | `O(n)` but high constant factor | `O(n)` (vectorized) |
| Space Complexity | `O(n)` | `O(n)` |

---

## 🚀 Recommendation (Best Practice)

> ✅ Use vectorized .loc[] operations whenever possible
> 
> 
> Reserve `.apply(axis=1)` for truly non-vectorizable or deeply nested logic (e.g., row-based stateful computations or mixed types).
> 

---

### **1667. Fix Names in a Table**

### ✅ **Approach 1: Using `str.capitalize()`**

```python
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str.capitalize()
    return users.sort_values(by="user_id")

```

- **Explanation:** Capitalizes the first character, lowercases the rest.
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) (modifies in-place)
- **Pros:** Clean, readable, efficient.
- **Cons:** All letters except the first become lowercase.

---

### ✅ **Approach 2: Using `str.title()`**

```python
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str.title()
    return users.sort_values(by="user_id")

```

- **Explanation:** Capitalizes the first letter of **each word**, e.g., `'john doe'` → `'John Doe'`.
- **Use case:** Use this if names may have multiple words.
- **Pros:** Better for full names.
- **Cons:** Slightly more expensive than `capitalize()`.

---

### ✅ **Approach 3: Using `.apply()` with `str.capitalize()`**

```python
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].apply(lambda x: x.capitalize())
    return users.sort_values(by="user_id")

```

- **Explanation:** Similar to `str.capitalize()` but uses `.apply()`.
- **Time Complexity:** O(n), but **slower** than vectorized `str.capitalize()`.
- **Pros:** Useful if you need more complex logic inside the lambda.
- **Cons:** Less performant, not needed here.

---

### ✅ **Approach 4: Return a new DataFrame (immutable approach)**

```python
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    df = users.copy()
    df["name"] = df["name"].str.capitalize()
    return df.sort_values(by="user_id")

```

- **Explanation:** Does not modify original input.
- **Use case:** Good in production pipelines where mutating input is risky.
- **Cons:** Slightly more memory usage.

---

### Comparison Summary

| Approach | Best For | Mutates Original | Performance | Notes |
| --- | --- | --- | --- | --- |
| `str.capitalize()` | Simple one-word names | ✅ Yes | 🔹 Fast |  |
| `str.title()` | Full names (multi-word) | ✅ Yes | 🔸 Slightly Slower | Capitalizes each word |
| `.apply(lambda)` | Custom name logic | ✅ Yes | 🔸 Slower | Use for custom logic |
| `copy + capitalize()` | Immutable transformation | ❌ No | 🔹 Fast | Safe in prod |

---

### **1517. Find Users With Valid E-Mails**

```python
import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    df = users[users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\?com)?\.com$')]
    return df
```

**Regex Pattern**: `^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\?com)?\.com$`

Let's break down the regex pattern step by step to clearly explain each part:

- **^**: Anchor the regex pattern to match from the start of the string.
- **[A-Za-z]**: Match any single uppercase or lowercase letter. The email prefix name must start with a letter.
- **[A-Za-z0-9_.-]**: Match any number of characters following the first letter in the email prefix name. It includes letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'.
- **@**: Match the literal '@' character, which separates the prefix name and the domain.
- **leetcode**: Match the literal 'leetcode', which is part of the email domain.
- **(?com)?**: Make the sequence ?com optional in the email domain. Allows the pattern to match both '@leetcode.com' and '@leetcode?com'.
- **.** : Match the literal '.' character, which separates the 'leetcode' part from the 'com' part of the domain.
- **com**: Match the literal 'com' at the end of the email domain.
- **$**: Anchor the regex pattern to match until the end of the string.

**Explanation**:

The regex pattern ensures that a valid email must have the following format:

- The prefix name starts with a letter.
- The prefix name can contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'.
- The domain must be '@leetcode.com' with an optional '?com' part.

Using this regex pattern, both the pandas and MySQL queries can identify and select rows with valid email addresses from the 'Users' table based on the specified conditions.

---

### **1527. Patients With a Condition**

```python
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df = patients[(patients['conditions'].str.startswith('DIAB1')) | (patients['conditions'].str.contains(' DIAB1'))]
    return df
```

## **Data Manipulation**

### Nth Highest Salary

```python
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Remove duplicate salaries and sort in descending order
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    # Check if N is within bounds
    if N > len(unique_salaries) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # Get the N-th highest salary (N-1 index since 0-based)
    nth_salary = unique_salaries.iloc[N - 1]
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_salary]})

```

### **176. Second Highest Salary**

```python
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_employeeDF = employee['salary'] \
			  .drop_duplicates() \
			  .sort_values(ascending = False)

    if len(unique_employeeDF) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    
    second_salary = unique_employeeDF.iloc[1] # 1 because of 0 based Indexing
    return pd.DataFrame({'SecondHighestSalary': [second_salary]})
```

### **184. Department Highest Salary**

```python
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Get the highest salary per department
    highest_salary = employee.groupby('departmentId')['salary'].max().reset_index()

    # Step 2: Join with employee to get employee(s) who have the highest salary in their department
    df = pd.merge(employee, highest_salary, on=['departmentId', 'salary'])

    # Step 3: Join with department table to get department names
    df = pd.merge(df, department, left_on='departmentId', right_on='id')

    # Step 4: Select and rename relevant columns
    return df[['name_y', 'name_x', 'salary']].rename(columns={
        'name_y': 'Department',
        'name_x': 'Employee',
        'salary': 'Salary'
    })

```

In **pandas**, the `reset_index()` function is used to reset the index of a DataFrame back to the default integer index. This is particularly useful after operations that set or modify the index (like `groupby`, `set_index`, or filtering), and you want to:

1. **Move the index back into a regular column**, and
2. **Restore a default 0-based integer index**.

---

### 🔹 Syntax:

```python
df.reset_index(drop=False, inplace=False)
```

---

### 🔹 Parameters:

| Parameter | Description |
| --- | --- |
| `drop` | If `True`, the index is reset **without adding it as a column**. |
| `inplace` | If `True`, modifies the original DataFrame. Otherwise, returns a new one. |

---

### 🔹 Example:

```python
import pandas as pd

data = {'department': ['IT', 'HR', 'IT', 'HR'], 'salary': [1000, 800, 1200, 900]}
df = pd.DataFrame(data)

# Group by department
grouped = df.groupby('department').max()
print(grouped)

```

**Output:**

```
            salary
department
HR             900
IT            1200

```

Now, if you want to convert `department` back to a column:

```python
grouped_reset = grouped.reset_index()
print(grouped_reset)

```

**Output:**

```
  department  salary
0         HR     900
1         IT    1200

```

---

### 🔹 Use Cases:

- After `groupby`, where the grouped column becomes the index.
- When merging or joining DataFrames (since indexed columns are not automatically matched unless reset).
- For clean display or export.

---

### 178. Rank Scores

```python
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    return scores[['score', 'rank']].sort_values(by = 'rank')
```

### 196. Delete Duplicates Eamils

```python
import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    emailDF = person.groupby("email")["id"].min().values
    print(emailDF)
    person.drop(person[~person['id'].isin(emailDF)].index, inplace=True)
```

### **1795. Rearrange Products Table**

```python
import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    meltDf = products.melt(
        id_vars = ['product_id'], 
        value_vars = ['store1', 'store2', 'store3'],
        var_name = 'store',
        value_name = 'price').dropna()
    return meltDf
```

### 1907. Count Salary Categories

```python
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_salary = (accounts['income'] < 20000).sum()
    avg_salary = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum()
    high_salary = (accounts['income'] > 50000).sum()

    data = pd.DataFrame([
        {'category': 'Low Salary', 'accounts_count': low_salary},
        {'category': 'Average Salary', 'accounts_count': avg_salary},
        {'category': 'High Salary', 'accounts_count': high_salary}
    ])

    return data

```

### 1741. Find Total Time Spend by Each Employee

```python
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = (employees['out_time'] - employees['in_time'])
    data = employees.groupby(by = ['emp_id', 'event_day'])['total_time'].sum().reset_index()
    return data.rename(columns={'event_day': 'day'})
```

### 511. Game Play Analysis I

```python
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby(by = 'player_id')['event_date'].min().reset_index() \
        .rename(columns = {'event_date': 'first_login'})
    return df
```

### **2356. Number of Unique Subjects Taught by Each Teacher**

```python
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return (
        teacher.groupby('teacher_id')['subject_id']
               .nunique()
               .reset_index(name='cnt')
    )

```

### 596. Classes With at Least 5 Students

```python
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    classCountDf = courses.groupby(by = 'class')['student'].count().reset_index(name = 'cnt')
    return classCountDf[classCountDf['cnt'] >= 5][['class']]
```

### **586. Customer Placing the Largest Number of Orders**

```python
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.value_counts("customer_number", ascending=False).reset_index()
    return df.head(1)[['customer_number']]
```

### 1484. Group Sold Products by The Date

```python
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = activities.groupby('sell_date').agg(
        num_sold=('product', pd.Series.nunique),
        products=('product', lambda x: ','.join(sorted(set(x))))
    ).reset_index()
    
    return df
```

### **1050. Actors and Directors Who Cooperated At Least Three Times**

```python
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    groupedData = actor_director.groupby(by = ['actor_id', 'director_id'])['timestamp'].count().reset_index(name = 'cnt')
    return groupedData[groupedData['cnt'] >= 3][['actor_id', 'director_id']]
```

### **1378. Replace Employee ID With the Unique Identifier**

```python
def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    id_map = dict(zip(employee_uni['id'], employee_uni['unique_id']))
    employees['id'] = employees['id'].map(id_map)
    return employees.rename(columns = {'id':'unique_id'})

```

**Alternative**

```python
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merged_df = employees.merge(employee_uni, on='id', how='left')
    merged_df.drop(columns=['id'], inplace=True)
    merged_df.rename(columns={'unique_id': 'id'}, inplace=True)
    return merged_df

```

### **1693. Daily Leads and Partners**

```python
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    distinct_lead_partner_df = daily_sales.groupby(by = ["date_id", "make_name"]).agg(
        unique_leads = ('lead_id', 'nunique'),
        unique_partners = ('partner_id', 'nunique')
    ).reset_index()
    
    return distinct_lead_partner_df
```

### **570. Managers with at Least 5 Direct Reports**

```python
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    direct_reports_cnt_df = employee.groupby(by = 'managerId')['id'].count().reset_index(name = 'cnt')
    five_direct_reports = direct_reports_cnt_df[direct_reports_cnt_df['cnt'] >= 5]
    return employee[employee['id'].isin(five_direct_reports['managerId'])][['name']]
```

### 607. Sales Person

```python
import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    com_order_df = orders.merge(company, left_on = 'com_id', right_on = 'com_id', how = 'inner')
    com_order_df = com_order_df[com_order_df['name'] == 'RED']
    answerDF = sales_person[~sales_person['sales_id'].isin(com_order_df['sales_id'])][['name']]
    return answerDF
```

### Students and Examinations

```python
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # cross joining student and subject
    leftDF = pd.merge(students, subjects, how = 'cross').sort_values(by = ['student_id', 'subject_name'])

    # preprocessing examination table
    rightDF = examinations.groupby(by = ['student_id', 'subject_name'])\
        .agg(attended_exams = ('subject_name', 'count')).reset_index()

    # finally joining leftDf and rightDF and filling null as 0
    return pd.merge(leftDF, rightDF, how = 'left', on = ['student_id', 'subject_name']) \
        .fillna({'attended_exams': 0})[['student_id', 'student_name', 'subject_name', 'attended_exams']]
```