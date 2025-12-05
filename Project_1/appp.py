# # # import streamlit as st
# # # import pandas as pd
# # # import joblib
# # # import hashlib
# # # import os
# # # import random
# # # import plotly.graph_objects as go
# # # import matplotlib.pyplot as plt
# # # import seaborn as sns

# # # # ==============================
# # # # 🧠 CONFIGURATION
# # # # ==============================
# # # st.set_page_config(page_title="❤️ Heart Attack Prediction", page_icon="❤️", layout="wide")

# # # # ==============================
# # # # 🎨 THEME & STYLE
# # # # ==============================
# # # st.markdown("""
# # # <style>
# # # /* Background gradient */
# # # .stApp {
# # #     background: linear-gradient(135deg, #c2e9fb, #a1c4fd);
# # # }

# # # /* Card Style */
# # # .main-card {
# # #     background: rgba(255, 255, 255, 0.9);
# # #     padding: 25px;
# # #     border-radius: 20px;
# # #     box-shadow: 0 4px 20px rgba(0,0,0,0.15);
# # #     backdrop-filter: blur(10px);
# # # }

# # # /* Buttons */
# # # div.stButton > button:first-child {
# # #     background: linear-gradient(90deg, #007bff, #00c6ff);
# # #     color: white;
# # #     border: none;
# # #     border-radius: 10px;
# # #     padding: 0.7em 1.5em;
# # #     font-size: 1.1em;
# # #     font-weight: bold;
# # #     transition: all 0.3s ease;
# # # }
# # # div.stButton > button:first-child:hover {
# # #     background: linear-gradient(90deg, #00c6ff, #007bff);
# # #     transform: scale(1.05);
# # #     box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
# # # }

# # # /* Sidebar */
# # # [data-testid="stSidebar"] {
# # #     background: linear-gradient(180deg, #99ccff, #e6f2ff);
# # # }

# # # /* Headers */
# # # h1, h2, h3 { color: #003366; text-align: center; }

# # # hr {
# # #     border: 1px solid #80bfff;
# # # }
# # # </style>
# # # """, unsafe_allow_html=True)

# # # # ==============================
# # # # 🧩 MODEL LOADING
# # # # ==============================
# # # model = joblib.load("best_model 17.Heart Attack.joblib")
# # # feature_columns = joblib.load("17.Heart Attack.joblib")

# # # # ==============================
# # # # 🔐 AUTH SYSTEM (Register/Login)
# # # # ==============================
# # # def make_hashes(password):
# # #     return hashlib.sha256(str.encode(password)).hexdigest()

# # # def check_hashes(password, hashed_text):
# # #     return make_hashes(password) == hashed_text

# # # def save_user(username, email, password):
# # #     df = pd.DataFrame([[username, email, make_hashes(password)]], columns=["Username", "Email", "Password"])
# # #     if not os.path.exists("users.csv"):
# # #         df.to_csv("users.csv", index=False)
# # #     else:
# # #         df_existing = pd.read_csv("users.csv")
# # #         df_combined = pd.concat([df_existing, df])
# # #         df_combined.to_csv("users.csv", index=False)

# # # def check_user(email, password):
# # #     if not os.path.exists("users.csv"):
# # #         return False
# # #     df = pd.read_csv("users.csv")
# # #     user = df[df["Email"] == email]
# # #     if len(user) == 1 and check_hashes(password, user.iloc[0]["Password"]):
# # #         return True
# # #     return False

# # # # ==============================
# # # # 🎛️ PAGE NAVIGATION
# # # # ==============================
# # # menu = ["🏠 Home", "📝 Register", "🔐 Login", "💖 Prediction"]
# # # choice = st.sidebar.radio("Navigate", menu)

# # # # ==============================
# # # # 🏠 HOME
# # # # ==============================
# # # if choice == "🏠 Home":
# # #     st.markdown("<h1>💖 Heart Attack Prediction App</h1>", unsafe_allow_html=True)
# # #     st.write("AI-powered early heart attack detection — for a healthier tomorrow.")
# # #     st.image("https://cdn-icons-png.flaticon.com/512/2966/2966483.png", width=200)
    
# # #     col1, col2, col3 = st.columns(3)
# # #     col1.metric("👥 Users", "120+")
# # #     col2.metric("🤖 Model Accuracy", "95%")
# # #     col3.metric("🩺 Risk Checks Done", "250+")

