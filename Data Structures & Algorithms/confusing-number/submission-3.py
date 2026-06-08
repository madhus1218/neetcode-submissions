class Solution:
    def confusingNumber(self, n: int) -> bool:
        my_dict = {
            0 : "0",
            1 : "1",
            2 : None,
            3 : None,
            4 : None,
            5 : None,
            6 : "9",
            7 : None,
            8 : "8",
            9 : "6"
        }
        str_nums = ""
        for num in str(n):
            if my_dict[int(num)] == None:
                return False
            str_nums += my_dict[int(num)]
        reversed_num = str_nums[::-1]
        return int(reversed_num) != n



            