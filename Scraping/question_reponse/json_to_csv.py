import json
import csv

# Open the JSON file and load the data
with open('Scraping/question_reponse/Question&answer&context.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Open a CSV file for writing
with open('Scraping\question_reponse\Finaldata.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["question", "answer", "context"])
    
    # Write the data
    for item in data['questions']:
        question = item.get("question", "")
        answer = item.get("answer", "")
        context = item.get("context", "")
        writer.writerow([question, answer, context])

print("Data has been written to Contextdata.csv")
