import requests

# Get URL from user
url = input("Enter a URL to scan (e.g., https://example.com): ")

# Make the request
response = requests.get(url)

# Print the headers
print("\n--- Headers found ---")
for header, value in response.headers.items():
    print(f"{header}: {value}")