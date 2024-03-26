# Scrapy_1

This Scrapy snippet is designed to scrape recipes and related information from a verified website dedicated to culinary delights. The spider crawls through the website's pages, extracting recipe titles, ingredients, instructions, cooking times, and more. The extracted data is then stored in structured JSON format for further analysis and use.

# Scraped Website: 'https://www.vegrecipesofindia.com/recipes/south-indian-recipes/'

## Project Structure

- scrapy.cfg            # Scrapy configuration file
- myproject             # Scrapy project directory
- spiders               # Directory for Scrapy spiders
- __init__.py           # Python initialization file
- recipe_spider.py      # Scrapy spider for scraping recipes
- items.py              # Defines the data model for scraped items
- middlewares.py        # Scrapy middleware settings
- pipelines.py          # Pipeline for processing scraped items
- settings.py           # Scrapy project settings
- README.md             # Project documentation
- requirements.txt      # List of project dependencies
- final_recipes.json    # Stored the scraped information in a JSON file

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository.
2. Navigate to the project directory.
3. Set up a virtual environment (optional but recommended).
   - python -m venv env             # Creating virtual environment
   - env\Scripts\activate           # Activating on Windows
   - source env/bin/activate        # Activating on macOS/Linux
4. Install the required dependencies using `pip install -r requirements.txt`.