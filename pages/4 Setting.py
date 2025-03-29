import streamlit as st

st.title("⚙️ Settings")

currency = st.selectbox("Choose your currency:", ["RM (Ringgit)", "USD ($)", "IDR (Rp)"])
st.success(f"Currency used: {currency}")

