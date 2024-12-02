# Project 4: LinkedIn-Based Company Data Enrichment

## Overview
This project automates the process of enriching company data by retrieving detailed information from LinkedIn profiles, such as:
- Website
- Industry
- Company size
- Headquarters
- Type
- Year founded
- Specialties

The solution is designed to save time for investment professionals and researchers by processing large datasets of company names in a CSV or Excel file, extracting the required data, and providing the results in a structured format.

---

## The Big Idea
Manually searching for company details on LinkedIn is time-consuming and error-prone. This project solves the problem by:
1. Automating LinkedIn profile searches using Google.
2. Scraping key company details directly from LinkedIn pages.
3. Compiling all the data into a single, downloadable file.

### Minimum Viable Product (MVP)
- Upload a file (CSV/Excel) with company names or enter a single asset manager name for which you want to retrieve information.
- Retrieve LinkedIn URLs and company details for each name.
- Download an updated file with the enriched data.

### Stretch Goals
- **Improved performance**: Use asynchronous execution or parallel processing to handle large datasets.
- **Error reporting**: Log failed attempts and skipped rows in a separate file.
- **Real-time updates**: Save intermediate progress during the search process.

---

## Learning Objectives
- **Python Web Scraping**: Master the use of `requests`, `BeautifulSoup`, and `googlesearch`.
- **Data Processing**: Gain experience manipulating and processing data with `pandas`.
- **Error Handling**: Learn to implement robust exception handling and logging.
- **Web Development**: Understand how to build a user-friendly interface using Flask.

---

## Features
### Current Features
- File upload support for CSV and Excel files.
- Single company search.
- Validation to ensure the input file contains a `Company` column.
- Automated Google search to find LinkedIn URLs.
- Scraping of key company details from LinkedIn pages.
- Downloadable enriched file in Excel format.

### Potential future Planned Enhancements
- **Data Visualization**: Add a dashboard for summarizing the results (e.g., industries, company sizes).
- **Asynchronous Scraping**: Reduce runtime for large datasets.

---

## Usage Instructions
### Prerequisites
- Python 3.9+
- Required libraries: Install them with:
  ```bash
  pip install -r requirements.txt

# Running the App

## Clone this repository:
```bash
git clone https://github.com/yourusername/Project_4_company_data.git
cd Project_4_company_data
```

## Start the Flask app:
```bash
python app.py
```

## Open your browser and navigate to:
```arduino
http://127.0.0.1:5000
```

## Steps to Use the App:
0. Choose whether you want to search a single company name or Upload a file with many names.
1. Search the company name or Upload a file (CSV or Excel) with a column labeled **Company** containing the company names.
2. Click **"Submit"** to start the data enrichment process.
3. Download the enriched file with LinkedIn data.

---

# Implementation Details

## Workflow

### File Upload:
- Users upload a file containing company names.
- The app validates the file format and checks for the required **Company** column.

### Google Search:
- The app searches for LinkedIn URLs using the `googlesearch` library.
- The first relevant LinkedIn URL is identified for each company.

### Data Scraping:
- The app fetches LinkedIn pages and extracts data using **BeautifulSoup**.
- Extracted fields include:
  - Website
  - Industry
  - Employees
  - Headquarters
  - Type
  - Year Founded
  - Specialties

### Result Compilation:
- All data is saved in a structured Excel file, ready for download.

---

# Results

## Input Example
A sample input file (`companies.csv`):

| Company    |
|------------|
| BlackRock  |
| Vanguard   |
| State Street |

## Output Example
The resulting enriched file (`company_info.xlsx`):

| Company    | LinkedIn URL                  | Website         | Industry    | Employees | Headquarters     | Type     | Founded |
|------------|-------------------------------|-----------------|-------------|-----------|------------------|----------|---------|
| BlackRock  | linkedin.com/company/blackrock | blackrock.com  | Finance     | 10,000+   | New York, USA    | Private  | 1988    |
| Vanguard   | linkedin.com/company/vanguard  | vanguard.com   | Investment  | 20,000+   | Valley Forge, USA| Private  | 1975    |

---

# Project Schedule

| Week | Goals                                                     |
|------|-----------------------------------------------------------|
| 1    | Define project scope and set up repository.               |
| 2    | Implement Google search integration and LinkedIn scraping.|
| 3    | Add error handling, validation, and intermediate result saving. |
| 4    | Optimize performance, polish the UI, and finalize the documentation. |

---

# Risks and Limitations

## Risks
- **Rate-Limiting**: Excessive requests to Google or LinkedIn may result in IP bans.
  - **Mitigation**: Add random delays between requests and limit scraping frequency.
- **Data Quality**: LinkedIn’s page structure may change, breaking the scraper.
  - **Mitigation**: Regularly update the scraping logic.

## Limitations
- Web scraping is inherently fragile and less reliable than API-based solutions.
- LinkedIn may restrict access to detailed data due to security measures.

---

# Additional Features for the Future
- **Dynamic Dashboard**: Use tools like Plotly or Dash to visualize enriched data.
- **API Integration**: Replace scraping with LinkedIn's official API for better reliability.
- **File Format Flexibility**: Support additional input/output formats (e.g., JSON).

---

# Attribution
This project uses the following tools and libraries:
- **Flask**: [Flask Documentation](https://flask.palletsprojects.com/)
- **pandas**: [pandas Documentation](https://pandas.pydata.org/)
- **BeautifulSoup**: [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/)
- **Google Search API**: [Google Search](https://developers.google.com/custom-search/)
