import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def load_data():
    train_df = pd.read_csv('/content/train.csv')
    test_df = pd.read_csv('/content/test.csv')
    return train_df, test_df

def train_model(train_df):
    y = train_df["Survived"]
    features = ["Pclass", "Sex", "SibSp", "Parch"]
    X = pd.get_dummies(train_df[features])
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
    model.fit(X_train, y_train)

    # Evaluate the model
    evaluate_model(model,X_val,y_val)

    return model

def evaluate_model(model, X_val, y_val):
    y_pred = model.predict(X_val)
    accuracy = accuracy_score(y_val, y_pred)
    print(f"Validation Accuracy: {accuracy}")

def main():
    train_df, test_df = load_data()

    # Train the model
    model = train_model(train_df)

if __name__ == '__main__':
    main()
