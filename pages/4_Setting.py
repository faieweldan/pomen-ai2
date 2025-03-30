import streamlit as st

st.set_page_config(page_title="Pomen - Settings", page_icon="⚙️", layout="centered")

# ---------- CSS Styling ----------
st.markdown("""
    <style>
    .section {
        background-color: #1e1e1e;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(0,0,0,0.2);
        margin-bottom: 30px;
    }

    .section h4 {
        color: #FF4B4B;
        margin-bottom: 10px;
    }

    .tender-card {
        background-color: #292929;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Settings Header ----------
st.title("⚙️ Settings")

# ---------- Currency Section ----------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("<h4>💱 Currency Preference</h4>", unsafe_allow_html=True)
currency = st.selectbox("Select your currency:", ["RM", "USD"])
st.success(f"Current currency: {currency}")
st.markdown('</div>', unsafe_allow_html=True)


