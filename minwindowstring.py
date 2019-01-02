s = 'a'
t = 'aa'

min_s = s
tr = {k:0 for k in t}
for v in t:
	tr[v] -= 1
i = -1 #tale
e = -1 #head
n = len(s) #limit
found = False
while i < n - 1:
	status = all([x >= 0 for x in tr.values()])
	if not status and e >= (n - 1):
	    w = s[i:e+1]
	    if len(w) < len(min_s):
		min_s = w
	    break
	if not status and e < n - 1:
	    e += 1
	    if s[e] in tr.keys():
		tr[s[e]] += 1
	if status:
		found = True
		if len(w) < len(min_s):
			min_s = w
		i += 1
		if s[i] in tr.keys():
			tr[s[i]] -= 1
	w = s[i+1:e+1]

if not found:
	print('')
else:
	print(min_s)
