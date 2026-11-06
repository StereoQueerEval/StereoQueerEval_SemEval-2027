
from sklearn.metrics import f1_score


TARGET_CLASSES = ["group", "individual"]
IDENTITY_CLASSES = [
    "l", "g", "b", "t", "q", "i", "a", "nb", "lgbtqia+"
]


def parse_label(combined_label):
    """
    Split a combined label into its target class and identity labels.

    Example:
        "group_l,g" -> ("group", ["l", "g"])
    """
    target_class, identity_string = (
        combined_label.strip().lower().split("_", maxsplit=1)
    )
    identity_labels = [
        identity.strip() for identity in identity_string.split(",")
    ]
    return target_class, identity_labels


def calculate_task_c_metrics(reference_labels, predicted_labels):
    """
    Evaluate Task C predictions using the Target–Identity Macro-F1 score.

    The final score is the average of two components, each contributing 50%:
        - Macro-averaged F1 over the two target type classes
            ( group / individual )
        - Macro-averaged F1 over the 9 identity labels
            ( l / g / b / t / q / i / a / nb / lgbtqia+ ),
            represented as binary vectors.
     Final scores:
        target_identity_macro_f1 = 0.5 * target_macro_f1 +
                                   0.5 * identity_macro_f1

    Args:
        reference_labels (list[str]): Ground-truth labels.
        predicted_labels (list[str]): Model-predicted labels.
        Must have the same length as reference_labels.

    Returns:
        dict[str, float]: Target macro F1, identity macro F1,
        and Target–Identity Macro-F1 score.
    """

    # Parse ground-truth and predicted labels.
    parsed_reference = [
        parse_label(label) for label in reference_labels
    ]
    parsed_predictions = [
        parse_label(label) for label in predicted_labels
    ]

    # 1. Target macro F1
    reference_target_classes = [
        target_class for target_class, _ in parsed_reference
    ]
    predicted_target_classes = [
        target_class for target_class, _ in parsed_predictions
    ]

    target_macro_f1 = f1_score(
        reference_target_classes,
        predicted_target_classes,
        labels=TARGET_CLASSES,
        average="macro",
        zero_division=0,
    )

    # Convert identity labels into binary indicator matrices.
    # Each column represents one identity class.
    def create_identity_matrix(parsed_labels):
        return [
            [
                int(identity in identity_labels)
                for identity in IDENTITY_CLASSES
            ]
            for _, identity_labels in parsed_labels
        ]

    reference_identity_matrix = create_identity_matrix(
        parsed_reference
    )
    predicted_identity_matrix = create_identity_matrix(
        parsed_predictions
    )

    # 2. Identity macro F1
    identity_macro_f1 = f1_score(
        reference_identity_matrix,
        predicted_identity_matrix,
        average="macro",
        zero_division=0,
    )

    # 6. Final weighted scores
    final_weighted_score = (
          0.5 * target_macro_f1
        + 0.5 * identity_macro_f1
    )

    return {
        "target_macro_f1": float(target_macro_f1),
        "identity_macro_f1": float(identity_macro_f1),
        "target_identity_macro_f1": float(final_weighted_score),
    }


# Example usage
reference_labels = [
    "group_l,g",
    "individual_b",
    "group_l",
    "individual_t,q",
]

predicted_labels = [
    "group_l",
    "individual_b",
    "group_g",
    "individual_t",
]

task_c_metrics = calculate_task_c_metrics(
    reference_labels,
    predicted_labels,
)

for metric_name, metric_value in task_c_metrics.items():
    print(f"{metric_name.replace('_', ' ').title():<30} {metric_value:>8.4f}")

# Output
# Target Macro F1                  1.0000
# Identity Macro F1                0.2963
# Target Identity Macro F1         0.6481