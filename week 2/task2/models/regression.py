class LinearRegressionModel:
    def __init__(self):
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        """Simulates training a linear regression model."""
        print(f"[Linear Regression] Fitting model on {len(X)} data points...")
        # In a real model, we would calculate weights here.
        # For this demo, we set dummy weights.
        self.weights = 0.5
        self.bias = 2.0

    def predict(self, X):
        """Returns predictions based on a simple linear formula."""
        print(f"[Linear Regression] Predicting for {len(X)} inputs...")
        # Simple formula: y = mx + b
        return [(x * self.weights) + self.bias for x in X]