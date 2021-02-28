1、电商定向广告和搜索广告有怎样的区别，算法模型是否有差别

电商定向广告和搜索广告二者的区别：
电商广告用户没有明显的意图（不主动Query查询）
用户来淘宝之前，自己没有特别明确的目标，需要利用以往的历史行为进行item推荐；定向广告需要考虑的样本特征更多和历史相关。
搜索广告中对于用户在搜索场景下，用户在搜索栏上搜query，更多是短时的强烈的意图，所以及时满足用户的需求。


2、定向广告都有哪些常见的使用模型，包括Attention机制模型？

LR+人工特征

DIN模型（Deep Interest Network 深度兴趣网络）：
在对用户兴趣的表示上引入了attention机制，即对用户的每个兴趣表示赋予不同的权值，这个权值是由用户的兴趣和待估算的广告进行匹配计算得到的

DIEN模型（Deep Interest Evolution Network 深度兴趣进化网络）：
输入层，user profile，ad，context这三类特征的低维嵌入向量的学习
使用behavior layer，interest extractor layer 以及 interest evolving layer从用户历史行为中挖掘用户与目标商品相关的兴趣及演变

DSIN模型（Deep Session Interest Network 深度会话兴趣网络）：
将用户的连续行为自然地划分为Session，通过带有偏置编码的self attention网络对每个会话进行建模
使用BI-LSTM捕捉用户不同历史会话兴趣的交互和演变
设计了两个Activation Unit，将它们与目标item聚合起来，形成行为序列的最终表示形式（黄色，蓝色）

3、DIN中的Attention机制思想和原理是怎样的?

Attention机制在对用户行为的embedding计算上引入了attention network (也称为Activation Unit) 。把用户历史行为特征进行embedding操作，视为对用户兴趣的表示，之后通过Attention Unit，
对每个兴趣表示赋予不同的权值。
Attention思想：在pooling的时候，与 candidate Ad 相关的商品权重大一些，与candidate Ad 不相关的商品权重小一些
Attention分数，将candidate Ad与历史行为的每个商品发生交互来加权计算
Activation Unit输出Activation Weight，输入包括用户行为embedding和候选广告embedding以外，还考虑了他们两个的外积。对于不同的candidate ad，得到的用户行为表示向量也不同

4、DIEN相比于DIN有哪些创新?

DIEN 模型弥补了DIN模型没有对行为序列进行建模的缺陷，它围绕兴趣进化这个点进一步对DIN模型做了改进。
DIEN结构引入序列模型AUGRU模拟用户兴趣进化的过程。embedding layer 和 concatenate layer之间加入生成兴趣的interest extractor layer和模拟兴趣演化的interest evolving layer，
使用behavior layer，interest extractor layer 以及 interest evolving layer从用户历史行为中挖掘用户与目标商品相关的兴趣及演变。

5、DSIN关于Session的洞察是怎样的，如何对Session兴趣进行表达?

每个session中的行为是相近的，而在不同会话之间差别是很大的（类似于聚类），即：用户的行为序列可以用一个个session序列表示，session内的用户兴趣变化不大；
和airbab一样，即：将用户的点击行为按照时间排序，前后的时间间隔大于30分钟，算成另外一个session。

6、如果你来设计淘宝定向广告，会有哪些future work（即下一个阶段的idea）

加入对客群所处位置的利用：
不同地区对不同商品有不同的喜好，将区域（省市县区）embedding引入，通过attention的方式对地区甚至周边地区进行加权处理
