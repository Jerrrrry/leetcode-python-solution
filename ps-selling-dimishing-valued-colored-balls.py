class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
            inventory.sort(reverse=True)
            inventory+=[0]
            res=0
            s=1
            for i in range(len(inventory)-1):
                if inventory[i]>inventory[i+1]:
                        if s*(inventory[i]-inventory[i+1])<orders:
                                res+=s*(inventory[i]+inventory[i+1]+1)(inventory[i]-inventory[i+1])
                                orders-=s*(inventory[i]-inventory[i+1])
                        else:
                                q,r=divmod(orders,s)
                                res+=s*(inventory[i]+inventory[i]-q+1)*q//2+r*(inventory[i]-q)
                                return res%(10**9+7)

                
                s+=1

