# 🧠 SQL vs pandas – Reference Guide

## 1. **Reading Input (DataFrames)**

- **SQL**: Data comes from pre-defined tables
- **pandas**:
    
    ```python
    import pandas as pd
    
    # From dictionary (e.g., in LeetCode problems)
    df = pd.DataFrame(data)
    
    # From CSV
    df = pd.read_csv('file.csv')
    
    ```
    

---

## 2. **SELECT Columns**

- **SQL**:
    
    ```sql
    SELECT column1, column2 FROM table;
    
    ```
    
- **pandas**:
    
    ```python
    df[['column1', 'column2']]
    
    ```
    

---

## 3. **Filtering Rows (WHERE)**

- **SQL**:
    
    ```sql
    SELECT * FROM table WHERE condition;
    
    ```
    
- **pandas**:
    
    ```python
    df[df['column'] == value]
    
    # Multiple conditions
    df[(df['col1'] > 5) & (df['col2'] != 'A')]
    
    ```
    

---

## 4. **Sorting (ORDER BY)**

- **SQL**:
    
    ```sql
    SELECT * FROM table ORDER BY column DESC;
    
    ```
    
- **pandas**:
    
    ```python
    df.sort_values(by='column', ascending=False)
    
    ```
    

---

## 5. **Aggregations (GROUP BY)**

- **SQL**:
    
    ```sql
    SELECT col, COUNT(*) FROM table GROUP BY col;
    
    ```
    
- **pandas**:
    
    ```python
    df.groupby('col').size().reset_index(name='count')
    
    # Aggregating with functions
    df.groupby('col').agg({'salary': 'sum', 'age': 'mean'})
    
    ```
    

---

## 6. **Renaming Columns (AS)**

- **SQL**:
    
    ```sql
    SELECT column AS new_name FROM table;
    
    ```
    
- **pandas**:
    
    ```python
    df.rename(columns={'old_name': 'new_name'})
    
    ```
    

---

## 7. **Joins**

- **SQL**:
    
    ```sql
    SELECT * FROM A
    JOIN B ON A.key = B.key;
    
    ```
    
- **pandas**:
    
    ```python
    pd.merge(df1, df2, on='key', how='inner')   # INNER JOIN
    pd.merge(df1, df2, on='key', how='left')    # LEFT JOIN
    pd.merge(df1, df2, on='key', how='right')   # RIGHT JOIN
    pd.merge(df1, df2, on='key', how='outer')   # FULL OUTER JOIN
    
    ```
    

---

## 8. **DISTINCT**

- **SQL**:
    
    ```sql
    SELECT DISTINCT column FROM table;
    
    ```
    
- **pandas**:
    
    ```python
    df['column'].drop_duplicates()
    # Or for multiple columns
    df.drop_duplicates(subset=['col1', 'col2'])
    
    ```
    

---

## 9. **Limiting Rows (TOP / LIMIT)**

- **SQL**:
    
    ```sql
    SELECT TOP 10 * FROM table;
    SELECT * FROM table LIMIT 10;
    
    ```
    
- **pandas**:
    
    ```python
    df.head(10)            # Top 10 rows
    df.tail(5)             # Last 5 rows
    df.iloc[5:10]          # Offset + limit (like LIMIT 5 OFFSET 5)
    
    ```
    

---

## 10. **Null Handling**

- **SQL**:
    
    ```sql
    WHERE column IS NULL
    WHERE column IS NOT NULL
    
    ```
    
- **pandas**:
    
    ```python
    df[df['column'].isnull()]       # IS NULL
    df[df['column'].notnull()]      # IS NOT NULL
    
    # Replace NULL with default
    df['column'].fillna(0)
    
    ```
    

---

## 11. **Aggregation Functions: MAX, MIN, COUNT, SUM, AVG**

| Operation | SQL Example | pandas Equivalent |
| --- | --- | --- |
| **MAX** | `SELECT MAX(salary) FROM emp;` | `df['salary'].max()` |
| **MIN** | `SELECT MIN(salary) FROM emp;` | `df['salary'].min()` |
| **COUNT** | `SELECT COUNT(*) FROM emp;` | `len(df)` or `df.count()` |
| **SUM** | `SELECT SUM(salary) FROM emp;` | `df['salary'].sum()` |
| **AVG** | `SELECT AVG(salary) FROM emp;` | `df['salary'].mean()` |

> For grouped aggregates:
> 

```python
df.groupby('department')['salary'].agg(['max', 'min', 'mean', 'sum', 'count']).reset_index()

```

---

## 12. **CASE WHEN (Conditional Logic)**

- **SQL**:
    
    ```sql
    SELECT
      name,
      CASE
        WHEN salary > 50000 THEN 'High'
        WHEN salary >= 20000 THEN 'Medium'
        ELSE 'Low'
      END AS salary_category
    FROM emp;
    
    ```
    
