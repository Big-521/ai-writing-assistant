import streamlit as st
import requests
import json

API_BASE = "http://127.0.0.1:8000"
st.set_page_config(page_title="AI 写作助手", layout="wide")
# CSS 美化
st.markdown("""
<style>
body {background: #f5f6fa;}
textarea, input, .stTextInput>div>div>input {
    border-radius: 8px!important;
}
.chat-bubble-user{
    background:#e6f3ff;
    padding:12px 15px;
    border-radius:8px;
    margin:8px 0;
}
.chat-bubble-assistant{
    background:#ffffff;
    border:1px solid #e5e9ef;
    padding:12px 15px;
    border-radius:8px;
    margin:8px 0;
</style>
""", unsafe_allow_html=True)
# 管理前端会话
if "session_id" not in st.session_state:
    r = requests.post(f"{API_BASE}/session/create")
    st.session_state.session_id = r.json()["session_id"]

if "history" not in st.session_state:
    st.session_state.history = []
# 页面布局：左侧参数区 / 右侧对话区
left, right = st.columns([1, 2])

# 左侧：模式 + 语气选择
with left:
    st.header("⚙️ 参数设置")
    mode = st.selectbox(
        "处理方式",
        ["revise", "expand", "outline", "continue"],
        format_func=lambda x: {
            "revise": "润色表达",
            "expand": "扩写内容",
            "outline": "生成大纲",
            "continue": "续写内容"
        }[x]
    )
    tone = st.selectbox(
        "语气风格",
        ["自然、清晰", "正式、精炼", "口语化表达", "书面学术", "富有情感"]
    )
    st.markdown("---")
    st.caption(f"当前会话 ID：`{st.session_state.session_id}`")

# 右侧：文本输入 & 调用接口
with right:
    st.header("✍️ AI 写作助手")
    user_text = st.text_area("输入文本", "", height=160, placeholder="在这里粘贴原文…")
    if st.button("🚀 生成"):
        payload = {
            "session_id": st.session_state.session_id,
            "text": user_text,
            "mode": mode,
            "tone": tone
        }
        r = requests.post(f"{API_BASE}/generate", json=payload)
        result = r.json().get("output", "")
        # 保存本地历史，便于前端展示
        st.session_state.history.append(("user", user_text))
        st.session_state.history.append(("assistant", result))
    st.markdown("---")

    st.subheader("📜 预览")
    # 聊天气泡展示输出
    for role, msg in st.session_state.history:
        if role == "user":
            st.markdown(
                f"<div class='chat-bubble-user'><b>你：</b><br>{msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(
                f"<div class='chat-bubble-assistant'><b>AI：</b><br>{msg}</div>", unsafe_allow_html=True)
