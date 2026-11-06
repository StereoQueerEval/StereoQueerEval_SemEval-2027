
from sklearn.metrics import f1_score


HATE_CLASSES = ["no", "yes_explicit", "yes_implicit"]


def evaluate_task_b_macro_f1(y_true, y_pred):
    """
    Evaluate Task B predictions using the macro-averaged F1-score.

    Computes the F1-score independently for each of the three classes
    and returns their unweighted average, giving each class equal
    importance regardless of its frequency in the dataset.

    Args:
        y_true (list[str]): Ground-truth class labels.
            Expected labels are 'no', 'yes_explicit',
            and 'yes_implicit'.
        y_pred (list[str]): Predicted class labels.
            Must have the same length as y_true.

    Returns:
        float: Macro F1-score between 0.0 and 1.0.
    """
    return f1_score(
        y_true,
        y_pred,
        labels=HATE_CLASSES,
        average="macro",
        zero_division=0,
    )


# Example usage
y_true = ["no", "yes_explicit", "yes_implicit", "no"]
y_pred = ["no", "yes_explicit", "no", "no"]

macro_f1 = evaluate_task_b_macro_f1(y_true, y_pred)
print(f"Macro F1: {macro_f1:.4f}")

# Output
# Macro F1: 0.6000