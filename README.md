# Data Processing with Python and MongoDB

This Python script demonstrates the process of exploring, cleaning, and updating recipe data using Python and MongoDB. The script takes a JSON file containing recipe data, performs data cleaning operations, enriches the data by categorizing recipes into specific Indian states based on cuisine, and finally, connects to a MongoDB database to store the updated recipe documents.

# Scraped Website: 'https://www.vegrecipesofindia.com/recipes/south-indian-recipes/'

## Project Structure

- data_insertion.py     # A Python script for Data processing
- README.md             # Project documentation
- requirements.txt      # List of project dependencies
- final_recipes.json    # Stored the scraped information in a JSON file
- .env                  # The .env file contains sensitive information such as the MongoDB connection URI. Ensure this file is properly configured with your credentials before running the script.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository.
2. Navigate to the project directory.
3. Set up a virtual environment (optional but recommended).
   - python -m venv env             # Creating virtual environment
   - env\Scripts\activate           # Activating on Windows
   - source env/bin/activate        # Activating on macOS/Linux
4. Install the required dependencies using `pip install -r requirements.txt`.

# Steps
1. Ensure you have Python installed on your system.
2. Install the required Python libraries using pip install -r requirements.txt.
3. Place your recipe data in JSON format in the same directory as the script (final_recipes.json in this example).
4. Configure the .env file with your MongoDB connection URI and other sensitive information.
5. Run the script using python data_insertion.py.
6. Check your MongoDB database for the updated 'recipes' collection.

# Additional Notes

- This script is designed to work with recipe data in JSON format. Ensure your data follows the required structure for successful - processing.
- Customize the script as needed for your specific dataset and requirements.