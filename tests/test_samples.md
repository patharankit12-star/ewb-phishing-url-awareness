# Test Results
Python version used: 3.10  | Operating system: Windows 11  | Date: 28-Oct-2026

| # | Input | Expected result | Actual result                          | Pass/Fail |
|---|---|---|----------------------------------------|---|
| 1 | https://www.example.com/login | No listed warning signs | Never enter passwords from unexpected links. | PASS |
| 2 | http://192.0.2.10/account | IP address + HTTP | 1. Uses an IP address instead of a familiar domain.2. Uses HTTP. HTTPS alone does not prove trust. | PASS |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | 1. Contains an @ symbol;inspect carefully.2. Uses HTTP. HTTPS alone does not prove trust. | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | 1. Contains many hostname segments/subdomains. | PASS |
| 5 | https://xn--example.invalid/ | Punycode-style hostname | 1. Contains a punycode-style hostname. | PASS |

## Notes
"From this project, I learned that HTTP or HTTPS only indicates the connection type, not the safety of the website. A URL with zero warning signs can still be a dangerous phishing link. Also, having an IP address or an @ symbol in the URL is highly suspicious."