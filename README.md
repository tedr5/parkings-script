# 🅿🅰🆁🅺🅸🅽🅶

📖 **Description**

PARKING is a command-line application designed to extract, process, and analyze parking data. The project aims to gather real-time information about available parking spaces, clean and organize this data, and store it in a MySQL database for further analysis. This solution facilitates efficient parking management and enables better decision-making based on accurate data.

⚙️ **Technologies**

- **Programming Language:** Python
- **Libraries:** pandas, numpy, mysql-connector-python

🛠️ **Installation**

Clone the repository:
```bash
 git clone https://github.com/tedr5/parkings-script.git
```
- Navigate to the project directory.
  
- Install the required libraries using pip:
```bash
pip install pandas numpy mysql-connector-python
```
- Run the main application script:
```bash
python parkings.py
```

🚀 **Features**

- **Data Extraction:** Downloads and processes parking data from CSV files.
- **Data Cleaning:** Merges and formats data from multiple sources.
- **Database Upload:** Exports cleaned data to a MySQL database.

📂 **Repository Files**

- **parkings.py:** Downloads a CSV file with parking availability, processes the data, and saves it to a MySQL database.  It serves as the initial step for sending data acquired by API to the landing zone database.
- **fills.py:** This is used when dealing with loss data from specific dates. It combines and cleans multiple CSV files containing parking information, preparing the data for database import. 
- **upload.py:** Downloads a CSV file from a URL, saves it locally, uploads it to a Mega account for backup. This is a safeguard against data loss during the extraction process. 

📊 **Data Structures**

Utilizes pandas DataFrames for managing and analyzing parking data, allowing for flexible operations and easy querying in the MySQL database.
