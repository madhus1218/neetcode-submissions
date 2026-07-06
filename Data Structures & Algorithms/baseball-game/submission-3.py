class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in operations:
            if i == "+":
                add_two = record[-1] + record[-2]
                record.append(add_two)
            elif i == "D":
                double = record[-1] * 2
                record.append(double)
            elif i == "C":
                record.pop()
            else:
                record.append(int(i))
        return sum(record)