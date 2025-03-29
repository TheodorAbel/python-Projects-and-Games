import json
import os
import pytest
from project import load_expenses, save_expenses

# Test file to avoid modifying the real JSON file
TEST_FILE = "test_expenses.json"

@pytest.fixture
def sample_data():
    """Sample expense data for testing."""
    return [
        {"category": "Food", "amount": 10.5, "description": "Lunch"},
        {"category": "Transport", "amount": 5.0, "description": "Bus fare"},
    ]

@pytest.fixture
def setup_test_file(sample_data):
    """Setup a test JSON file with sample data."""
    with open(TEST_FILE, "w") as file:
        json.dump(sample_data, file, indent=4)
    yield
    os.remove(TEST_FILE)  # Cleanup after test

def test_load_expenses(setup_test_file):
    """Test loading expenses from file."""
    expenses = load_expenses()
    assert isinstance(expenses, list)
    assert len(expenses) == 2
    assert expenses[0]["category"] == "Food"
    assert expenses[1]["amount"] == 5.0

def test_save_expenses(sample_data):
    """Test saving expenses to file."""
    save_expenses(sample_data)
    with open("expenses.json", "r") as file:
        data = json.load(file)
    assert len(data) == 2
    assert data[0]["description"] == "Lunch"

if __name__ == "__main__":
    pytest.main()
