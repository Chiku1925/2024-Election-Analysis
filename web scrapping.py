import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Identify the URL
url = 'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-743.htm'

# Step 2: Fetch the webpage
response = requests.get(url)
if response.status_code == 200:
    page_content = response.content

    # Step 3: Parse the webpage content
    soup = BeautifulSoup(page_content, 'html.parser')

    # Step 4: Extract the data
    # (Example: Extracting data from a table)
    data = []
    table = soup.find('table')  # Adjust according to the actual HTML structure
    headers = [header.text for header in table.find_all('th')]
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if columns:
            data.append([column.text for column in columns])
    
    # Step 5: Save the data to an Excel file
    df = pd.DataFrame(data, columns=headers)
    df.to_excel('IND.xlsx', index=False)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
