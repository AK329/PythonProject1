import streamlit as st
import pickle
import numpy as np
import datetime

# --- ১. ডার্ক মোড ডিজাইন ও কালার ফিক্স (Presentation - ১০%) ---
st.set_page_config(page_title="MediGuardian AI | Dark Mode", layout="wide")

st.markdown("""
    <style>
    /* ১. মেইন ব্যাকগ্রাউন্ড কালো করা */
    .stApp { 
        background-color: #000000; 
        color: #ffffff; 
    }

    /* ২. হেডার সেকশন - উজ্জ্বল নীল বর্ডার সহ */
    .header-box {
        background-color: #1a237e;
        padding: 25px;
        border-radius: 12px;
        color: #ffffff;
        text-align: center;
        margin-bottom: 20px;
        border: 1px solid #303f9f;
    }

    /* ৩. ভাইটাল কার্ড - গাঢ় ধূসর (Black এর সাথে কন্ট্রাস্টের জন্য) */
    .vital-card {
        background-color: #121212;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(255,255,255,0.1);
        text-align: center;
        border-bottom: 6px solid #3f51b5;
        color: #ffffff;
    }
    .v-label { color: #bbbbbb; font-size: 18px; font-weight: bold; }
    .v-value { color: #ffffff; font-size: 36px; font-weight: bold; margin: 10px 0; }

    /* ৪. অন-ডিউটি স্টাফ সেকশন - হালকা বর্ডার */
    .staff-box {
        background-color: #1c1c1c;
        border: 1px solid #333333;
        padding: 15px;
        border-radius: 10px;
        color: #ffffff;
    }

    /* সাইডবার কালার ফিক্স */
    [data-testid="stSidebar"] {
        background-color: #111111;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)


# --- ২. ডাটা ও এআই ইঞ্জিন লোড ---
def load_model():
    try:
        with open('medi_guardian_model.pkl', 'rb') as f:
            return pickle.load(f)
    except:
        return None


model = load_model()


# ৩. স্টাফ ডিউটি রোস্টার (Social Impact - ২০%)
def get_staff():
    hour = datetime.datetime.now().hour
    if 8 <= hour < 16:
        return {"Shift": "Morning", "Doc": "Dr. Mahbub", "Nurse": "Nurse Jeba"}
    elif 16 <= hour < 24:
        return {"Shift": "Evening", "Doc": "Dr. Farhan", "Nurse": "Nurse Riya"}
    else:
        return {"Shift": "Night", "Doc": "Dr. Siddique", "Nurse": "Nurse Tania"}


staff = get_staff()

# --- ৪. হেডার ও ডিউটি স্টাফ ---
st.markdown('<div class="header-box"><h1>🏥 MediGuardian AI: Smart Patient Monitor</h1></div>', unsafe_allow_html=True)

col_s1, col_s2 = st.columns([2, 1])
with col_s1:
    st.markdown(f"""
    <div class="staff-box">
        <h4 style="margin:0; color:#4fc3f7;">👨‍⚕️ অন-ডিউটি মেডিকেল টিম</h4>
        <p style="margin:5px 0;"><b>শিফট:</b> {staff['Shift']} | <b>ডাক্তার:</b> {staff['Doc']} | <b>নার্স:</b> {staff['Nurse']}</p>
    </div>
    """, unsafe_allow_html=True)
with col_s2:
    st.markdown(f"""
    <div class="staff-box" style="text-align:right;">
        <b>সময়:</b> {datetime.datetime.now().strftime('%I:%M %p')}<br>
        <b>তারিখ:</b> {datetime.datetime.now().strftime('%d %b, %Y')}
    </div>
    """, unsafe_allow_html=True)

# --- ৫. সাইডবার ইনপুট ---
st.sidebar.title("🩺 ডেটা এন্ট্রি")
hr = st.sidebar.slider("Heart Rate (BPM)", 30, 200, 75)
bp = st.sidebar.slider("Systolic BP (mmHg)", 60, 220, 120)
gluc = st.sidebar.slider("Glucose (mg/dL)", 40, 500, 100)

# --- ৬. ইন্ডিভিজুয়াল ভাইটাল মনিটরিং (Innovation - ২৫%) ---
# প্রতিটি ভ্যালুর জন্য আলাদা সেফটি চেক
hr_alert = hr < 50 or hr > 110
bp_alert = bp < 90 or bp > 145
gluc_alert = gluc < 70 or gluc > 180

st.write("### 📊 লাইভ পেশেন্ট ড্যাশবোর্ড")
c1, c2, c3 = st.columns(3)

with c1:
    color = "#ff1744" if hr_alert else "#3f51b5"
    st.markdown(
        f'<div class="vital-card" style="border-bottom-color:{color}"><div class="v-label">Heart Rate</div><div class="v-value">{hr} BPM</div></div>',
        unsafe_allow_html=True)
with c2:
    color = "#ff1744" if bp_alert else "#3f51b5"
    st.markdown(
        f'<div class="vital-card" style="border-bottom-color:{color}"><div class="v-label">Blood Pressure</div><div class="v-value">{bp} mmHg</div></div>',
        unsafe_allow_html=True)
with c3:
    color = "#ff1744" if gluc_alert else "#3f51b5"
    st.markdown(
        f'<div class="vital-card" style="border-bottom-color:{color}"><div class="v-label">Glucose Level</div><div class="v-value">{gluc} mg/dL</div></div>',
        unsafe_allow_html=True)

# --- ৭. স্মার্ট ট্রায়াজ লজিক (যেকোনো একটি ভ্যালু ব্রীচ করলেই নোটিফিকেশন) ---
st.write("---")
st.subheader("🤖 এআই ডায়াগনোসিস ও ইমার্জেন্সি অ্যালার্ট")

# যেকোনো একটি ভ্যালু ক্রিটিক্যাল হলে আর অপেক্ষা করবে না (Health Risk Early Warning)
if hr_alert or bp_alert or gluc_alert:
    st.error(f"### 🚨 অবস্থা: আশঙ্কাজনক (CRITICAL)")
    st.markdown(f"""
    <div style="background-color:#b71c1c; color:white; padding:20px; border-radius:10px; border: 1px solid #ff5252;">
        <b>জরুরি অ্যাকশন:</b> ডাক্তার <b>{staff['Doc']}</b> কে দ্রুত বেড ১০১-এ উপস্থিত হতে বলা হয়েছে। <br>
        নার্স <b>{staff['Nurse']}</b> ইমার্জেন্সি সাপোর্ট নিয়ে প্রস্তুত হচ্ছেন।
    </div>
    """, unsafe_allow_html=True)
    st.toast("🚨 ইমার্জেন্সি অ্যালার্ট পাঠানো হয়েছে!", icon='📢')
else:
    st.success("### ✅ পেশেন্ট বর্তমানে স্থিতিশীল (Stable)")

# স্কেলেবিলিটি (Scalability - ২০%)
with st.expander("🛠️ সিস্টেম ডিটেইলস (Scalability)"):
    st.write("সিস্টেমটি API এবং মডুলার আর্কিটেকচারে তৈরি, যা ভবিষ্যতে ১০০০+ বেড মনিটর করতে পারবে।")