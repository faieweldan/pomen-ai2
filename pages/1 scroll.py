import streamlit as st

st.title("📢 Tender Feed")

st.markdown("Browse repair requests or offers posted by users and mechanics:")


# Simulated tender data (later boleh pull dari database)
tenders = [
    {"nama": "rauhan", "kereta": "Proton Saga", "harga": "RM 120", "role": "Customer", 'problem': 'engine overheating', "gambar": "https://linktoimage1.jpg"},
    {"nama": "ruj", "kereta": "Myvi 1.5", "harga": "RM 90", "role": "Pomen", 'problem' : 'kemek bos' ,"gambar": "https://linktoimage2.jpg"},
    {"nama": "hariz", "kereta": "Axia", "harga": "RM 100", "role": "Customer", 'problem' : 'tak reti pasang taya', "gambar": "https://linktoimage3.jpg"},
]

for tender in tenders:
    st.image(tender["gambar"], width=300)
    st.markdown(f"**Nama:** {tender['nama']}")
    st.markdown(f"**Kereta:** {tender['kereta']}")
    st.markdown(f"**Harga:** {tender['harga']}")
    st.markdown(f"**Role:** {tender['role']}")
    st.markdown(f"**Problem**: {tender['problem']}")
    st.markdown("---")