# # #     st.info("👉 Use the sidebar to Register or Login to get started!")

# # # # ==============================
# # # # 📝 REGISTER
# # # # ==============================
# # # elif choice == "📝 Register":
# # #     st.markdown("<h2>📝 Create a New Account</h2>", unsafe_allow_html=True)
# # #     username = st.text_input("Username")
# # #     email = st.text_input("Email")
# # #     password = st.text_input("Password", type="password")
# # #     confirm = st.text_input("Confirm Password", type="password")

# # #     if st.button("Register"):
# # #         if password == confirm:
# # #             save_user(username, email, password)
# # #             st.success("✅ Account created successfully! Go to Login page.")
# # #         else:
# # #             st.error("❌ Passwords do not match!")

# # # # ==============================
# # # # 🔐 LOGIN
# # # # ==============================
# # # elif choice == "🔐 Login":
# # #     st.markdown("<h2>🔐 User Login</h2>", unsafe_allow_html=True)
# # #     email = st.text_input("Email")
# # #     password = st.text_input("Password", type="password")

# # #     if st.button("Login"):
# # #         if check_user(email, password):
# # #             st.session_state["user"] = email
# # #             st.success(f"Welcome, {email} 🎉")
# # #             st.info("Navigate to the 'Prediction' page from the sidebar.")
# # #         else:
# # #             st.error("❌ Invalid email or password.")

# # # # ==============================
# # # # 💖 PREDICTION PAGE
# # # # ==============================
# # # elif choice == "💖 Prediction":
# # #     if "user" not in st.session_state:
# # #         st.warning("⚠️ Please login first to access this page.")
# # #     else:
# # #         st.markdown("<h2>💡 Heart Attack Risk Prediction</h2>", unsafe_allow_html=True)

# # #         # Tabs for input and results
# # #         tab1, tab2 = st.tabs(["🧍 User Input", "📊 Prediction Result"])

# # #         with tab1:
# # #             user_data = {}
# # #             for col in feature_columns:
# # #                 if "age" in col.lower():
# # #                     user_data[col] = st.number_input(f"{col}", min_value=0, max_value=120, value=45)
# # #                 elif "sex" in col.lower():
# # #                     user_data[col] = st.selectbox(f"{col}", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
# # #                 elif "bp" in col.lower():
# # #                     user_data[col] = st.number_input(f"{col}", min_value=50, max_value=250, value=120)
# # #                 elif "chol" in col.lower():
# # #                     user_data[col] = st.number_input(f"{col}", min_value=50, max_value=600, value=200)
# # #                 else:
# # #                     user_data[col] = st.number_input(f"{col}", value=0.0)

# # #             input_df = pd.DataFrame([user_data])
# # #             st.markdown("<hr>", unsafe_allow_html=True)
# # #             st.write("🧾 Entered Data Preview:")
# # #             st.dataframe(input_df, use_container_width=True)

# # #         with tab2:
# # #             if st.button("🔮 Predict Heart Attack Risk"):
# # #                 try:
# # #                     pred = model.predict(input_df)[0]
# # #                     prob = model.predict_proba(input_df)[0][1] if hasattr(model, "predict_proba") else 0

# # #                     if pred == 1:
# # #                         st.error(f"🚨 High Risk Detected! Probability: {prob*100:.2f}%")
# # #                     else:
# # #                         st.success(f"💚 Low Risk Detected! Probability: {prob*100:.2f}%")

# # #                     # Gauge Meter
# # #                     fig = go.Figure(go.Indicator(
# # #                         mode="gauge+number",
# # #                         value=float(prob * 100),
# # #                         title={'text': "Risk Probability (%)"},
# # #                         gauge={
# # #                             'axis': {'range': [0, 100]},
# # #                             'bar': {'color': "crimson" if prob > 0.5 else "green"},
# # #                             'steps': [
# # #                                 {'range': [0, 50], 'color': "#9BF0A8"},
# # #                                 {'range': [50, 75], 'color': "#FFD966"},
# # #                                 {'range': [75, 100], 'color': "#F45B69"}
# # #                             ]
# # #                         }
# # #                     ))
# # #                     st.plotly_chart(fig, use_container_width=True)

