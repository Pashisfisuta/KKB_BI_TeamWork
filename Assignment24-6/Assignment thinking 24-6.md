1、什么是近似最近邻查找，常用的方法有哪些
    简称：ANN，英文全称：Approximate Nearest Neighbor，近似最近邻查找，通过牺牲一定的精度来提高提高查找效率,最近邻查找的时间复杂度是线性O(n)的，ANN方法比较适合于在大数据上的使用。
    常用的方法有：LSH（Locality-Sensitive Hashing）、MinHash、MinHashLSH、MinHashLSHForest、SimHash、MinHashLSHEnsemble等。

2、为什么两个集合的minhash值相同的概率等于这两个集合的Jaccard相似度
    如果两个文档相似，那么他们会有很多的singles也是相同的，对于海量数据，可以形成稀疏矩阵。目标是需要找到一个Hash函数，将原来的Jaccard相似度计算矩阵等价映射成一个相似度矩阵计算且维度较低。
    原来文档的Jaccard相似度高，那么它们的hash值相同的概率高；原来文档的Jaccard相似度低，那么它们的hash值不相同的概率高。

3、SimHash在计算文档相似度的作用是怎样的？
    通过SimHash算法得到每篇文档的fingerprint，计算两个文档fingerprint的hamming距离，一般文档之间的Hamming距离在3以内，两篇文档的hamming距离越小，相似度越高。
    Step1，设置SimHash的位数，综合考虑存储成本以及数据集的大小
    Step2，初始化SimHash为0 
    Step3，提取文本中的特征，比如采用n-gram
    "the cat sat on the mat"=>{"the cat", "cat sat", "sat on", "on the", "the mat"}  2-gram
    Step4，使用传统的hash函数计算各个word的hash编码
    Step5，各word的hash编码的每一位进行映射，如果该位为1，则simhash相应位的值加它的权重；否则减它的权重 
    Step6，计算最后得到的SimHash，如果该位大于0，则设为1；否则设为0 


4、为什么YouTube采用期望观看时间作为评估指标
    广告点击率和转化率在广告的场景中对开发人员有一定对欺骗性，不能很好的度量算法对于增加流量的作用，youtube提出采用期望观看时间作为评估指标，可以一定程度上解决该问题。
