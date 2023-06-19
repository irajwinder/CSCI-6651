#pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = "https://www.newhaven.edu/engineering/faculty.php"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all the individual instructor elements
instructors = soup.find_all("div", {"class": "person"})

# Loop through each instructor and extract the details
for instructor in instructors:
    name_element = instructor.find("h3", {"class": "person-name"}).find("a")
    name = name_element.text.strip()
    
    
    designation_element = instructor.find("p", {"class": "person-title"}).find("em")
    designation = designation_element.text.strip()

    email_element = instructor.find("a", href=lambda href: href.startswith("mailto:"))
    email = email_element.text.strip().lower()


    # Print the details to the console
    print("Instructor:", name)
    print("Designation:", designation)
    print("Email:", email)
    print()
