import numpy as np
# 版本
print(np.version.version)
# 空
print(np.zeros(8))
arr = [1, 2, 3], [4, 5, 6, ], [7, 8, 9]
a = np.array(arr)
# 二维
a = np.zeros((4, 4))
print(type(a))
print(a)
# 指定值
a = np.full((4, 4), 2)
print(a)
# like
b = np.full_like(a, 6.01, dtype=float)
print(b)
# random  随机数
print(np.random.randint(5, 10))
print(np.random.random())
# range 5-10,步长2
print(np.arange(5, 10, 2))

# linspace 5-10,四个值
print(np.linspace(5, 10, 4))

# 矩阵
print(np.eye(5))

print('########################## 元素访问 ##########################')

# 访问
arr = [1, 2, 3], [4, 5, 6, ], [7, 8, 9]
a = np.array(arr)

print(a[0])
print(a[0][1])

# 切片
print(a[:1])
print(a[1:])

# 两种方式结果不同
print(a[:2, :2])
print(a[:2][:2])
print('########################## 其他 ##########################')
# 纬度
print(a.ndim)
# shape 大小
print(a.shape)
# dtype 类型
print(a.dtype)
# 每个元素大小
print(a.itemsize)
# 总大小
print(a.nbytes)

print('########################## 运算 ##########################')
# 所有元素加减
print(a + 10)
print(np.subtract(a, 10))
print(a * 10)
print(np.divide(a, 10))
print(np.sin(a))

print('########################## 统计类型 ##########################')

print(np.sum(a))  # 效率更高
print(a.sum())
print(np.sum(a, axis=1))
print(np.max(a))

print('########################## 比较 ##########################')
print(a > 6)
print(a == 6)

# 所有元素都？
print(np.all(a > 0))
print(np.all(a > 1))
print('########################## 变形 ##########################')

a = np.full((2, 10), 1)
print(a.reshape(4, 5))
print(a.reshape(5, 4))

# 排序
arr = [3, 2, 3], [8, 5, 6, ], [11, 8, 9]
a = np.array(arr)
print(np.sort(a))

# 拼接
a = np.array([1, 2, 3])
b = np.array([[4, 5, 6], [7, 8, 9]])
print(np.concatenate([a, a, a]))
print(np.concatenate([b, b,b]))

# 按列
print(np.concatenate([b, b,b],axis=0))
# 按行
print(np.concatenate([b, b,b],axis=1))
