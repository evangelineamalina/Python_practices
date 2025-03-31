import pandas as pd
import requests

# Replace 'http://example.com/data.csv' with your CSV file URL
url = 'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'

response = requests.get(url)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Read the CSV data into a DataFrame
    df = pd.read_csv(response.content)

    # Specify the local path to save the CSV file
    local_path = 'C:\\Users\\EvangelineJoseph\\Box\\Evan\\local_data.csv'

    # Write the DataFrame to a CSV file
    df.to_csv(local_path, index=False)

    print(f"Data successfully saved to {local_path}")
else:
    print(f"Failed to fetch data: {response.status_code}")
