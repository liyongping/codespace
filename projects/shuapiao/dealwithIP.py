#!/usr/bin/env python 
#-*- coding: utf-8 -*- 

proxylist = open('proxy3.txt', 'r').readlines();

print len(proxylist)
results = []
for proxy in proxylist:
    newproxy =  proxy[:proxy.find('@')]
    #print newproxy
    if len(newproxy) > 8:
        results.append(newproxy)
print len(results)

results = list(set(results))
for x in results:
    print x