import pandas as pd
from questions import ask_questions

# Load and clean the Excel file
file_path = "IMdB Top 250 List for Namik.xlsx"
df = pd.read_excel(file_path, skiprows=4)
df = df.dropna(subset=["RANK", "TITLE"])
df.columns = ["Rank", "Title"]
df.reset_index(drop=True, inplace=True)

# Ask user questions and get preferences
preferences = ask_questions()

# Create a simple scoring system
def score_movie(title):
    score = 0
    title_lower = title.lower()

    # Match based on keywords from preferences
    if preferences['title_keywords'].lower() in title_lower:
        score += 2
    if preferences['mood'].lower() in title_lower:
        score += 1
    if preferences['iconic_quote'].lower() in title_lower:
        score += 2
    if preferences['setting'].lower() in title_lower:
        score += 1
    if preferences['fear'].lower() in title_lower:
        score += 1
    if preferences['memorable'].lower() in title_lower:
        score += 1
    if preferences['fantasy_level'].lower() in title_lower:
        score += 1
    if preferences['style'].lower() in title_lower:
        score += 1
    if preferences['group'].lower() in title_lower:
        score += 1
    if preferences['era'] in title:
        score += 1

    return score

# Apply scoring to all films
df['Score'] = df['Title'].apply(score_movie)

# Sort and show top 5
top5 = df.sort_values(by="Score", ascending=False).head(5)

print("🎯 Your Top 5 Film Matches:")
print(top5[['Rank', 'Title', 'Score']].to_string(index=False))
