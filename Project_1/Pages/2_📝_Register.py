import streamlit as st
import pandas as pd
import hashlib
import os
import re
import time

# ==============================
# 🧠 CONFIGURATION
# ==============================
st.set_page_config(
    page_title="Register - Heart Attack Prediction",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==============================
# 🎨 CUSTOM STYLES
# ==============================
st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
[data-testid="stSidebar"] {display: none;}

.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.navbar {
    position: fixed;
    top: 0; left: 0; right: 0;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    padding: 15px 50px;
    box-shadow: 0 2px 20px rgba(0,0,0,0.1);
    z-index: 999;
    display: flex; justify-content: space-between; align-items: center;
}

.navbar-brand {
    font-size: 1.8em;
    font-weight: bold;
    color: #003366;
    display: flex;
    align-items: center;
    gap: 10px;
}

.navbar-menu {
    display: flex;
    gap: 20px;
    align-items: center;
}

.nav-link {
    color: #003366;
    text-decoration: none;
    font-weight: 600;
    font-size: 1.1em;
    padding: 8px 20px;
    border-radius: 8px;
    transition: all 0.3s ease;
}

.nav-link:hover {
    background: linear-gradient(90deg, #667eea, #764ba2);
    color: white;
    transform: translateY(-2px);
}

.main .block-container {padding-top: 100px;}

.form-container {
    background: rgba(255, 255, 255, 0.95);
    padding: 50px;
    border-radius: 25px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    backdrop-filter: blur(10px);
}

h1 {color: #003366; text-align: center; font-weight: 800; margin-bottom: 10px;}

.stTextInput > div > div > input {
    border-radius: 12px;
    border: 2px solid #e0e0e0;
    padding: 12px;
    font-size: 1.1em;
    transition: all 0.3s ease;
}

.stTextInput > div > div > input:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102,126,234,0.1);
}

div.stButton > button {
    background: linear-gradient(90deg, #667eea, #764ba2);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.8em 2em;
    font-size: 1.2em;
    font-weight: bold;
    transition: all 0.3s ease;
    width: 100%;
    box-shadow: 0 8px 20px rgba(102,126,234,0.3);
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #764ba2, #667eea);
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(102,126,234,0.5);
}

.icon-container {
    text-align: center;
    font-size: 5em;
    margin: 20px 0;
    animation: bounce 2s infinite;
}

@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

hr {border: 1px solid rgba(255,255,255,0.3); margin: 30px 0;}
</style>
""", unsafe_allow_html=True)

# ==============================
# 🧭 NAVBAR
# ==============================
st.markdown("""
<div class="navbar">
    <div class="navbar-brand">
        <span>❤️</span>
        <span>Heart Health AI</span>
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

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def check_user_exists(email):
    if not os.path.exists("users.csv"):
        return False
    df = pd.read_csv("users.csv")
    return email in df["Email"].values

def save_user(username, email, password):
    df = pd.DataFrame([[username, email, make_hashes(password)]], columns=["Username", "Email", "Password"])
    if not os.path.exists("users.csv"):
        df.to_csv("users.csv", index=False)
    else:
        df_existing = pd.read_csv("users.csv")
        df_combined = pd.concat([df_existing, df], ignore_index=True)
        df_combined.to_csv("users.csv", index=False)

def validate_password_strength(password):
    if len(password) < 6:
        return False, "Password must be at least 6 characters long"
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one number"
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter"
    return True, "Strong password"

# ==============================
# 📝 REGISTRATION FORM
# ==============================
st.markdown('<div class="icon-container">📝</div>', unsafe_allow_html=True)
st.markdown("<h1>Create Your Account</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#666;font-size:1.2em;'>Join us to start your heart health journey</p>", unsafe_allow_html=True)
st.markdown("---")

with st.form("register_form", clear_on_submit=False):
    st.markdown("### 📋 Personal Information")
    username = st.text_input("Username", placeholder="Enter your username")
    email = st.text_input("Email", placeholder="your.email@example.com")
    password = st.text_input("Password", type="password", placeholder="Create a strong password")
    confirm = st.text_input("Confirm Password", type="password", placeholder="Re-enter your password")

    terms = st.checkbox("I agree to the Terms & Conditions and Privacy Policy")
    submit = st.form_submit_button("🚀 Create Account", use_container_width=True)

    if submit:
        if not username or not email or not password or not confirm:
            st.error("❌ Please fill in all fields!")
        elif not validate_email(email):
            st.error("❌ Invalid email format!")
        elif check_user_exists(email):
            st.error("❌ This email is already registered!")
        elif not validate_password_strength(password)[0]:
            st.error(f"❌ {validate_password_strength(password)[1]}")
        elif password != confirm:
            st.error("❌ Passwords do not match!")
        elif not terms:
            st.warning("⚠️ Please accept the Terms & Conditions")
        else:
            save_user(username, email, password)
            st.success("✅ Account created successfully!")
            st.balloons()
            st.info("🎉 Redirecting to login page...")
            time.sleep(2)
            st.switch_page("pages/3_🔐_Login.py")

st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.write("Already have an account?")
with col2:
    if st.button("🔐 Go to Login", use_container_width=True, key="goto_login"):
        st.switch_page("pages/3_🔐_Login.py")

st.markdown("---")
st.markdown("""
<div style="text-align:center;padding:20px;color:white;">
💖 Developed by <b>Manikandan</b> | Powered by AI & Streamlit 🚀
</div>
""", unsafe_allow_html=True)
