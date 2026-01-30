# -------------------------------
# STEP 1: Import Required Libraries
# -------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report


# -------------------------------
# STEP 2: Load Dataset
# -------------------------------
df = pd.read_csv("student_performance_new.csv")


# -------------------------------
# STEP 3: Data Pre-Processing
# -------------------------------
df.columns = (
    df.columns
      .str.strip()
      .str.replace(" ", "_")
      .str.replace(",", "")
      .str.lower()
)

# -------------------------------
# STEP 4: Feature Selection
# -------------------------------
X = df[['test_result', 'quiz_result', 'assignment_result']]
y = df['result']


# -------------------------------
# STEP 5: Train-Test Split
# -------------------------------
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=20
)


# -------------------------------
# STEP 6: Train Decision Tree Model
# -------------------------------
clf = DecisionTreeClassifier(
    criterion='gini',
    max_depth=3,
    random_state=20
)

clf.fit(x_train, y_train)


# -------------------------------
# STEP 7: Model Evaluation
# -------------------------------
y_pred = clf.predict(x_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))


# -------------------------------
# STEP 8: Confusion Matrix
# -------------------------------
cm = confusion_matrix(y_test, y_pred)
classnames = ['Fail', 'Pass']

sn.heatmap(
    cm,
    annot=True,
    fmt='g',
    cmap='Greens',
    xticklabels=classnames,
    yticklabels=classnames
)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


# -------------------------------
# STEP 9: Plot Decision Tree
# -------------------------------
plt.figure(figsize=(14, 8))
plot_tree(
    clf,
    feature_names=X.columns,
    class_names=['Fail', 'Pass'],
    filled=True
)
plt.title("Decision Tree for Student Performance")
plt.show()


# -------------------------------
# STEP 10: USER INPUT PREDICTION
# -------------------------------
print("\n--- Enter Student Details for Prediction ---")

test_result = int(input("Enter Test Result (1 = Pass, 0 = Fail): "))
quiz_result = int(input("Enter Quiz Result (1 = Pass, 0 = Fail): "))
assignment_result = int(input("Enter Assignment Result (1 = Pass, 0 = Fail): "))

# Create DataFrame for user input
user_input = pd.DataFrame(
    [[test_result, quiz_result, assignment_result]],
    columns=['test_result', 'quiz_result', 'assignment_result']
)

# Predict
user_prediction = clf.predict(user_input)

# Display result
if user_prediction[0] == 1:
    print("\n✅ Predicted Result: PASS")
else:
    print("\n❌ Predicted Result: FAIL")


# -------------------------------
# STEP 11: Feature Importance
# -------------------------------
feature_importance = pd.Series(
    clf.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print("\nFeature Importance:\n", feature_importance)

feature_importance.plot(kind='bar', color='green')
plt.title("Important Features Affecting Student Performance")
plt.ylabel("Importance Score")
plt.show()
