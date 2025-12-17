import requests

# Get URL from user
url = input("Enter a URL to scan (e.g., https://example.com): ")


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
print(f"Status: {response.status_code}\n")

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


# Cookie security checking
security_cookies = {
    "Secure": "Prevents stealing over unencrypted connections",
    "HttpOnly": "Prevents XSS attacks from stealing session cookies",
    "SameSite": "Prevents CSRF attacks",
}

print("\n🍪 Checking Cookies...\n")

# Check if any cookies were set
if len(response.cookies) == 0:
    print("No cookies set in response.")
else:
    print(f"Found {len(response.cookies)} cookie(s)\n")

    # Loop through each cookie
    for cookie in response.cookies:
        print(f"Cookie: {cookie.name}")

        # Check Secure flag
        if cookie.secure:
            print("  ✅ Secure: True")
        else:
            print("  ❌ Secure: False (Risk: Can be stolen over HTTP)")

        # Check HttpOnly flag
        if cookie.has_nonstandard_attr('HttpOnly'):
            print("  ✅ HttpOnly: True")
        else:
            print("  ❌ HttpOnly: False (Risk: JavaScript can access it)")

        # Check SameSite flag
        samesite = cookie.get_nonstandard_attr('SameSite')
        if samesite != 'None':
            print(f"  ✅ SameSite: {samesite}")
        elif samesite == 'None':
            print(f"  ⚠️ SameSite: None (Least secure, requires Secure flag)")
        else:
            print("  ❌ SameSite: Not set (Risk: CSRF attacks)")
        print()