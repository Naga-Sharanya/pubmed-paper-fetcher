# pubmed-paper-fetcher
A CLI tool to fetch PubMed research papers with company-affiliated authors and export them as a CSV.
📚 PubMed Paper Fetcher
    A Python program that fetches research papers from PubMed based on a user-specified query. It identifies papers where at least one author is affiliated with a pharmaceutical or biotech company and returns the results as a CSV or JSON file.


🚀 Features
    ✅ Fetches research papers using the PubMed API
    ✅ Identifies non-academic authors from pharmaceutical/biotech companies
    ✅ Returns results in both CSV and JSON formats
    ✅ Provides a command-line interface with multiple options
    ✅ Error handling for invalid queries, API failures, and missing data
    ✅ Published as a package on PyPI and TestPyPI


📦 PyPI and TestPyPI Package
The project is published on PyPI and TestPyPI for easy installation.


🎉 Install from PyPI:
    To install the package from PyPI, run:
        pip install pubmed-paper-fetcher-sharanya


🧪 Install from TestPyPI:
    To install from TestPyPI:
        pip install --index-url https://test.pypi.org/simple/ pubmed-paper-fetcher-sharanya


🔗 Package Links:
    🔗 PyPI Package Link : https://pypi.org/project/pubmed-paper-fetcher-sharanya/ 
    🔗 TestPyPI Package Link : https://test.pypi.org/project/pubmed-paper-fetcher-sharanya/ 


🛠️ Installation
    1️⃣ Clone the Repository:
        git clone https://github.com/sharanya/pubmed-paper-fetcher.git
        cd pubmed-paper-fetcher
    2️⃣ Install Dependencies Using Poetry:
        poetry install
    3️⃣ Activate the Virtual Environment:
        poetry env activate


📖 Usage
    You can run the program using the command:
        poetry run get-papers-list "cancer treatment"
    🔥 Command-Line Options:
        poetry run get-papers-list --help


Available Options:
    -h / --help – Show usage instructions
    -d / --debug – Print debug information during execution
    -f / --file <filename> – Specify the filename to save results (default: results.csv or results.json)
    --format <csv/json> – Specify the format for output (default: CSV)


📂 Project Structure
    /pubmed-paper-fetcher
    ├── /src
    │   └── /pubmed_fetcher
    │       ├── __init__.py
    │       ├── main.py          # Main CLI logic
    │       └── utils.py         # Utility functions for API and processing
    ├── /tests
    │   ├── __init__.py
    │   └── test_main.py         # Test cases for main.py
    ├── .gitignore               # Ignore unwanted files
    ├── README.md                # Project documentation
    ├── pyproject.toml           # Poetry dependency and build config
    └── poetry.lock              # Lockfile for dependencies


🧪 Running Tests
    1. To run the test suite:
        poetry run pytest
    2. All test cases are in the tests/test_main.py file.
    3. Run tests with detailed output:
            poetry run pytest -v


🎯 Publishing to PyPI and TestPyPI
    1️⃣ Build the Package:
        poetry build
    2️⃣ Publish to TestPyPI:
        poetry publish --repository testpypi
    3️⃣ Publish to PyPI:
        poetry publish --repository pypi


🔗 API and External Tools Used
    PubMed API – Used to fetch research papers.
    Poetry – Dependency management and packaging.
    PyPI/TestPyPI – Publishing the package.


📝 API Documentation
    🔍 Fetching Paper IDs:
        https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=<query>&retmode=json
    📄 Fetching Paper Details:
        https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=<paper_id>&retmo


📣 Contribution Guidelines
If you'd like to contribute to this project:
    Fork the repository.
        Create a feature branch (git checkout -b feature-name).
        Commit your changes (git commit -m "Add feature").
        Push to your branch (git push origin feature-name).
        Open a pull request.


🤝 Author and Contact
    Author:  Naga Sharanya
    GitHub:  (https://github.com/Naga-Sharanya)
    Email:   kashanagasharanya@gmail.com

