
Objective: Toxic comment classifier
Dependencies: Python 3.6, numpy, pandas, keras, sklearn

Main goal: create a classifier for one protected class
Sub goal: Evaluate bias of model on another protected class

Data resources
Step 0: Load data
  - https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data
  - Example
    - Comment: Continue to stand strong LGBT community. Yes, indeed, you'll overcome and you have.
    - Toxicity Labels: All 0.0
    - Identity Mention Labels: homosexual_gay_or_lesbian: 0.8, bisexual: 0.6, transgender: 0.3 (all others 0.0)
    - To download all the data: https://www.kaggle.com/c/12500/download-all

Step 1: Convert to pandas DF
data = pd.read_csv('./train.csv')
You can start with the training set as the full dataset my take a while to load if you are using Colab

Step 2: Explore columns and content of columns

Step 3: DATA PROCESSING STEPS
  - Restrict the data to having a specific identify mention label (or multiple)
  - Investigate data imbalance
  - Create a balanced dataset (alternatively could weight differently in the future)
  - Remove stop words
  - Add tokenizing
  - Optional: Add other preprocessing steps

Step 4: FEATURE GEN+EXPLORATION STEPS
  - TF-IDF (restrict words to a set number vocabulary, probably ~2000)
  - Explore these features
    - PCA and/or UMAP  probably
    - Could also use tsne or umap instead

Step 5: MODELING STEPS
  - Train test split the data
  - Create x_train, x_test, y_train, y_test
    - These have to have the toxic classification labels concatenated to them
  - Modeling (train it)
    - Logistic regression is easiest
    - Optional: do other models
  - Evaluate the model on train and test
    - ~60% accuracy is decent if
      - Restraining to single protected class
      - Balancing the data via downsampling
      - No stop words
      - No tokenizing


Solutions:
- [A+](https://colab.research.google.com/drive/1UnOC6mIfIHpq5Sc7dTYAVvuOhdgqyuZn#scrollTo=eOPtjvP2syVm)
- [A](https://colab.research.google.com/drive/1hVV966ioupI5_f__VEHk5RotPlVGIrhd)
- [B+](https://colab.research.google.com/drive/1leJ4qLMr4yBUlG4CkX1GixQAhMjSQMnS)
- [B](https://colab.research.google.com/drive/1FOpzu4X9CChrfXcFeypGp5oS0ymi1WXi)
