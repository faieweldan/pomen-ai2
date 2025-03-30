import streamlit as st

st.set_page_config(
    page_title="Pomen - AI Mechanic Platform",
    page_icon="🛠️",
)

st.title("🛠️ Welcome to Pomen!")
st.subheader("AI-powered. Scam-free. Your trusted car repair assistant.")

st.markdown("""
Pomen is a smart platform that connects vehicle owners with reliable mechanics.

🚗 Find nearby mechanics  
🤖 Use AI to predict car issues  
💬 Chat directly with technicians  
📢 Browse open repair tenders
""")

# Simulated tender data (later boleh pull dari database)
tender_data = [
    {"name": "rauhan", "car": "Proton Saga", "price": "RM 120", "role": "Customer", 'problem': 'engine overheating', "image": "https://linktoimage1.jpg"},
    {"name": "ruj", "car": "Myvi 1.5", "price": "RM 90", "role": "Mechanic", 'problem': 'kemek bos', "image": "https://linktoimage2.jpg"},
    {"name": "hariz", "car": "Axia", "price": "RM 100", "role": "Customer", 'problem': 'tak reti pasang taya', "image": "https://linktoimage3.jpg"},
]


# Save in session state
st.session_state["tenders"] = tender_data

if st.button("Get price estimates for your car issues!"):
    st.switch_page("pages/2_Model.py")