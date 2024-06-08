import svgwrite

def generate_svg(total_contributions, current_streak, longest_streak):
    dwg = svgwrite.Drawing('output/contributions.svg', profile='full', size=('500px', '200px'))
    dwg.add(dwg.rect(insert=(0, 0), size=('500px', '200px'), fill='#1e1e2e'))
    
    dwg.add(dwg.text('Total Contributions', insert=(20, 40), fill='#ff79c6', font_size='20px', font_family='Arial'))
    dwg.add(dwg.text(str(total_contributions), insert=(20, 70), fill='#f1fa8c', font_size='30px', font_family='Arial'))
    
    dwg.add(dwg.text('Current Streak', insert=(200, 40), fill='#ff79c6', font_size='20px', font_family='Arial'))
    dwg.add(dwg.text(str(current_streak), insert=(200, 70), fill='#f1fa8c', font_size='30px', font_family='Arial'))
    
    dwg.add(dwg.text('Longest Streak', insert=(380, 40), fill='#ff79c6', font_size='20px', font_family='Arial'))
    dwg.add(dwg.text(str(longest_streak), insert=(380, 70), fill='#f1fa8c', font_size='30px', font_family='Arial'))
    
    dwg.save()