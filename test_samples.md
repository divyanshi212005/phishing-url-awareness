# Test Results

## Test 1
URL: https://www.example.com/login

Expected: No listed warning signs.
Actual: No listed warning signs were detected.
Result: PASS

## Test 2
URL: http://192.0.2.10/account

Expected: IPv4 address and plain HTTP warnings.
Actual: Hostname is an IPv4 address; Uses plain HTTP instead of HTTPS.
Result: PASS

## Test 3
URL: http://example.com@sample.invalid/login

Expected: @ symbol and plain HTTP warnings.
Actual: Contains '@' symbol; Uses plain HTTP instead of HTTPS.
Result: PASS

## Test 4
URL: https://a.b.c.d.e.example.invalid/path

Expected: Many hostname segments warning.
Actual: Hostname has many segments.
Result: PASS

## Test 5
URL: https://xn--example.invalid/

Expected: Punycode marker warning.
Actual: Hostname contains punycode marker 'xn--'.
Result: PASS