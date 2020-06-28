# LBP特征   

   局部二值模式（Local Binary Pattern, LBP）是一种用来描述图像局部纹理特征的算子，LBP特征具有灰度不变性和旋转不变性等显著优点，它将图像中的各个像素与其邻域像素值进行比较，将结果保存为二进制数，并将得到的二进制比特串作为中心像素的编码值，也就是LBP特征值。LBP提供给了一种衡量像素间邻域关系的特征模式，因此可以有效地提取图像的局部特征，而且由于其计算简单，可用于基于纹理分类的实时应用场景，例如目标检测、人脸识别等。

 

## 原始LBP特征

  原始的LBP算子定义于图像中3x3的邻域窗口，取窗口内中心像素的灰度值作为阈值，将8邻域像素的灰度值与其进行比较，若邻域像素值大于中心像素值，则比较结果为1，否则为0。这样邻域内的8个像素点经过比较后可得到8位二进制数，将其按顺序依次排列即可得到中心像素的LBP值。LBP特征值反映了中心像素和其邻域的纹理信息。LBP的取值一共有种，和一副普通的灰度图像类似，因此可将LBP特征以灰度图的形式表达出来。由于LBP特征考虑的是纹理信息，而不包含颜色信息，因此彩色图需转换为灰度图。原始LBP特征的提取过程如下图所示：

