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


def read_csv_file(filename):
    
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



def calculate_median_sales_by_segment(data):
   
    if not data:
        return {}

    segment_sales = {}
    for row in data:
        seg = row.get('Segment')
        subcat = row.get('Sub-Category')
        sale = row.get('Sales', 0)
        if seg and subcat:
            key = (seg, subcat)
            segment_sales.setdefault(key, []).append(sale)

    return {key: statistics.median(sales) for key, sales in segment_sales.items()}



def calculate_median_sales_by_city(data):
   
    if not data:
        return {}

    city_sales = {}
    for row in data:
        city = row.get('City')
        subcat = row.get('Sub-Category')
        sale = row.get('Sales', 0)
        if city and subcat:
            key = (city, subcat)
            city_sales.setdefault(key, []).append(sale)

    return {key: statistics.median(sales) for key, sales in city_sales.items()}



def write_results_to_csv(results_dict, filename, label1, label2):
   
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([label1, label2, 'Median Sales'])
        for (val1, val2), median in results_dict.items():
            writer.writerow([val1, val2, round(median, 2)])
    print(f"Results successfully written to {filename}")



def main():
    filename = "SampleSuperstore.csv"
    data = read_csv_file(filename)

  
    median_segment = calculate_median_sales_by_segment(data)
    median_city = calculate_median_sales_by_city(data)

  
    write_results_to_csv(median_segment, "median_sales_segment_subcat.csv", "Segment", "Sub-Category")
    write_results_to_csv(median_city, "median_sales_city_subcat.csv", "City", "Sub-Category")



class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.sample_data = [
            {"Segment": "Consumer", "City": "New York", "Sub-Category": "Phones", "Sales": 100.0},
            {"Segment": "Corporate", "City": "Boston", "Sub-Category": "Binders", "Sales": 200.0},
            {"Segment": "Consumer", "City": "New York", "Sub-Category": "Phones", "Sales": 300.0},
            {"Segment": "Home Office", "City": "Chicago", "Sub-Category": "Chairs", "Sales": 400.0},
            {"Segment": "Corporate", "City": "Boston", "Sub-Category": "Binders", "Sales": 600.0},
        ]



    def test_segment_general_case(self):
        result = calculate_median_sales_by_segment(self.sample_data)
        self.assertEqual(result[("Consumer", "Phones")], 200.0)
        self.assertEqual(result[("Corporate", "Binders")], 400.0)

    def test_segment_empty(self):
        result = calculate_median_sales_by_segment([])
        self.assertEqual(result, {})

    def test_segment_one_entry(self):
        data = [{"Segment": "Consumer", "City": "Miami", "Sub-Category": "Tables", "Sales": 120.0}]
        result = calculate_median_sales_by_segment(data)
        self.assertEqual(result[("Consumer", "Tables")], 120.0)

    def test_segment_missing_subcat(self):
        data = [{"Segment": "Consumer", "City": "Miami", "Sales": 150.0}]
        result = calculate_median_sales_by_segment(data)
        self.assertEqual(result, {})  

    

    def test_city_general_case(self):
        result = calculate_median_sales_by_city(self.sample_data)
        self.assertEqual(result[("Boston", "Binders")], 400.0)
        self.assertEqual(result[("New York", "Phones")], 200.0)

    def test_city_empty(self):
        result = calculate_median_sales_by_city([])
        self.assertEqual(result, {})

    def test_city_one_entry(self):
        data = [{"Segment": "Corporate", "City": "LA", "Sub-Category": "Tables", "Sales": 250.0}]
        result = calculate_median_sales_by_city(data)
        self.assertEqual(result[("LA", "Tables")], 250.0)

    def test_city_missing_subcat(self):
        data = [{"Segment": "Corporate", "City": "LA", "Sales": 250.0}]
        result = calculate_median_sales_by_city(data)
        self.assertEqual(result, {})  



if __name__ == "__main__":
    # Uncomment ONE of these lines at a time:

    # Option 1: Run your main project
    main()

    # Option 2: Run unit tests
    #unittest.main()
