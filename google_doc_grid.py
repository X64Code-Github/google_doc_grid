import requests
from bs4 import BeautifulSoup

def fetch_google_doc(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_google_doc(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table')

    spans = table.find_all('span')
    coordinates = []

    for i in range(3, len(spans) - 2, 3):
        x_row = int(spans[i].text)
        char_row = spans[i + 1].text
        y_row = int(spans[i + 2].text)

        coordinates.append((x_row, y_row, char_row))

    return coordinates

def create_and_print_grid(coordinates):
    if not coordinates:
        print("No coordinates found.")
        return

    max_x = max(coord[0] for coord in coordinates)
    max_y = max(coord[1] for coord in coordinates)
    
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    for x, y, char in coordinates:
        grid[y][x] = char
    
    for row in grid:
        print(''.join(row))

def display_google_doc_grid(url):
    html_content = fetch_google_doc(url)
    coordinates = parse_google_doc(html_content)
    create_and_print_grid(coordinates)

url = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"
display_google_doc_grid(url)
