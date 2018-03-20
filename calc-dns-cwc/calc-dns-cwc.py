import os
def main():	
	url = ['one', 'two', 'three']
	ip = ['10.183.0.101', '10.183.0.102', '10.183.0.103']
	print (url)
	print(ip)
	for i in  range (0, 3):
		urlstring1 = url[i]+'.ioe'
		urlstring2 = 'www.'+url[i]+'.ioe'
		urlstring3 = 'video.'+url[i]+'.ioe'
		cmd0 = 'touch '+ urlstring1
		os.system(cmd0)
		echo1 = 'address=/'+urlstring1+'/'+ip[i]
		echo2 = 'address=/'+urlstring2+'/'+ip[i]
		echo3 = 'address=/'+urlstring3+'/'+ip[i]
		cmd1 = 'echo "'+echo1+'" >>'+urlstring1
		cmd2 = 'echo "'+echo2+'" >>'+urlstring1
		cmd3 = 'echo "'+echo3+'" >>'+urlstring1
		print(cmd1)
		print(cmd2)
		print(cmd3)
		os.system(cmd1)
		os.system(cmd2)
		os.system(cmd3)

main()


#address=/icebowl.ioe/10.183.1.30
#address=/www.icebowl.ioe/10.183.1.30
#address=/ftp.icebowl.ioe/10.183.1.30
#address=/video.icebowl.ioe/10.183.1.30
