import re
from urllib.parse import urlparse

def inspect_url(raw_url):
    """check visible URL text for selected warning sign."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]


    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
    except ValueError:
        return ["This text is not a valid URL format."]

    host = (parsed.hostname or "").lower()

    if not host:
      return ["Could not identify a hostname."]

    # 1.check @#$% symbol
    if "@" in candidate:
       findings.append("Contains an @ symbol;inspect carefully.")

    # 2. check very long URL
    if len(url) > 100:
       findings.append("Unusually long url ( over 100 characters).")

    # 3. check IP  Address
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}",host):
       findings.append("Uses an IP address instead of a familiar domain.")

    # 4.check multiple subdomains
    labels = [part for part in host.split(".") if part]
    if len(labels) >=5:
       findings.append("Contains many hostname segments/subdomains.")

    # 5. check punycode (xn--)
    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    # 6. check  HTTP / HTTPS

    if parsed.scheme.lower() == "http":
         findings.append("Uses HTTP. HTTPS alone does not prove trust.")


    if not findings:
          findings.append("No listed warning signs found. This does not prove safety. ")

    return findings

def main():
     print("EWB Phishing URL Awareness Checker")
     print("Text checks only- this program does not open URLs.")

     while True:
         raw_url = input("\nEnter a sample URL (OR type q to quit):")

         if raw_url.strip().lower() in ("q", "quit", "exit"):
             print("Goodbye! Stay alert online.")
             break

         print("\nResult:")
         for item in inspect_url(raw_url):
            print("- " + item)
         print("\n Never enter passwords from unexpected links.")
if __name__ == "__main__":
    main()














