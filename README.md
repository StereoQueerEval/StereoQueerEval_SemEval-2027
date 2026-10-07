## 🚨🚨🚨 Data access 🚨🚨🚨

Access to the data requires filling in the [**Data Usage Agreement**](https://forms.gle/Pnvv96zXbnaA3Tcp8) and accepting all the terms and conditions. Once the agreement has been processed, you will be added to the task's **Google Group**, where the password to extract the archives is communicated.

The data files are distributed as a **password-protected RAR archive**. We recommend extracting it with [WinRAR](https://www.win-rar.com/) on Windows; on macOS you can use the command-line version of WinRAR or a free tool that supports encrypted RAR archives, such as [The Unarchiver](https://theunarchiver.com/) or [Keka](https://www.keka.io/); on Linux, `unrar x archive.rar`.




## Files

Training data for **StereoQueerEval** (SemEval 2027): detection of queer stereotypes and hate speech in YouTube comments, in **English, Italian and Dutch**. For Persian, we release 100 textual triplets as part of development set. The rest of the Persian data will be released only as part of the test set.

Each instance is a YouTube comment posted under a news video about LGBTQIA+ topics, annotated for the three subtasks. Comments are provided together with the title and description of the video they respond to, since the target of a comment is often only interpretable in context.

| File | Textual Triplets |
|---|---|
| `StereoQueerEval_EN_training.tsv` | 2,989 |
| `StereoQueerEval_IT_training.tsv` | 2,400 |
| `StereoQueerEval_NL_training.tsv` | 2,238 |
| `StereoQueerEval_FA_development.tsv` | 100 |

The test sets (English, Italian, Dutch _with the addition of Persian_) will be released according to the task schedule in January 2027.


## Format

UTF-8, tab-separated, one header line, fields quoted where needed.
⚠️ Titles, descriptions and comments may contain **newlines ("\n") inside quoted fields**: read the files with a proper TSV parser (e.g. `pandas.read_csv(..., sep="\t")`, Python `csv`, Hugging Face `datasets`), not with line-based tools.

## Columns

| Column | Description |
|---|---|
| `StereoQueerEval_id` | Unique instance ID, e.g. `training_EN_0001`. |
| `yt_title` | Title of the YouTube video. |
| `yt_description` | Description of the YouTube video. |
| `yt_comment` | The comment to be classified. |
| `stereotype` | Does the comment convey a stereotype about queer people? `yes` / `no`. |
| `hate_speech` | Is the comment hateful, and how? `no` / `yes_implicit` / `yes_explicit`. |
| `target` | Target of the hate: `none` if `hate_speech` is `no`; otherwise scope (`group` or `individual`) + one or more target identities, e.g. `group_lgbtqia+`, `individual_t,nb`. |

Target identities: `l`, `g`, `b`, `t`, `q`, `i`, `a`, `nb` (non-binary), `lgbtqia+` (the community as a whole), always listed in this order. `target` is present **if and only if** the comment is hateful, if the comment is not hateful then `target` must default to `none`.

## Content warning

The data contains offensive, hateful and discriminatory language towards LGBTQIA+ people, reproduced unaltered for research purposes.

## Terms of Use

By accessing or using this dataset, you agree to the following terms.

###### 1. Permitted Use
This dataset may be used only for academic, non-commercial research, and solely for participation in the StereoQueerEval shared task or directly related research.

###### 2. No Redistribution
You may not share, publish, or redistribute the raw dataset, or any substantial portion of it, to third parties in any form. This includes, but is not limited to, public repositories, websites, and supplementary materials.

###### 3. No Commercial Use
You may not use the dataset, or any derivative of it, for commercial purposes of any kind.

###### 4. Retention
You may keep the dataset after the shared task concludes for ongoing non-commercial research, provided you continue to comply with all other terms listed here.

###### 5. Ethical Use
This dataset contains content related to LGBTQ+ communities and stereotypes. Please handle it with care and respect. You may not use the dataset, any outputs derived from it, or any models trained on it in ways that could target, harm, discriminate against, or demean LGBTQ+ individuals or communities.
