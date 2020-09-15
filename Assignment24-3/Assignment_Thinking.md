一、如何使用用户标签来指导业务？
根据用户生命周期不同的三个阶段，考虑使用用户标签的方式：
1、获客：如何进行拉新，通过更加精准的营销获取客户；
2、粘客：个性化推荐，搜索排序、场景运营等，如访问频率能否提升？用户在页面的停留时间能否更长。
3、留客：流失率预测，分析关键节点降低流失率的幅度以及原因。


二、如果给你一堆用户数据，没有打标签。你该如何处理？
遵循八字原则（用户、消费、行为、内容）
1、用户标签：包括性别、年龄、地域、收入、学历、职业等用户属性；
2、消费标签：包括消费习惯、购买意向、是否对促销敏感等；
3、行为标签：时间段、频次、时长、收藏、点击、喜欢、评分；（User Behavior可以分成Explicit Behavior和Implicit Behavior）；
4、内容分析：对用户平时浏览的内容进行分析，比如学术、游戏、运动等。

标签是对高维事物的抽象（降维），典型的打标签方式有PGC:专家生产、UGC:普通生产；
                          常用的降维方法可以通过聚类算法，如：K-Means，EM聚类，Mean-Shift，DBSCAN，层次聚类，PCA


三、准确率和精确率有何不同（评估指标）？
1、准确率：(TP+FN)/(TP+TN+FP+FN),即：预测正确的结果占样本总量的百分比。反映模型分类正确的能力，但是缺点在于样本如果不平衡，该指标会失效。
2、精确率：也成查准率，TP/(TP+FR),即：预测为正样本的结果中，实际也是正样本所占但比例。
二者但区别：精确率Precision代表正样本结果但预测准确程度。准确率代表对样本整体对预测准确程度。


四、如果你使用大众点评，想要给某个餐厅打标签。这时系统可以自动提示一些标签，你会如何设计（标签推荐）？
1、方法1：向我推荐大众点评的热门标签；
2、方法2：向我推荐餐厅里对最热门标签；
3、方法3：向我推荐我自己经常使用的标签；
4、将方法2和3进行加权融合，生成最终的标签推荐结果。


五、使用TPOT等AutoML工具，有怎样的好处和不足?
TPOT除了不能解决数据清洗与数据抽取对过程之外，它可以处理特征选择、特征预处理、特征衍生、模型选择、参数优化等机器学习过程。
优点是易于操作，代码简洁，自动融合一个不错对模型，能为之后对模型优化打好基础。
缺点是需要比较大对算力，处理大规模的数据效率比较低，可以通过跑小批量的样本缓解该问题。


六、我们今天使用了10种方式来解MNIST，这些方法有何不同？你还有其他方法来解决MNIST识别问题么（分类方法）?
1、逻辑回归：本质是在伯努利分布的假定下，使用极大似然估计的方法估计参数并采用梯度下降的方法逼近真实参数，最终达到二分类的目的。逻辑回归会得到一个介于0-1之间的概率值，根据概率值的大小判断其属于哪个分类。逻辑回归不容易过拟合，泛化能力强。 逻辑回归算法需要提前做无量纲化处理。
2、决策树：既可以做分类模型，也可以做回归模型，决策树是通过信息增益entropy或者基尼系数 gini找到最高效的决策顺序，具有可视化、可解释性强的优点，缺点是容易过拟合，泛化能力弱。 
3、朴素贝叶斯：朴素贝叶斯既可以做分类模型，也可以做回归模型。 它的前提是假定了特征与特征之间相互独立，且符合贝叶斯公式。
4、支持向量机：SVM的思想是将线性不可分问题转化为非线性可分的问题，将低维数据映射到高维空间中，使用核函数映射的超平面起到分隔的作用。运算速度较慢，但精度较高。
5、KNN：K近邻算法的原理是对于一个新样本，K近邻的目的是在已有数据中找与它相似的K个数据，或者说“离它最近”的K个数据，如果这K个数据大多数属于同一个类别 ，则该样本也属于这个类别。 更适用于小数据场景。 优点：简单,易于理解,易于实现。 缺点： 懒惰算法，对测试样本分类时的计算量大，内存开销大； 
6、Adaboost自适应提升法：Adaboost根据前一次分类结果调整数据的权重，在上一个弱分类器中分类错误的样本权重 会在下一个若学习器中增加，分类正确的样本的权重则相应减少，并且在每一轮迭代时会向模型加入一个新的若学习器。不断重复调整权重和训练弱学习器，直到误分类数低于预设值或迭代次数达到指定最大值，最终得到一个强学习器。
7、XGBoost：与ada原理类似，区别在于失函数除了本身的损失，还加上了正则化部分，从而可以防止过拟合，泛化能力更强。它的损失 函数是对误差部分做了二阶泰勒展开，相较于GBDT算法的损失函数只对误差部分做负梯度(一阶泰勒)展开，更准确。
8、LDA线性判别式分析 LDA基本想法是使不同类别的样本尽量远离，同时使相同类别的样本尽可能靠近。这一目标通过扩大不同类别样本的类中心距离，同时缩小每个类 的类内方差来实现。 LDA的分类过程分为两步：首先，使用权重向量w将样本空间投影到直线上；然后，寻找直线上的一个点，把正负样本分开。
9、TPOT TPOT是基于Python的AutoML工具。它可以解决：特征选择，特征预处理、模型选择、参数优化等机器学习流程，但不包括数据清洗。
10、keras：深度学习但库，代码可读性强，适合处理大规模数据集但分类、回归问题。
还有随即森林、lightGBM可以做分类问题。


