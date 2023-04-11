from typing import List
def sum_num(numbers: List[int]):
    result = sum(numbers)
    response= {'the sum of your numbers is': result}
    return response
