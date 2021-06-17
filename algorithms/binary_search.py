arr = [ 2, 3, 4, 10, 40 ] 

# array must be sorted


def call_recur(elements, to_find, left, right):
    if left > right:
        return False
    mid = int((left + right)/2)
    if elements[mid] == to_find:
        return True
    if to_find < elements[mid]:
        return call_recur(elements, to_find,left, mid - 1)
    if to_find > elements[mid]:
        return call_recur(elements, to_find, mid + 1, right)

def main(elements, to_find):
    return call_recur(elements,to_find, 0, len(elements) - 1)

result = main(arr, 3)