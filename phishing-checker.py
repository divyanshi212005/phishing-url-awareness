
import re
from urllib.parse import urlparse


EXPLANATIONS = {
    "@": "The @ symbol can hide the real destination of a URL.",
    "length": "Very long URLs can be used to hide suspicious parts.",
    "ip": "An IP address is being used instead of a normal domain name.",
    "segments": "Many hostname segments can make a URL harder to recognize.",
    "punycode": "Punycode can represent international characters in a domain name.",
    "http": "HTTP does not provide the encryption normally provided by HTTPS.",
}


def inspect_url(raw_url):
    raw_url = raw_url.strip()

    if not raw_url:
        return ["No URL entered."]

    if "://" not in raw_url:
        raw_url = "http://" + raw_url

    try:
        parsed = urlparse(raw_url)
    except ValueError:
        return ["Could not parse this URL."]

    hostname = parsed.hostname or ""
    warnings = []

    if "@" in raw_url:
        warnings.append(("Contains '@' symbol.", EXPLANATIONS["@"]))

    if len(raw_url) > 100:
        warnings.append(
            ("URL is unusually long (>100 characters).", EXPLANATIONS["length"])
        )

    if re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", hostname):
        warnings.append(("Hostname is an IPv4 address.", EXPLANATIONS["ip"]))

    if len(hostname.split(".")) >= 5:
        warnings.append(("Hostname has many segments.", EXPLANATIONS["segments"]))

    if "xn--" in hostname.lower():
        warnings.append(
            ("Hostname contains punycode marker 'xn--'.", EXPLANATIONS["punycode"])
        )

    if parsed.scheme.lower() == "http":
        warnings.append(
            ("Uses plain HTTP instead of HTTPS.", EXPLANATIONS["http"])
        )

    return warnings


def main():
    print("Phishing URL Awareness Checker")
    print("--------------------------------")

    while True:
        user_url = input("\nEnter a URL to inspect (or type 'quit'): ").strip()

        if user_url.lower() == "quit":
            print("Goodbye!")
            break

        warnings = inspect_url(user_url)

        if not warnings:
            print("\nNo listed warning signs were detected.")
        else:
            print("\nWarning signs:")
            for warning, explanation in warnings:
                print("- " + warning)
                print("  Explanation: " + explanation)

        print("\nReview links carefully. This tool does not prove a URL is safe.")


if __name__ == "__main__":
    main()