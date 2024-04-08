import os
import json
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read the JSON file into a pandas DataFrame
df = pd.read_json(r"C:\Users\venki\Work\scrapy_data_project_app\myproject\final_recipes.json")

if 'receipe_data' in df.columns:
    # Define the condition to check for empty values for all keys except "Title" and "Description"
    def is_empty_record(record):
        keys_to_check = ['Ingredients', 'Instructions', 'Prep Time', 'Cook Time', 'Total Time', 'Cuisine', 'Course']
        # Check if all keys except "Title" and "Description" have empty values
        return all((key not in record or key in ['Title', 'Description'] or
                    (isinstance(record[key], list) and len(record[key]) == 0) or
                    (isinstance(record[key], str) and not record[key].strip())) for key in keys_to_check)

    # Filter records based on the condition
    empty_records = df.loc[df['receipe_data'].apply(is_empty_record)]

    # Drop the rows with empty values for all specified keys
    df.drop(empty_records.index, inplace=True)

    # Convert the DataFrame to a list of dictionaries
    updated_records = df['receipe_data'].tolist()

    # Add new key-value pair 'Country': 'India' to each dictionary
    for record in updated_records:
        cuisine = record.get('Cuisine', '').lower()
        if 'tamil nadu' in cuisine:
            record['State'] = 'Tamilnadu'
        elif 'karnataka' in cuisine:
            record['State'] = 'Karnataka'
        elif 'kerala' in cuisine:
            record['State'] = 'Kerala'
        elif 'andhra' in cuisine or 'hyderabadi' in cuisine:
            record['State'] = 'Andhra Pradesh'
        else:
            # Default state if cuisine doesn't match
            record['State'] = 'Other'
        record['Country'] = 'India'

   
    # Get MongoDB connection URI from environment variable
    MONGODB_URI = os.getenv("MONGODB_URI")

    if MONGODB_URI:
        # Establish connection to MongoDB
        client = MongoClient(MONGODB_URI)
        
        # Specify the database and collection
        db = client.get_default_database()  # Use default database from URI
        collection = db['recipes']

        # Overwrite the entire collection with new documents
        collection.delete_many({})  # Delete all existing documents
        result = collection.insert_many(updated_records)  # Insert new documents
        
        # Print the number of documents inserted
        print("Number of documents inserted:", len(result.inserted_ids))

        print("Updated records inserted into MongoDB collection 'recipes'.")
    else:
        print("MongoDB connection URI not found in environment variables.")
else:
    print("'receipe_data' column not found in the DataFrame.")