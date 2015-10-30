######Authenticate
To authenticate, you need the 3 or 4 digit number from the prime number url, and your ip.
`curl -u $(curl averyhardtest.com/421563647 | grep -Eo \[0-9\]\{3,4\}):$(curl ipinfo.io/ip) averyhardtest.com:64 -v`
