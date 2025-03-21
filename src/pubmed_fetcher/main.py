import json
import requests
import pandas as pd
import argparse
import re


def fetch_pubmed_data(query):
    """Fetches PubMed papers for a given query and returns PubMed IDs."""
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={query}&retmode=json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        ids = data.get("esearchresult", {}).get("idlist", [])
        return ids
    else:
        print("Error fetching data from PubMed!")
        return []


def fetch_paper_details(paper_id):
    """Fetches details of a paper using PubMed ID."""
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={paper_id}&retmode=json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("result", {}).get(paper_id, {})
    else:
        return None


def extract_company_authors(authors):
    """Identifies non-academic authors affiliated with companies."""
    company_authors = []
    companies = []
    for author in authors:
        affiliation = author.get("affiliation", "").lower()
        if affiliation and any(keyword in affiliation for keyword in ["inc", "ltd", "pharma", "biotech", "company"]):
            company_authors.append(author.get("name"))
            companies.append(affiliation)
    return company_authors, companies


def process_papers(paper_ids):
    """Processes paper details and identifies authors with company affiliations."""
    results = []
    
    for paper_id in paper_ids:
        paper_data = fetch_paper_details(paper_id)
        
        if not paper_data:
            continue
        
        title = paper_data.get("title", "N/A")
        pub_date = paper_data.get("pubdate", "N/A")
        authors = paper_data.get("authors", [])
        corresponding_email = paper_data.get("correspondence", "")

        # Get company authors and their affiliations
        company_authors, companies = extract_company_authors(authors)
        
        results.append({
            "PubmedID": paper_id,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": ", ".join(company_authors) if company_authors else "N/A",
            "Company Affiliation(s)": ", ".join(companies) if companies else "N/A",
            "Corresponding Author Email": corresponding_email
        })
    
    return results


def save_results(results, filename="results.csv", output_format="csv"):
    """Saves results to a CSV or JSON file."""
    if not results:
        print("No data to save.")
        return

    if output_format == "csv":
        df = pd.DataFrame(results)
        df.to_csv(filename, index=False)
        print(f"✅ Results saved to {filename}")

    elif output_format == "json":
        json_filename = filename.replace(".csv", ".json")
        with open(json_filename, "w", encoding="utf-8") as file:
            json.dump(results, file, indent=4)
        print(f"✅ Results saved to {json_filename}")

    else:
        print("❌ Invalid output format. Use 'csv' or 'json'.")


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description="Fetch PubMed papers based on a query.")
    parser.add_argument("query", help="Search query for PubMed.")
    parser.add_argument("-f", "--file", help="Filename to save the results (CSV/JSON).", default="results.csv")
    parser.add_argument("--format", help="Output format: 'csv' or 'json'", choices=["csv", "json"], default="csv")
    parser.add_argument("-d", "--debug", help="Print debug info.", action="store_true")

    args = parser.parse_args()

    if args.debug:
        print(f"Fetching data for query: {args.query}")

    # Fetch paper IDs from PubMed
    paper_ids = fetch_pubmed_data(args.query)

    if not paper_ids:
        print("No papers found for the given query.")
        return

    # Process paper details
    results = process_papers(paper_ids)

    if results:
        # Save results in CSV or JSON based on format
        save_results(results, args.file, args.format)
    else:
        print("No relevant papers with company affiliations found.")


if __name__ == "__main__":
    main()
