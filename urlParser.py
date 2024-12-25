import requests
from bs4 import BeautifulSoup

def fetch_website_content(url, output_filename):
    # Send a GET request to the website
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse the page content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract text from the page
        text_content = soup.get_text()
        
        # Save the text content to a .txt file
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(text_content)
        print(f"Content successfully saved to {output_filename}")
    else:
        print(f"Failed to retrieve the content. Status code: {response.status_code}")

# Example usage
website_url = "https://cybernxs.blogspot.com"
output_filename = "website_content.txt"  # Name of the output text file
fetch_website_content(website_url, output_filename)
