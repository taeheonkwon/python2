def das(file_names):
	try:
		with open(file_names,'r',encoding='cp949') as f:
			data_lines = f.readlines()
	except Exception as e:
		print(e)
	data_lines[0] = 'id,site,date,temperature,precipitation,ws,wd,hm,pressure'
	datas = []
	fn = file_names+'.replaced'
	with open(fn,'w') as f:
		for item in data_lines:
			line = item.replace('서울', 'seoul').replace('\n','')
			datas.append(line)
			f.write(line+'\n')	
	return(datas)
