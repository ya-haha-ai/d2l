import scipy.io as sio
import skimage.io
import numpy as np
# tif图
imgpath = r'C:\GF2\GF2_PMS1_E117.1_N39.9_20191212_L1A0004467085_Cut-MSS1.tif'
imggt = skimage.io.imread(imgpath)
# 转为mat
sio.savemat(r"D:\indianpines_ts.mat", {'imggt': imggt})
print(imggt.T)