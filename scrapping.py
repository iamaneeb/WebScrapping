from selenium import webdriver
from bs4 import BeautifulSoup

search_url = "search?q=software+developer&l="
url = f"https://www.simplyhired.co.in/{search_url}"

# Use the appropriate webdriver for your browser (e.g., ChromeDriver, GeckoDriver)
driver = webdriver.Chrome()

driver.get(url)

# Wait for the page to load (you may need to adjust the waiting time)
driver.implicitly_wait(10)

# Get the page source after it has been dynamically updated
page_source = driver.page_source

# Use BeautifulSoup to parse the updated page source
soup = BeautifulSoup(page_source, 'html.parser')

# Find elements based on their attributes
# Initialize empty lists to store data
titles = []
details = []
hrefs = []

# Find all li elements with the specified class
list_items = soup.find_all("li", {'class': 'css-0'})

# Loop through each li element
for li in list_items:
    # Find the h2 and p elements inside each li
    title = li.find('h2')
    detail = li.find('p')
    link = li.find('a')

    # Check if all elements are found before accessing their text or href
    if title:
        titles.append(title.text.strip())
    else:
        titles.append("No title available")

    if detail:
        details.append(detail.text.strip())
    else:
        details.append("No details available")

    if link and 'href' in link.attrs:
        hrefs.append(link['href'])
    else:
        hrefs.append("No href available")

# Print or return the lists as needed
# print("Titles:", titles)
# print("Details:", details)
# print("Hrefs:", hrefs)
print(titles[0])

# Close the webdriver
driver.quit()
