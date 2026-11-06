
from sklearn.metrics import f1_score


STEREOTYPE_CLASSES = ["no", "yes"]


def evaluate_task_a_macro_f1(y_true, y_pred):
    """
    Evaluate Task A predictions using the macro-averaged F1-score.

    Computes the F1-score independently for each class and returns
    their unweighted average, giving both classes equal importance
    regardless of their frequency in the dataset.

    Args:
        y_true (list[str]): Ground-truth class labels.
            Expected labels are 'no' and 'yes'.
        y_pred (list[str]): Predicted class labels.
            Must have the same length as y_true.

    Returns:
        float: Macro F1-score between 0.0 and 1.0.
    """
    return f1_score(
        y_true,
        y_pred,
        labels=STEREOTYPE_CLASSES,
        average="macro",
        zero_division=0,
    )


# Example usage
y_true = ["yes", "no", "yes", "no", "yes", "no"]
y_pred = ["yes", "no", "no", "no", "yes", "yes"]

macro_f1 = evaluate_task_a_macro_f1(y_true, y_pred)
print(f"Macro F1: {macro_f1:.4f}")

# Output
# Macro F1: 0.6667