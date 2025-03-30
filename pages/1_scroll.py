import streamlit as st

st.title("📢 Tender Feed")

st.markdown("Browse repair requests or offers posted by users and mechanics:")

for tender in st.session_state["tenders"]:
    st.image(tender["image"], width=300)
    st.markdown(f"**Name:** {tender['name']}")
    st.markdown(f"**Car:** {tender['car']}")
    st.markdown(f"**Price:** {tender['price']}")
    st.markdown(f"**Role:** {tender['role']}")
    st.markdown(f"**Problem:** {tender['problem']}")
    st.markdown("---")


