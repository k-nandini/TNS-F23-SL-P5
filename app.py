#
# Self as System - The New School
# Project done by Nandini Kumar
#

#
# REFERENCES
#
# FLASK Tutorial
# https://www.youtube.com/watch?v=Z1RJmh_OqeA
# - https://github.com/jakerieger/FlaskIntroduction
# - https://flask.palletsprojects.com/en/3.0.x/
# - https://www.freecodecamp.org/
#
# Tailwind CSS Tutorial with Flask
# https://www.youtube.com/watch?v=xxkDLvS5MTY
# - https://tailwindcss.com/
# - https://tailblocks.cc/
#

#
# ISSUES (BIG-TRACKER)
#
# The Duplicate removal function removes all data from DB
#

# Import necessary modules and create a Flask app
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import os
import random

# Initialize the Flask app and configure the SQLite database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sas.db'
db = SQLAlchemy(app)

# Define a database model for content
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))

# Setting home page route to index.html
@app.route('/')
def index():
    # Render the 'index.html' template
    return render_template('index.html')

# Function to import CSV Data from a path to the database
@app.route('/import_data')
def import_data():
    csv_dir = './static/assets/csv/' # Location of CSV
    csv_filename = 'comments.csv' # Name of CSV
    csv_path = os.path.join(csv_dir, csv_filename)

    # Check if the CSV file exists
    if not os.path.exists(csv_path):
        return "CSV file not found."

    # Using Pandas to parse CSV
    data = pd.read_csv(csv_path)

    # Import the data from the column named 'content'
    for index, row in data.iterrows():
        content = row['content']

        # Check if the same content exists in the database
        existing_content = Content.query.filter_by(content=content).first()

        # Import the data if it doesn't already exist
        if not existing_content:
            new_content = Content(content=content)
            db.session.add(new_content)

    db.session.commit()
    return "Data imported successfully!"

# Function to remove duplicate content from the database
@app.route('/remove_duplicates')
def remove_duplicates():
    unique_content = db.session.query(Content.content).distinct()

    # Delete all existing content in the database
    Content.query.delete()

    # Add unique content back to the database
    for row in unique_content:
        new_content = Content(content=row[0])
        db.session.add(new_content)

    db.session.commit()
    return "Duplicates removed successfully!"

# Route to display a random content from the database
@app.route('/results')
def display_random_content():
    # Query all content items from the database
    all_content = Content.query.all()

    # Check if there is any content available in the database
    if all_content:
        # If content is available, select a random content item
        random_content = random.choice(all_content)
        content_to_display = random_content.content
    else:
        # If there is no content in the database, display a message
        content_to_display = "No advice available at this time."

    # Render the 'results.html' template and pass the selected content to it
    return render_template('results.html', content=content_to_display)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=False)
