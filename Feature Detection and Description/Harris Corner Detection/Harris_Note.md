## Harris 笔记

### 一 Harris简介

​		Harris算法用于检测角点，角点为图像中的特征。粗略的讲下特征的定义，**特征就是有意义的图像区域，该区域具有独特特征和易于识别性**

​		

### 二 Harris函数

下面给出我们要使用的函数：

```
cornerHarris(src, blockSize, ksize, k[,dst[,borderType]]);
```

参数详解：

- image：输入的单通道8位或者浮点图像
- blockSize：窗口大小
- kszie：cornerHarris函数使用了Sobel算子，该参数定义了Sobel算子的中孔。简单来说，该函数定义了角点检测的敏感度，其值必须介于3~31之间的奇数
- k：harris计算响应公式中的`k`值，一般取0.04~0.06
- borderType：像素插值方法

下面我们使用这个函数来检测角点

```python
import cv2 
import numpy as np

filename = 'resource\\data\\chessboard.png'
img = cv2.imread(filename)
img = cv2.resize(img, dsize=(600,400))
# 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,3,23,0.04)

dst = cv2.dilate(dst, None)

img[dst>0.01*dst.max()] = [0,0,255]

cv2.imshow('dst', img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
```

结果图为：

![dst](C:\Users\xjw\Desktop\dst.png)

​    

### 三 Harris检测原理

下面给出一张图来认识一下什么是角点。

![img](https://images2018.cnblogs.com/blog/1328274/201808/1328274-20180820211915487-1077934383.png)

上图中的E、F就是角点。它们具有以下特征：

- 轮廓之间的交点

- 对于同一场景，即使视角发生变化，通常具备稳定性质的特征

- 该点附近区域的像素点无论在梯度方向上还是其梯度幅值上有着较大变化
  			

  ![img](https://images2018.cnblogs.com/blog/1328274/201808/1328274-20180820212053678-579008700.png)



**Harris角点检测的基本思想：**使用一个固定窗口在图像上进行任意方向上的滑动，比较滑动前与滑动后两种情况，窗口中的像素灰度变化程度，如果存在任意方向上的滑动，都有着较大灰度变化，那么我们可以认为该窗口存在角点。

![img](https://images2018.cnblogs.com/blog/1328274/201808/1328274-20180821200118673-747876394.png)



1. **灰度变化描述**

   当窗口发生$ [u,v] $移动时，那么滑动前与滑动后对应的窗口中的像素点灰度变化描述如下：

   ​						$$ E(u,v)=\sum\limits_{(x,y)€W}w(x,y)[I(x+u,y+v)-I(x,y)]^2 $$

   参数解释：

   - $[u,v]$是窗口$W$的偏移量

   - $(x,y)$是窗口$W$所对应的的像素坐标位置

   - $I(x,y)$是像素坐标位置$(x,y)$的图像灰度值

   - $w(x,y)$是窗口函数，就相当于kernel，最简单的情形就是窗口$W$内的所有像素所对应的的$w$权重系数均为1（均值滤波）。有时，我们会将$w(x,y)$函数设置为以窗口$W$中心为原点的二元正态分布。如果窗口$W$中心点是角点时，移动前与移动后，该点在灰度变化贡献最大；而离窗口$W$中心（角点）较远的点，这些点的灰度几乎平缓，可以给这些点设置小值，以示该点对灰度变化贡献较小

     ![img](https://images2018.cnblogs.com/blog/1328274/201808/1328274-20180821181229682-539508279.png)

   根据上述表达式，当窗口在平坦区域上移动，灰度不会发生什么变换。$E(u,v)=0$；如果窗口处在纹理比较丰富的区域上滑动，那么灰度变化会很大。

   

   2. **$E(u,v)$化简**

      首先需要了解下泰勒公式，下面给出二元泰勒公式的展开形式：

      ​							$$f(x+u,y+v)≈f(x,y)+uf_x(x,y)+vf_y(x,y)$$

      那么，可以得到

      ​							$$\sum\limits_{(x,y)€W}w(x,y)[I(x+u,y+v)-I(x,y)]^2$$

      ​							$$≈\sum\limits_{(x,y)€W}w(x,y)[I(x,y)+uI_x+vI_y-I(x,y)]^2$$

      ​							$$=\sum\limits_{(x,y)€W}w(x,y)[u^2I_x^2+2uvI_xI_y+v^2I_y^2]$$

      ​							$$=\sum\limits_{(x,y)€W}w(x,y)\begin{bmatrix}u & v\end{bmatrix}\begin{bmatrix} I_x^2 & I_xIy \\  I_xI_y & I_y^2\end{bmatrix}\begin{bmatrix}u \\ v\end{bmatrix}$$

      ​							$$=\begin{bmatrix}u & v\end{bmatrix}(\sum\limits_{(x,y)€W}w(x,y)\begin{bmatrix} I_x^2 & I_xIy \\  I_xI_y & I_y^2\end{bmatrix})\begin{bmatrix}u \\ v\end{bmatrix}$$

      最后，$E(u,v)$表达式可以更新为：

      ​							$$E(u,v)=\begin{bmatrix}u & v\end{bmatrix}M\begin{bmatrix}u \\ v\end{bmatrix}$$

      其中，$M=\sum\limits_{(x,y)€W}w(x,y)\begin{bmatrix} I_x^2 & I_xIy \\  I_xI_y & I_y^2\end{bmatrix}$，$I_x,I_y$分别为窗口像素点$(x,y)$在$x$方向上和$y$方向上的梯度值

      

      3. **矩阵$M$的关键性**

      Harris角点检测是通过对窗口内的每个像素的$x$方向上的梯度与$y$方向上的梯度进行统计分析。这里以$I_x,I_y$为坐标轴，因此每个像素的梯度坐标可以表示成$(I_x,I_y)$，下面，针对平坦区域、边缘区域以及角点区域三种情形进行分析：

      ![img](https://images2018.cnblogs.com/blog/1328274/201808/1328274-20180821184446489-1586548234.png)

      ​	下面是对这三种情况窗口中的对应像素的梯度分布进行绘制：

      ​										![img](https://images2018.cnblogs.com/blog/1328274/201808/1328274-20180821184738432-562053567.png)

      ​		

      ​	可以注意到这三个区域的特点：

       - 平坦区域上的每个像素点所对应的的$(I_x, I_y)$坐标分布在原点附近，但是方差较小

       - 边缘区域有一个坐标轴分布较散

       - 角点区域的$x,y$方向上的梯度分布都比较散

         为了简化运算，我们先假设$M$矩阵中的权重系数$w(x,y)=1$

         $$M=\sum\limits_{(x,y)€W}\begin{bmatrix} I_x^2 & I_xIy \\  I_xI_y & I_y^2\end{bmatrix}$$
          
         



**参考：**

[1] [Harris角点检测原理](https://www.cnblogs.com/zyly/p/9508131.html#_labelTop)

[2] [Harris角点检测](https://www.cnblogs.com/ronny/p/4009425.html)





