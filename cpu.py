import json

# Assuming the JSON data is stored in a variable called 'json_data'

# Parse the JSON data
with open("./parts/cpu.json") as file:
    # Load the JSON data
    data = json.load(file)

# Extract the last 10 CPU details
cpu_list = data["cpu"][-10:]

# Extract the required details for each CPU
for cpu in cpu_list:
    brand = cpu["brand"]
    model = cpu["model"]
    clock_speed = cpu["base_clock"]["cycles"]
    price = cpu["price"]["amount"]

    print(f"Brand: {brand}, Model: {model}, Clock Speed: {clock_speed}, Price: {price}")
