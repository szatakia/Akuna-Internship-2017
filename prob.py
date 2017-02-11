def prob(ms, sw):
	n = len(ms)
	while True:
		nm = []
		for i in range(0, n):
			a = 0
			
			for j in range(0, n):
				a += sw[j][i]*ms[j]
				#v += sw[j][i]*ms[j]
			nm.append(a)
		if nm == ms:
			break
		ms = nm
	for item in ms:
		print round(item, 3),



