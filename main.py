from fetch_contributions import fetch_github_events, calculate_streaks
from generate_svg import generate_svg
import os

if __name__ == '__main__':
    username = 'your-username'
    token = 'your-github-token'  # Generate a GitHub token and use it here

    # Ensure the output directory exists
    if not os.path.exists('output'):
        os.makedirs('output')

    events = fetch_github_events(username, token)
    total_contributions, current_streak, longest_streak = calculate_streaks(events)
    generate_svg(total_contributions, current_streak, longest_streak)