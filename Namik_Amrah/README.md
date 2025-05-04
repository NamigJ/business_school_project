MovieMatch 250 

A Python-based personality quiz that recommends 5 movies from IMDb's Top 250 list based on your answers.

How it works

Loads a list of 250 top-rated films (from Excel)
Asks 10 fun questions to understand your movie personality
Scores each movie based on keyword matches
Suggests your Top 5 matches
Technologies Used

Python 3
pandas
openpyxl

How to Run

Install required libraries:
pip install -r requirements.txt
Run the app in Terminal:
python3 main.py

Project Structure

main.py → Runs the app
questions.py → Quiz logic
imdb_top_250.xlsx → Movie data
requirements.txt → Dependencies
README.md → Project overview
