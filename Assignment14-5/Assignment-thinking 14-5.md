1、在实际工作中，FM和MF哪个应用的更多，为什么
在实际工作中，MF应用更多。
因为MF只有user, item两个特征，FM：有多个特征，MF是FM的特殊情况
FM一般用于应用于点击率预估的场景。

2、FFM与FM有哪些区别？
FFM算法是FM算法的改进。
在FM算法中，每个特征对应一个隐向量(即：该特征与任何特征进行特征组合都用相同的隐向量)。
在FFM算法中，每个特征有f-1个隐向量(其中field的个数为f，同一个field中的特征不会进行组合)。

3、DeepFM相比于FM解决了哪些问题，原理是怎样的
DeepFM是FM与DNN的结合：FM提取低阶特征，DNN提取高阶特征，最后将DNN和FM的结果组合后通过激活函数输出。


4、Surprise工具中的baseline算法原理是怎样的？BaselineOnly和KNNBaseline有什么区别？
Baseline算法：基于统计的基准预测打分
BaselineOnly：给定用户和Item，给出基于baseline的估计值
KNNBaseline：考虑基线评级的协同过滤

5、基于邻域的协同过滤都有哪些算法，请简述原理
KNNBasic：最基础的K近邻协同协同，
KNNWithMeans：将每个用户评分均值考虑在内的协同过滤
KNNWithZScore：协同过滤算法的变种，考虑每个用户评分的归一化操作
KNNBaseline：协同过滤算法的变种，考虑每个用户评分的基线