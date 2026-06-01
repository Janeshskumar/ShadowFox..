# ShadowFox Intermediate Task - Sentiment Analysis of X Data Using VADER

## Overview
This project performs sentiment analysis on social media data (X/Twitter posts) using the **VADER (Valence Aware Dictionary and sEntiment Reasoner)** library. The script cleans the raw text data, calculates sentiment polarity scores, categorizes the posts into Positive, Negative, or Neutral sentiments, and visualizes the results.

## Features
- **Data Loading & Preprocessing:** Handles missing values and loads data from CSV.
- **Text Cleaning:** Removes URLs, mentions, hashtags, special characters, and numbers, converting text to lowercase.
- **Sentiment Analysis:** Utilizes VADER to assign sentiment scores and classify text into Positive, Negative, or Neutral.
- **Data Visualization:** Generates Bar and Pie charts to display the distribution of sentiments using Seaborn and Matplotlib.
- **Data Export:** Saves the processed text and sentiment labels to a new CSV file.

## Prerequisites
Make sure you have Python installed. You will need the following libraries:
- `pandas`
- `matplotlib`
- `seaborn`
- `vaderSentiment`

You can install the required libraries using pip:
```bash
pip install pandas matplotlib seaborn vaderSentiment
```

## Dataset
The project expects an input file named `X_data.csv` in the same directory as the script. The dataset must contain a column named `clean_text` which holds the text data to be analyzed.

## Usage
1. Ensure that `X_data.csv` is placed in the project directory.
2. Run the script:
   ```bash
   python tast2.py
   ```
3. The script will output dataset information, sentiment counts, and sample results to the console.
4. Two charts will be displayed:
   - A Bar Chart showing the count of each sentiment.
   - A Pie Chart showing the percentage distribution.
5. The final results will be saved automatically as `sentiment_analysis_results.csv` in the same directory.

## Output Files
- `sentiment_analysis_results.csv`: Contains the original data along with the new columns: `Processed_Text` (the cleaned text) and `Sentiment` (Positive, Negative, or Neutral).
