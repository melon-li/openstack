for i in api cert compute novncproxy scheduler consoleauth  conductor;do service openstack-nova-$i restart ;done
