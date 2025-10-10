"""
Name: Ariana
Student ID: Your ID
Email: namei@umich.edu
Collaborators: None
AI Tools Used: ChatGPT

Functions Created By: 
- read_csv_file(): Ariana
- calculate_median_sales_by_segment(): Ariana
- calculate_median_sales_by_city(): Ariana
- write_results_to_csv(): Ariana
- test_calculate_median_sales_by_segment(): Ariana
- test_calculate_median_sales_by_city(): Ariana
- main(): Ariana
"""

import csv
import statistics
import unittest


# --------------------------------------------------
# 1. Read CSV File
# --------------------------------------------------
def read_csv_file(filename):
    """
    Reads a CSV file and returns a list of dictionaries.
    Converts the 'Sales' field to float for calculations.
    """
    data = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                row['Sales'] = float(row['Sales'])
            except ValueError:
                row['Sales'] = 0.0
            data.append(row)
    return data


# --------------------------------------------------
# 2. Median Sales by Segment
# --------------------------------------------------
def calculate_median_sales_by_segment(data):
    """
    Groups data by Segment and calculates median sales.
    Returns a dictionary like {'Consumer': 250.0, 'Corporate': 300.5, ...}
    """
    if not data:
        return {}

    segment_sales = {}
    for row in data:
        seg = row.get('Segment')
        sale = row.get('Sales', 0)
        if seg:
            segment_sales.setdefault(seg, []).append(sale)

    return {seg: statistics.median(sales) for seg, sales in segment_sales.items()}


# --------------------------------------------------
# 3. Median Sales by City
# --------------------------------------------------
def calculate_median_sales_by_city(data):
    """
    Groups data by City and calculates median sales.
    Returns a dictionary like {'New York': 320.2, 'Los Angeles': 210.7, ...}
    """
    if not data:
        return {}

    city_sales = {}
    for row in data:
        city = row.get('City')
        sale = row.get('Sales', 0)
        if city:
            city_sales.setdefault(city, []).append(sale)

    return {city: statistics.median(sales) for city, sales in city_sales.items()}


# --------------------------------------------------
# 4. Write Results to CSV File
# --------------------------------------------------
def write_results_to_csv(results_dict, filename, label_name):
    """
    Writes dictionary results to a CSV file.
    Columns: label_name, Median Sales
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([label_name, 'Median Sales'])
        for key, value in results_dict.items():
            writer.writerow([key, round(value, 2)])
    print(f"Results successfully written to {filename}")


# --------------------------------------------------
# 5. Main Program
# --------------------------------------------------
def main():
    filename = "SampleSuperstore.csv"
    data = read_csv_file(filename)

    # Perform both calculations
    median_segment = calculate_median_sales_by_segment(data)
    median_city = calculate_median_sales_by_city(data)

    # Write results
    write_results_to_csv(median_segment, "median_sales_segment.csv", "Segment")
    write_results_to_csv(median_city, "median_sales_city.csv", "City")


# --------------------------------------------------
# 6. Unit Tests
# --------------------------------------------------
class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.sample_data = [
            {"Segment": "Consumer", "City": "New York", "Sales": 100.0},
            {"Segment": "Corporate", "City": "Boston", "Sales": 200.0},
            {"Segment": "Consumer", "City": "New York", "Sales": 300.0},
            {"Segment": "Home Office", "City": "Chicago", "Sales": 400.0},
            {"Segment": "Corporate", "City": "Boston", "Sales": 600.0},
        ]

    # --- Tests for calculate_median_sales_by_segment() ---

    def test_segment_general_case(self):
        result = calculate_median_sales_by_segment(self.sample_data)
        self.assertEqual(result["Consumer"], 200.0)
        self.assertEqual(result["Corporate"], 400.0)

    def test_segment_empty(self):
        result = calculate_median_sales_by_segment([])
        self.assertEqual(result, {})

    def test_segment_one_entry(self):
        data = [{"Segment": "Consumer", "City": "Miami", "Sales": 120.0}]
        result = calculate_median_sales_by_segment(data)
        self.assertEqual(result["Consumer"], 120.0)

    def test_segment_missing_sales(self):
        data = [{"Segment": "Consumer", "City": "Miami"}]  # missing 'Sales'
        result = calculate_median_sales_by_segment(data)
        self.assertEqual(result["Consumer"], 0.0)

    # --- Tests for calculate_median_sales_by_city() ---

    def test_city_general_case(self):
        result = calculate_median_sales_by_city(self.sample_data)
        self.assertEqual(result["Boston"], 400.0)
        self.assertEqual(result["New York"], 200.0)

    def test_city_empty(self):
        result = calculate_median_sales_by_city([])
        self.assertEqual(result, {})

    def test_city_one_entry(self):
        data = [{"Segment": "Corporate", "City": "LA", "Sales": 250.0}]
        result = calculate_median_sales_by_city(data)
        self.assertEqual(result["LA"], 250.0)

    def test_city_missing_sales(self):
        data = [{"Segment": "Corporate", "City": "LA"}]
        result = calculate_median_sales_by_city(data)
        self.assertEqual(result["LA"], 0.0)


# --------------------------------------------------
# 7. Run Program or Tests
# --------------------------------------------------
if __name__ == "__main__":
    # Uncomment ONE of these lines at a time:
    
    # Option 1: Run your main project
    #main()

    # Option 2: Run unit tests
    #unittest.main()

