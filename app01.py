import streamlit as st
import openpyxl
import random
import os


st.set_page_config(
    page_title="破冰遊戲推薦系統",
    page_icon="🎲",
    layout="centered"
)

st.markdown("""
<style>

/* 整個背景 */
.stApp{
    background-color:#f5f9ff;
}

/* 標題 */
h1{
    color:#f05b5b !important;
    text-align:center;
    font-weight:900;
}

/* 下拉選單標題 */
label{
    color:#444 !important;
    font-weight:bold;
}

/* 按鈕 */
.stButton>button{
    background-color:#ffd34d;
    color:#444;
    border:none;
    border-radius:12px;
    font-size:20px;
    font-weight:bold;
    width:100%;
    height:60px;
}

/* 滑鼠移上去 */
.stButton>button:hover{
    background-color:#ffca28;
}

/* 成功訊息 */
.stSuccess{
    border-radius:15px;
}

/* 圖片 */
img{
    border-radius:15px;
}

/* Selectbox */
.stSelectbox{
    background:white;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

st.title("破冰遊戲推薦系統")

# 讀取 Excel
wb = openpyxl.load_workbook("game.xlsx")
ws = wb.worksheets[0]

st.write("請選擇你想要的遊戲條件")

people = st.selectbox(
    "遊戲人數",
    ["1", "2"],
    format_func=lambda x: "10人以下" if x == "1" else "10人以上"
)

game_type = st.selectbox(
    "類型",
    ["1", "2"],
    format_func=lambda x: "動態" if x == "1" else "靜態"
)

tool = st.selectbox(
    "道具",
    ["1", "2"],
    format_func=lambda x: "有" if x == "1" else "無"
)

level = st.selectbox(
    "玩家彼此熟悉程度",
    ["1", "2", "3"],
    format_func=lambda x: {
        "1": "一分熟",
        "2": "五分熟",
        "3": "全熟"
    }[x]
)

if st.button("開始推薦遊戲"):
    games = []

    for row in ws.rows:
        if (
            str(row[2].value) == people and
            str(row[3].value) == game_type and
            str(row[4].value) == tool and
            str(row[5].value) == level
        ):
            games.append(row[1].value)

    if len(games) > 0:
        game_ans = random.choice(games)

        st.subheader("系統最終隨機抽出的遊戲是：")
        st.success(game_ans)

        image_path = f"{game_ans}.jpg"

        if os.path.exists(image_path):
            st.image(image_path, caption=game_ans)
        else:
            st.warning("目前沒有找到對應圖片")
    else:
        st.error("目前沒有符合條件的遊戲")

