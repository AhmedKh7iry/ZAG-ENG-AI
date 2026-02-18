
import random

class KNNModel:
    def __init__(self, k=3):
        self.k = k
        self.X_train = []
        self.y_train = []

    def train(self, X, y):
        """Stores training data (Lazy Learning)."""
        self.X_train = X
        self.y_train = y
        print(f"[KNN] Model trained with K={self.k} on {len(X)} samples.")

    def predict(self, X):
        """Simulates class prediction."""
        print(f"[KNN] Classifying {len(X)} inputs...")
        # In a real KNN, we would calculate distances here.
        # For this demo, we return random classes (0 or 1).
        return [random.choice([0, 1]) for _ in X]