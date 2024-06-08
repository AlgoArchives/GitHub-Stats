import requests
from datetime import datetime

def fetch_github_events(username, token):
    events = []
    page = 1
    while True:
        url = f'https://api.github.com/users/{username}/events?page={page}&per_page=100'
        headers = {'Authorization': f'token {token}'}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            break
        page_events = response.json()
        if not page_events:
            break
        events.extend(page_events)
        page += 1
    return events

def calculate_streaks(events):
    dates = [datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ').date() for event in events if event['type'] == 'PushEvent']
    if not dates:
        return 0, 0, 0

    dates = sorted(set(dates))  # Sort and remove duplicates
    total_contributions = len(dates)
    
    current_streak = 1
    longest_streak = 1
    streak = 1
    
    for i in range(1, len(dates)):
        if (dates[i] - dates[i - 1]).days == 1:
            streak += 1
        else:
            streak = 1
        longest_streak = max(longest_streak, streak)
    
    # Calculate current streak
    if (datetime.now().date() - dates[-1]).days == 0:
        current_streak = streak
    else:
        current_streak = 0
    
    return total_contributions, current_streak, longest_streak