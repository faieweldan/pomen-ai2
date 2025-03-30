import streamlit as st

st.title("⚙️ Settings")

# Currency switcher
currency = st.selectbox("Select your currency:", ["RM", "USD"])
st.success(f"Current currency: {currency}")

# Access tender data from session safely
if "tenders" in st.session_state:
    tenders = st.session_state["tenders"]
    
    if tenders:
        st.markdown("### 📋 Active Tender Info (from session state):")
        for t in tenders:
            st.markdown(f"- {t['name']} | {t['car']} | {t['price']} | {t['problem']}")
else:
    st.warning("Tender data not found. Please open the Tender Feed page first.")
