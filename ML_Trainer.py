import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# ১. ডেটাসেট তৈরি (Technical Implementation: Data Use)
# এই ডেটাগুলো দিয়ে মডেলটি শিখবে কোনটি সুস্থ আর কোনটি বিপদজনক অবস্থা
data = {
    'Heart_Rate': [72, 140, 45, 100, 160, 60, 110, 80],
    'Systolic_BP': [120, 170, 90, 145, 180, 110, 150, 120],
    'Glucose': [100, 250, 80, 210, 300, 90, 190, 105],
    'Condition': [0, 2, 2, 1, 2, 0, 1, 0] # 0=Stable, 1=Warning, 2=Critical
}

df = pd.DataFrame(data)

# ২. ফিচার এবং টার্গেট আলাদা করা
X = df[['Heart_Rate', 'Systolic_BP', 'Glucose']]
y = df['Condition']

# ৩. মডেল ট্রেইনিং (Innovation: Advanced Algorithm)
# আমরা Random Forest ব্যবহার করছি কারণ এটি মেডিকেল ডেটার জন্য খুব নির্ভরযোগ্য
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# ৪. মডেলটি সেভ করা (Scalability)
with open('medi_guardian_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ এআই মডেল সফলভাবে ট্রেইন করা হয়েছে এবং 'medi_guardian_model.pkl' নামে সেভ হয়েছে।")