import streamlit as st

st.set_page_config(
    page_title="Pomen - AI Mechanic Platform",
    page_icon="🛠️",
    layout="centered"
)

# --------- Custom CSS for style + background image ---------
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1612817159948-d6e3022f9057?auto=format&fit=crop&w=1350&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .big-font {
        font-size: 42px !important;
        font-weight: bold;
        text-align: center;
        margin-top: 30px;
    }

    .subtle {
        color: #dddddd;
        font-size: 18px;
        text-align: center;
        margin-bottom: 10px;
    }

    .desc {
        text-align: center;
        font-size: 16px;
        color: #eeeeee;
        max-width: 700px;
        margin: 0 auto;
        margin-bottom: 40px;
    }

    .feature-list {
        font-size: 18px;
        line-height: 1.8;
        text-align: center;
        color: white;
    }

    div.stButton > button:first-child {
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        box-shadow: 0px 5px 10px rgba(0,0,0,0.2);
        margin-top: 50px;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #ff2e2e;
        transform: scale(1.03);
    }
    </style>
""", unsafe_allow_html=True)

# --------- Main Content ---------
st.markdown('<p class="big-font">🛠️ Welcome to Pomen!</p>', unsafe_allow_html=True)
st.markdown('<p class="subtle">AI-powered. Scam-free. Your trusted car repair assistant.</p>', unsafe_allow_html=True)
st.markdown('<p class="desc">Pomen is a smart, all-in-one platform that helps vehicle owners quickly find trusted mechanics, predict car issues using AI, and manage repair needs — all in one place.</p>', unsafe_allow_html=True)

# --------- Feature Points ---------
st.markdown("""
<div class="feature-list">
🚗 Find nearby mechanics<br>
🤖 Predict issues with Gemini AI<br>
💬 Chat with technicians instantly<br>
📢 Browse open repair tenders
</div>
""", unsafe_allow_html=True)

# --------- Tender Data ---------
if "tenders" not in st.session_state:
    st.session_state["tenders"] = [
        {
            "name": "Rifaie",
            "car": "BMW 320i",
            "price": "RM 850",
            "role": "Customer",
            "problem": "check engine light keeps turning on",
            "image": "https://upload.wikimedia.org/wikipedia/commons/3/38/2019_BMW_320i_M_Sport_2.0_Front.jpg"
        },
        {
            "name": "Ali",
            "car": "Perodua Alza",
            "price": "RM 230",
            "role": "Mechanic",
            "problem": "replace aircond compressor",
            "image": "https://paultan.org/image/2022/06/2022-Perodua-Alza-render-f.jpg"
        },
        {
            "name": "Abu",
            "car": "Proton X50",
            "price": "RM 300",
            "role": "Customer",
            "problem": "weird noise near left tyre",
            "image": "https://www.proton.com/-/media/project/proton/car-models/x50/gallery/x50gallery03.jpg"
        },
        {
            "name": "Ruj",
            "car": "Myvi 1.5 SE",
            "price": "RM 90",
            "role": "Mechanic",
            "problem": "kemek bos",
            "image": "https://paultan.org/image/2022/12/2022-Perodua-Myvi-1.5-AV-Malaysia_Ext-1_BM-e1653047441721.jpg"
        },
        {
            "name": "Hariz",
            "car": "Axia",
            "price": "RM 100",
            "role": "Customer",
            "problem": "tak reti pasang tayar",
            "image": "https://paultan.org/image/2023/02/2023-Perodua-Axia-1.0-AV-Exterior_Ext-1_BM-630x420.jpg"
        },
        {
            "name": "Ain",
            "car": "Perodua Bezza",
            "price": "RM 180",
            "role": "Customer",
            "problem": "brake pedal rasa longgar",
            "image": "https://paultan.org/image/2020/01/2020-Perodua-Bezza-1.3-AV_Ext-1_BM-e1580012260769.jpg"
        },
    ]


st.session_state["tenders"] = st.session_state["tenders"]

# --------- Button ---------
if st.button("🚘 Get price estimates for your car issues!"):
    st.switch_page("pages/2_Model.py")
