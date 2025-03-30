import streamlit as st
import json
from google import genai
from PIL import Image

st.set_page_config(page_title="Pomen - Diagnose Model", page_icon="🔧", layout="centered")

st.title("🔧 AI Diagnostic Model")
st.subheader("📸 Upload photo of your car issue")

@st.cache_data
def evaluate_damage(_im, _extra_desc):

    prompt = f"""Give 3 prices for the damage car. Here are some additional details: {_extra_desc}

    Return the output using this schema:
        [{{"Price": int,"reasoning": str}}]
    """
    
    client = genai.Client(api_key=st.secrets["gemini_api_key"])
    response = client.models.generate_content(
        model="gemini-2.5-pro-exp-03-25",
        contents=[prompt, _im])
    
    response_details = json.loads(response.text.replace("\n", "")[7:-3])
    return response_details

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
uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "png", "jpeg"])

# buang kalau tak perlu
description = st.text_input("🔍 Briefly describe what’s wrong (optional)")

# If image uploaded
if uploaded_file:
    st.success("✅ Image uploaded successfully!")
    st.image(uploaded_file, caption="Uploaded Photo Preview")
    
    if description:
        st.markdown(f"📝 Description: *{description}*")

    res = evaluate_damage(Image.open(uploaded_file), description)
    for i in range(len(res)):
        res[i]["image"] = uploaded_file

    st.session_state['selected_price'] = res[0]

    # Placeholder: future Gemini response or model
    st.info("🚧 Select the price you are willing to pay:")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        button1 = st.button('Price 1')

    with col2:
        button2 = st.button('Price 2')

    with col3:
        button3 = st.button('Price 3')


    if button1:
        st.session_state['selected_price'] = res[0]

    if button2:
        st.session_state['selected_price'] = res[1]

    if button3:
        st.session_state['selected_price'] = res[2]

    if "selected_price" in st.session_state:
        st.write(st.session_state["selected_price"])
        st.info(f"${st.session_state["selected_price"]["Price"]}\n{st.session_state["selected_price"]["reasoning"]}")

    # --------- Button ---------
    if st.button("Publish"):
        temp = st.session_state["tenders"]
        temp.append(st.session_state["selected_price"])
        st.session_state["tenders"] = temp
        st.switch_page("pages/1_scroll.py")



    
st.markdown("</div>", unsafe_allow_html=True)
