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

# 📸 Image Uploader
st.markdown("### 📸 Upload a Photo of Your Car Issue")
uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "png"])

if uploaded_file:
    st.success("Image uploaded successfully!")
    st.image(uploaded_file, caption="Uploaded Photo Preview", use_column_width=True)
