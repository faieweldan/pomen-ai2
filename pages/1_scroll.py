import streamlit as st

if "tenders" not in st.session_state:
    st.session_state["tenders"] = [
        {"name": "rauhan", "car": "Proton Saga", "price": "RM 120", "role": "Customer", 'problem': 'engine overheating', "image": "https://linktoimage1.jpg"},
        {"name": "ruj", "car": "Myvi 1.5", "price": "RM 90", "role": "Mechanic", 'problem': 'kemek bos', "image": "https://linktoimage2.jpg"},
        {"name": "hariz", "car": "Axia", "price": "RM 100", "role": "Customer", 'problem': 'tak reti pasang taya', "image": "https://linktoimage3.jpg"},
    ]

st.title("📢 Tender Feed")

st.markdown("""
Browse repair requests or offers posted by users and mechanics:
""")

# ---------- CSS Styling for Cards ----------
st.markdown("""
    <style>
    .card {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
        margin-bottom: 30px;
    }
    .card img {
        border-radius: 10px;
        width: 100%;
    }
    .card h4 {
        margin-bottom: 5px;
        color: #FF4B4B;
    }
    .card p {
        margin: 0;
        font-size: 15px;
        color: #dddddd;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Display Tenders in Columns ----------
tenders = st.session_state["tenders"]
cols = st.columns(2)

for index, tender in enumerate(tenders):
    with cols[index % 2]:
        st.markdown(f"""
            <div class="card">
                <img src="{tender['image']}" alt="Car Photo">
                <h4>{tender['car']} - {tender['price']}</h4>
                <p><b>Posted by:</b> {tender['name']} ({tender['role']})</p>
                <p><b>Problem:</b> {tender['problem']}</p>
            </div>
        """, unsafe_allow_html=True)
        

