# Web Security Scanner

A Python CLI tool that analyzes websites for common security misconfigurations including missing security headers and insecure cookie attributes.

##  What It Does

This scanner checks websites for:
- **Security Headers**: Identifies missing headers that protect against XSS, clickjacking, and protocol downgrade attacks
- **Cookie Security**: Validates that cookies have proper security flags (Secure, HttpOnly, SameSite)
- **Security Grading**: Provides an instant security score (A+ to F) based on findings

## Features

- Checks 4 critical security headers recommended by OWASP
- Analyzes cookie security attributes
- Clear visual output with ✅/❌ indicators
- Security grading system
- Error handling for invalid URLs
- Fast scanning (5 second timeout)

## Prerequisites

- Python 3.7 or higher
- `requests` library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Rayane-Ts/web-security-scanner.git
cd web-security-scanner
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the scanner:
```bash
python scanner.py
```

Enter a URL when prompted:
```
Enter a URL to scan (e.g., https://example.com): https://github.com
```

### Example Output

```
🔍 Scanning https://github.com for security headers...

Status: 200

Content-Security-Policy: FOUND ✅
  Value: default-src 'none'; ...

X-Frame-Options: FOUND ✅
  Value: deny

Strict-Transport-Security: FOUND ✅
  Value: max-age=31536000

X-Content-Type-Options: FOUND ✅
  Value: nosniff

📊 Summary: 0/4 security headers are missing
🛡️ Grade: A+ (Excellent security)

🍪 Checking Cookies...

Found 2 cookie(s)

Cookie: _gh_sess
  ✅ Secure: True
  ✅ HttpOnly: True
  ✅ SameSite: Lax
```

## What Gets Checked

### Security Headers

| Header | Purpose |
|--------|---------|
| Content-Security-Policy | Protects against XSS attacks |
| X-Frame-Options | Protects against clickjacking |
| Strict-Transport-Security | Forces HTTPS connections |
| X-Content-Type-Options | Prevents MIME-sniffing attacks |

### Cookie Security Flags

| Flag | Purpose |
|------|---------|
| Secure | Ensures cookies only sent over HTTPS |
| HttpOnly | Prevents JavaScript access to cookies |
| SameSite | Protects against CSRF attacks |

## 📊 Grading System

- **A+**: All security headers present
- **B**: 1 header missing (minor gaps)
- **C**: 2 headers missing (moderate risk)
- **F**: 3+ headers missing (significant gaps)

##  Technical Details

Built with:
- Python 3
- `requests` library for HTTP requests
- Standard library modules (`sys`, error handling)

## What I Learned

Through building this project, I learned:
- HTTP request/response cycle and headers
- Common web security vulnerabilities (XSS, CSRF, clickjacking)
- Cookie security best practices
- Python error handling and user input validation
- Git version control and GitHub workflow

##  Use Cases

- **Learning**: Understand web security fundamentals
- **Security Audits**: Quick security posture check for websites
- **Development**: Verify security headers during development
- **Resume/Portfolio**: Demonstrates security knowledge and Python skills

##  Limitations

- Only checks initial response (doesn't follow redirects)
- Cannot scan authenticated pages
- Basic checks only (not a comprehensive security audit)
- Some sites may block automated requests

## Future Enhancements

Potential features to add:
- [ ] Scan multiple URLs from a file
- [ ] Export results to JSON/CSV
- [ ] Check for additional security headers
- [ ] HTTPS certificate validation
- [ ] Colored terminal output
- [ ] Command-line arguments support

## License

MIT License - feel free to use and modify

## Author

**Rayane-Ts**
- GitHub: [@Rayane-Ts](https://github.com/Rayane-Ts)

##  Acknowledgments

- OWASP Secure Headers Project for security header guidelines
- Built as a learning project to understand web security fundamentals

---

*This tool is for educational and ethical security testing purposes only. Always obtain permission before scanning websites you don't own.*