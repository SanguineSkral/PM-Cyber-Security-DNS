import os
def main():	
	url = ['williamp', 'bravo',   'Micahb345' ,'bipolar2','cynthia',
		   'keegy',    'spider',  'amospia',   'komodo',  'h27',
		   'shew',     'croisant','pmoscar',   'papa15',  'bryan', 'p51']
	ip = ['10.183.2.1',  '10.183.2.2',  '10.183.2.3',   '10.183.2.4',  '10.183.2.5',
		  '10.183.2.6',  '10.183.2.8',  '10.183.2.9',  '10.183.2.10', '10.183.2.12',
		  '10.183.2.13', '10.183.2.14', '10.183.2.15', '10.183.2.16', '10.183.2.20', '10.183.2.11']
	print (url)
	print(ip)
	length=len(url);
	for i in range(length):
		urlstring1 = url[i]+'.ioe'
		urlstring2 = 'www.'+url[i]+'.ioe'
		urlstring3 = 'video.'+url[i]+'.ioe'
		cmd1 = 'touch '+ urlstring1
		os.system(cmd1)
		echo1 = 'address=/'+urlstring1+'/'+ip[i]
		cmd2 = 'echo "'+echo1+'" >>'+urlstring1
		echo2 = 'address=/'+urlstring2+'/'+ip[i]
		cmd3 = 'echo "'+echo2+'" >>'+urlstring1
		echo3 = 'address=/'+urlstring3+'/'+ip[i]
		cmd4 = 'echo "'+echo3+'" >>'+urlstring1
		print(cmd2)
		os.system(cmd2)
		print(cmd3)
		os.system(cmd3)
		print(cmd4)
		os.system(cmd4)

main()


#address=/icebowl.ioe/10.183.1.30
#address=/www.icebowl.ioe/10.183.1.30
#address=/ftp.icebowl.ioe/10.183.1.30
#address=/video.icebowl.ioe/10.183.1.30
