#!/bin/env python
#coding=utf-8
import os
origin_names = "openstack-ceilometer-alarm-evaluator.service openstack-ceilometer-alarm-notifier.service openstack-ceilometer-api.service openstack-ceilometer-central.service openstack-ceilometer-collector.service openstack-ceilometer-notification.service openstack-glance-api.service openstack-glance-registry.service openstack-glance-scrubber.service openstack-keystone.service openstack-nova-api.service openstack-nova-cert.service openstack-nova-compute.service openstack-nova-conductor.service openstack-nova-consoleauth.service openstack-nova-console.service openstack-nova-metadata-api.service openstack-nova-novncproxy.service openstack-nova-scheduler.service openstack-nova-xvpvncproxy.service"

names_l = [elem for elem in origin_names.split(" ") if elem]
for name in names_l:
	if(name.find("openstack") >= 0):
		pos = name.find("-")
		rename = name[pos+1:]
		cmd = 'mv ' + name + " " + rename
		print cmd
		os.system(cmd)
