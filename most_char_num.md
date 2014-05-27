#问题：

查找字符串中出现最多的字符和个数？

如 sdsdsddssssssdd -> 字符最多的是s，出现9次

#思路说明

利用python中的collections模块的Counter，[查此函数详细内容](https://docs.python.org/2/library/collections.html).对字符串进行统计。

然后将结果转化为字典类型。

特别注意，在字符串中可能会出现数量并列第一的字符，因此要通过循环找出最大数之后，再通过循环找出最大数对应的字母（键）。

#解答

    import collections

    def most_character_number(one_string):
        static_result = collections.Counter(one_string) 
        result = dict(static_result)                            
        most_number = max([value for value in result.values()])
        most_character = [key for key,value in result.items() if value==most_number]
        return (most_number,most_character)

    if __name__ == "__main__":
        (most_num,most_char) = most_character_number("yyyyyyddddddkuuuiii")
        print ("The most character is:%s"%most_num)
        print ("The number is:")
        for char in most_char:
            print char

