"""
int(x) 将x转换为一个整数。
float(x) 将x转换到一个浮点数。
str(x) 将对象 x 转换为字符串
"""

a1 = str(1.1)
print(a1, type(a1))

print("========分割线=======")

true_2_int = int(True)
false_2_int = int(False)
print(true_2_int, type(true_2_int))
print(false_2_int, type(false_2_int))

print("========分割线=======")
# nihao_int = int("nihao")
# print(nihao_int, type(nihao_int))

int2Float = float(11)
print(int2Float, type(int2Float))

float2Int = int(11.1)
print(float2Int, type(float2Int))
