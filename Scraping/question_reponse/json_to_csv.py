import json
import csv

def json_to_csv(json_file, csv_file):
    # Open the JSON file and load the data
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Extract the list of questions from the JSON data
    questions = data['questions']

    # Open CSV file in write mode
    with open(csv_file, 'w', newline='') as f:
        # Create a CSV writer object
        writer = csv.writer(f)

        # Write header using the keys of the first question
        writer.writerow(questions[0].keys())

        # Write each row using the values of each question
        for question in questions:
            writer.writerow(question.values())


# Example usage
json_file = 'Q&A.json'
csv_file = 'data.csv'
json_to_csv(json_file, csv_file)
