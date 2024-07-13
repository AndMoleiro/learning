import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

# Function to clean the full name
def clean_full_name(cell):
    full_name_div = cell.find("div", class_="d3-o-club-fullname")
    if full_name_div:
        for sup_tag in full_name_div.find_all("sup"):
            sup_tag.decompose()
        return full_name_div.get_text(strip=True)
    return cell.text.get_text(strip=True)

# Function to get rows from the table
def get_rows(table):
    rows = []
    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td")
        row_data = [
            clean_full_name(cell) if index == 0 else cell.get_text(strip=True)
            for index, cell in enumerate(cells)
        ]
        rows.append(row_data)
    return rows

# URL of the webpage to scrape
url = "https://www.nfl.com/standings/league/2021/REG"

# Fetch the webpage content
page = requests.get(url)

# Parse the webpage content with BeautifulSoup
soup = BeautifulSoup(page.text, "lxml")

# Find the table with the specified summary attribute
table_full_html = soup.find("table", {"summary": "Standings - Detailed View"})

# Extract headers (assuming headers are within 'th' tags)
headers = [th.get_text(strip=True) for th in table_full_html.find_all("th")]

# Extract rows from the table
rows = get_rows(table=table_full_html)

# Create DataFrame
df = pd.DataFrame(columns=headers, data=rows)
sorted_df = df.sort_values(by=[df.columns[4], df.columns[1]], ascending=[False, True])


# Print the DataFrame
print(tabulate(df, headers='keys', showindex=False ,tablefmt='simple_grid'))


