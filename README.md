# Phishing URL Awareness Checker

## Overview

This project is a beginner-friendly Python tool that checks a URL for selected warning signs commonly associated with suspicious links.

The tool only analyzes the URL text entered by the user. It does not open or visit the website.

## Features

The checker looks for:

- `@` symbol in the URL
- Unusually long URLs
- IPv4 address used as hostname
- Many hostname segments
- Punycode marker `xn--`
- Plain HTTP instead of HTTPS

It also includes:

- A quit option
- Short explanations for warning signs
- Safe sample testing

## Requirements

- Python 3.10 or newer
- No external Python packages are required

## How to Run

Open the project folder in VS Code and run:

```text
python phishing-checker.py