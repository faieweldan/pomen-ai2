import streamlit as st

st.set_page_config(page_title="Pomen - Diagnose Model", page_icon="🔧", layout="centered")

st.title("🔧 AI Diagnostic Model")
st.subheader("📸 Upload photo of your car issue")

# 🔒 SAFETY REMINDER FIRST
with st.expander("🛡️ **View Safety Instructions Before Uploading**", expanded=False):
    st.markdown("""
    **Please make sure you’ve done the following before using this feature:**

    - 🚘 **Stop your car at a safe location**, away from traffic. Avoid highway shoulder unless it’s an emergency.
    - ⚠️ **Turn on your hazard lights** to alert other drivers.
    - 🔥 **Switch off the engine** and let it cool down.
    - 🚷 **Do not touch** any moving or hot parts.
    - 📷 **Take a clear photo** from a safe distance. Avoid crawling under the car.
    - 📞 **Call for help** if the situation feels unsafe.

    Your safety is more important than any diagnosis. Pomen is here to assist, not replace emergency procedures.
    """)

# ---------- Styling ----------
st.markdown("""
    <style>
    .card {
        background-color: #1e1e1e;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(0,0,0,0.3);
        margin-top: 30px;
    }

    .card h3 {
        color: #FF4B4B;
    }

    .desc {
        font-size: 16px;
        color: #cccccc;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Page Content ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("<h3>📸 Upload a Photo of Your Car Issue</h3>", unsafe_allow_html=True)
st.markdown('<p class="desc">Snap a photo of the problem (e.g. engine leak, broken light) and let our AI assist in analyzing the issue.</p>', unsafe_allow_html=True)

# Upload image
uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "png"])

# buang kalau tak perlu
description = st.text_input("🔍 Briefly describe what’s wrong (optional)")

# If image uploaded
if uploaded_file:
    st.success("✅ Image uploaded successfully!")
    st.image(uploaded_file, caption="Uploaded Photo Preview", use_column_width=True)
    
    if description:
        st.markdown(f"📝 Description: *{description}*")

    # Placeholder: future Gemini response or model
    st.info("🚧 AI diagnosis feature coming soon...")
    
st.markdown("</div>", unsafe_allow_html=True)
