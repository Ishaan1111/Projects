import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTENC
import numpy as np

# Load the training and test data
train_data = pd.read_csv(r'C:\Users\ishaa\Desktop\Project dataset\train.csv')
test_data = pd.read_csv(r'C:\Users\ishaa\Desktop\Project dataset\test.csv')

# Combine the data to ensure LabelEncoder sees all categories
combined_data = pd.concat([train_data, test_data], keys=['train', 'test'])

# Convert Dates to datetime and extract features
combined_data['Dates'] = pd.to_datetime(combined_data['Dates'], format='%Y-%m-%d %H:%M:%S')
combined_data['Year'] = combined_data['Dates'].dt.year
combined_data['Month'] = combined_data['Dates'].dt.month
combined_data['Day'] = combined_data['Dates'].dt.day
combined_data['Hour'] = combined_data['Dates'].dt.hour
combined_data['DayOfWeek'] = combined_data['Dates'].dt.dayofweek
combined_data['IsWeekend'] = combined_data['DayOfWeek'].apply(lambda x: 1 if x >= 5 else 0)  # New feature: Is weekend

# Encode categorical variables
label_encoder = LabelEncoder()
combined_data['Category'] = label_encoder.fit_transform(combined_data['Category'].astype(str))
combined_data['PdDistrict'] = label_encoder.fit_transform(combined_data['PdDistrict'].astype(str))
combined_data['Resolution'] = label_encoder.fit_transform(combined_data['Resolution'].astype(str))

# Separate the data back into train and test sets
train_data = combined_data.loc['train'].reset_index(drop=True)
test_data = combined_data.loc['test'].reset_index(drop=True)

# Define features and target
features = ['Year', 'Month', 'Day', 'Hour', 'DayOfWeek', 'IsWeekend', 'PdDistrict', 'X', 'Y']
X = train_data[features]
y = train_data['Category']

# Remove rows with NaN values
train_data.dropna(inplace=True)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Impute missing values with the mean
imputer = SimpleImputer(strategy='mean')
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

# Handle class imbalance using SMOTENC
categorical_features = [4, 5, 6]  # Indices of categorical features in `X`
smotenc = SMOTENC(categorical_features=categorical_features, random_state=42, k_neighbors=3)
X_train_res, y_train_res = smotenc.fit_resample(X_train, y_train)

# Initialize and train the Random Forest classifier
model = RandomForestClassifier(random_state=42)
params = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10]
}
grid_search = GridSearchCV(model, param_grid=params, cv=3, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train_res, y_train_res)

# Best model from grid search
best_model = grid_search.best_estimator_

# Make predictions
y_pred = best_model.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred, zero_division=1))
print(confusion_matrix(y_test, y_pred))

# Define features for test data
X_new = test_data[features]

# Impute missing values in the test data
X_new = imputer.transform(X_new)

# Predict categories
predictions = best_model.predict(X_new)

# Add predictions to test_data
test_data['PredictedCategory'] = label_encoder.inverse_transform(predictions)

# Optionally save the predictions
test_data.to_csv(r'C:\Users\ishaa\Desktop\Project dataset\predicted_test_data.csv', index=False)
    