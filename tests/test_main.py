import pytest
import sys
import os

# Add src to sys.path so pytest can recognize it
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from pubmed_fetcher.main import fetch_pubmed_data


def test_fetch_pubmed_data():
    """Test to check fetching data from PubMed API."""
    query = "cancer"
    result = fetch_pubmed_data(query)
    assert isinstance(result, list)
    assert len(result) > 0
