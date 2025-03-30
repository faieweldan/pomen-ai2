import streamlit as st  

st.markdown("### 📸 Upload a Photo of Your Car Issue")
uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "png"])

if uploaded_file:
    st.success("Image uploaded successfully!")
    st.image(uploaded_file, caption="Uploaded Photo Preview", use_column_width=True)
