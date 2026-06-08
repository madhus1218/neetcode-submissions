class Solution:
    def confusingNumber(self, n: int) -> bool:
        my_dict = {
            0 : "0",
            1 : "1",
            6 : "9",
            8 : "8",
            9 : "6"
        }
        str_nums = ""
        for num in str(n):
            if int(num) not in my_dict:
                return False
            str_nums += my_dict[int(num)]
        reversed_num = str_nums[::-1]
        return int(reversed_num) != n



            