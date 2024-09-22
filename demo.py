import streamlit as st

# 在侧边栏中创建选择框
calculation_type = st.sidebar.selectbox("选择要计算的内容", ["BMI", "体脂"])

if calculation_type == "BMI":
    st.header("BMI 计算")

    # 输入身高和体重
    height = st.number_input("请输入身高（cm）", min_value=0.0, format="%.2f")
    weight = st.number_input("请输入体重（kg）", min_value=0.0, format="%.2f")

    # 如果输入的身高或体重为负数，显示报错提示
    if height <= 0 or weight <= 0:
        st.error("身高和体重必须为正数")
    else:
        # 计算BMI
        height_m = height / 100  # 转换为米
        bmi = weight / (height_m ** 2)
        st.write(f"您的 BMI 值为: {bmi:.2f}")

        # 判断BMI结果
        if bmi < 18.5:
            st.warning("您属于体重过轻")
        elif 18.5 <= bmi < 24.9:
            st.success("您的体重正常")
        elif 24.9 <= bmi < 29.9:
            st.warning("您属于超重")
        else:
            st.error("您属于肥胖")

elif calculation_type == "体脂":
    st.header("体脂 计算")

    # 输入BMI、年龄和性别
    bmi = st.number_input("请输入BMI值", min_value=0.0, format="%.2f")
    age = st.number_input("请输入年龄", min_value=0, format="%d")
    gender = st.selectbox("请选择性别", ["男性", "女性"])

    # 性别编码：男性为1，女性为0
    gender_value = 1 if gender == "男性" else 0

    # 计算体脂百分比
    body_fat = (1.2 * bmi) + (0.23 * age) - 5.4 - (10.8 * gender_value)
    st.write(f"您的体脂百分比为: {body_fat:.2f}%")

    # 根据体脂百分比判断
    if gender_value == 1:
        # 男性标准
        if body_fat < 10:
            st.warning("您的体脂率过低")
        elif 10 <= body_fat < 20:
            st.success("您的体脂率正常")
        else:
            st.error("您的体脂率偏高")
    else:
        # 女性标准
        if body_fat < 18:
            st.warning("您的体脂率过低")
        elif 18 <= body_fat < 25:
            st.success("您的体脂率正常")
        else:
            st.error("您的体脂率偏高")
