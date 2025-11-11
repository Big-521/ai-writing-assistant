from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os
import uuid


app = FastAPI()
# 配置 Qwen（通义千问）API 客户端
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
# 用字典维护会话历史
SESSIONS = {}

# 定义前端请求字段格式


class InputText(BaseModel):
    session_id: str
    text: str
    mode: str = "revise"
    tone: str = "自然、清晰"
# 生成新的写作会话


@app.post("/session/create")
def create_session():
    session_id = str(uuid.uuid4())
    SESSIONS[session_id] = []
    return {"session_id": session_id}

# 定义 /generate POST 接口


@app.post("/generate")
def generate_text(data: InputText):

    # 构造 Prompt（模型输入）
    system_prompt = f"""
你是一个专业的中文写作助手，擅长润色、扩写、续写与提炼。
要求：
1. 语言自然流畅，表达准确，不夸张、不生造信息。
2. 根据 mode 改变行为：
   - revise：润色表达，使其更自然准确
   - expand：扩写充实内容，增加细节和表达深度
   - outline：生成结构清晰的内容大纲
   - continue：自然衔接续写后文
3. 语气风格保持为：{data.tone}
请直接输出结果，不要解释。
"""
    # 取历史对话拼接为上下文
    history = [{"role": "system", "content": system_prompt}] + \
        SESSIONS.get(data.session_id, [])
    history.append({"role": "user", "content": data.text})

    # 调用模型 API
    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=history
    )
    # 提取模型输出内容
    result = (completion.choices[0].message.content or "").strip()
    # 将当前轮对话保存起来
    SESSIONS[data.session_id] = history + [
        {"role": "assistant", "content": result}
    ]
    # 返回 JSON 响应
    return {"output": result}
