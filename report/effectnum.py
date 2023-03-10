import numpy as np
import math
from decimal import Decimal

# 小数点后n位-V2
def new_round(num,n=2):
    # 1 判断num是否为整数(1 是整数，直接用'{:.2f}'.format(num);2 是小数，进入第2步)
    # 2 查找小数点后第2位是原始数字的第几位(如果小数点后没有两位，则直接用'{:.2f}'.format(num))
    # 3 判断小数点后第3位开始是否有字符(1 没有，返回原字符串；2 有，进入第4步)
    # 4 判断小数点后第3位是哪个数字(1 <=4或>=6，直接用'{:.2f}'.format(num);2 是5，进入第5步)
    # 5 判断小数点后第4位开始是否有字符(1 没有;2 有且全是0；3 有且不全为0)
        # 1和2，判断小数点第2位是奇数还是偶数
        # 3 
    num=str(num)
    if n==2:
        num_t = Decimal(num).quantize(Decimal("0.01"),rounding="ROUND_HALF_EVEN")
        return str(num_t)
    elif n==3:
        num_t = Decimal(num).quantize(Decimal("0.001"),rounding="ROUND_HALF_EVEN")
        return str(num_t)

    elif n==4:
        num_t = Decimal(num).quantize(Decimal("0.0001"),rounding="ROUND_HALF_EVEN")
        return str(num_t)

    elif n==1:
        num_t = Decimal(num).quantize(Decimal("0.1"),rounding="ROUND_HALF_EVEN")
        return str(num_t)


# 有效位数-V2
def effectnum(num,n):
    Decimalnum=["1.","0.1","0.01","0.001","0.0001","0.00001","0.000001","0.0000001"]
    if isinstance(num, str):
        # 如原始结果中含有“<”号(如“<0”)，需手动去除
        if "<" in num:
            num = num.replace('<', '')

        if "." not in num:
            if "e" not in num:
                index1 = n - len(num)
                if index1>=0:
                    num_t = Decimal(num).quantize(Decimal(Decimalnum[index1]),rounding="ROUND_HALF_EVEN")
                else:
                    num_t = effectnum_V1(num,n)      
            else:
                num_t = effectnum_V1(num,n)
            return str(num_t)
        else:
            if "e" not in num:
                pointindex = num.find(".") #小数点所处索引
                index2 = n - len(num)+1
                if index2>=0:
                    num_t = Decimal(num).quantize(Decimal(Decimalnum[len(num)-pointindex-1+index2]),rounding="ROUND_HALF_EVEN")
                else:
                    index3 = n-pointindex
                    num_t = Decimal(num).quantize(Decimal(Decimalnum[index3]),rounding="ROUND_HALF_EVEN")
            else:
                num_t = effectnum_V1(num,n) 
            return str(num_t)

    else:
        num=str(num)
        if "." not in num:
            if "e" not in num:
                index1 = n - len(num)
                if index1>=0:
                    num_t = Decimal(num).quantize(Decimal(Decimalnum[index1]),rounding="ROUND_HALF_EVEN")
                else:
                    num_t = effectnum_V1(num,n)      
            else:
                num_t = effectnum_V1(num,n)
            return str(num_t)
        else:
            if "e" not in num:
                pointindex = num.find(".") #小数点所处索引
                index2 = n - len(num)+1
                if index2>=0:
                    num_t = Decimal(num).quantize(Decimal(Decimalnum[len(num)-pointindex-1+index2]),rounding="ROUND_HALF_EVEN")
                else:
                    index3 = n-pointindex
                    num_t = Decimal(num).quantize(Decimal(Decimalnum[index3]),rounding="ROUND_HALF_EVEN")
            else:
                num_t = effectnum_V1(num,n) 
            return str(num_t)



# 小数点后两位结果转浮点数
def float_newround(num,n):
    return float(new_round(num,n))



