######Authenticate
To authenticate, you need the 3 or 4 digit number from the prime number url, and your ip.
`curl -u $(curl -s http://averyhardtest.com/421563647 | grep -Po "[0-9]{2,4}(?=:)"):$(curl ipinfo.io/ip) averyhardtest.com:64 -v`
