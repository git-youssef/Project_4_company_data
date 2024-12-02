from flask import Flask, render_template, request, send_file
import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import time

app = Flask(__name__)

# Set up folder paths using absolute paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
OUTPUT_FOLDER = os.path.join(BASE_DIR, 'outputs')

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Configure Flask app paths
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Function to perform Google search
def google_search(query, num_results=5):
    try:
        search_results = list(search(query, num_results=num_results))
        return search_results
    except Exception as e:
        print(f"Error performing Google search: {e}")
        return []

# Function to make requests to a company's LinkedIn URL
def make_request(CompanyURL):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }
    print(f"Requesting URL: {CompanyURL}")
    response = requests.get(CompanyURL, headers=headers)
    if response.status_code == 200:
        return response
    return None

# Function to parse the HTML response and extract company details
def parse_response(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    data = {}
    elements = soup.find_all('div', class_='mb-2 flex papabear:mr-3 mamabear:mr-3 babybear:flex-wrap')
    for element in elements:
        key = element.find('dt').get_text(strip=True)
        value = element.find('dd').get_text(strip=True)
        data[key] = value
    cleaned_data = {key.lower().replace(' ', '_'): value for key, value in data.items()}
    return cleaned_data

# Flask route for the homepage
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        choice = request.form.get("choice")

        if choice == "single":
            # Process a single company name
            company_name = request.form.get("company_name")
            if company_name:
                search_query = f"{company_name} investment fund linkedin"
                search_results = google_search(search_query)
                linkedin_url = None
                for result in search_results:
                    if "linkedin.com" in result:
                        linkedin_url = result
                        break
                if linkedin_url:
                    response = make_request(linkedin_url)
                    if response:
                        single_company_details = parse_response(response)
                        single_company_details["LinkedIn"] = linkedin_url
                        return render_template("index.html", single_company_details=single_company_details)
                    else:
                        return render_template("index.html", error_message=f"Error retrieving LinkedIn page for {company_name}.")
                else:
                    return render_template("index.html", error_message=f"No LinkedIn URL found for {company_name}.")
            else:
                return render_template("index.html", error_message="Please enter a valid company name.")

        elif choice == "file":
            # Process a file upload
            file = request.files.get("file")
            if file:
                input_filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(input_filepath)

                # Read the input file
                if file.filename.endswith('.csv'):
                    df = pd.read_csv(input_filepath)
                elif file.filename.endswith('.xlsx'):
                    df = pd.read_excel(input_filepath)
                else:
                    return render_template("index.html", error_message="Unsupported file format. Upload a CSV or Excel file.")

                # Ensure the file has a 'Company' column
                df.columns = [col.strip().lower() for col in df.columns]
                if 'company' not in df.columns:
                    return render_template("index.html", error_message="The uploaded file must have a 'Company' column.")

                # Prepare the output DataFrame
                output_data = []
                for _, row in df.iterrows():
                    company_name = row['company']
                    print(f"Processing company: {company_name}")

                    # Perform Google search for LinkedIn URL
                    search_query = f"{company_name} investment fund linkedin"
                    search_results = google_search(search_query)
                    linkedin_url = None
                    for result in search_results:
                        if "linkedin.com" in result:
                            linkedin_url = result
                            break

                    # Scrape company details from LinkedIn (if URL found)
                    company_details = {"Company": company_name, "LinkedIn": linkedin_url or "Not Found"}
                    if linkedin_url:
                        response = make_request(linkedin_url)
                        if response:
                            parsed_data = parse_response(response)
                            company_details.update({
                                "Website": parsed_data.get("website", "Not Found"),
                                "Industry": parsed_data.get("industry", "Not Found"),
                                "Employees": parsed_data.get("company_size", "Not Found"),
                                "Headquarters": parsed_data.get("headquarters", "Not Found"),
                                "Type": parsed_data.get("type", "Not Found"),
                                "Founded": parsed_data.get("founded", "Not Found"),
                            })
                    output_data.append(company_details)
                    time.sleep(2)  # Add a delay to avoid rate-limiting

                # Save the output file
                output_filepath = os.path.join(app.config['OUTPUT_FOLDER'], "company_info.xlsx")
                try:
                    output_df = pd.DataFrame(output_data)
                    output_df.to_excel(output_filepath, index=False)
                    print(f"File successfully saved to: {output_filepath}")
                except Exception as e:
                    print(f"Error while saving file: {e}")
                    return render_template("index.html", error_message="Failed to save the output file.")

                # Ensure the file exists before sending
                if os.path.exists(output_filepath):
                    return send_file(output_filepath, as_attachment=True)
                else:
                    print(f"File not found: {output_filepath}")
                    return render_template("index.html", error_message="Output file could not be found.")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