# 有效位数结果转浮点数
def floateffectnum(num,n):
    if "." not in effectnum(num,n):
        return int(effectnum(num,n))
    else:
        return float(effectnum(num,n))


def Reverse(lst):
    return [ele for ele in reversed(lst)]

# 均值
def mean(lst):
    meanresult = np.mean(lst)

    return new_round(meanresult)

# sd
def sd(lst):
    sdresult = np.std(lst, ddof=1)

    return new_round(sdresult)

# se
def se(lst):
    sdresult = np.std(lst, ddof=1)
    n=len(lst)
    seresult = sdresult/math.sqrt(n)

    return new_round(seresult)

# cv
def cv(lst):
    meanresult = np.mean(lst)
    sdresult = np.std(lst,ddof=1)
    cvresult = sdresult/meanresult*100

    return new_round(cvresult)


import re
def handle_str(str_info, match_result):
    def not_empty(s):
        return s and s.strip()
    punctuation_list = list(filter(not_empty, match_result))
    for punctuation in punctuation_list:
        str_info = str_info.replace(punctuation, '')

    return str_info

# AB厂家数据读取查找定量表格
def matchfun(example_list, str_info):
    match_result = re.findall(r"\W", str_info)
    str_info = handle_str(str_info, match_result)
    str_info = set(str_info.lower().split(' '))
    iterable = set([example.lower() for example in example_list])
    if iterable & str_info:
        return True
    else:
        return False

example_str = "1-Acetyltyrosine 1 (224.0 / 136.0)"
example_list = ['224.0', '104.0', '62.0', '104.2', '90.1', '205.0', '132.0', '132.0', '166.0', '132.0', '150.0', '118.0', '182.0', '104.0', '126.0', '130.0', '90.1', '162.0', '120.2', '116.0', '76.0', '90.1', '148.0', '106.2', '175.1', '132.0', '156.0', '133.0', '147.0', '170.1', '147.0', '226.9', '133.0', '190.0', '170.0', '385.0', '163.1', '176.1', '240.9', '134.0', '269.2', '291.0', '223.0', '142.0', '241.0', '277.1', '202.0', '186.1'] 
example_list2 = ["your", "what", "I", "going"]

resp1 = matchfun(example_list, example_str)  # True
# resp2 = func(example_list2, example_str)  # True

print(resp1)
# print(resp2)


