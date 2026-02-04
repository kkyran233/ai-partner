import streamlit as st
#设置页面配置项

st.set_page_config(
    page_title="streamlit 入门",
    page_icon="🧊",
    #布局
    layout="wide",
    #控制侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={}
)



# 大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")
#段落文字
st.write("布偶猫，被誉为“猫中仙女”，是一种性格与外貌同样迷人的大型长毛猫。")
st.write("它们最引人注目的便是那双如星空般的湛蓝眼睛，清澈而深邃，仿佛能映出天空。其体型健壮，骨骼粗大，成年后需要三到四年才能完全成熟。一身丝质般顺滑的长毛，配以重点色的毛色分布（如海豹色、蓝色、巧克力色等），宛如一只优雅的布偶娃娃。")
st.write("但布偶猫真正俘获人心的，是它们无与伦比的温和性格。它们极其亲人，像小狗一样喜欢跟随主人走动，享受被拥抱的时光。它们忍耐力强，对小童和其他宠物友善，安静而不好斗，发起脾气来也只会默默走开。最独特的是，当被抱起时，它们会像真正的布偶一样柔软地放松在人的臂弯中，因此得名。")
st.write("这种甜美、安静的伴侣猫，非常适合寻求情感互动与陪伴的家庭。它们用一生的温柔与忠诚，诠释着何为“行走的云端天使”和“甜蜜的负担”。拥有一只布偶猫，便是拥有了一份触手可及的温柔与宁静。")
#图片
st.image("./resources/cat.jpg")
#音频
st.audio("./resources/news.mp3")
st.video("./resources/news.mp4")
#logo
st.logo("./resources/logo.png")
#表格
student_data={
    "姓名":["王琳","李牧晚","贝罗","茉莉海","实效"],
    "学号":["2026001","2026002","2026003","2026004","2026005"],
    "语文":[98,99,75,44,33],
    "数学":[34,55,89,66,89],
    "英语":[89,55,99,78,67]
}
st.table(student_data)
#输入框
name=st.text_input("请输入姓名")
st.write(f"您输入的姓名是{name}")
password=st.text_input("请输入密码",type="password")
st.write(f"您输入的密码是{password}")
#单选按钮

gender=st.radio("请输入您的性别",["男","女","未知"],index=1)
st.write(f"您的性别是:{gender}")