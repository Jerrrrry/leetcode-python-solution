from tmp import data
from datetime import datetime
import collections
class Solution:
        def test(self):
                print(data)

        def count(self):
                res=collections.defaultdict()
                ag=collections.defaultdict(int)
                cc=collections.defaultdict(int)
                ach=collections.defaultdict(int)
                for x in data:
                        t=datetime.fromtimestamp(x['timestamp']).strftime('%m/%d/%Y')
                        if x['user_id'] not in res:
                                res[x['user_id']]={}
                        if x['type']=='buy':
                                s=1
                        else:
                                s=-1
                        if t not in res[x['user_id']]:
                                res[x['user_id']][t]={}
                                res[x['user_id']][t]['btc']=ag[x['user_id']]
                                res[x['user_id']][t]['ach']=0
                                res[x['user_id']][t]['cc']=0
                        res[x['user_id']][t]['btc']+=float(x['btc'])*s
                        ag[x['user_id']]+=float(x['btc'])*s
                        if x['payment_method']=='ach':
                                res[x['user_id']][t]['ach']+=float(x['usd'])*s
                                ach[x['user_id']]+=float(x['usd'])*s
                        else:
                                if s<0:
                                     res[x['user_id']][t]['ach']-=float(x['usd'])*s   
                                else:
                                        res[x['user_id']][t]['cc']+=float(x['usd'])*s
                                cc[x['user_id']]+=float(x['usd'])*s
                        
                print(res)
c=Solution()
c.count()