import streamlit as st
import pandas as pd
import hashlib
import os
import time

# ==============================
# 🧠 CONFIGURATION
# ==============================
st.set_page_config(
    page_title="Login - Heart Attack Prediction",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==============================
# 🎨 CUSTOM STYLES
# ==============================
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stSidebar"] {display: none;}

.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
.navbar {
    position: fixed; top: 0; left: 0; right: 0;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    padding: 15px 50px;
    box-shadow: 0 2px 20px rgba(0,0,0,0.1);
    z-index: 999; display: flex; justify-content: space-between; align-items: center;
}
.navbar-brand {
    font-size: 1.8em; font-weight: bold; color: #003366; display: flex; align-items: center; gap: 10px;
}
.navbar-menu {display: flex; gap: 20px; align-items: center;}
.nav-link {
    color: #003366; text-decoration: none; font-weight: 600;
    font-size: 1.1em; padding: 8px 20px; border-radius: 8px; transition: all 0.3s ease;
}
.nav-link:hover {
    background: linear-gradient(90deg, #667eea, #764ba2);
    color: white; transform: translateY(-2px);
}
.main .block-container {padding-top: 100px;}
.icon-container {
    text-align: center; font-size: 5em; margin: 20px 0; animation: pulse 2s infinite;
}
@keyframes pulse {0%,100%{transform:scale(1);}50%{transform:scale(1.05);}}
.welcome-box {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white; padding: 30px; border-radius: 20px;
    text-align: center; margin: 20px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}
div.stButton > button {
    background: linear-gradient(90deg, #667eea, #764ba2);
    color: white; border: none; border-radius: 12px;
    padding: 0.8em 2em; font-size: 1.2em; font-weight: bold;
    transition: all 0.3s ease; width: 100%; box-shadow: 0 8px 20px rgba(102,126,234,0.3);
}
div.stButton > button:hover {
    background: linear-gradient(90deg, #764ba2, #667eea);
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

# ==============================
# 🧭 NAVBAR
# ==============================
st.markdown("""
<div class="navbar">
    <div class="navbar-brand">
        <span>❤️</span><span>Heart Health AI</span>
    </div>
    <div class="navbar-menu">
        <a href="/" target="_self" class="nav-link">🏠 Home</a>
        <a href="/Register" target="_self" class="nav-link">📝 Register</a>
        <a href="/Login" target="_self" class="nav-link">🔐 Login</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ==============================
# 🔐 AUTH FUNCTIONS
# ==============================
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    return make_hashes(password) == hashed_text

def check_user(email, password):
    if not os.path.exists("users.csv"):
        return False, None
    df = pd.read_csv("users.csv")
    user = df[df["Email"] == email]
    if len(user) == 1 and check_hashes(password, user.iloc[0]["Password"]):
        return True, user.iloc[0]["Username"]
    return False, None

# ==============================
# 🔐 LOGIN PAGE
# ==============================
if "logged_in" in st.session_state and st.session_state["logged_in"]:
    st.markdown('<div class="icon-container">✅</div>', unsafe_allow_html=True)
    st.markdown("<h1>You're Already Logged In!</h1>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="welcome-box">
        <h2>Welcome back, {st.session_state.get('username', 'User')}! 🎉</h2>
        <p>You're ready to start predicting heart attack risks.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("💖 Go to Prediction"):
            st.switch_page("pages/4_💖_Prediction.py")
    with col2:
        if st.button("🚪 Logout"):
            st.session_state.clear()
            st.success("✅ Logged out successfully!")
            st.rerun()

else:
    st.markdown('<div class="icon-container">🔐</div>', unsafe_allow_html=True)
    st.markdown("<h1>Welcome Back!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#fff;'>Login to access your health dashboard</p>", unsafe_allow_html=True)
    st.markdown("---")

    with st.form("login_form"):
        st.markdown("### 🔑 Enter Your Credentials")
        email = st.text_input("Email", placeholder="your.email@example.com")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        remember = st.checkbox("Remember me", value=True)
        submit = st.form_submit_button("🚀 Login")

        if submit:
            if not email or not password:
                st.error("❌ Please fill in all fields!")
            else:
                valid, username = check_user(email, password)
                if valid:
                    st.session_state["user"] = email
                    st.session_state["username"] = username
                    st.session_state["logged_in"] = True
                    st.success(f"✅ Welcome back, {username}! 🎉")
                    st.balloons()
                    time.sleep(2)
                    st.switch_page("pages/4_💖_Prediction.py")
                else:
                    st.error("❌ Invalid email or password!")

    st.markdown("---")
    st.markdown("<p style='color:white;text-align:center;'>Don't have an account?</p>", unsafe_allow_html=True)
    if st.button("📝 Register Now"):
        st.switch_page("pages/2_📝_Register.py")

# ==============================
# 📊 STATS + FOOTER
# ==============================
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("👥 Active Users", "120+", "+12")
with col2:
    st.metric("✅ Login Success", "98.5%", "+1.2%")
with col3:
    st.metric("⚡ Avg Response", "< 1s", "-0.2s")

st.info("🔒 **Security Notice:** Never share your password with anyone. We will never ask for it via email or phone.")
st.markdown("""
<div style="text-align:center;padding:20px;background:rgba(255,255,255,0.1);border-radius:15px;">
<p style="color:white;font-size:1em;">💖 Developed by <b>Manikandan</b> | Powered by AI & Streamlit 🚀</p>
</div>
""", unsafe_allow_html=True)
