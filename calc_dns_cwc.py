import os
def main():	
	url = ['one', 'two', 'three']
	ip = ['10.183.0.200', '10.183.0.201', '10.183.0.202']
	print (url)
	print(ip)
	urlstring1 = url[0]+'.ioe'
	urlstring2 = 'www'+url[0]+'.ioe'
	urlstring3 = 'video'+url[0]+'.ioe'
	cmd1 = 'touch '+ urlstring1
	os.system(cmd1)
	echo1 = 'address=/'+urlstring1+'/'+ip[0]
	cmd2 = 'echo "'+echo1+'" >>'+urlstring1
	print(cmd2)
	os.system(cmd2)

main()


#address=/icebowl.ioe/10.183.1.30
#address=/www.icebowl.ioe/10.183.1.30
#address=/ftp.icebowl.ioe/10.183.1.30
#address=/video.icebowl.ioe/10.183.1.30