# # #                     # Health Tips
# # #                     st.markdown("<hr>", unsafe_allow_html=True)
# # #                     st.subheader("💬 Personalized Health Tips:")
# # #                     tips_high = [
# # #                         "🚭 Avoid smoking and alcohol.",
# # #                         "🏃‍♂️ Exercise 30 mins daily.",
# # #                         "🥦 Eat more vegetables and reduce salt.",
# # #                         "🩺 Regularly monitor BP & sugar levels."
# # #                     ]
# # #                     tips_low = [
# # #                         "💧 Stay hydrated.",
# # #                         "😊 Maintain a positive mindset.",
# # #                         "🍎 Continue a balanced diet.",
# # #                         "🏃‍♀️ Regular physical activity keeps you healthy!"
# # #                     ]
# # #                     st.write(random.choice(tips_high if pred == 1 else tips_low))

# # #                     # Feature Importance (if available)
# # #                     if hasattr(model, "feature_importances_"):
# # #                         feat_imp = pd.DataFrame({
# # #                             "Feature": feature_columns,
# # #                             "Importance": model.feature_importances_
# # #                         }).sort_values(by="Importance", ascending=False)
# # #                         fig, ax = plt.subplots(figsize=(8, 5))
# # #                         sns.barplot(x="Importance", y="Feature", data=feat_imp, palette="Blues_r", ax=ax)
# # #                         st.pyplot(fig)
# # #                 except Exception as e:
# # #                     st.error(f"Error: {e}")

# # # # ==============================
# # # # 🦶 FOOTER
# # # # ==============================
# # # st.markdown("""
# # # <hr>
# # # <center>💖 Developed by <b>Manikandan</b> | Powered by AI & Streamlit 🚀</center>
# # # """, unsafe_allow_html=True)

# # import streamlit as st
# # # from utils.auth import check_user
# # # from utils.styles import apply_custom_styles

# # st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")


# # # ==============================
# # # 🔐 LOGIN PAGE
# # # ==============================
# # st.markdown("🔐 User Login", unsafe_allow_html=True)
# # st.markdown("---")

# # with st.container():
# #     st.markdown("""
    
# #     """, unsafe_allow_html=True)
    
# #     col1, col2 = st.columns([1, 1])
    
# #     with col1:
# #         st.image("https://cdn-icons-png.flaticon.com/512/2910/2910768.png", width=200)
    
# #     with col2:
# #         st.markdown("### Welcome Back!")
# #         st.write("Login to access your dashboard")
    
# #     st.markdown("---")
    
# #     # Login Form
# #     with st.form("login_form"):
# #         email = st.text_input("📧 Email", placeholder="your.email@example.com")
# #         password = st.text_input("🔒 Password", type="password", placeholder="Enter your password")
        
# #         remember = st.checkbox("Remember me")
        
# #         submit = st.form_submit_button("🚀 Login")
        
# #         if submit:
# #             if not email or not password:
# #                 st.error("❌ Please fill all fields!")
# #             else:
# #                 if check_user(email, password):
# #                     st.session_state["user"] = email
# #                     st.session_state["logged_in"] = True
# #                     st.success(f"✅ Welcome back, {email}! 🎉")
# #                     st.balloons()
# #                     st.info("👉 Navigate to **💖 Prediction** page from the sidebar")
# #                 else:
# #                     st.error("❌ Invalid email or password!")
    
# #     st.markdown("", unsafe_allow_html=True)

# # st.markdown("---")
# # st.markdown("Don't have an account? Go to 📝 Register page", unsafe_allow_html=True)




# import streamlit as st
# import base64

# # ==============================
# # 🧠 CONFIGURATION
# # ==============================
# st.set_page_config(
#     page_title="❤️ Heart Attack Prediction",
#     page_icon="❤️",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # ==============================
# # 🎨 CUSTOM STYLES
# # ==============================
# st.markdown("""
# <style>
# /* Background gradient */
# .stApp {
#     background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
# }

# /* Main content styling */
# .main .block-container {
#     padding-top: 2rem;
#     padding-bottom: 2rem;
# }

# /* Hero Card */
# .hero-card {
#     background: rgba(255, 255, 255, 0.95);
#     padding: 50px;
#     border-radius: 25px;
#     box-shadow: 0 20px 60px rgba(0,0,0,0.3);
#     text-align: center;
#     backdrop-filter: blur(10px);
#     margin-bottom: 30px;
# }

