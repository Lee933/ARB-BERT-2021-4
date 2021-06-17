# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/15 21:35
@Auth ： JsHou
@Email : 137073284@qq.com
@File ：predeal_data.py

"""

import numpy as np
import pandas as pd


def load_from_excel(path):
    """
    读取.xslx数据文件，按类别返回样本
    :param path: 文件路径
    :return:
        x: (n, p), 自变量
        y: (n, ), 因变量
    """
    data = pd.read_excel(path, engine='openpyxl')
    x, y = data['description'].values, data['REGRESSION'].values
    return x[y == 'YES'], x[y == 'NO']


def save_as_txt(path, file0, file1):
    """
    按类别将文件保存到txt文件中
    :param path: 待保存文件路径
    :param file0: ndarray, 类别0
    :param file1: ndarray, 类别1
    :return: None
    """
    with open(path, 'w', encoding='utf-8') as f:
        for e in file0:
            f.write(str(e) + '\t0\n')
        for e in file1:
            f.write(str(e) + '\t1\n')


# 读取原始数据文件和人工数据文件
x0, x1 = load_from_excel(r'./data/data1_4.xlsx')
x0_art, x1_art = load_from_excel(r'./data/data_artificial.xlsx')

# 原始数据中两个类别的样本数量
n_samples = [x0.shape[0], x1.shape[0]]

n_secs = 5  # 节的数目

# 划分为5节后，每一节样本数量
n_samples_sec = [int(n_samples[0] / n_secs), int(n_samples[1] / n_secs)]

for i in range(n_secs):
    # ----------测试集处理----------
    # 分段取测试集
    x0_test = x0[n_samples_sec[0] * i:n_samples_sec[0] * (i + 1)]
    x1_test = x1[n_samples_sec[1] * i:n_samples_sec[1] * (i + 1)]
    if i == 0:
        print(f'测试集样本数目：{x0_test.shape[0]}, {x1_test.shape[0]}\n')
    # 保存测试集
    save_as_txt(f'./output/test{i + 1}.txt', x0_test, x1_test)

    # ----------训练集、验证集处理----------
    # 将剩余数据拼接，用于划分训练集和测试集
    x0_remainder = np.concatenate((x0[0:n_samples_sec[0] * i], x0[n_samples_sec[0] * (i + 1) + 1:]), axis=0)
    x1_remainder = np.concatenate((x1[0:n_samples_sec[0] * i], x1[n_samples_sec[0] * (i + 1) + 1:]), axis=0)
    # ----------k折交叉验证----------
    k = 5  # 折的数目，可调整

    # 计算两个类别每一折样本数目
    n_samples_fold = [int(x0_remainder.shape[0] / k), int(x1_remainder.shape[0] / k)]
    for j in range(k):
        # ----------验证集处理----------
        # 分段取出验证集
        x0_validation = x0_remainder[n_samples_fold[0] * j:n_samples_fold[0] * (j + 1)]
        x1_validation = x1_remainder[n_samples_fold[1] * j:n_samples_fold[1] * (j + 1)]
        if i == 0 and j == 0:
            print(f'验证集样本数目：{x0_validation.shape[0]}, {x1_validation.shape[0]}\n')
        # 保存验证集
        save_as_txt(f'./output/dev{i + 1}{j + 1}.txt', x0_validation, x1_validation)

        # ----------训练集处理----------
        # 将剩余数据拼接，用作测试集
        x0_train = np.concatenate(
            (x0_remainder[0:n_samples_fold[0] * j], x0_remainder[n_samples_fold[0] * (j + 1) + 1:]), axis=0)
        x1_train = np.concatenate(
            (x1_remainder[0:n_samples_fold[1] * j], x1_remainder[n_samples_fold[1] * (j + 1) + 1:]), axis=0)
        # 加入人工数据集
        x0_train_ = np.concatenate((x0_train, x0_art), axis=0)
        x1_train_ = np.concatenate((x1_train, x1_art), axis=0)

        # ----------少数类样本过采样----------
        # 保证x0_为少数类样本
        if x0_train_.shape[0] > x1_train_.shape[0]:
            x0_train_, x1_train_ = x1_train_, x0_train_
        over_sample_ratio = max(int(x1_train_.shape[0] / x0_train_.shape[0] - 0.5), 2)
        num_minor = over_sample_ratio * x0_train_.shape[0]  # 少数类样本过采样后样本数目
        # 根据采样比例生成新样本集index
        index0 = np.random.rand(num_minor) * x0_train_.shape[0]
        index0 = index0.astype(int)  # 转int，用于index

        x0_resampled = x0_train_[index0]
        # ----------多数类样本降采样----------
        num_major = num_minor  # 多数类样本降采样后样本数目和少数类样本过采样后样本数目相同
        index1 = np.random.rand(num_major) * x1_train_.shape[0]
        index1 = index1.astype(int)

        x1_resampled = x1_train_[index1]
        # ----------保存训练集----------
        if i == 0 and j == 0:
            print(f'训练集样本数目：{x0_resampled.shape[0]}, {x1_resampled.shape[0]}\n')
        save_as_txt(f'./output/train{i + 1}{j + 1}.txt', x0_resampled, x1_resampled)
