[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)]() [![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)]() [![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)]() [![License](https://img.shields.io/badge/License-MIT-yellow.svg)]()

# AI 写作助手（FastAPI + Streamlit）

## 📝 项目简介
本项目是一个基于 **FastAPI** + **Streamlit** 实现的中文写作辅助工具，支持：
- 润色文本
- 扩写充实内容
- 生成内容大纲
- 连续自然续写

后端调用 **通义千问 Qwen** 接口，并支持多轮会话记忆，可以持续保持上下文进行写作。

适用于：文章润色、论文语句优化、内容扩写、文案撰写、故事续写等多场景。

---

## 💡 功能特性
| 模式 (mode) | 功能说明 |
|------------|---------|
| revise | 润色表达，使句子更自然、准确、清晰 |
| expand | 扩写内容，增加细节与表达深度 |
| outline | 根据输入内容生成结构化大纲 |
| continue | 自然衔接续写后续内容 |

并可选择不同语气风格：自然、正式、口语、书面、富有情感等。

---

## 🔧 技术栈
| 模块 | 技术 |
|------|------|
| 前端界面 | Streamlit |
| 后端接口 | FastAPI |
| 模型调用 | Qwen API（OpenAI 兼容格式） |

---

## 🚀 本地运行步骤

### 1. 克隆项目

### 2. 安装依赖

### 3. 配置环境变量
```bash
set DASHSCOPE_API_KEY=你的API密钥   # Windows
export DASHSCOPE_API_KEY=你的API密钥 # Linux / Mac
```

### 4. 启动后端（FastAPI）
```bash
uvicorn main:app --reload
```

### 5. 启动前端（Streamlit）
```bash
streamlit run app.py
```

---

## 🧊 项目结构
```
project/
│── main.py          # FastAPI 后端（文件1）
│── app.py           # Streamlit 前端（文件2）
│── README.md
```

---

## 📚 使用说明
1. 启动后端和前端后，浏览器会自动打开界面
2. 左侧选择 **处理方式 + 语气风格**
3. 在右侧输入文本，点击 **生成** 按钮
4. 下方聊天窗口将以气泡形式展示历史内容

支持多轮对话，模型会记住同一 session 内的上下文。

---

## 🗂️ 示例
**输入：**
> 这部电影真的很好看，我特别喜欢里面的角色。

**模式：** 润色（revise）

**输出：**
> 这部电影十分精彩，我尤其喜爱片中角色的塑造与表现。

---

## 🧭 后续可扩展方向
- 增加 Markdown 导出
- 加入文档对比和改写差异高亮
- 支持长文片段连续处理

---

## 📄 License
本项目可自由使用与二次开发。