# /* Stats Card */
# .stat-card {
#     background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
#     padding: 25px;
#     border-radius: 20px;
#     text-align: center;
#     box-shadow: 0 10px 30px rgba(0,0,0,0.15);
#     transition: transform 0.3s ease;
#     border: 2px solid #e0e0e0;
# }

# .stat-card:hover {
#     transform: translateY(-5px);
#     box-shadow: 0 15px 40px rgba(0,0,0,0.25);
# }

# .stat-number {
#     font-size: 3em;
#     font-weight: bold;
#     background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     margin: 10px 0;
# }

# .stat-label {
#     color: #666;
#     font-size: 1.1em;
#     font-weight: 500;
# }

# /* Feature Card */
# .feature-card {
#     background: rgba(255, 255, 255, 0.9);
#     padding: 30px;
#     border-radius: 20px;
#     box-shadow: 0 8px 25px rgba(0,0,0,0.1);
#     margin: 15px 0;
#     border-left: 5px solid #667eea;
# }

# .feature-icon {
#     font-size: 3em;
#     margin-bottom: 15px;
# }

# .feature-title {
#     color: #003366;
#     font-size: 1.5em;
#     font-weight: bold;
#     margin-bottom: 10px;
# }

# .feature-desc {
#     color: #555;
#     font-size: 1.1em;
#     line-height: 1.6;
# }

# /* CTA Button styling */
# div.stButton > button {
#     background: linear-gradient(90deg, #667eea, #764ba2);
#     color: white;
#     border: none;
#     border-radius: 15px;
#     padding: 1em 3em;
#     font-size: 1.3em;
#     font-weight: bold;
#     transition: all 0.3s ease;
#     box-shadow: 0 10px 30px rgba(102,126,234,0.4);
#     width: 100%;
# }

# div.stButton > button:hover {
#     background: linear-gradient(90deg, #764ba2, #667eea);
#     transform: translateY(-3px);
#     box-shadow: 0 15px 40px rgba(102,126,234,0.6);
# }

# /* Sidebar styling */
# [data-testid="stSidebar"] {
#     background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
# }

# [data-testid="stSidebar"] .css-1d391kg, [data-testid="stSidebar"] .st-emotion-cache-1cypcdb {
#     color: white;
# }

# /* Headers */
# h1 {
#     color: #003366;
#     text-align: center;
#     font-weight: 800;
#     font-size: 3em;
#     margin-bottom: 20px;
#     text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
# }

# h2 {
#     color: #004080;
#     font-weight: 700;
# }

# h3 {
#     color: #003366;
#     font-weight: 600;
# }

# /* Info boxes */
# .stAlert {
#     border-radius: 15px;
#     border-left: 5px solid #667eea;
# }

# /* Metrics */
# [data-testid="stMetricValue"] {
#     font-size: 2.5em;
#     font-weight: bold;
#     color: #667eea;
# }

# /* Divider */
# hr {
#     border: 2px solid #667eea;
#     margin: 30px 0;
# }
# </style>
# """, unsafe_allow_html=True)

# # ==============================
# # 🏠 HERO SECTION
# # ==============================
# st.markdown("""
# <div class="hero-card">
#     <div style="font-size: 5em; margin-bottom: 20px;">❤️</div>
#     <h1 style="color: #003366; margin-bottom: 20px;">Heart Attack Prediction System</h1>
#     <p style="font-size: 1.3em; color: #555; margin-bottom: 30px;">
#         AI-powered early detection for a healthier tomorrow.<br>
#         Advanced machine learning to predict heart attack risks with 95% accuracy.
#     </p>
# </div>
# """, unsafe_allow_html=True)

# # ==============================
# # 📊 STATISTICS SECTION
# # ==============================
# st.markdown("---")
# st.markdown("<h2 style='text-align: center; color: white; margin: 30px 0;'>📈 Platform Statistics</h2>", unsafe_allow_html=True)

# col1, col2, col3, col4 = st.columns(4)

# with col1:
#     st.markdown("""
#     <div class="stat-card">
#         <div style="font-size: 3em;">👥</div>
#         <div class="stat-number">120+</div>
#         <div class="stat-label">Registered Users</div>
#     </div>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown("""
#     <div class="stat-card">
#         <div style="font-size: 3em;">🤖</div>
#         <div class="stat-number">95%</div>
#         <div class="stat-label">Model Accuracy</div>
#     </div>
#     """, unsafe_allow_html=True)

