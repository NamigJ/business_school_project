# MovieMatch 250 — Personality-Based Film Recommendation App

## About the Project

MovieMatch 250 is a Python-based quiz app that recommends films based on the user’s personality.
It uses a database of the IMDb Top 250 movies and matches user preferences by analyzing their answers to 10 creative, non-technical questions.

The app is entirely terminal-based and lightweight, built with Python and pandas.

## Key Features

Data Analysis:

* Reads and cleans raw Excel data with pandas
* Filters and scores movies based on quiz answers
* Ranks and returns the 5 best-matched films

Quiz System:

* Asks 10 engaging questions to understand the user's mood, interests, and vibe
* Each answer contributes to a preference profile used in movie scoring

Recommendation Logic:

* Title-based scoring system
* Uses keywords and concepts to match films to user profiles
* No ML or API dependency — fully self-contained

## Installation

Prerequisites:

* Python 3.8 or higher
* pip (Python package installer)

Install required libraries:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python3 main.py
```

## Project Structure

| File                | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| main.py             | Runs the full app: loads data, calls the quiz, scores movies |
| questions.py        | Contains all 10 questions and returns user answers           |
| imdb\_top\_250.xlsx | Excel sheet of 250 movies                                    |
| requirements.txt    | Contains Python library dependencies                         |
| README.md           | This documentation file                                      |

