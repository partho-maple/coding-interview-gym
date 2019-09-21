

# O(n) time  | O(d) space - where nn is the total number of elements in the array
# including sub-elements, and d is the greatest depth of 'special' arrays in the array
def productSum(array, multiplier = 1):
    sumProd = 0
    for element in array:
        if type(element) is list:
            sumProd += productSum(element, multiplier + 1)
        else:
            sumProd += element
    return sumProd * multiplier