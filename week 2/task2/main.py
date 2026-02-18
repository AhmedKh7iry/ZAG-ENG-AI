from models.regression import LinearRegressionModel
from models.classification import KNNModel
from utils.metrics import accuracy_score

def main():
    # --- Test Linear Regression ---
    print("--- Testing Regression ---")
    reg_model = LinearRegressionModel()
    
    # Dummy data (Input X, Target y)
    X_reg = [1, 2, 3, 4, 5]
    y_reg = [2, 4, 6, 8, 10]
    
    reg_model.fit(X_reg, y_reg)
    preds_reg = reg_model.predict([6, 7])
    print(f"Regression Predictions: {preds_reg}\n")


    # --- Test Classification ---
    print("--- Testing Classification ---")
    clf_model = KNNModel(k=3)
    
    # Dummy data (Input features, Class labels)
    X_clf = [[1.2], [1.4], [5.1], [5.2]]
    y_clf = [0, 0, 1, 1]
    
    clf_model.train(X_clf, y_clf)
    
    # Test data
    y_test_true = [0, 1]
    y_test_pred = clf_model.predict([[1.3], [5.0]])
    
    print(f"Predicted Classes: {y_test_pred}")
    
    # --- Test Metrics ---
    acc = accuracy_score(y_test_true, y_test_pred)
    print(f"Model Accuracy: {acc:.2f}")

if __name__ == "__main__":
    main()