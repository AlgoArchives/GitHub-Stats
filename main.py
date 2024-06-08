import requests
from datetime import datetime

# Replace 'your-username' with your GitHub username
username = 'your-username'
response = requests.get(f'https://api.github.com/users/{username}/events')
events = response.json()

# Function to calculate streaks
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

total_contributions, current_streak, longest_streak = calculate_streaks(events)

print(f'Total Contributions: {total_contributions}')
print(f'Current Streak: {current_streak}')
print(f'Longest Streak: {longest_streak}')

import svgwrite

def generate_svg(total_contributions, current_streak, longest_streak):
    dwg = svgwrite.Drawing('contributions.svg', profile='full', size=('500px', '200px'))
    dwg.add(dwg.rect(insert=(0, 0), size=('500px', '200px'), rx=None, ry=None, fill='#1e1e2e'))
    
    dwg.add(dwg.text('Total Contributions', insert=(20, 40), fill='#ff79c6', font_size='20px', font_family='Arial'))
    dwg.add(dwg.text(str(total_contributions), insert=(20, 70), fill='#f1fa8c', font_size='30px', font_family='Arial'))
    
    dwg.add(dwg.text('Current Streak', insert=(200, 40), fill='#ff79c6', font_size='20px', font_family='Arial'))
    dwg.add(dwg.text(str(current_streak), insert=(200, 70), fill='#f1fa8c', font_size='30px', font_family='Arial'))
    
    dwg.add(dwg.text('Longest Streak', insert=(380, 40), fill='#ff79c6', font_size='20px', font_family='Arial'))
    dwg.add(dwg.text(str(longest_streak), insert=(380, 70), fill='#f1fa8c', font_size='30px', font_family='Arial'))
    
    dwg.save()

generate_svg(total_contributions, current_streak, longest_streak)