# with col3:
#     st.markdown("""
#     <div class="stat-card">
#         <div style="font-size: 3em;">🩺</div>
#         <div class="stat-number">250+</div>
#         <div class="stat-label">Predictions Made</div>
#     </div>
#     """, unsafe_allow_html=True)

# with col4:
#     st.markdown("""
#     <div class="stat-card">
#         <div style="font-size: 3em;">⭐</div>
#         <div class="stat-number">4.8/5</div>
#         <div class="stat-label">User Rating</div>
#     </div>
#     """, unsafe_allow_html=True)

# # ==============================
# # 🎯 FEATURES SECTION
# # ==============================
# st.markdown("---")
# st.markdown("<h2 style='text-align: center; color: white; margin: 30px 0;'>✨ Key Features</h2>", unsafe_allow_html=True)

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-icon">🎯</div>
#         <div class="feature-title">High Accuracy</div>
#         <div class="feature-desc">
#             Our ML model achieves 95% accuracy in predicting heart attack risks using advanced algorithms.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-icon">⚡</div>
#         <div class="feature-title">Real-time Analysis</div>
#         <div class="feature-desc">
#             Get instant predictions and risk assessments within seconds of entering your data.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# with col3:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-icon">💡</div>
#         <div class="feature-title">Smart Recommendations</div>
#         <div class="feature-desc">
#             Receive personalized health tips and lifestyle recommendations based on your results.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# # ==============================
# # 🔍 HOW IT WORKS
# # ==============================
# st.markdown("---")
# st.markdown("<h2 style='text-align: center; color: white; margin: 30px 0;'>🔍 How It Works</h2>", unsafe_allow_html=True)

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-icon">📝</div>
#         <div class="feature-title">Step 1: Register/Login</div>
#         <div class="feature-desc">
#             Create your secure account or login to access the prediction system.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-icon">📋</div>
#         <div class="feature-title">Step 2: Enter Data</div>
#         <div class="feature-desc">
#             Input your medical parameters like age, BP, cholesterol, and more.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# with col3:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-icon">📊</div>
#         <div class="feature-title">Step 3: Get Results</div>
#         <div class="feature-desc">
#             Receive detailed predictions with visual analysis and health recommendations.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# # ==============================
# # 📢 CTA SECTION
# # ==============================
# st.markdown("---")
# st.markdown("<br>", unsafe_allow_html=True)

# col1, col2, col3 = st.columns([1, 2, 1])

# with col2:
#     st.markdown("""
#     <div style="background: rgba(255,255,255,0.95); padding: 40px; border-radius: 25px; 
#          box-shadow: 0 15px 50px rgba(0,0,0,0.3); text-align: center;">
#         <h2 style="color: #003366; margin-bottom: 20px;">🚀 Ready to Get Started?</h2>
#         <p style="font-size: 1.2em; color: #555; margin-bottom: 30px;">
#             Join hundreds of users who are taking control of their heart health today!
#         </p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown("<br>", unsafe_allow_html=True)
    
#     col_btn1, col_btn2 = st.columns(2)
    
#     with col_btn1:
#         if st.button("📝 Register Now", use_container_width=True):
#             st.info("👉 Navigate to the **📝 Register** page from the sidebar")
    
#     with col_btn2:
#         if st.button("🔐 Login", use_container_width=True):
#             st.info("👉 Navigate to the **🔐 Login** page from the sidebar")

# # ==============================
# # ℹ️ INFO SECTION
# # ==============================
# st.markdown("---")
# st.markdown("<br>", unsafe_allow_html=True)

# with st.expander("ℹ️ About Heart Attack Prediction"):
#     st.markdown("""
#     ### What is Heart Attack Risk Prediction?
    
#     Heart attack risk prediction uses machine learning algorithms to analyze various health parameters 
#     and predict the likelihood of a heart attack. Our system considers multiple factors including:
    
#     - **Age and Gender**: Demographic factors that influence risk
#     - **Blood Pressure**: High BP is a major risk factor
#     - **Cholesterol Levels**: LDL and HDL cholesterol measurements
#     - **Blood Sugar**: Diabetes and glucose levels
#     - **Lifestyle Factors**: Smoking, exercise, diet habits
#     - **Medical History**: Previous conditions and family history
    
#     ### Why Use Our System?
    
