from bs4 import BeautifulSoup

with open('./bin/gdp_asean.html', 'r', encoding='utf-8') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

    # Use the XPath to select the element
    selected_element = soup.select('html > body > div:nth-of-type(2)')

    # Check if the element is found
    if selected_element:
        print(selected_element[0].prettify())
    else:
        print("Element not found.")
