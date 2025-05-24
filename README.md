
# 📱 Flipkart Smartphone Scraper

A simple Python project that scrapes smartphone listings from Flipkart, extracts relevant product information, and exports the results into a clean `.csv` file.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-orange)
![WebScraping](https://img.shields.io/badge/WebScraping-BeautifulSoup-green)

---


## ✨ Features

- Collect smartphone listing HTML cards from Flipkart.
- Save raw HTML pages for offline data processing.
- Parse HTML to extract smartphone data.
- Generate a structured CSV file from the collected data.

---

## 🧰 Tech Stack

- Python
- Selenium
- BeautifulSoup (bs4)
- Pandas

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-link>
cd <your-project-folder>
````

### 2. Set Up a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install selenium pandas bs4
```

---

## 🚀 How to Use

### Step 1: Scrape HTML files

Run the scraper script to collect smartphone product pages:

```bash
python basic_smartphone_webscraping.py
```

➡️ This will create approximately 700+ .html files in the smartphone\_flipkart/ folder.

### Step 2: Extract Data & Generate CSV

```bash
python data_collect.py
```

➡️ This script will parse the HTML files and generate a .csv file with structured smartphone data.

---

## 📁 Project Structure

```
├── basic_smartphone_webscraping.py   # Scraper to collect HTML pages
├── data_collect.py                   # Parser to extract data from HTML
├── smartphone_flipkart/              # Folder to store HTML files
├── Flipkart_Smartphoneslist.csv      # Final generated CSV file
└── README.md
```


Let me know if you’d like  to include a live preview of this basic code!
