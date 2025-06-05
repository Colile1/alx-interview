
### **Question 1**

**1.1 Classification vs Regression**

* **Classification**: Predicts categories.
  *Example*: Spam or Not Spam.
* **Regression**: Predicts continuous values.
  *Example*: Predict house price.

**1.2 Median vs Mean Imputation**

* Prefer **median** when data has **outliers**.
  *Example*: Income data—median is not skewed by extreme values.

**1.3 Five Python ML Libraries**

* scikit-learn
* TensorFlow
* Keras
* PyTorch
* XGBoost

**1.4 Bias-Variance Trade-off**

* **High bias**: Model too simple → underfits.
* **High variance**: Model too complex → overfits.
  *Example*: A polynomial model fitting noise in training data.

---

### **Question 2**

**2.1 Unlabeled Dataset Use in Supervised Learning**

* Use **semi-supervised learning** or **label via domain experts**. Unlabeled data alone isn't suitable for supervised learning.

**2.2 Standardize `Age` in DataFrame `df`**

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df['Age'] = scaler.fit_transform(df[['Age']])
```

**2.3 Overfitting vs Underfitting + Mitigation**

* **Overfitting**: High train accuracy, low test accuracy.
  *Mitigations*:

  * Cross-validation
  * Pruning (for trees)
  * Regularization (L1/L2)
  * Reduce model complexity
* **Underfitting**: Poor performance on both train/test.
  *Mitigations*:

  * Use more complex model
  * Add features
  * Increase training time
  * Reduce regularization

**2.4 Performance Metrics Calculations**

|                 | Predicted Positive | Predicted Negative |
| --------------- | ------------------ | ------------------ |
| Actual Positive | 40                 | 10                 |
| Actual Negative | 20                 | 30                 |

* **Accuracy** = (TP + TN) / Total = (40+30)/100 = 0.70
* **Precision** = TP / (TP + FP) = 40 / (40+20) = 0.667
* **Recall** = TP / (TP + FN) = 40 / (40+10) = 0.80
* **F1-score** = 2 \* (P \* R) / (P + R) = 2\*(0.667\*0.8)/(0.667+0.8) ≈ 0.727
* **Specificity** = TN / (TN + FP) = 30 / (30+20) = 0.60

---

### **Question 3**

**(a) Load Data into DataFrame**

```python
data = {
 'square_footage': [800,1200,1500,1800,2500,900,1100,2200],
 'num_bedrooms': [2,3,4,3,4,2,5,4],
 'age': [10,5,10,20,7,25,15,17],
 'location': ['Urban','Suburban','Urban','Urban','Rural','Urban','Suburban','Rural'],
 'price': [350000,245000,400000,300000,200000,250000,320000,280000]
}
df = pd.DataFrame(data)
```

**(b) Separate Features and Target**

```python
X = df.drop('price', axis=1)
y = df['price']
```

**(c) One-Hot Encode Location**

```python
X = pd.get_dummies(X, columns=['location'], drop_first=True)
```

**(d) Train-Test Split**

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

**(e) Train Model and Predict**

```python
model = LinearRegression()
model.fit(X_train, y_train)

new_data = pd.DataFrame([[2000, 5, 5, 1, 0]], columns=['square_footage','num_bedrooms','age','location_Urban','location_Suburban'])
prediction = model.predict(new_data)
```

---

### **Question 4**

**4.1 K-Means Pseudo Code**

```
1. Initialize k cluster centers randomly
2. Repeat until convergence:
   a. Assign each point to nearest center
   b. Recalculate centers as mean of assigned points
```

**4.2 Why Accuracy is Not Always Ideal**

* In imbalanced datasets, it can be misleading.
  *Example*: 95% healthy, 5% sick — predicting all healthy gives 95% accuracy but misses all sick cases.

**4.3 Train Decision Tree and Logistic Regression**

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

# Decision Tree
tree_model = DecisionTreeClassifier()
tree_model.fit(X_train, y_train)
tree_preds = tree_model.predict(X_test)

# Logistic Regression
log_model = LogisticRegression()
log_model.fit(X_train, y_train)
log_preds = log_model.predict(X_test)
```
