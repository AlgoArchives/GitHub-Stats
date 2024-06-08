from fetch_contributions import fetch_github_events, calculate_streaks
from generate_svg import generate_svg

if __name__ == '__main__':
    username = 'Vikranth3140'
    events = fetch_github_events(username)
    total_contributions, current_streak, longest_streak = calculate_streaks(events)
    generate_svg(total_contributions, current_streak, longest_streak)