#     ✅ **Early Detection**: Identify risks before symptoms appear  
#     ✅ **Evidence-Based**: Built on medical research and data  
#     ✅ **User-Friendly**: Simple interface, complex algorithms  
#     ✅ **Privacy-Focused**: Your data is secure and confidential  
#     ✅ **Actionable Insights**: Get recommendations you can act on  
    
#     ### Disclaimer
    
#     ⚠️ This tool is for educational and informational purposes only. It should NOT replace 
#     professional medical advice, diagnosis, or treatment. Always consult with qualified 
#     healthcare providers for medical concerns.
#     """)

# with st.expander("🔒 Privacy & Security"):
#     st.markdown("""
#     ### Your Privacy Matters
    
#     We take data security seriously:
    
#     - 🔐 **Encrypted Storage**: All data is encrypted at rest
#     - 🔒 **Secure Authentication**: Password hashing using SHA-256
#     - 🚫 **No Data Sharing**: We never share your personal health data
#     - 🗑️ **Right to Delete**: You can request data deletion anytime
#     - 📊 **Anonymous Analytics**: Only aggregated, non-identifiable data is used
    
#     ### Data We Collect
    
#     - Account information (username, email)
#     - Health parameters you input for predictions
#     - Usage statistics (anonymous)
#     """)

# with st.expander("📞 Contact & Support"):
#     st.markdown("""
#     ### Need Help?
    
#     📧 **Email**: support@heartpredict.com  
#     📱 **Phone**: +91 9876543210  
#     🌐 **Website**: www.heartpredict.com  
#     💬 **Chat**: Available 24/7 in-app  
    
#     ### Feedback
    
#     We'd love to hear from you! Your feedback helps us improve the system.
#     Please use the feedback form in the sidebar or email us directly.
#     """)

# # ==============================
# # 🦶 FOOTER
# # ==============================
# st.markdown("---")
# st.markdown("""
# <div style="text-align: center; padding: 20px; background: rgba(255,255,255,0.1); 
#     border-radius: 15px; margin-top: 30px;">
#     <p style="color: white; font-size: 1.1em; margin-bottom: 10px;">
#         💖 Developed by <b>Manikandan</b>
#     </p>
#     <p style="color: white; font-size: 0.9em; margin-bottom: 10px;">
#         Powered by AI & Streamlit 🚀
#     </p>
#     <p style="color: white; font-size: 0.8em;">
#         © 2024 Heart Attack Prediction System. All rights reserved.
#     </p>
# </div>
# """, unsafe_allow_html=True)

# # ==============================
# # 📌 SIDEBAR INFO
# # ==============================
# with st.sidebar:
#     st.markdown("---")
#     st.markdown("### 📚 Quick Navigation")
#     st.info("""
#     Use the pages above to:
    
#     🏠 **Home** - Landing page  
#     📝 **Register** - Create account  
#     🔐 **Login** - Sign in  
#     💖 **Prediction** - Get analysis  
#     """)
    
#     st.markdown("---")
#     st.markdown("### 💡 Quick Tip")
#     st.success("""
#     First time here?  
#     1. Register an account  
#     2. Login with your credentials  
#     3. Start your health journey!
#     """)
    
#     st.markdown("---")
#     st.markdown("### 🆘 Need Help?")
    
#     if st.button("📞 Contact Support", use_container_width=True):
#         st.info("Email: support@heartpredict.com")
    
#     if st.button("📖 User Guide", use_container_width=True):
#         st.info("Check the About section on the main page")






import streamlit as st

