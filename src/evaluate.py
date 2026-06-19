# a function that:
#   - takes in true labels and predicted labels/probabilities
#   - computes accuracy, F1 score, AUC-ROC, and confusion matrix
#   - returns a summary of all metrics

from typing import Dict, Any, Optional
import numpy as np
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, confusion_matrix

def calculate_metrics(y_true: np.ndarray, y_pred: np.ndarray, y_prob: Optional[np.ndarray] = None) -> Dict[str, Any]:
    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "f1_score": f1_score(y_true, y_pred, zero_division=0),
        "confusion_matrix": confusion_matrix(y_true, y_pred).tolist()
    }

    if y_prob is not None:
        try:
            metrics["roc_auc"] = roc_auc_score(y_true, y_prob)
        except ValueError:
            # Handles cases where y_true contains only one class in a small validation fold
            metrics["roc_auc"] = None

    return metrics

def print_evaluation_summary(metrics: Dict[str, Any], title: str = "Evaluation Summary") -> None:
    print(f"\n{'='*10} {title} {'='*10}")
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print(f"F1 Score: {metrics['f1_score']:.4f}")
    if "roc_auc" in metrics and metrics["roc_auc"] is not None:
        print(f"ROC AUC:  {metrics['roc_auc']:.4f}")
    else:
        print("ROC AUC:  N/A")
    
    cm = metrics["confusion_matrix"]
    print("\nConfusion Matrix:")
    print(f"   Pred Down/Flat   Pred Up")
    print(f"True Down/Flat   {cm[0][0]:<15} {cm[0][1]}")
    print(f"True Up          {cm[1][0]:<15} {cm[1][1]}")
    print(f"{'='*(len(title) + 22)}")

if __name__ == "__main__":
    # Test block to verify evaluate.py works as expected
    print("Testing evaluate.py...")
    
    # 1. Sample predictions: 0 = Down/Flat, 1 = Up
    y_true_sample = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])
    y_pred_sample = np.array([1, 0, 0, 1, 0, 1, 1, 0, 1, 0])
    y_prob_sample = np.array([0.9, 0.1, 0.4, 0.85, 0.2, 0.75, 0.6, 0.15, 0.95, 0.3])

    # 2. Calculate metrics
    sample_metrics = calculate_metrics(y_true_sample, y_pred_sample, y_prob_sample)
    
    # 3. Print the summary
    print_evaluation_summary(sample_metrics, "Sample Model Evaluation")
