# tao 1 list moi
list_library = ["numpy", "pandas", "matplotlib"]
# them 1 phan tu moi vao list
list_library.append("sklearn")
# xoa 1 phan tu khoi list
list_library.remove("matplotlib")

# khai bao thu vien
import numpy
import tkinter
import matplotlib.pyplot as plt
import pandas

# lam viec voi numpy
mang_1d = numpy.array([1, 2, 3, 4, 5, 6]) 
mang_2d = numpy.array([[1,2,3], [4,5,6]])
print(mang_2d)
print(mang_2d)
print("kieu du lieu mang: ", mang_2d.dtype)
print("kich thuoc cua mang: ", mang_2d.shape)
print("so phan tu cua mang: ", mang_2d.size)
print("so chieu cua mang: ", mang_2d.ndim)

# # lam viec voi matplotlib
xpoints = numpy.array([0,1,2,3,4])
ypoints = numpy.array([6,18,12,18,6])
plt.plot(xpoints, ypoints)
plt.show()

# lam viec voi pandas
myarray = numpy.array([[1, 2, 3], [4, 5, 6]])
rownames = ['hang1','hang2']
colnames = ['cot1','cot2','cot3']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)
