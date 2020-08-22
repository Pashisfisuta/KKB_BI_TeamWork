1、既然内容相似度计算简单，能频繁更新，为什么还需要协同过滤算法呢？
协同过滤与基于内容的推荐相比,最大的好处是动态更新用户的偏好与item之间的相似度,但基于内容的推荐是考虑到历史数据的静态推荐,与动态推荐相比，推荐的准确性与实时性也不会太准确且物品相似度会发生变化。

2、你需要推荐系统么？哪些情况下不需要推荐系统？
需要。无论是听音乐、电商购物还是社交都是推荐系统应用的场景,对于了解用户需求实现平台盈利具有至关重要的作用
推荐系统变成推送系统的时候可能会对用户的体验造成困扰，而且无法进行反馈与AB测试的环境对于推荐系统也是很大的干扰，用户数量比较少，item少的时候，推荐系统的成本很大，性价比很低。

3、如果给一个视频打标签，视频中有音乐作为背景音乐，采用了NLP方式对内容自动打标签，可能存在什么问题？
NLP对内容打上的标签是一个文本分类的问题，对视频内容的打标签与NLP对内容打上的标签是不一样, 而且推荐系统的标签可能会对后面的结果产生误导，先开始使用一些人工打标签的方法比较合适。