# Project_4_company_data
Retrieve company data for Asset managers (company project)

# Project Proposal: LinkedIn-Based Company Data Enrichment

## The Big Idea
The primary goal of this project is to develop a Python script that automates the process of enriching company data by extracting LinkedIn profiles and relevant company details such as website, industry, company size, headquarters, type, year founded, and specialties. The project addresses the challenge of manually searching for and collecting such data, particularly for investment firms or companies listed in an Excel spreadsheet.

### Minimum Viable Product (MVP)
- A script that:
  - Reads a list of company names from an Excel file.
  - Performs a Google search to identify LinkedIn URLs for each company.
  - Scrapes company details from LinkedIn pages and populates the corresponding rows in the Excel file.

### Stretch Goals
- Add error logging and reporting to handle skipped rows or failed attempts.
- Implement parallel processing or asynchronous execution to reduce runtime for example.
- Save document across the search.

---

## Learning Objectives
- Gain hands-on experience with web scraping and data enrichment using Python.
- Learn to handle rate-limiting and error recovery in automated workflows.
- Understand how to structure reusable, maintainable Python scripts for real-world applications.

### Individual Goals
- Improve skills in using Python libraries for web scraping (e.g., `requests`, `BeautifulSoup`).
- Learn about data manipulation with `pandas` and Excel integration.
- Enhance knowledge of exception handling, logging, and debugging in Python.

---

## Implementation Plan
### Technology Stack
- **Libraries** such as `requests`, `pandas`, `BeautifulSoup`, `googlesearch`,... may be useful


### Plan of Action
1. Set up the project repository and ensure all dependencies are installed.
2. Break down the script into smaller modules (e.g., Google search, request handling, data parsing).
3. Implement a proof-of-concept for scraping LinkedIn data using static URLs.
4. Add functionality for searching LinkedIn URLs through Google.
5. Develop error handling and rate-limiting mechanisms.
6. Test the script with sample data and refine the parsing logic.

### Uncertainty Areas
- Whether LinkedIn's structure or Google’s search results format will change during the project. 
- How much data can be retrieved, can it be solved with a time sleep?
- Reliance on scraping (as opposed to using APIs) may introduce limitations.

---

## Project Schedule
### Week 1
- Define project scope and set up the repository.
- Review the provided codebase and identify areas for improvement.

### Week 2
- Implement Google search functionality and integrate it with LinkedIn scraping.
- Add basic error handling and logging.

### Week 3
- Expand the scraping logic to extract additional company details.
- Test the script on a larger dataset.

### Week 4
- Optimize the script for performance (e.g., rate-limiting, retries).
- Add a mechanism to save intermediate progress.
- Complete documentation and polish the final deliverable.
- Prepare the final submission, including reflections on challenges and solutions.


---

## Risks and Limitations
- **Biggest Risk**: Rate-limiting or IP bans from Google or LinkedIn due to frequent requests. This could halt data collection.
- **Mitigation**: Implement randomized delays and pauses, and explore proxies or VPNs for distributed requests.
- **Limitations**:
  - Web scraping is fragile and may break if LinkedIn’s structure changes.
  - Dependency on search results may lead to inconsistent data quality.

---

## Additional Course Content
- **Web Scraping Best Practices**: Strategies to avoid detection and ensure ethical scraping.
- **Asynchronous Programming**: To improve the runtime efficiency of the script.
- **API Integration**: Using APIs like LinkedIn’s to reduce reliance on scraping.
