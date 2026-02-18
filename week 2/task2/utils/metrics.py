def accuracy_score(y_true, y_pred):
    """Calculates the percentage of correct predictions."""
    if len(y_true) != len(y_pred):
        raise ValueError("Lists must have the same length")
    
    correct = sum(1 for true, pred in zip(y_true, y_pred) if true == pred)
    return correct / len(y_true)