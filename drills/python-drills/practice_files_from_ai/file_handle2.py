notes_path = "C:/dev-lab/drills/python-drills/practice_files_from_ai/notes.txt"
sales_path = "C:/dev-lab/drills/python-drills/practice_files_from_ai/sales.txt"


with open(notes_path, "r") as f:
    notes_content = f.readlines()

    non_empty_line_count = sum(1 for line in notes_content if line.strip())

    # print(f"Number of non-empty lines: {non_empty_line_count}")
    

with open(sales_path, "r") as f:
    sales_content = f.readlines()

    sales_list = []

    for line in sales_content:
        try:
            line = float(line)
       
            sales_list.append(line)
        except ValueError:
            print("Skipping value: could not convert to number")    
try:
    total = sum(line for line in sales_list)
    maximum = max(sales_list)
    average = total / len(sales_list)
except:
    print("Something went wrong with the conversion")


summary_path = "C:/dev-lab/drills/python-drills/practice_files_from_ai/summary.txt"
with open(summary_path, "w") as f:
    f.write(f"Total is: {total}" + "\n") 
    f.write(f"maximum sale is: {maximum}" + "\n") 
    f.write(f"Average is: {average}" + "\n") 
    print()
        
    # print(f"The file at {summary_path} was created!")

import csv
people_path = "C:/dev-lab/drills/python-drills/practice_files_from_ai/people.csv"

with open(people_path, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    people_over_30_list = []

    for row in csv_reader:
        if int(row['age']) >= 30:
            print(row['name'])
            people_over_30_list.append(row)

# csv DictWriter for people over 30
people_over_30_path = "C:/dev-lab/drills/python-drills/practice_files_from_ai/people_over_30.csv"

with open(people_over_30_path, 'w') as f:
    csv_writer = csv.DictWriter(f, fieldnames=['name', 'age', 'city'])
    csv_writer.writeheader()

    for row in people_over_30_list:
        csv_writer.writerow(row)
    
    # print(f"csv path '{people_over_30_path}' created successfully!")

# Computing total spend per customer in orders.csv
orders_path = "C:/dev-lab/drills/python-drills/practice_files_from_ai/orders.csv"

with open(orders_path, 'r') as f:
    csv_reader = csv.DictReader(f)
    Ben_amount = []
    Chloe_amount = []
    Amina_amount = []

    for row in csv_reader:
        if row['customer'] == "Ben":
            Ben_amount.append(float(row['amount']))
        elif row['customer'] == "Chloe":
            Chloe_amount.append(float(row['amount']))
        elif row['customer'] == "Amina":
            Amina_amount.append(float(row['amount']))
    
    Ben_total = sum(Ben_amount)
    Chloe_total = sum(Chloe_amount)
    Amina_total = sum(Amina_amount)

    totals = [Ben_total, Chloe_total, Amina_total]

# Totals for each customer
customer_totals_path = "C:/dev-lab/drills/python-drills/practice_files_from_ai/customer_totals.csv"

with open(customer_totals_path, 'w') as f:

    arranged_dict = [
        {'customer': 'Ben', 'total': Ben_total},
        {'customer': 'Chloe', 'total': Chloe_total},
        {'customer': 'Amina', 'total': Amina_total}
    ]

    csv_writer = csv.DictWriter(f, fieldnames=['customer', 'total'])
    csv_writer.writeheader()

    for row in arranged_dict:
        csv_writer.writerow(row)

    # print(f"csv file at '{customer_totals_path}' was created!")


# Print names of products in stock
import json
products_path = "C:\dev-lab\drills\python-drills\practice_files_from_ai\products.json"

try:
    with open(products_path, "r") as f:
        content = json.load(f)
        
        for product in content:
            if product["in_stock"] == True:
                print(product)
except FileNotFoundError:
    print("Sorry, the file couldn't be found!")    


# Creating a products.json which is simplified.
simple_products_path = "C:\dev-lab\drills\python-drills\practice_files_from_ai\products_simple.json"
with open(simple_products_path, 'w') as f:

    products_path = "C:\dev-lab\drills\python-drills\practice_files_from_ai\products.json"
    with open(products_path, 'r') as f_read:
        content = json.load(f_read)
        simple_data = []
        for product in content:
            simple_data.append({"id" : product["id"], "name": product["name"]})

    json.dump(simple_data, f, indent=4)
    print(f"Successfully created simplified file at '{simple_products_path}'.")


# Making people csv a json file
people_json ="C:\dev-lab\drills\python-drills\practice_files_from_ai\people.json"
with open(people_json, "w") as json_file:
    
    people_path = "C:/dev-lab/drills/python-drills/practice_files_from_ai/people.csv"
    with open(people_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        data_from_csv = list(csv_reader)
        for person in csv_reader:
            data_from_csv.append(person)

    json.dump(data_from_csv, json_file, indent=4)

    print(f"people content succesfully written to '{people_json}'.")


# Cleaning the feedback.txt of extra spaces and empty lines
feedback_path = "C:/dev-lab/drills/python-drills/practice_files_from_ai/feedback.txt"
clean_feedback_path = "C:/dev-lab/drills/python-drills/practice_files_from_ai/clean_feedback.txt"

with open(clean_feedback_path, 'w') as f:
    with open(feedback_path, 'r') as f_read:
        content = f_read.readlines()
        clean_data = []
        for line in content:
            line = line.strip()
            if line.strip():
                clean_data.append(line)
    
    f.writelines(line + "\n" for line in clean_data)
    print(f"The feedback file at '{clean_feedback_path}' was created.")