![clip_image002](https://github.com/woshihaozhu/OpenCV_tutorial/blob/master/Feature%20Detection%20and%20Description/LBP%20Detection/img/clip_image002.jpg?raw=true)



公式定义如下：

![img](https://github.com/woshihaozhu/OpenCV_tutorial/blob/master/Feature%20Detection%20and%20Description/LBP%20Detection/img/clip_image003.png?raw=true)

![img](https://github.com/woshihaozhu/OpenCV_tutorial/blob/master/Feature%20Detection%20and%20Description/LBP%20Detection/img/clip_image004.png?raw=true)

![摘录](https://github.com/woshihaozhu/OpenCV_tutorial/blob/master/Feature%20Detection%20and%20Description/LBP%20Detection/img/clip_image005.png?raw=true) **代码插入**

```c++
// 原始LBP特征
void elbp1(Mat& src, Mat& dst)
{
  // 循环处理图像数据
  for (int row = 1; row < src.rows - 1; row++)
  {
    for (int col = 1; col < src.cols - 1; col++)
   {
      uchar pixel = src.at<uchar>(row, col);
      unsigned char r_pixel = 0;
      r_pixel |= (pixel < src.at<uchar>(row - 1, col - 1)) << 7;
      r_pixel |= (pixel < src.at<uchar>(row - 1, col)) << 6;
      r_pixel |= (pixel < src.at<uchar>(row - 1, col + 1)) << 5;
     r_pixel |= (pixel < src.at<uchar>(row, col + 1)) << 4;
      r_pixel |= (pixel < src.at<uchar>(row + 1, col + 1)) << 3;
      r_pixel |= (pixel < src.at<uchar>(row + 1, col)) << 2;
      r_pixel |= (pixel < src.at<uchar>(row + 1, col - 1)) << 1;
      r_pixel |= (pixel < src.at<uchar>(row, col - 1)) << 0;
     dst.at<uchar>(row - 1, col - 1) = r_pixel;
    }
  }
}
```

 

## 圆形LBP特征

  原始LBP特征考虑的是固定半径范围内的邻域像素，不能满足不同尺寸和频率纹理的需求，当图像的尺寸发生变化时，LBP特征将不能正确编码局部邻域的纹理信息。为了适应不同尺寸的纹理特征，Ojala等人对LBP算子进行了改进，将3x3邻域窗口扩展到任意邻域，并用圆形邻域代替了正方形邻域，改进后的LBP算子允许在半径为R的邻域内有任意多个像素点，从而得到在半径为R的区域内含有P个采样点的LBP算子。

![circular-lbp.png](https://github.com/woshihaozhu/OpenCV_tutorial/blob/master/Feature%20Detection%20and%20Description/LBP%20Detection/img/clip_image006.png?raw=true)

采样点的坐标可通过以下公式计算：

![img](https://github.com/woshihaozhu/OpenCV_tutorial/blob/master/Feature%20Detection%20and%20Description/LBP%20Detection/img/clip_image007.png?raw=true)

![img](https://github.com/woshihaozhu/OpenCV_tutorial/blob/master/Feature%20Detection%20and%20Description/LBP%20Detection/img/clip_image008.png?raw=true)

![img](https://github.com/woshihaozhu/OpenCV_tutorial/blob/master/Feature%20Detection%20and%20Description/LBP%20Detection/img/clip_image009.png?raw=true)

![img](https://github.com/woshihaozhu/OpenCV_tutorial/blob/master/Feature%20Detection%20and%20Description/LBP%20Detection/img/clip_image010.png?raw=true)

 

## 旋转不变LBP特征（Rotation Invariant LBP）

  无论是原始LBP算子还是圆形LBP算子，都只是灰度不变的，而不是旋转不变的，旋转图像会得到不同的LBP特征值。Maenpaa等人又将LBP算子进行了扩展，提出了具有旋转不变形的LBP算子，即旋转圆形邻域的采样点，或者以不同的邻域像素作为起始点，顺时针遍历所有采样点，得到一系列编码值（P个），取其中最小的作为该邻域中心像素的LBP值。旋转不变LBP算子的示意图如下：

 

![Rota-inv-lbp.jpg](https://github.com/woshihaozhu/OpenCV_tutorial/blob/master/Feature%20Detection%20and%20Description/LBP%20Detection/img/clip_image011.jpg?raw=true)



 

## LBP等价模式（Uniform LBP）

  对于一个半径为R的圆形区域，包含有P个邻域采样点，则LBP算子可能产生$2^P$种模式。随着邻域内采样点数的增加，LBP值的取值数量呈指数级增长。例如邻域内20个采样点，则对应有$2^{20}$中模式。

**缺点**：过多的二进制模式不利于纹理信息的天提取、分类、识别。例如，将LBP特征用于纹理特征或人脸识别时，一般采用LBP特征的统计直方图来表达图像的信息，而较多的模式种类将使得数据量过大，且直方图过于稀疏。

因此，需要对原始的LBP特征进行降维，使得数据量减少的情况下能最好地表达图像的信息。

   为了解决二进制模式过多的问题，提高统计性，Ojala提出了一种“等价模式（Uniform Pattern）”来对LBP特征的模式种类进行降维。Ojala认为，在实际图像中，绝大多数LBP模式最多只包含两次从0到1或者从1到0跳变。

![重要](https://github.com/woshihaozhu/OpenCV_tutorial/blob/master/Feature%20Detection%20and%20Description/LBP%20Detection/img/clip_image013.png?raw=true) 等价模式的定义：当某个LBP所对应的循环二进制数从0到1或者从1到0最多有两次跳变是，该LBP所对应的二进制就是一个等价模式类。如00000000（0次跳变），11000011（2次跳变）都是等价模式类。

除等价模式类以外的模式都归为一类，称为混合模式类，例如10010111（4次跳变）。

通过改进，二进制模式的种类大大减少，由原来的$2^P$中降为$P(P-1)+2+1$种，其中为2次跳变的模式数，2为0次跳变（全“0”或全“1”）的模式数，1为混合模式的数量，由于是循环二进制数，因此“0”，“1”跳变次数不可能为奇数次。对于3x3邻域内8个采样点来说，二进制模式由原始的256种变为59种。这使得特征向量的维数大大减少，并且可以减少高频噪声带来的影响。

![重要](https://github.com/woshihaozhu/OpenCV_tutorial/blob/master/Feature%20Detection%20and%20Description/LBP%20Detection/img/clip_image013.png?raw=true) 实验表明，一般情况下，等价模式的数目占全部模式的90%以上，可以有效对数据进行降维。

下图为58种等价模式类：

![uniform LBP.png](https://github.com/woshihaozhu/OpenCV_tutorial/blob/master/Feature%20Detection%20and%20Description/LBP%20Detection/img/clip_image015.png?raw=true)

 

## 图像的LBP特征向量（Local Binary Patterns Histograms）

  对图像中的每个像素求LBP特征值可得到图像的LBP特征图谱，但一般不直接将LBP图谱作为特征向量用于分类识别，而是类似于HOG特征，采用LBP特征的统计直方图作为特征向量。将LBP特征图谱划分为若干个子连通区域，并提取每个局部块的直方图，然后将这些直方图一次连接在一起形成LBP特征的统计直方图(LBPH)，即可用于分类识别的LBP特征向量。

LBP特征向量的具体计算过程如下：

- 按照上述算法计算图像的LBP特征图谱
- 将LBP特征图谱分块，例如分成区域$8*8 = 64$区域
- 计算每个子区域中LBP特征值的统计直方图，并进行归一化，直方图大小为$1 * numPatterns$
- 将所有区域的统计直方图按空间顺序依次连接，得到整幅图像的LBP特征向量，大小为$1 * (numPatterns * 64)$
- 从足够数量的样本中提取LBP特征，并利用机器学习的方法（SVM）进行训练得到模型，用于分类和识别等领域。

    对于LBP特征向量的维度，邻域采样点为8个，如果是原始的LBP特征，其模式数量为256，特征维数为$64 * 256 = 16384$；如果是$Uniform LBP$特征，其模式数量为$64 * 59 =3776$，使用等价模式特征，可以有效进行数据降维，而对模型性能却无较大影响。

 

参考：

[1] https://senitco.github.io/2017/06/12/image-feature-lbp/#comments

[2] https://blog.csdn.net/zouxy09/article/details/7929531

[3] https://www.cnblogs.com/qw12/p/9539582.html

 

 