# 小数点后n位-V1
def new_round_V1(num,n=2):
    # 1 判断num是否为整数(1 是整数，直接用'{:.2f}'.format(num);2 是小数，进入第2步)
    # 2 查找小数点后第2位是原始数字的第几位(如果小数点后没有两位，则直接用'{:.2f}'.format(num))
    # 3 判断小数点后第3位开始是否有字符(1 没有，返回原字符串；2 有，进入第4步)
    # 4 判断小数点后第3位是哪个数字(1 <=4或>=6，直接用'{:.2f}'.format(num);2 是5，进入第5步)
    # 5 判断小数点后第4位开始是否有字符(1 没有;2 有且全是0；3 有且不全为0)
        # 1和2，判断小数点第2位是奇数还是偶数
        # 3 
    num=str(num)
    if n==2:
        if "." not in num:
            return '{:.2f}'.format(float(num))
        else:  
            if "e" in num:  
                return '{:.3f}'.format(float(num))
            else:  
                index1=num.find(".") #小数点所处索引
                # 判断小数点后是否有两位，没有则直接调用'{:.2f}'.format(num))
                if len(num)<=index1+2:
                    return '{:.2f}'.format(float(num))
                else:
                    index2=index1+2 #小数点后第2位所处索引
                    if (index2+1)==len(num):
                        return num
                    else:
                        if int(num[index2+1])<=4 or int(num[index2+1])>=6:
                            return '{:.2f}'.format(float(num))
                        else:
                            if (index2+2)==len(num): #小数点后第4位开始没有字符
                                if (int(num[index2])%2)==0: #偶数，不进位，把小数点后第三位的5变成4，再调用'{:.2f}'.format(num)
                                    num2=num[:-1]+"4"
                                    return '{:.2f}'.format(float(num2))
                                else: #奇数，进一位，，把小数点后第三位的5变成6，再调用'{:.2f}'.format(num)
                                    num2=num[:-1]+"6"
                                    return '{:.2f}'.format(float(num2)) 
                            else:
                                return '{:.2f}'.format(float(num))
    
    elif n==3:
        if "." not in num:
            return '{:.3f}'.format(float(num))
        else:  
            if "e" in num:  
                return '{:.4f}'.format(float(num))
            else:
                index1=num.find(".") #小数点所处索引
                
                if len(num)<=index1+3:
                    return '{:.3f}'.format(float(num))
                else:
                    index2=index1+3 
                    if (index2+1)==len(num):
                        return num
                    else: 
                        if int(num[index2+1])<=4 or int(num[index2+1])>=6:
                            return '{:.3f}'.format(float(num))
                        else:
                            if (index2+2)==len(num): 
                                if (int(num[index2])%2)==0: #偶数，不进位，把小数点后第三位的5变成4，再调用'{:.3f}'.format(num)
                                    num2=num[:-1]+"4"
                                    return '{:.3f}'.format(float(num2))
                                else: #奇数，进一位，，把小数点后第三位的5变成6，再调用'{:.3f}'.format(num)
                                    num2=num[:-1]+"6"
                                    return '{:.3f}'.format(float(num2)) 
                            else:  #小数点后第4位开始有字符，直接进位
                                return '{:.3f}'.format(float(num))

    elif n==4:
        if "." not in num:
            return '{:.4f}'.format(float(num))
        else:  
            if "e" in num:  
                return '{:.5f}'.format(float(num))
            else:
                index1=num.find(".") #小数点所处索引
                
                if len(num)<=index1+4:
                    return '{:.4f}'.format(float(num))
                else:
                    index2=index1+4 
                    if (index2+1)==len(num):
                        return num
                    else: 
                        if int(num[index2+1])<=4 or int(num[index2+1])>=6:
                            return '{:.4f}'.format(float(num))
                        else:
                            if (index2+2)==len(num): 
                                if (int(num[index2])%2)==0: #偶数，不进位，把小数点后第三位的5变成4，再调用'{:.3f}'.format(num)
                                    num2=num[:-1]+"4"
                                    return '{:.4f}'.format(float(num2))
                                else: #奇数，进一位，，把小数点后第三位的5变成6，再调用'{:.4f}'.format(num)
                                    num2=num[:-1]+"6"
                                    return '{:.4f}'.format(float(num2)) 
                            else:  #小数点后第4位开始有字符，直接进位
                                return '{:.4f}'.format(float(num))

    elif n==1:
        if "." not in num:
            return '{:.1f}'.format(float(num))
        else:     
            index1=num.find(".") #小数点所处索引
            
            # 判断小数点后是否有一位，没有则直接调用'{:.1f}'.format(num))
            if len(num)<=index1+1:
                return '{:.1f}'.format(float(num))
            else:
                index2=index1+1 #小数点后第3位所处索引
                if (index2+1)==len(num):  #如果小数点后恰好有3位，则返回原始数据
                    return num
                else: 
                    if int(num[index2+1])<=4 or int(num[index2+1])>=6:
                        return '{:.1f}'.format(float(num))
                    else:
                        if (index2+2)==len(num):
                            if (int(num[index2])%2)==0: #偶数，不进位，把小数点后第三位的5变成4，再调用'{:.3f}'.format(num)
                                num2=num[:-1]+"4"
                                return '{:.1f}'.format(float(num2))
                            else: #奇数，进一位，，把小数点后第三位的5变成6，再调用'{:.3f}'.format(num)
                                num2=num[:-1]+"6"
                                return '{:.1f}'.format(float(num2)) 
                        else:  #小数点后第4位开始有字符，直接进位
                            return '{:.1f}'.format(float(num))


