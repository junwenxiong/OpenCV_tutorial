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

         $$M=\sum\limits_{(x,y)€W}\begin{bmatrix} I_x^2 & I_xIy \\  I_xI_y & I_y^2\end{bmatrix}$$

         我们可以将$E(u,v)$近似为二项函数
         
         ​									$$E(u,v)=Au^2+2Cuv+Bv^2$$
         
         其中
         
         ​									$$A=\sum\limits_{(x,y)€W}w(x,y)*I_x^2$$
         
         ​									$$B=\sum\limits_{(x,y)€W}w(x,y)*I_y^2$$
         
         ​									$$C=\sum\limits_{(x,y)€W}w(x,y)*I_xI_y$$
         
         二次项函数本质上就是一个椭圆函数。椭圆的长和宽都是由$M$的特征值$λ_1,λ_2$决定的（椭圆的长短轴正是矩阵$M$特征值平方根的倒数），椭圆的方向是由$M$的特征向量决定的，椭圆方程为：
         
         ​									$$\begin{bmatrix} u & v \end{bmatrix}M\begin{bmatrix} u \\ v \end{bmatrix}=1$$
         
         使用椭圆对数据集进行绘制，
      
      ​	![img](https://images2018.cnblogs.com/blog/1328274/201808/1328274-20180821184753999-21886520.png)
      
      ​	椭圆函数特征值与图像中的角点、直线（边缘）和平面之间的关系如下图所示，
      
      - 图像中的直线。一个特征值大，另一个特征值小，$\lambda_1\gg \lambda_2$或$\lambda_2\gg \lambda_1$。自相关函数值在某一方向上大，在其他方向上小
      - 图像中的平面。两个特征值都小，且近似相等；自相关函数值在各个方向上都小。
      - 图像中的角点，两个特征值都大，且近似想等；自相关函数在所有方向都增大。
      
      ![image](https://images0.cnblogs.com/blog/378920/201410/081646535629047.png)
      
      **4.如何度量角点响应**
      
      ​	通常用下面表达式进行度量，对每一个窗口计算得到一个分数$R$，根据$R$的大小来判定窗口内是否存在harris特征，分数$R$根据下面公式计算得到：
      
      ​									$$R=det(M)-k(trace(M))^2$$
      
      ​										$$det(M)=λ_1λ_2$$
      
      ​									$$trace(M)=λ_1+λ_2$$
      
      
      
      这里$λ_1,λ_2$是矩阵$M$的2个特征值，$k$是一个指定值，这是一个经验参数，需要实验确定它的合适大小，通常它的值在0.04和0.06之间，它的存在只是调节函数的形状而已。
      
      $R$取决于$M$的特征值，对于角点$|R|$很大，平坦的区域$|R|$很小，边缘的$|R|$为负值
      
      ![img](https://images2018.cnblogs.com/blog/1328274/201808/1328274-20180821201225052-2129812886.png)
      
      
      
      
      
      最后设定$R$的阈值，进行角点判断，后面的操作还有非极大值抑制
      
      非极大值抑制的原理，在一个窗口内，如果有很多角点则用值最小的那个角点，其他的角点都删除。

### 四 Harris角点算法实现

​		根据上述讨论，Harris角点检测可以分为5个步骤：	

  1. 计算图像$I(x,y)$在$x$和$y$两个方向的梯度$I_x,I_y$：

     ​									$$I_x=\frac{∂I}{∂x}=I×\begin{bmatrix} -1 & 0 & 1 \end{bmatrix}$$

     ​									$$I_y=\frac{∂I}{∂y}=I×\begin{bmatrix} -1 & 0 & 1 \end{bmatrix}^T$$

 2.计算图像两个方向梯度的乘积：

​									$$I_x^2=I_x*I_x$$

​									$$I_y^2=I_Y*I_y$$

​									$$I_xI_y=I_x*I_y$$

3. 使用高斯函数对上面乘积进行高斯加权（取$σ=2,ksize=3$）,计算中心点为$(x,y)$的窗口$W$对应的矩阵$M$:

​							$$A=\sum\limits_{(x,y)€W}g(I_x^2)=\sum\limits_{(x,y)€W}I_x^2*w(x,y)$$

​							$$B=\sum\limits_{(x,y)€W}g(I_y^2)=\sum\limits_{(x,y)€W}I_y^2*w(x,y)$$

​							$$C=\sum\limits_{(x,y)€W}g(I_xI_y)=\sum\limits_{(x,y)€W}I_xI_y*w(x,y)$$



​        其中$M=\begin{bmatrix} A& C \\C & B\end{bmatrix}=\sum\limits_{(x,y)€W}w(x,y)\begin{bmatrix} I_x^2 & I_xIy \\  I_xI_y & I_y^2\end{bmatrix}$

4. 计算每个像素点$(x,y)$处的Harris响应值$R$

​							$$R=det(M)-k(trace(M))^2$$

  5.过滤大于某一阈值$t$的$R$值

​							$$R=\{R:det(M)-k(trace(M))^2 > t \}$$

​	如果需要在3x3或者5x5的邻域上进行非极大值抑制，则局部极大值点即为图像中的角点。

### 五 Harris角点的性质

1. Harris角点检测算子对亮度和对比度的变化不灵敏

   对亮度和对比度的仿射变换并不改变Harris响应的极值点出现的位置

   ![img](https://images2018.cnblogs.com/blog/1328274/201808/1328274-20180822145049673-297166835.png)

   左图表示亮度变化，右图表示对比度变化

2. Harris角点检测算子具有旋转不变性

   Harris角点检测算子使用的是角点附近的区域灰度二阶矩矩阵。而二阶矩矩阵可以表示成一个椭圆，椭圆的长短轴正是二阶矩矩阵特征值平方根的倒数。当特征椭圆转动时，特征值并不发生变化，所以判断角点响应值也不会发生变化，由此说明Harris角点检测算子具有旋转不变性

   ![在这里插入图片描述](https://camo.githubusercontent.com/ee3ee1b2c7df120a7243ce309470d94250249c63/68747470733a2f2f696d67636f6e766572742e6373646e696d672e636e2f6148523063484d364c7939706257466e5a584d794d4445314c6d4e75596d78765a334d75593239744c324a73623263764e4455784e6a59774c7a49774d5459774e4338304e5445324e6a41744d6a41784e6a41304d6a45784d5445784e4441314e5451744d5451784e546b794d446b794e693577626d633f782d6f73732d70726f636573733d696d6167652f666f726d61742c706e67237069635f63656e746572)

   

3. Harris角点检测算子不具有尺度不变性

   ​			当图像被缩小时，在检测窗口尺度不变的前提下，在窗口内所包含图像的内容是完全不同的。左侧的图像可能被检测为边缘或曲线，而右侧的图像可能被检测为一个角点。

   ​			![img](https://images2018.cnblogs.com/blog/1328274/201808/1328274-20180822145140496-1031047638.png)





**参考：**

[1] [Harris角点检测原理](https://www.cnblogs.com/zyly/p/9508131.html#_labelTop)

[2] [Harris角点检测](https://www.cnblogs.com/ronny/p/4009425.html)





