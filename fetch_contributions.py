import requests
from datetime import datetime

def fetch_github_events(username):
    response = requests.get(f'https://api.github.com/users/{username}/events')
    return response.json()

def calculate_streaks(events):
    dates = [datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ').date() for event in events]
    current_streak = longest_streak = 0
    total_contributions = len(dates)
    
    if dates:
        dates.sort(reverse=True)
        current_streak = 1
        longest_streak = 1
        streak = 1
        
        for i in range(1, len(dates)):
            if (dates[i - 1] - dates[i]).days == 1:
                streak += 1
                current_streak = max(current_streak, streak)
            else:
                streak = 1
            longest_streak = max(longest_streak, streak)
    
    return total_contributions, current_streak, longest_streak