# 有效位数-V1
def effectnum_V1(num,n):
    if isinstance(num, str):
        # num为字符串
        # print("str")
        # 如原始结果中含有“<”号(如“<0”)，需手动去除
        if "<" in num:
            num = num.replace('<', '')
        num=float(num)
        if num>=1:
            if "." in f'%.{n}g' % num:
                if "e" not in f'%.{n}g' % num:
                    if len(f'%.{n}g' % num)==n+1:
                        return f'%.{n}g' % num
                    else:
                        a=f'%.{n}g' % num
                        for i in range(n+1-len(f'%.{n}g' % num)):
                            a=a+"0"
                        return a
                else:
                    x = str(f'%.{n}g' % num).split("e")
                    if len(x[0])==n+1:
                        return x[0]+"e"+x[1] 
                    else:
                        for i in range(n+1-len(x[0])):
                            x[0]=x[0]+"0"
                        return x[0]+"e"+x[1]     

            else:
                if "e" not in f'%.{n}g' % num:
                    if len(f'%.{n}g' % num)==n:
                        return f'%.{n}g' % num
                    else:
                        b=f'%.{n}g' % num
                        for i in range(n-len(f'%.{n}g' % num)):
                            if i == 0:
                                b=b+"."
                            b = b+"0"
                        return b

                else:
                    x = str(f'%.{n}g' % num).split("e")
                    if len(x[0])==n:
                        return x[0]+"e"+x[1] 
                    else:
                        for i in range(n-len(x[0])):
                            if i == 0:
                                x[0]=x[0]+"."
                            x[0] = x[0]+"0"
                        return x[0]+"e"+x[1]  
        elif num<=-1:
            if "." in f'%.{n}g' % num:
                if "e" not in f'%.{n}g' % num:
                    if len(f'%.{n}g' % num)==n+2:
                        return f'%.{n}g' % num
                    else:
                        a=f'%.{n}g' % num
                        for i in range(n+2-len(f'%.{n}g' % num)):
                            a=a+"0"
                        return a
                else:
                    x = str(f'%.{n}g' % num).split("e")
                    if len(x[0])==n+2:
                        return x[0]+"e"+x[1] 
                    else:
                        for i in range(n+2-len(x[0])):
                            x[0]=x[0]+"0"
                        return x[0]+"e"+x[1]     

            else:
                if "e" not in f'%.{n}g' % num:
                    if len(f'%.{n}g' % num)==n+1:
                        return f'%.{n}g' % num
                    else:
                        b=f'%.{n}g' % num
                        for i in range(n+1-len(f'%.{n}g' % num)):
                            if i == 0:
                                b=b+"."
                            b = b+"0"
                        return b

                else:
                    x = str(f'%.{n}g' % num).split("e")
                    if len(x[0])==n:
                        return x[0]+"e"+x[1] 
                    else:
                        for i in range(n+1-len(x[0])):
                            if i == 0:
                                x[0]=x[0]+"."
                            x[0] = x[0]+"0"
                        return x[0]+"e"+x[1]

        elif num>0 and num<1:          
            strs=f'%.{n}g' % num
            count_0=0
            for i in range(2,len(strs)):  #从2开始是因为"0."的长度为2
                if strs[i]=="0":
                    count_0+=1
                else:
                    break
            if len(strs)==n+2+count_0: 
                return f'%.{n}g' % num
            else:
                for i in range(n+2+count_0-len(f'%.{n}g' % num)):
                    strs=strs+"0"
                return strs  

        elif num>-1 and num<0:          
            strs=f'%.{n}g' % num
            count_0=0
            for i in range(3,len(strs)):  #从3开始是因为"-0."的长度为2
                if strs[i]=="0":
                    count_0+=1
                else:
                    break
            if len(strs)==n+3+count_0: 
                return f'%.{n}g' % num
            else:
                for i in range(n+3+count_0-len(f'%.{n}g' % num)):
                    strs=strs+"0"
                return strs        
        
        else:
            return "0"

    else:
        # num为数值
        print(f'%.{n}g' % num)
        if num>=1:
            if "." in f'%.{n}g' % num:
                if "e" not in f'%.{n}g' % num:
                    if len(f'%.{n}g' % num)==n+1:
                        return f'%.{n}g' % num
                    else:
                        a=f'%.{n}g' % num
                        for i in range(n+1-len(f'%.{n}g' % num)):
                            a=a+"0"
                        return a
                else:
                    x = str(f'%.{n}g' % num).split("e")
                    if len(x[0])==n+1:
                        return x[0]+"e"+x[1] 
                    else:
                        for i in range(n+1-len(x[0])):
                            x[0]=x[0]+"0"
                        return x[0]+"e"+x[1]     

            else:
                if "e" not in f'%.{n}g' % num:
                    if len(f'%.{n}g' % num)==n:
                        return f'%.{n}g' % num
                    else:
                        b=f'%.{n}g' % num
                        for i in range(n-len(f'%.{n}g' % num)):
                            if i == 0:
                                b=b+"."
                            b = b+"0"
                        return b

                else:
                    x = str(f'%.{n}g' % num).split("e")
                    if len(x[0])==n:
                        return x[0]+"e"+x[1] 
                    else:
                        for i in range(n-len(x[0])):
                            if i == 0:
                                x[0]=x[0]+"."
                            x[0] = x[0]+"0"
                        return x[0]+"e"+x[1]  
        elif num<=-1:
            if "." in f'%.{n}g' % num:
                if "e" not in f'%.{n}g' % num:
                    if len(f'%.{n}g' % num)==n+2:
                        return f'%.{n}g' % num
                    else:
                        a=f'%.{n}g' % num
                        for i in range(n+2-len(f'%.{n}g' % num)):
                            a=a+"0"
                        return a
                else:
                    x = str(f'%.{n}g' % num).split("e")
                    if len(x[0])==n+2:
                        return x[0]+"e"+x[1] 
                    else:
                        for i in range(n+2-len(x[0])):
                            x[0]=x[0]+"0"
                        return x[0]+"e"+x[1]     

            else:
                if "e" not in f'%.{n}g' % num:
                    if len(f'%.{n}g' % num)==n+1:
                        return f'%.{n}g' % num
                    else:
                        b=f'%.{n}g' % num
                        for i in range(n+1-len(f'%.{n}g' % num)):
                            if i == 0:
                                b=b+"."
                            b = b+"0"
                        return b

                else:
                    x = str(f'%.{n}g' % num).split("e")
                    if len(x[0])==n:
                        return x[0]+"e"+x[1] 
                    else:
                        for i in range(n+1-len(x[0])):
                            if i == 0:
                                x[0]=x[0]+"."
                            x[0] = x[0]+"0"
                        return x[0]+"e"+x[1]

        elif num>0 and num<1:
            strs=f'%.{n}g' % num
            count_0=0
            for i in range(2,len(strs)):  #从2开始是因为"0."的长度为2
                if strs[i]=="0":
                    count_0+=1
                else:
                    break
            if len(strs)==n+2+count_0: 
                return f'%.{n}g' % num
            else:
                for i in range(n+2+count_0-len(f'%.{n}g' % num)):
                    strs=strs+"0"
                return strs    

        elif num>-1 and num<0:          
            strs=f'%.{n}g' % num
            count_0=0
            for i in range(3,len(strs)):  #从3开始是因为"-0."的长度为2
                if strs[i]=="0":
                    count_0+=1
                else:
                    break
            if len(strs)==n+3+count_0: 
                return f'%.{n}g' % num
            else:
                for i in range(n+3+count_0-len(f'%.{n}g' % num)):
                    strs=strs+"0"
                return strs     

        else:
            return "0"

