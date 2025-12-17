import requests

# Get URL from user
url = input("Enter a URL to scan (e.g., https://example.com): ")


"""# Set headers so the request don't seem as a script 
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "fr-FR,fr;q=0.9",
    "Accept-Encoding": "gzip, deflate"
}
"""

# Define the security headers we're checking for
security_headers = {
    "Content-Security-Policy": "Protects against XSS attacks",
    "X-Frame-Options": "Protects against clickjacking",
    "Strict-Transport-Security": "Forces HTTPS connections",
    "X-Content-Type-Options": "Prevents MIME-sniffing attacks"
}

# Make the request
try:
    response = requests.get(url=url, timeout=5)
except requests.exceptions.RequestException as e:
    print(f"Error: Could not connect to {url}")
    print(f"Details: {e}")
    exit()


print(f"\n🔍 Scanning {url} for security headers...\n")

# Check each security header
for header, description in security_headers.items():
    if header in response.headers:
        print(f"{header}: FOUND ✅")
        print(f"  Value: {response.headers[header]}")
    else:
        print(f"{header}: MISSING! ❌")
        print(f"  Risk: {description}")
    print()

# Summary
missing_count = sum(1 for h in security_headers if h not in response.headers)
print(f"\n📊 Summary: {missing_count}/{len(security_headers)} security headers are missing")

# A security summary
if missing_count == 0:
    print("🛡️ Grade: A+ (Excellent security)")
elif missing_count == 1:
    print("Grade: B (Good security, minor gaps)")
elif missing_count == 2:
    print("Grade: C (Moderate security risks)")
else:
    print("❗Grade: F (Significant security gaps)")