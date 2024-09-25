import streamlit as st

# 设置页面标题
st.title("欢迎来到 Streamlit 介绍网站")
st.write("我是北京大学信息管理系的本科生，在上机器学习课程时学习了如何使用 Streamlit。这个网站是我用 Streamlit 搭建的，既是自己的一次实践锻炼，也希望能帮助大家更好地了解 Streamlit。")

# 侧边栏目录
st.sidebar.title("目录")

# 一级标题
st.sidebar.markdown("### 1. What is Streamlit")

# 一级标题
st.sidebar.markdown("### 2. Why Streamlit?")

# 二级标题（带缩进）
st.sidebar.markdown("&nbsp;&nbsp;&nbsp;&nbsp;**2.1 Streamlit的主要特点**")
st.sidebar.markdown("&nbsp;&nbsp;&nbsp;&nbsp;**2.2 Streamlit在机器学习中的应用领域**")
st.sidebar.markdown("&nbsp;&nbsp;&nbsp;&nbsp;**2.3 使用Streamlit的具体案例介绍**")

# 一级标题
st.sidebar.markdown("### 3. How to use Streamlit")

# 二级标题（带缩进）
st.sidebar.markdown("&nbsp;&nbsp;&nbsp;&nbsp;**3.1 安装方法**")
st.sidebar.markdown("&nbsp;&nbsp;&nbsp;&nbsp;**3.2 一个自己做的小的Streamlit demo**")
st.sidebar.markdown("&nbsp;&nbsp;&nbsp;&nbsp;**3.3 Streamlit的部署与分享**")

# 一级标题
st.sidebar.markdown("### 4. Get started immediately!")
# What is Streamlit
st.header("1. What is Streamlit")
st.write("""
Streamlit 是一个开源应用框架，可以帮助你快速创建和分享数据应用。
它允许数据科学家和机器学习工程师将 Python 脚本转化为漂亮的网页应用。""")
st.write("""
Streamlit 于 2019 年 10 月正式发布。它的目标是简化数据应用的构建过程，
自发布以来，Streamlit 迅速获得了广泛的关注和使用，热度不断飙升（图1展示了streamlit的GitHub stars变化情况，数据来源：https://star-history.com/#streamlit/streamlit&Date ），
成为数据可视化和机器学习应用开发的热门工具。""")
st.image("imgs/star-history.png")

# Why Streamlit?
st.header("2. Why Streamlit?")
st.subheader("2.1 Streamlit的主要特点")
st.markdown("""
- **简单易用**：使用简单的 Python 代码构建应用。
- **实时更新**：在数据变化时自动更新应用。
- **交互性**：内置多种控件，允许用户与应用进行互动。
- **分享方便**：可以轻松分享你的应用，支持多种部署方式。
""")
st.subheader("2.2 Streamlit在机器学习中的应用领域")
st.markdown("""
- **数据集的探索分析**:
在数据科学过程中，数据探索是前期的关键环节。Streamlit可以用来快速进行数据集分析，让用户通过选择不同的可视化方式（如散点图、柱状图等）来分析数据集的特征。这种探索过程有助于发现数据中的潜在规律和异常值。

- **超参数调优**:
超参数调优是机器学习中提升模型性能的重要步骤。通过Streamlit，用户可以创建交互式界面，让用户在应用中选择不同的超参数组合。实时反馈的可视化效果使得用户能够直观地了解参数变化对模型性能的影响。

- **模型展示与分享**:
在机器学习项目中，模型的效果展示至关重要。使用Streamlit，数据科学家可以创建直观的仪表板，展示模型的训练过程和结果。例如，用户可以上传数据集，选择不同的算法进行训练，并通过图表实时显示模型的性能指标（如准确率、损失值等）。

- **部署与分享**:
Streamlit应用程序可以轻松部署到云平台上，让更多用户访问和使用。开发者只需将代码推送到GitHub，使用Streamlit Cloud等工具，就可以将应用快速上线。这样的分享机制大大促进了团队之间的合作和交流。""")
st.subheader("2.3 使用Streamlit的具体案例介绍")


# How to use
st.header("3. How to use Streamlit")
st.subheader("3.1 安装方法")
st.write("安装方法，命令行输入(下载时间较长，请耐心等待，如有需要可以先建立虚拟环境，然后在虚拟环境中下载)")
st.code("pip install streamlit")
st.write("下载完成后可输入“streamlit hello”进行检验，如成功下载将跳转至以下界面")
st.image("imgs/官方网站.png")
st.write("在这可以观看官网给的几个使用demo，然后新建py文件，在终端输入以下代码即可用streamlit实现自己的网址功能")
st.code('streamlit run xxx.py')
st.subheader("3.2 几个自己做的小的Streamlit demo")
st.image("imgs/demo网站.png")
st.write("用streamlit实现计算bmi和体脂的功能，代码见demo.py")
st.image()
st.subheader("3.3 Streamlit的部署与分享")
st.write("streamlit的部署方法有很多种，例如Streamlit Sharing,Heroku,Docker,AWS,Google Cloud或Azure，现在着重介绍下Streamlit Sharing")
st.write("首先打开官网https://share.streamlit.io/ ， 注册账号管理GitHub，然后就可以manage app，值得注意的是需要在自己的仓库中写好requirements.txt，否则会报ModuleNotFound Error;另外flask建构的网站是不能部署在Streamlit cloud上的，必须严格是使用Streamlit函数的才可以，否则会出现以下错误")
st.image("imgs/ValueError.png")
st.write("部署好后可以把链接分享给好友，可以选择general，任何拿到链接的人都可以访问，也可以选择只有被邀请的人才能访问")

# conclusion
st.header("4. Get started immediately!")
st.write("访问 [Streamlit 官方网站](https://streamlit.io) 了解更多信息。")
st.write("官方api参考：https://docs.streamlit.io/develop/api-reference")
st.write("streamlit中文版学习文档：http://cw.hubwiz.com/card/c/streamlit-manual/1/2/3/" )

