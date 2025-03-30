import streamlit as st


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
        st.image(tender["image"], caption="Uploaded Photo Preview")
        st.markdown(f"""
            <div class="card">
                <h4> ${tender["Price"]} </h4>
                <p> {tender["reasoning"]} </h4>
            </div>
        """, unsafe_allow_html=True)
        if st.button("🛠️Pick tender"):
            st.switch_page("pages/3_Chatbox.py")
        

