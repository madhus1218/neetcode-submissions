class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            if operations[i] == "+":
                add_two = record[len(record) - 1] + record[len(record) - 2]
                record.append(add_two)
            elif operations[i] == "D":
                double = record[len(record) - 1] * 2
                record.append(double)
            elif operations[i] == "C":
                record.pop()
            else:
                record.append(int(operations[i]))
        return sum(record)