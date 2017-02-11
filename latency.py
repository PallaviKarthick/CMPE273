import subprocess

regDict = {"23.23.255.255":"us-east-1" , "50.18.56.1" :"us-west-1"  , "34.248.60.213": "eu-west-1" , "35.160.63.253":"us-west-2" , "35.156.63.252" : "eu-central-1",
"52.222.9.163":"us-gov-west-1" , "52.56.34.0":"eu-west-2" , "13.112.63.251":"ap-northeast-1" , "52.78.63.252":"ap-northeast-2" , "46.51.216.14":"ap-southeast-1",
"13.54.63.252":"ap-southeast-2" , "35.154.63.252":"ap-south-1" , "52.67.255.254":"sa-east-1" , "52.14.64.0":"us-east-2" , "52.60.50.0":"ca-central-1"}


latencyDict={}
count=1
for host, region in regDict.items():
	ping = subprocess.Popen(
	    ["ping", "-c", "3", host],
	    stdout = subprocess.PIPE,
	    stderr = subprocess.PIPE
	)

	out, error = ping.communicate()
	#print(out)
	lines = out.splitlines()
	line = lines[len(lines)-1]
	#print (host ," ****" ,line)
	words = str(line).split('/')
	avgTime = words[4]
	avgTime= float(avgTime)
	latencyDict[host] = avgTime
	
#print(latencyDict)
sortedLatencyDict = sorted(latencyDict, key=lambda x: latencyDict[x])

for host in sortedLatencyDict:
    #print(host, latencyDict[host])
    print(count, "." , regDict[host] , '['+host+']  -' , latencyDict[host] , "ms")
    count=count+1
    

	
		
		
	