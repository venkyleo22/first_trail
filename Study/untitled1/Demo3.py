iplist=['209.85.238.4','216.23.51.98','64.233.173.198','64.3.17.208','64.233.173.238']

tmp=[tuple(map(int,ip.split("."))) for ip in iplist]
tmp.sort(reversed=False)
#print tmp
iplist=[".".join(map(str,add)) for add in tmp]
print(iplist)