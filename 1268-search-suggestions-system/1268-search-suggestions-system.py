class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        for i in range(1 , len(searchWord)+1):
            prefix = searchWord[:i]
            suggestions = []
            for product in products:
                if product.startswith(prefix):
                    suggestions.append(product)
                if len(suggestions) == 3 :
                    break 
            result.append(suggestions)
        return result
        