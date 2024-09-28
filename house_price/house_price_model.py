# 导入必要的库
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
import pickle

# 加载加利福尼亚州房价数据集
data = fetch_california_housing()

# 转换为 pandas DataFrame 方便处理
df = pd.DataFrame(data.data, columns=data.feature_names)
df['price'] = data.target

# 定义特征和目标变量
X = df[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup']]
y = df['price']

# 分割数据为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练线性回归模型
model = LinearRegression()
model.fit(X_train, y_train)

# 保存模型
with open('california_house_price_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("success")#检查模型是否训练完成
