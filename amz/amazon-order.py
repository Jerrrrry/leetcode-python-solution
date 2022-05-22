# Amazon is trying to optimize its warehouse inventory for 2-hour delivery items. 
# As part of that effort you are given a real-time stream of individual items ordered
# through Amazon.  Each entry in the stream includes a single item SKU, number
# of those items in the individual order, and a timestamp.
# Write a program, that will store the stream data. This program can also be
# queried, separately, at any time, to return the SKUs for all the items ordered in
# the last 6 hours as well as the combined, overall volume for each item.
#
# Example data:
# (“ITEM_1”, 5, 1620311721066)
# (“ITEM_2”, 2, 1620311782011)
# (“ITEM_3”, 12, 1620311822562)
# (“ITEM_1”, 14, 1620311851135)
# (“ITEM_4”, 15, 1620311893213)
# (“ITEM_2”, 10, 1620311926421)
# (“ITEM_3”, 6, 1620311979012)
# 
# Output - [(“ITEM_1”, 19), (“ITEM_2”, 12), (“ITEM_3”, 18), (“ITEM_4”, 15)]

#6 hours mean ts-3600
from datetime import datetime
def compare(t1,t2):
        r1=datetime.fromtimestamp(t1)
        print(r1)
        r2=datetime.fromtimestamp(t2)
        d=r1-r2
        ds=d.total_seconds()
        minutes=int(divmod(ds,60)[0])
        print(minutes)

compare(1620311721066,1620311721066)