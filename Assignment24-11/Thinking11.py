1、常见的规划问题都包括哪些？
规划问题分为：
LP：Linear Programming 线性规划，研究线性约束条件下线性目标函数的极值问题
ILP：Integer Linear Programming 整数线性规划，全部决策变量必须为整数
MIP：Mixed Integer Programming 混合整数规划，混合整数规划是LP的一种，其中部分的决策变量是整数
VRP：Vehicle Routing Problem 车辆路径问题
其中线性规划的速度最快，计算时间复杂度最低。

2、常用的规划工具包都有哪些？
常用的规划包是：pulp、ortools，可以通过pip install package进行安装
pulp只用于线性模型，包括如整数规划、01规划、混合整数线性规划
ortools由google开发，可以解决车辆路径、流程、整数和线性规划等问题

3、RFM模型的原理是怎样的
RFM：Recency(距离最近一次交易) Frequency（交易频率） Monetary（交易金额） 
RFM采用了分层管理的思想，通过RFM对用户进行分层，划分八类客户价值并制定相应的沟通策略
