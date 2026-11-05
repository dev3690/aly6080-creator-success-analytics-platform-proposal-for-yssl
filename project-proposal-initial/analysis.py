# Python implementation using scikit-learn
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Prepare data
X = creator_features[['experience_years', 'portfolio_diversity', 
                     'collaboration_score', 'education_level']]
y = creator_features['success']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Build decision tree
dt_model = DecisionTreeClassifier(max_depth=5, min_samples_split=10, random_state=42)
dt_model.fit(X_train, y_train)

# Evaluate model
predictions = dt_model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
