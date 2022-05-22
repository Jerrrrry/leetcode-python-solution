#https://leetcode.com/problems/search-suggestions-system
#def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:


def suggestedProducts(products,search):
        products.sort()
        res=[]

        for i in range(len(search)):
                d=[]

                for product in products:
                        if product[:i+1]==search[:i+1]:
                                if len(d)>=3:
                                        break
                                else:
                                        d.append(product)

                res.append(d)

        return res
