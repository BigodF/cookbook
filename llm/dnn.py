import numpy as np
import math
from typing import Optional, List, Dict

# def tf_idf(corpus: List[List[str]], query: List[str]):
def test():
    corpus = [["hello", "world"], ["hello", "python"]]
    query = ["hello", "python"]
    words = list(set([w for doc in corpus for w in doc]))
    w2i = {w: i for i, w in enumerate(words)}
    
    tf = np.zeros((len(corpus), len(words)))
    for doc_idx, doc in enumerate(corpus):
        for w in doc:
            w_i = w2i[w]
            tf[doc_idx, w_i] += 1
        tf[doc_idx] /= len(doc)
    w_dc = (tf > 0).sum(axis=0, keepdims=True)
    idf = np.log((len(corpus) +1 ) / (w_dc + 1)) + 1
    tf_idf = tf * idf
    
    query_idxes = [w2i[w] for w in query]
    s = tf_idf[:, query_idxes]
    s = np.round(s, 5)
    s = s.tolist()
    
    # print(s)
    
    return s

def sigmoid(x):
    s = 1 / 1 + np.exp(-x)
    print(f'{s:.4f}')

def leaky_relu(z: np.ndarray, alpha=0.01):
    return np.where(z>0, z, alpha*z)

def kl_loss(p, q):
    loss = p * (np.log(p) - np.log(q))
    return loss


p1 = '''微博智搜-模型效果自动评估 2025.05 - 2025.07
项目背景： 评估不同模型在微博智搜主流程上的效果差异。
主要工作： 迭代效果评估维度、流程。在基础维度上，借鉴Deepseek-GRM论文中的做法，让模型根据需要，自动添加其它评估
维度。为了减低模型的生成难度，增加鲁棒性，每个基础维度独立多次调用模型判断打分，通过加权的方式计算该维度的最终
得分。评估模型在有些情况下会过度理解，针对几类主要的问题类型，通过fewshot的方式，增加后处理过程，让模型二次判
断。搭建一个网页展示模型的评估效果，便于人工校验。最终实现快速的对模型效果进行初步分析。'''

'''
- 模型性能。
- 模型效果：
    - 简洁性。输出内容是否冗余、重复。
    - 行文结构。文章结构、表，是否易于理解。
    - 物料遵循。答案是否来源于物料。
    - 相关性。回答的内容和query的相关性，是否围绕query回答。
    - 自适应维度。时效性“最新的演唱会”等。
    问题类型：
        - case。
'''


p2 = '''微博智搜-快速回答版 2025.01 - 2025.04
项目背景： 在搜索场景下，结合搜索落地页相关内容，实时为用户生成一个快速、简要的答案。
主要工作：
阶段一：基于Qwen2.5系列开源模型，构造prompt工程，搭建agent流程；通过不同大小模型的效果、首字符RT、平均token时
间综合确定模型选型，最终选择Qwen2.5 14B模型；
阶段二：开源模型缺乏对于微博数据、prompt指令的充分理解。在部分Query下，在筛选相关搜索结果、回答风格等维度效果
较差，使用SFT的方式优化。首先使用更大的模型，构建合成数据集，在均匀采集query log的基础上，增加困难类型的数据比
例，数据集采用Alpaca格式。使用Llama-Factory训练框架，在单机4卡A800上，采用Deepspeed进行分布式训练。训练时，由
于搜索结果过多，prompt过长，会出现爆显存的情况。最终采用Deepspeed ZeRO stage2的方式，将优化器、梯度在不同GPU
内进行分片，在保证训练速度的同时，提升可训练的token长度。全参SFT后效果可接受率由79%提升至92%，线上点击率由
4.3%提升至7.5%。'''

def test():
# def softmax(scores: list[float]) -> list[float]:
    scores = [2.0, 2.0, 3.0]
    s = np.array(scores)
    s_max = s.max()
    a = np.exp(s - s_max)
    b = a.sum()
    probabilities = [t for t in (a / b).rounr(4).tolist()]
    
    print(probabilities)
    return probabilities

def rnn_forward(input_sequence, initial_hidden_state, Wx, Wh, b):
    h = np.array(initial_hidden_state)
    Wx = np.array(Wx)
    Wh = np.array(Wh)
    b = np.array(b)
    for x in input_sequence:
        x = np.array(x)
        h = np.tanh(np.dot(Wx, x) + np.dot(Wh, h) + b)
    final_hidden_state = np.round(h, 4)
    return final_hidden_state.tolist()

class LSTM:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size

        # Initialize weights and biases
        self.Wf = np.random.randn(hidden_size, input_size + hidden_size)
        self.Wi = np.random.randn(hidden_size, input_size + hidden_size)
        self.Wc = np.random.randn(hidden_size, input_size + hidden_size)
        self.Wo = np.random.randn(hidden_size, input_size + hidden_size)

        self.bf = np.zeros((hidden_size, 1))
        self.bi = np.zeros((hidden_size, 1))
        self.bc = np.zeros((hidden_size, 1))
        self.bo = np.zeros((hidden_size, 1))

    def forward(self, x, initial_hidden_state, initial_cell_state):
        h = initial_hidden_state
        c = initial_cell_state
        outputs = []

        for t in range(len(x)):
            xt = x[t].reshape(-1, 1)
            concat = np.vstack((h, xt))

            # Forget gate
            ft = self.sigmoid(np.dot(self.Wf, concat) + self.bf)

            # Input gate
            it = self.sigmoid(np.dot(self.Wi, concat) + self.bi)
            c_tilde = np.tanh(np.dot(self.Wc, concat) + self.bc)

            # Cell state update
            c = ft * c + it * c_tilde

            # Output gate
            ot = self.sigmoid(np.dot(self.Wo, concat) + self.bo)

            # Hidden state update
            h = ot * np.tanh(c)

            outputs.append(h)

        return np.array(outputs), h, c

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))


if __name__ == '__main__':
    test()