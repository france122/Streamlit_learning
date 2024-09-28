# 导入必要的库
import streamlit as st
import numpy as np
import pickle
import pandas as pd
# 加载训练好的加利福尼亚房价预测模型
with open('california_house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit 应用
st.title("加利福尼亚州房价预测应用")

# 创建侧边栏输入表单
st.sidebar.title("输入变量")
MedInc = st.sidebar.slider("家庭收入中位数（单位：万美元）", 0.5, 15.0, 5.0)
HouseAge = st.sidebar.slider("房屋年龄（年）", 1, 100, 25)
AveRooms = st.sidebar.slider("平均房间数量", 1, 10, 5)
AveBedrms = st.sidebar.slider("平均卧室数量", 1, 5, 2)
Population = st.sidebar.slider("人口数量", 100, 40000, 3000)
AveOccup = st.sidebar.slider("平均居住人数", 1, 10, 3)


# 创建输入特征数组
input_features = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup]])

# 通过模型预测房价
predicted_price = model.predict(input_features)

# 展示预测结果
st.subheader(f"预测的房价为: ${predicted_price[0]*100000:.2f}")

# 展示模型系数（特征重要性）
st.subheader("特征重要性:")
st.bar_chart(pd.DataFrame(model.coef_, index=["家庭收入中位数", "房屋年龄", "平均房间数量", "平均卧室数量", "人口数量", "平均居住人数"], columns=["系数"]))
