import streamlit as st
from datetime import datetime

# Simulated tendors
matched_tendors = ['Tendor A', 'Tendor B', 'Tendor C']

st.sidebar.title("Messages")

# If no messages
if not matched_tendors:
    st.sidebar.info("You have no messages yet.")
    st.title("No active chats")
    st.stop()

# Store selection in session state
if "selected_tendor" not in st.session_state:
    st.session_state.selected_tendor = matched_tendors[0]

# Render sidebar buttons with ✅ and handle selection
for tendor in matched_tendors:
    is_selected = tendor == st.session_state.selected_tendor
    btn_label = f"🔘   {tendor}" if is_selected else tendor
    if st.sidebar.button(btn_label, use_container_width=True, key=f"tendor_btn_{tendor}"):
        st.session_state.selected_tendor = tendor
        st.rerun()

# Get current selected tendor
selected_tendor = st.session_state.selected_tendor

# Chat history state setup
if f"chat_{selected_tendor}" not in st.session_state:
    st.session_state[f"chat_{selected_tendor}"] = [
        {"sender": "system", "msg": "Hi! I'm interested in fixing your car.", "time": datetime.now().strftime("%H:%M")}
    ]

# Show chat title
st.title(f"{selected_tendor}")

# Scrollable chat window
chat_container = st.container()
with chat_container:
    for message in st.session_state[f"chat_{selected_tendor}"]:
        align = "right" if message["sender"] == "mechanic" else "left"
        bubble_color = "#DCF8C6" if align == "right" else "#FFFFFF"
        st.markdown(
            f"""
            <div style='text-align: {align}; margin: 5px 0;'>
                <span style='background-color: {bubble_color}; 
                        padding: 10px 15px; 
                        border-radius: 15px; 
                        display: inline-block; 
                        max-width: 70%; 
                        word-wrap: break-word;
                        color: black;'>
                    {message["msg"]}
                </span><br><small>{message["time"]}</small>
            </div>
            """,
            unsafe_allow_html=True
        )

# Input and Send
msg_key = f"input_{selected_tendor}"

with st.form(key=f"form_{selected_tendor}", clear_on_submit=True):
    new_msg = st.text_input("Type your message", key=msg_key)
    submitted = st.form_submit_button("Send")
    if submitted and new_msg.strip():
        st.session_state[f"chat_{selected_tendor}"].append({
            "sender": "mechanic",
            "msg": new_msg,
            "time": datetime.now().strftime("%H:%M")
        })
        st.rerun()