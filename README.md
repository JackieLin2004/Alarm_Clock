# Alarm_Clock

## Python语言设计与实践 第二次项目

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

### 需求

实现一个闹钟的功能，同时要支持手机端可以扫码使用

### 环境

`python` 版本:3.11

### 快速开始

```
pip install -r requirements.txt

pnpm install
```

### 实现思路

- 本项目主要分为两个部分，一个是 `Python` 代码来生成二维码；另外一个是用 `Vue3` 框架实现闹钟界面，我们组主要参考
手机的闹钟功能，分为闹钟、世界时钟、秒表和计时器四个部分，将其部署到腾讯云服务器，把网址给到二维码，进而连接起来


- 在二维码方面，主要是调整老师发的代码，让其形成一个二维码，同时也设计了一个logo图标，将其置于二维码中央![QR_Code.png](QR_Code%2FQR_Code.png)


- 在界面设计方面，我们主要使用 `Vue3` 来设计界面，通过路由来切换界面，同时也实现了倒计时和秒表的功能

### 小组成员

Lin Xiaoyi, Tang Jiajun, Wang Zhen, Chen Guanrui, Wang Jing

### 此项目仅供学习交流使用，转载请注明出处！
