# FSTT Chatbot

This repository contains the code and data for the FSTT Chatbot project. The project involves web scraping, data preprocessing, and fine-tuning a chatbot model to answer questions related to the FSTT (Faculté des Sciences et Techniques de Tanger).

## Project Structure

chatbot_Data/
├── fine_tuning/
│ ├── finetuning.ipynb
│ ├── model_final.ipynb
│ └── test_de_module.ipynb
├── Scraping/

│ ├── json_files/

│ │ ├── Equipes.json

│ │ ├── formation_continu.json

│ │ ├── Formation_cycle.json

│ │ ├── Formation_deust.json

│ │ ├── Formation_initial.json

│ │ ├── Formation_licence.json

│ │ ├── Formation_master.json

│ │ └── Laboratoire.json

│ ├── question_reponse/

│ │ ├── Finaldata.csv

│ │ ├── json_to_csv.py

│ │ └── Question&answer&context.json

│ ├── FSTT_DATA.txt

│ ├── FSTT_Web_Scraping_Formation_part.ipynb

│ └── FSTT_Web_Scraping_presentation_part.ipynb

├── Fine-tuning_dataset.csv

└── FSTT_chatbot.iml

### Directories and Files

- **fine_tuning/**: Contains Jupyter notebooks for fine-tuning the chatbot model.
  - `finetuning.ipynb`: Notebook for initial fine-tuning.
  - `model_final.ipynb`: Notebook for the final model fine-tuning.
  - `test_de_module.ipynb`: Notebook for testing the fine-tuned model.

- **Scraping/**: Contains scripts and data for web scraping.
  - `json_files/`: Directory containing scraped JSON data files.
    - `Equipes.json`, `formation_continu.json`, `Formation_cycle.json`, `Formation_deust.json`, `Formation_initial.json`, `Formation_licence.json`, `Formation_master.json`, `Laboratoire.json`: JSON files containing information about different aspects of FSTT.
  - `question_reponse/`: Directory containing question and answer data.
    - `Finaldata.csv`: CSV file containing processed Q&A data.
    - `json_to_csv.py`: Script to convert JSON Q&A data to CSV.
    - `Question&answer&context.json`: JSON file containing Q&A with context.
  - `FSTT_DATA.txt`: Text file with raw FSTT data.
  - `FSTT_Web_Scraping_Formation_part.ipynb`: Notebook for scraping formation part of the FSTT website.
  - `FSTT_Web_Scraping_presentation_part.ipynb`: Notebook for scraping presentation part of the FSTT website.

- **Fine-tuning_dataset.csv**: CSV file containing the dataset used for fine-tuning the chatbot model.

- **FSTT_chatbot.iml**: IntelliJ IDEA module file.

## Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook
- Required Python packages (listed in `requirements.txt` or in the notebooks)

### Installation

1. Clone the repository:
```bash
   git clone https://github.com/yourusername/chatbot_Data.git
   cd chatbot_Data
 ```
2. Install the required packages:
```bash
 pip install -r requirements.txt
 ```
**Usage**
1. Run the scraping notebooks to gather data:
```bash
jupyter notebook Scraping/FSTT_Web_Scraping_Formation_part.ipynb
jupyter notebook Scraping/FSTT_Web_Scraping_presentation_part.ipynb
 ```
2. Preprocess the data and prepare it for fine-tuning:
```bash
python Scraping/question_reponse/json_to_csv.py
 ```
3. Fine-tune the chatbot model:
```bash
jupyter notebook fine_tuning/finetuning.ipynb
 ```

4. Test the fine-tuned model:
```bash
jupyter notebook fine_tuning/test_de_module.ipynb
 ```

**Contributing**
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

**License**
This project is licensed under the MIT License. See the LICENSE file for details.
