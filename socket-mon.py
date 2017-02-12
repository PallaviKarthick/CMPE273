import collections
import psutil
from itertools import groupby

sconn = collections.namedtuple('sconn', ['fd', 'family', 'type',
'laddr','raddr','status','pid'])



sconn_list=[sconn(fd=16, family=2, type=2, laddr=('0.0.0.0', 0), raddr=(), status='NONE', pid=395),
sconn(fd=122, family=30, type=1, laddr=('2602:306:ce97:c5d0:39ad:d76f:c76:7ba8', 49767), raddr=('2607:f8b0:4007:80a::200e', 443), status='ESTABLISHED', pid=245),
sconn(fd=37, family=2, type=1, laddr=('192.168.1.65', 49170), raddr=('17.172.192.201', 993), status='ESTABLISHED', pid=255),
sconn(fd=16, family=2, type=2, laddr=('10.10.10.10', 0), raddr=('17.172.192.201', 93), status='NONE', pid=395),
sconn(fd=3, family=2, type=2, laddr=('20.20.20.20', 137), raddr=('17.172.192.201', 99), status='NONE', pid=345),
]

sconn_list1 = psutil.net_connections()
# Access the namedtuple as a dict



ls_valid_sconn=[]
for item in sconn_list1:
    if len(item.__dict__['raddr'])!=0:
        ls_valid_sconn.append(item)
print "Total Number of processes that has valid socket connections " , len(ls_valid_sconn) ,"\n"


pid_Groups = groupby(ls_valid_sconn, lambda a: (a.pid))


ls = {}
for pid, group in pid_Groups:
    length = len(list(group))
    ls[pid] = length
ls_No_Of_Conn =  sorted(ls.items(), key = lambda value : value[1] , reverse=True)
# print ls_No_Of_Conn

for pid , count in ls_No_Of_Conn:
    print "PID: %s - Total number of Connections: %s" % (pid, count )

print "\n"
templ = "%-8s %-20s %-25s %-10s \n"
print(templ % ("pid", "laddr", "raddr", "status"))
#print  """"pid","laddr","raddr","status" """

for pid, value in ls_No_Of_Conn:
    for item in ls_valid_sconn:
        if pid == (item.__dict__['pid']):
            print '"%d" , "%s" , "%s" , "%s"' %(item.__dict__['pid'] , item.__dict__['laddr'][0]+"@"+str(item.__dict__['laddr'][1]) ,item.__dict__['raddr'][0]+"@"+str(item.__dict__['raddr'][1]),
            item.__dict__['status'])
    print("\n")
