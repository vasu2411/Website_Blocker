import time
from datetime import datetime as dt

#path of hosts file
hosts_path="C:\\Windows\\System32\\drivers\\etc\\hosts"

#redirection path
redirect="127.0.0.1"

#list of websites to be blocked
websites=["www.youtube.com","youtube.com","www.instagram.com","instagram.com"]

#working hours
time_from = dt(dt.now().year,dt.now().month,dt.now().day,1)
time_to = dt(dt.now().year,dt.now().month,dt.now().day,18)

while True:
    #if working hours append lines to hosts file or check for lines exist or not
    if time_from < dt.now() < time_to:
        print("working hours...")
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    #if not working hours then remove lines from the hosts file
    else:
        print("Fun hours...")
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
    #sleep for 5 seconds
    time.sleep(5)