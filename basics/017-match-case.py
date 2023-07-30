# only works after python 3.1, no working for python
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        print(operations)
        res = []
        for op in operations:
            print (op)
            match op:
                case "C":
                    if (len(res) > 0):
                        res.pop()
                case "D":
                    print(res)
                    last = int(res[len(res) -1])
                    res.append(last *2)
                case "+":
                    a = int(res[len(res) -1])
                    b = int(res[len(res) -2])
                    res.append(a + b)
                case _:

                    res.append(int(op))
                    print(res)
        return sum(res)