- **pandas**:
    
    ```python
    df['salary_category'] = pd.cut(
        df['salary'],
        bins=[-float('inf'), 20000, 50000, float('inf')],
        labels=['Low', 'Medium', 'High']
    )
    
    # OR using np.select
    import numpy as np
    conditions = [
        df['salary'] > 50000,
        (df['salary'] >= 20000) & (df['salary'] <= 50000),
        df['salary'] < 20000
    ]
    choices = ['High', 'Medium', 'Low']
    df['salary_category'] = np.select(conditions, choices)
    
    ```
    

---

## 13. **UNION / UNION ALL**

- **SQL**:
    
    ```sql
    SELECT 'abc' AS col, salary1 AS salary FROM xyz
    UNION
    SELECT 'pqe' AS col, salary2 AS salary FROM xyz;
    
    ```
    
- **pandas**:
    
    ```python
    df1 = xyz[['salary1']].rename(columns={'salary1': 'salary'})
    df1['col'] = 'abc'
    
    df2 = xyz[['salary2']].rename(columns={'salary2': 'salary'})
    df2['col'] = 'pqe'
    
    result = pd.concat([df1, df2], ignore_index=True).drop_duplicates()  # UNION
    # For UNION ALL, remove `.drop_duplicates()`
    
    ```
    

---

## 14. **RANK, DENSE_RANK, ROW_NUMBER (Window Functions)**

- **SQL**:
    
    ```sql
    SELECT *,
           RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS rank
    FROM emp;
    
    ```
    
- **pandas**:
    
    ```python
    df['rank'] = df.groupby('dept')['salary'].rank(method='min', ascending=False)       # RANK
    df['dense_rank'] = df.groupby('dept')['salary'].rank(method='dense', ascending=False) # DENSE_RANK
    df['row_number'] = df.groupby('dept').cumcount() + 1                                 # ROW_NUMBER
    
    ```
    

---

## 15. **IN / NOT IN**

- **SQL**:
    
    ```sql
    SELECT * FROM emp WHERE dept_id IN (1, 2, 3);
    
    ```
    
- **pandas**:
    
    ```python
    df[df['dept_id'].isin([1, 2, 3])]
    
    # NOT IN
    df[~df['dept_id'].isin([1, 2, 3])]
    
    ```
    

---

## 16. **EXISTS / NOT EXISTS**

- **SQL**:
    
    ```sql
    SELECT * FROM A WHERE EXISTS (SELECT 1 FROM B WHERE A.id = B.id);
    
    ```
    
- **pandas**:
    
    ```python
    df = A[A['id'].isin(B['id'])]            # EXISTS
    df = A[~A['id'].isin(B['id'])]           # NOT EXISTS
    
    ```
    

---

## 17. **Subqueries (Derived Tables)**

- **SQL**:
    
    ```sql
    SELECT name FROM (
        SELECT name, salary FROM emp WHERE dept = 'IT'
    ) AS sub WHERE salary > 50000;
    
    ```
    
- **pandas**:
    
    ```python
    sub = df[df['dept'] == 'IT'][['name', 'salary']]
    result = sub[sub['salary'] > 50000]
    
    ```
    

---

## 18. **UPDATE / SET**

- **SQL**:
    
    ```sql
    UPDATE emp SET bonus = 1000 WHERE dept = 'HR';
    
    ```
    
- **pandas**:
    
    ```python
    df.loc[df['dept'] == 'HR', 'bonus'] = 1000
    
    ```
    

---

## 19. **DELETE**

- **SQL**:
    
    ```sql
    DELETE FROM emp WHERE salary < 10000;
    
    ```
    
- **pandas**:
    
    ```python
    df = df[df['salary'] >= 10000]    # Reassign filtered DataFrame
    
    ```
    

---

## 20. **Insert New Row / Append**

- **SQL**:
    
    ```sql
    INSERT INTO emp (name, salary) VALUES ('John', 50000);
    
    ```
    
- **pandas**:
    
    ```python
    new_row = pd.DataFrame([{'name': 'John', 'salary': 50000}])
    df = pd.concat([df, new_row], ignore_index=True)
    
    ```
    

---

### 21. Multiple aggregations on the same group with **String Aggregation in Pandas (like SQL’s STRING_AGG)**

- SQL:
    
    ```sql
    select sell_date,
            count(distinct product) as num_sold,
            string_agg(distinct product, ',' order by product) as products
    from activities
    group by sell_date
    order by sell_date
    ```
    
- pandas:
    
    ```python
    import pandas as pd
    
    def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
        df = activities.groupby('sell_date').agg(
            num_sold=('product', pd.Series.nunique),
            products=('product', lambda x: ','.join(sorted(set(x))))
        ).reset_index()
        
        return df
    ```