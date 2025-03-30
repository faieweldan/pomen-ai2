import streamlit as st
import json
from google import genai
from PIL import Image
from pymongo import MongoClient
from datetime import datetime
import base64
from io import BytesIO

# --- MongoDB Setup ---
client = MongoClient(st.secrets["mongo_uri"])  # uses .streamlit/secrets.toml
db = client["carFix"]
collection = db["submissions"]

st.set_page_config(page_title="Pomen - Diagnose Model", page_icon="🔧", layout="centered")

st.title("🔧 AI Diagnostic Model")
st.subheader("📸 Upload photo of your car issue")

@st.cache_data
def evaluate_damage(image_bytes, extra_desc):
    """
    Evaluate damage by sending image and extra description.
    """
    # Open image from the raw bytes (wrap in BytesIO)
    pil_image = Image.open(BytesIO(image_bytes))
    prompt = f"""Give 3 prices for the damaged car. Describe car damage in the reasoning. Here are some additional details: {extra_desc}

    Return the output using this schema:
        [{{"Price": int, "reasoning": str}}]
    """
    
    client_ai = genai.Client(api_key=st.secrets["gemini_api_key"])
    response = client_ai.models.generate_content(
        model="gemini-2.5-pro-exp-03-25",
        contents=[prompt, pil_image])
    
    response_details = json.loads(response.text.replace("\n", "")[7:-3])
    return response_details

@st.cache_data  # 👈 Add the caching decorator
def update_list_tenders():
    temp = st.session_state.get("tenders", [])
    temp.append(st.session_state["selected_price"])
    st.session_state["tenders"] = temp
    return st.session_state["tenders"]

# 🔒 Safety Reminder
with st.expander("🛡 *View Safety Instructions Before Uploading*", expanded=False):
    st.markdown("""
    - 🚘 Stop your car at a safe location  
    - ⚠ Turn on hazard lights  
    - 🔥 Let engine cool  
    - 🚷 Do not touch hot parts  
    - 📷 Take photo safely  
    - 📞 Call for help if needed  
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
    .card h3 { color: #FF4B4B; }
    .desc { font-size: 16px; color: #cccccc; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# ---------- Page Content ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("<h3>📸 Upload a Photo of Your Car Issue</h3>", unsafe_allow_html=True)
st.markdown('<p class="desc">Snap a photo of the problem (e.g. engine leak, broken light) and let our AI assist in analyzing the issue.</p>', unsafe_allow_html=True)

# Upload image and read file bytes once
uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "png", "jpeg"])
description = st.text_input("🔍 Briefly describe what’s wrong (optional)")

if uploaded_file:
    file_bytes = uploaded_file.read()  # Read the file once and store it
    st.success("✅ Image uploaded successfully!")
    st.image(file_bytes, caption="Uploaded Photo Preview")

    if description:
        st.markdown(f"📝 Description: {description}")

    # Use the same file_bytes for evaluating damage
    res = evaluate_damage(file_bytes, description)
    # Store file_bytes in each response for later reference if needed
    for i in range(len(res)):
        res[i]["image"] = file_bytes

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
        # st.write(st.session_state["selected_price"])
        st.info(f"${st.session_state['selected_price']['Price']}\n{st.session_state['selected_price']['reasoning']}")

    # --------- Save to MongoDB + Go to Feed ---------
    if st.button("Publish"):
        # Use file_bytes to encode the image
        image_data = base64.b64encode(file_bytes).decode("utf-8")
        submission = {
            "image": image_data,
            "description": description,
            "rating_score": st.session_state["selected_price"]["Price"],
            "reasoning": st.session_state["selected_price"]["reasoning"],
            "submitted_at": datetime.now(),
            "username": st.experimental_user.name  # Save the user's username
        }
        collection.insert_one(submission)
        st.success("🚀 Published to MongoDB!")
        temp = st.session_state.get("tenders", [])
        temp.append(st.session_state["selected_price"])
        st.session_state["tenders"] = temp
        # update_list_tenders()
        st.switch_page("pages/1_Listing.py")

st.markdown("</div>", unsafe_allow_html=True)