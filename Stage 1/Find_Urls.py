import httplib

urls = ["", "disclaimer", "news", "contributors","users"]

data = ""

for u in urls:
	conn = httplib.HTTPConnection("averyhardtest.com")
	conn.request("GET", "/"+u)
	r1 = conn.getresponse()
	data += r1.read()
	conn.close()


words = [""]
for c in data:
	if c == ' ':
		if words[len(words)-1] != "":
			words.append("")
	else:
		words[len(words)-1] += c
		
for x in range(0,len(words)):
	acceptable=True
	for c in words[x]:
		if c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
			acceptable=False
	if acceptable:
		conn = httplib.HTTPConnection("averyhardtest.com")
		conn.request("GET", "/"+words[x])
		r2 = conn.getresponse()
		if r2.status != 404:
			print(words[x] + ': ' + str(r2.status))
		conn.close()
print("Done")
