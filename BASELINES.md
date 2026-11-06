# StereoQueerEval – Baselines

Scores are averaged macro-F1. For Subtask C, Final Weighted Score = 0.5 × Target Macro-F1 + 0.5 × Identity Macro-F1. Random baselines on FA are reported as mean ± std over 10-fold cross-validation; LLM baselines have no ± value.

## Subtask A – Stereotype detection

| System | EN | IT | NL | FA |
|---|---|---|---|---|
| Random (uniform) | 0.4911 | 0.4674 | 0.5027 | 0.4525 ± 0.0423 |
| Random (stratified) | 0.4791 | 0.4906 | 0.4983 | 0.4805 ± 0.0364 |
| Random (most frequent) | 0.3517 | 0.4193 | 0.3803 | 0.4350 ± 0.0091 |
| Qwen2.5-0.5B-Instruct | 0.4633 | 0.4355 | 0.4111 | 0.3825 |
| Qwen2.5-7B-Instruct | 0.6833 | 0.6353 | 0.6254 | 0.5584 |

## Subtask B – Hate detection

| System | EN | IT | NL | FA |
|---|---|---|---|---|
| Random (uniform) | 0.3417 | 0.3251 | 0.2941 | 0.3076 ± 0.0338 |
| Random (stratified) | 0.3156 | 0.3405 | 0.3257 | 0.3457 ± 0.0271 |
| Random (most frequent) | 0.2042 | 0.2190 | 0.2118 | 0.2296 ± 0.0105 |
| Qwen2.5-0.5B-Instruct | 0.1601 | 0.1752 | 0.1918 | 0.1650 |
| Qwen2.5-7B-Instruct | 0.4418 | 0.5033 | 0.4515 | 0.4219 |

## Subtask C – Target detection

### Target Macro-F1

| System | EN | IT | NL | FA |
|---|---|---|---|---|
| Random (uniform) | 0.4223 | 0.4912 | 0.4983 | 0.4157 ± 0.0470 |
| Random (stratified) | 0.5224 | 0.4960 | 0.5019 | 0.4930 ± 0.0444 |
| Random (most frequent) | 0.4407 | 0.4008 | 0.4150 | 0.4526 ± 0.0131 |
| Qwen2.5-0.5B-Instruct | 0.1871 | 0.2412 | 0.2417 | 0.5373 |
| Qwen2.5-7B-Instruct | 0.7123 | 0.7456 | 0.7126 | 0.4994 |

### Identity Macro-F1

| System | EN | IT | NL | FA |
|---|---|---|---|---|
| Random (uniform) | 0.1573 | 0.1612 | 0.1775 | 0.2583 ± 0.0274 |
| Random (stratified) | 0.1883 | 0.1835 | 0.2047 | 0.2807 ± 0.0219 |
| Random (most frequent) | 0.1863 | 0.1915 | 0.1984 | 0.2702 ± 0.0188 |
| Qwen2.5-0.5B-Instruct | 0.0735 | 0.0784 | 0.0442 | 0.0812 |
| Qwen2.5-7B-Instruct | 0.1835 | 0.1605 | 0.1680 | 0.1899 |

### Final Weighted Score

| System | EN | IT | NL | FA |
|---|---|---|---|---|
| Random (uniform) | 0.2898 | 0.3262 | 0.3379 | 0.3370 ± 0.0313 |
| Random (stratified) | 0.3553 | 0.3397 | 0.3533 | 0.3869 ± 0.0188 |
| Random (most frequent) | 0.3135 | 0.2961 | 0.3067 | 0.3614 ± 0.0109 |
| Qwen2.5-0.5B-Instruct | 0.1303 | 0.1598 | 0.1430 | 0.3093 |
| Qwen2.5-7B-Instruct | 0.4479 | 0.4531 | 0.4403 | 0.3446 |
