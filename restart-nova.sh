
for i in api cert novncproxy scheduler consoleauth  conductor
do 
	service nova-$i  $1
done
