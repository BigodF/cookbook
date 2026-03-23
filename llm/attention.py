import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.modules
from transformers.models import BertForSequenceClassification
from torch.optim import AdamW


def mha(q, k, v):
    dim, head_num = 16, 4
    bs = 4
    seq = 8
    q_fn = nn.Linear(dim, dim)
    k_fn = nn.Linear(dim, dim)
    v_fn = nn.Linear(dim, dim)

    q, k, v = torch.zeros((bs, seq, dim))
    mask = torch.zeros(bs, seq, seq)
    q = q.view(bs, seq, head_num, -1).transpose(1, 2)
    # 来自encode
    k = k.view(bs, seq, head_num, -1).transpose(1, 2)
    v = v.view(bs, seq, head_num, -1).transpose(1, 2) # bs, head_num, seq, head_size

    s = torch.matmul(q, k.transpose(1, 2)) / (dim ** 0.5) # bs, head_num, seq, seq
    s = s.masked_fill(mask.unsqueeze(1)==0, float('-inf'))
    s = F.softmax(s, dim=-1)
    
    o = s.matmul(v).transpose(1, 2).contiguous().view(bs, seq, -1) # bs, seq, head_num, kead_size
    return o

def repeat_kv(q: torch.Tensor, rep_n):
    # q: bs, head_num, seq, head_size
    bs = head_num = seq = head_size = 0
    q = q[:, :, None, :, :].expand(bs, head_num, rep_n, seq, head_size)
    return q.view(bs, -1, seq, head_size)
    
def rms_norm(x: torch.Tensor, eps=1e-8):
    rms = torch.sqrt(x.pow(2).sum(dim=-1, keepdim=True))
    x = x / (rms + eps)
    return x


def layernorm(x: torch.Tensor, shape=8, eps=1e-8):
    mean = x.mean(dim=-1, keepdim=True)
    var = x.var(dim=-1, keepdim=True, unbiased=False)
    
    x_norm = (x - mean) / torch.sqrt(var + eps)
    return x_norm * weight + bias

def rotate_position(q: torch.Tensor, k: torch.Tensor):
    def cal_freq(dim, seq, theta=10000.0):
        freq = 1 / (theta ** (torch.arange(0, seq, 2).float() / dim))
        pos = torch.arange(seq)
        freq = torch.outer(pos, freq).float()
        freq_emb = torch.cat([freq, freq], dim=-1)
        # seq, dim
        freq_cos = freq_emb.cos()
        freq_sin = freq_emb.sin()
        return freq_cos.unsqueeze(0), freq_sin.unsqueeze(0)
    def rotate_half(x: torch.Tensor):
        x1, x2 = x[..., :x.shape[-1]//2], x[..., x.shape[-1]//2:]
        return torch.cat([-x2, x1], dim=-1)
    freq_cos, freq_sin = cal_freq(16, 128)
    q = rotate_half(q)
    k = rotate_half(k)
    q_out = q * freq_cos + q * freq_sin
    k_out = k * freq_cos + k * freq_sin
    return q_out, k_out

def contrastive_loss(feats: torch.Tensor, temp=0.5):
    feats = F.normalize(feats, dim=1)
    sim = torch.matmul(feats, feats.T)
    sim = sim / temp
    
    pos_mask = torch.zeros_like(sim, dtype=torch.bool)
    bs = feats.size()[0] // 2
    for i in range(bs):
        pos_mask[i, i+bs] = True
        pos_mask[i+bs, i] = True
    neg_mask = ~torch.eye(2*bs, dtype=torch.bool)
    
    pos_sim = sim[pos_mask].view(2*bs, -1)
    neg_sim = sim[neg_mask].view(2*bs, -1)
    sim_new = torch.cat([pos_sim, neg_sim], dim=-1)
    loss = F.log_softmax(sim_new, dim=-1)[:, 0].mean()
    return loss

a = torch.arange(5).unsqueeze(0).expand(3, 5)
print(a)
print(a.T)