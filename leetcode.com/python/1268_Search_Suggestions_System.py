import bisect

# Usig binary search
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        result, prefix, startIdx = [], "", 0
        for char in searchWord:
            prefix += char
            startIdx = bisect.bisect_left(products, prefix, startIdx)
            currnetSearchRes = []
            for product in products[startIdx: startIdx + 3]:
                if product.startswith(prefix):
                    currnetSearchRes.append(product)
            result.append(currnetSearchRes)
        return result


