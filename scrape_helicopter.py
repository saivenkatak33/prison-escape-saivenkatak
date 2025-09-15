import requests
import pandas as pd
from bs4 import BeautifulSoup

# Wikipedia page URL
url = "https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes"

# Use headers to avoid being blocked
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find the first wikitable
table = soup.find("table", {"class": "wikitable"})

if not table:
    raise Exception(" No table found on the page. Wikipedia may have changed the structure.")

# Extract headers
headers = [th.get_text(strip=True) for th in table.find_all("th")]

# Extract rows
rows = []
for tr in table.find_all("tr")[1:]:  # skip header row
    cells = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
    if cells:
        rows.append(cells)

# Create DataFrame
df = pd.DataFrame(rows, columns=headers)

# Save as CSV
df.to_csv("helicopter_prison_escapes.csv", index=False, encoding="utf-8")

print(" CSV file created successfully: helicopter_prison_escapes.csv")
print(df.head())



