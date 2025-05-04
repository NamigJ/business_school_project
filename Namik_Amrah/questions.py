def ask_questions():
    print("🎥 Welcome to the Film Personality Quiz!\nAnswer these 10 questions to discover your perfect movie match.\n")

    preferences = {}

    # Q1: Time Travel
    print("1. You’re time-traveling. Which era would you visit?")
    print("   a) 1970s\n   b) 1990s\n   c) 2000s\n   d) Future")
    ans = input("   Your answer (a/b/c/d): ").strip().lower()
    preferences['era'] = {'a': '1970', 'b': '1990', 'c': '2000', 'd': '2010'}.get(ans, '2000')

    # Q2: Mood
    print("\n2. What do you need most today?")
    print("   a) Hope\n   b) Power\n   c) Love\n   d) Revenge")
    ans = input("   Your answer (a/b/c/d): ").strip().lower()
    preferences['mood'] = {'a': 'Redemption', 'b': 'Crime', 'c': 'Romance', 'd': 'Thriller'}.get(ans, 'Drama')

    # Q3: Movie night guests
    print("\n3. You’re hosting a movie night. Who are you inviting?")
    print("   a) Myself\n   b) Family\n   c) Friends\n   d) Crush")
    ans = input("   Your answer (a/b/c/d): ").strip().lower()
    preferences['group'] = {'a': 'Short', 'b': 'Heartwarming', 'c': 'Fun', 'd': 'Romantic'}.get(ans, 'Fun')

    # Q4: Life story title
    print("\n4. Pick a title for your life story.")
    print("   a) The Rise\n   b) Eternal Struggle\n   c) One Last Chance\n   d) Kingdom Within")
    ans = input("   Your answer (a/b/c/d): ").strip().lower()
    preferences['title_keywords'] = {'a': 'Rise', 'b': 'Fight', 'c': 'Hope', 'd': 'King'}.get(ans, 'Hope')

    # Q5: Fictional item
    print("\n5. Which item would you keep forever?")
    print("   a) The One Ring\n   b) A Notebook\n   c) Infinity Gauntlet\n   d) A Samurai Sword")
    ans = input("   Your answer (a/b/c/d): ").strip().lower()
    preferences['fantasy_level'] = {'a': 'Fantasy', 'b': 'Realistic', 'c': 'Epic', 'd': 'Martial'}.get(ans, 'Epic')

    # Q6: Tattoo quote
    print("\n6. Choose a quote to tattoo.")
    print("   a) 'Why so serious?'\n   b) 'I am your father.'\n   c) 'Hope is a good thing.'\n   d) 'Hasta la vista, baby.'")
    ans = input("   Your answer (a/b/c/d): ").strip().lower()
    preferences['iconic_quote'] = {'a': 'Dark Knight', 'b': 'Star Wars', 'c': 'Shawshank', 'd': 'Terminator'}.get(ans, 'Dark Knight')

    # Q7: Ideal movie setting
    print("\n7. What's your ideal movie setting?")
    print("   a) Space\n   b) Prison\n   c) New York City\n   d) Battlefield")
    ans = input("   Your answer (a/b/c/d): ").strip().lower()
    preferences['setting'] = {'a': 'Space', 'b': 'Prison', 'c': 'City', 'd': 'War'}.get(ans, 'City')

    # Q8: Fighting style
    print("\n8. Pick your fighting style.")
    print("   a) Guns blazing\n   b) Mind games\n   c) Silence & strategy\n   d) Big speeches")
    ans = input("   Your answer (a/b/c/d): ").strip().lower()
    preferences['style'] = {'a': 'Action', 'b': 'Thriller', 'c': 'Mystery', 'd': 'Drama'}.get(ans, 'Drama')

    # Q9: Biggest fear
    print("\n9. What do you fear most?")
    print("   a) Boredom\n   b) Death\n   c) Betrayal\n   d) The Unknown")
    ans = input("   Your answer (a/b/c/d): ").strip().lower()
    preferences['fear'] = {'a': 'Exciting', 'b': 'Survival', 'c': 'Crime', 'd': 'Sci-Fi'}.get(ans, 'Drama')

    # Q10: What makes a movie unforgettable?
    print("\n10. What makes a movie unforgettable?")
    print("   a) The ending\n   b) The actors\n   c) The music\n   d) The realism")
    ans = input("   Your answer (a/b/c/d): ").strip().lower()
    preferences['memorable'] = {'a': 'Plot twist', 'b': 'Cast', 'c': 'Score', 'd': 'True story'}.get(ans, 'Cast')

    print("\n🧠 Thanks! Generating your movie recommendations...\n")
    return preferences
