#!/usr/bin/env python
#coding:utf-8

"""
统计一个一维数组中的各个元素的个数，然后删除多出来的重复元素，并输出结果。
例如：[1,2,2,2,3,3,3,3,3]-->[1,2,3]
"""

def count_element(one_list):
    element_number = {}
    for e in one_list:
        number = one_list.count(e)      #数出某个元素的个数
        element_number[e] = number     #生成类似：{1:1,2:3,3:5}的结果，key-element,value-元素的个数
    return element_number

def no_repeat_element(element_number):      #element_number是count_element(one_list)的返回值
    no_repeat_list = [key for key in element_number]
    return no_repeat_list

if __name__=="__main__":

    ls = ["a","a","b","b",'b','c','c']
    el_num=count_element(ls)
    print el_num
    no_repeat = no_repeat_element(el_num)
    print no_repeat