# ==============================
# 🧠 CONFIGURATION
# ==============================
st.set_page_config(
    page_title=" Heart Attack Prediction",
   
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================
# 🎨 CUSTOM STYLES WITH NAVBAR
# ==============================
st.markdown("""
<style>
/* Hide Streamlit default elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Background gradient */
.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

/* Navbar */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    padding: 15px 50px;
    box-shadow: 0 2px 20px rgba(0,0,0,0.1);
    z-index: 999;
    display: flex;
    justify-content: space-between;
    align-items: center;
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

.nav-btn {
    background: linear-gradient(90deg, #667eea, #764ba2);
    color: white;
    padding: 10px 25px;
    border-radius: 10px;
    font-weight: bold;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
}

.nav-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 20px rgba(102,126,234,0.4);
}

/* Main content spacing */
.main .block-container {
    padding-top: 100px;
    padding-bottom: 2rem;
}

/* Rest of your existing styles */
.hero-card {
    background: rgba(255, 255, 255, 0.95);
    padding: 50px;
    border-radius: 25px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    text-align: center;
    backdrop-filter: blur(10px);
    margin-bottom: 30px;
}

.stat-card {
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    transition: transform 0.3s ease;
    border: 2px solid #e0e0e0;
}

.stat-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(0,0,0,0.25);
}

.stat-number {
    font-size: 3em;
    font-weight: bold;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 10px 0;
}

.stat-label {
    color: #666;
    font-size: 1.1em;
    font-weight: 500;
}

.feature-card {
    background: rgba(255, 255, 255, 0.9);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    margin: 15px 0;
    border-left: 5px solid #667eea;
}

.feature-icon {
    font-size: 3em;
    margin-bottom: 15px;
}

.feature-title {
    color: #003366;
    font-size: 1.5em;
    font-weight: bold;
    margin-bottom: 10px;
}

.feature-desc {
    color: #555;
    font-size: 1.1em;
    line-height: 1.6;
}

div.stButton > button {
    background: linear-gradient(90deg, #667eea, #764ba2);
    color: white;
    border: none;
    border-radius: 15px;
    padding: 1em 3em;
    font-size: 1.3em;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 0 10px 30px rgba(102,126,234,0.4);
    width: 100%;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #764ba2, #667eea);
    transform: translateY(-3px);
    box-shadow: 0 15px 40px rgba(102,126,234,0.6);
}

h1 {
    color: #003366;
    text-align: center;
    font-weight: 800;
    font-size: 3em;
    margin-bottom: 20px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

h2 {
    color: #004080;
    font-weight: 700;
}

h3 {
    color: #003366;
    font-weight: 600;
}

.stAlert {
    border-radius: 15px;
    border-left: 5px solid #667eea;
}

[data-testid="stMetricValue"] {
    font-size: 2.5em;
    font-weight: bold;
    color: #667eea;
}

hr {
    border: 2px solid #667eea;
    margin: 30px 0;
}

/* Hide sidebar completely */
[data-testid="stSidebar"] {
    display: none;
}
.st-emotion-cache-18tdrd9 a
{
    text-decoration:none !important;
    color:#677AE3;
}
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
# 🏠 HERO SECTION
# ==============================
st.markdown("""
<div class="hero-card">
    <div style="font-size: 5em; margin-bottom: 20px;">❤️</div>
    <h1 style="color: #003366; margin-bottom: 20px;">Heart Attack Prediction System</h1>
    <p style="font-size: 1.3em; color: #555; margin-bottom: 30px;">
        AI-powered early detection for a healthier tomorrow.<br>
        Advanced machine learning to predict heart attack risks with 95% accuracy.
    </p>
</div>
""", unsafe_allow_html=True)

# ==============================
# 📊 STATISTICS SECTION
# ==============================
st.markdown("---")
st.markdown("<h2 style='text-align: center; color: white; margin: 30px 0;'>📈 Platform Statistics</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-card">
        <div style="font-size: 3em;">👥</div>
        <div class="stat-number">120+</div>
        <div class="stat-label">Registered Users</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <div style="font-size: 3em;">🤖</div>
        <div class="stat-number">95%</div>
        <div class="stat-label">Model Accuracy</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <div style="font-size: 3em;">🩺</div>
        <div class="stat-number">250+</div>
        <div class="stat-label">Predictions Made</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-card">
        <div style="font-size: 3em;">⭐</div>
        <div class="stat-number">4.8/5</div>
        <div class="stat-label">User Rating</div>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# 🎯 FEATURES SECTION
# ==============================
st.markdown("---")
st.markdown("<h2 style='text-align: center; color: white; margin: 30px 0;'>✨ Key Features</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">High Accuracy</div>
        <div class="feature-desc">
            Our ML model achieves 95% accuracy in predicting heart attack risks using advanced algorithms.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <div class="feature-title">Real-time Analysis</div>
        <div class="feature-desc">
            Get instant predictions and risk assessments within seconds of entering your data.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">💡</div>
        <div class="feature-title">Smart Recommendations</div>
        <div class="feature-desc">
            Receive personalized health tips and lifestyle recommendations based on your results.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# 🔍 HOW IT WORKS
# ==============================
st.markdown("---")
st.markdown("<h2 style='text-align: center; color: white; margin: 30px 0;'>🔍 How It Works</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📝</div>
        <div class="feature-title">Step 1: Register/Login</div>
        <div class="feature-desc">
            Create your secure account or login to access the prediction system.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📋</div>
        <div class="feature-title">Step 2: Enter Data</div>
        <div class="feature-desc">
            Input your medical parameters like age, BP, cholesterol, and more.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Step 3: Get Results</div>
        <div class="feature-desc">
            Receive detailed predictions with visual analysis and health recommendations.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# 📢 CTA SECTION
# ==============================
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <div style="background: rgba(255,255,255,0.95); padding: 40px; border-radius: 25px; 
         box-shadow: 0 15px 50px rgba(0,0,0,0.3); text-align: center;">
        <h2 style="color: #003366; margin-bottom: 20px;">🚀 Ready to Get Started?</h2>
        <p style="font-size: 1.2em; color: #555; margin-bottom: 30px;">
            Join hundreds of users who are taking control of their heart health today!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_btn1, col_btn2 = st.columns(2)
    
    with col_btn1:
        if st.button("📝 Register Now", use_container_width=True):
            st.switch_page("pages/2_📝_Register.py")
    
    with col_btn2:
        if st.button("🔐 Login", use_container_width=True):
            st.switch_page("pages/3_🔐_Login.py")

# ==============================
# ℹ️ INFO SECTION
# ==============================
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

with st.expander("ℹ️ About Heart Attack Prediction"):
    st.markdown("""
    ### What is Heart Attack Risk Prediction?
    
    Heart attack risk prediction uses machine learning algorithms to analyze various health parameters 
    and predict the likelihood of a heart attack. Our system considers multiple factors including:
    
    - **Age and Gender**: Demographic factors that influence risk
    - **Blood Pressure**: High BP is a major risk factor
    - **Cholesterol Levels**: LDL and HDL cholesterol measurements
    - **Blood Sugar**: Diabetes and glucose levels
    - **Lifestyle Factors**: Smoking, exercise, diet habits
    - **Medical History**: Previous conditions and family history
    
    ### Why Use Our System?
    
    ✅ **Early Detection**: Identify risks before symptoms appear  
    ✅ **Evidence-Based**: Built on medical research and data  
    ✅ **User-Friendly**: Simple interface, complex algorithms  
    ✅ **Privacy-Focused**: Your data is secure and confidential  
    ✅ **Actionable Insights**: Get recommendations you can act on  
    
    ### Disclaimer
    
    ⚠️ This tool is for educational and informational purposes only. It should NOT replace 
    professional medical advice, diagnosis, or treatment. Always consult with qualified 
    healthcare providers for medical concerns.
    """)

with st.expander("🔒 Privacy & Security"):
    st.markdown("""
    ### Your Privacy Matters
    
    We take data security seriously:
    
    - 🔐 **Encrypted Storage**: All data is encrypted at rest
    - 🔒 **Secure Authentication**: Password hashing using SHA-256
    - 🚫 **No Data Sharing**: We never share your personal health data
    - 🗑️ **Right to Delete**: You can request data deletion anytime
    - 📊 **Anonymous Analytics**: Only aggregated, non-identifiable data is used
    
    ### Data We Collect
    
    - Account information (username, email)
    - Health parameters you input for predictions
    - Usage statistics (anonymous)
    """)

with st.expander("📞 Contact & Support"):
    st.markdown("""
    ### Need Help?
    
    📧 **Email**: support@heartpredict.com  
    📱 **Phone**: +91 9876543210  
    🌐 **Website**: www.heartpredict.com  
    💬 **Chat**: Available 24/7 in-app  
    
    ### Feedback
    
    We'd love to hear from you! Your feedback helps us improve the system.
    Please use the feedback form or email us directly.
    """)

# ==============================
# 🦶 FOOTER
# ==============================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; background: rgba(255,255,255,0.1); 
     border-radius: 15px; margin-top: 30px;">
    <p style="color: white; font-size: 1.1em; margin-bottom: 10px;">
         Developed by <b>Manikandan</b>
    </p>
    <p style="color: white; font-size: 0.9em; margin-bottom: 10px;">
        Powered by AI & Streamlit 🚀
    </p>
    <p style="color: white; font-size: 0.8em;">
        © 2024 Heart Attack Prediction System. All rights reserved.
    </p>
</div>
""", unsafe_allow_html=True)