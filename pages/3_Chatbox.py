import streamlit as st
from datetime import datetime
import google.generativeai as genai
import os
import html  # Import the html module

# Load API key from Streamlit secrets or environment variables
if 'gemini_api_key' in st.secrets:  # Corrected key name
    GEMINI_API_KEY = st.secrets['gemini_api_key']  # Corrected key name
elif 'GEMINI_API_KEY' in os.environ:
    GEMINI_API_KEY = os.environ['GEMINI_API_KEY']
else:
    GEMINI_API_KEY = None
    st.error("Gemini API key not found. Please set it as a Streamlit secret or environment variable.")
    st.stop()  # Stop the app if the API key is missing

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash')  # Or the appropriate model
else:
    model = None


# Initialize function to act as Gemini AI for chat responses
def generate_response(prompt):
    """
    Function to generate responses using Gemini AI.
    """
    if model is None:
        return "Gemini AI is not initialized. Please check API key."

    try:
        response = model.generate_content(prompt)
        return response.text  # Access the text directly.  Handles safety filters automatically

    except Exception as e:
        return f"Error: {str(e)}"


# Simulated tendors (These should probably be pulled dynamically from tenders posted!)
matched_tendors = ['Tendor A', 'Tendor B', 'Tendor C']

st.sidebar.title("Messages")

# Check if selected_price exists in session_state (important!)
if "selected_price" in st.session_state:
    selected_price = st.session_state["selected_price"]
    st.write(f"Selected Price: ${selected_price['Price']}") # Displays selected price/reasoning
else:
    st.warning("No price selected yet. Please go back to the Diagnose Model page.")
    st.stop() # Prevent using the chat if no price is selected

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
    # INITIAL MESSAGE COMES FROM MECHANIC - Include data from selected_price!
    initial_message = f"Hi! I'm interested in fixing your car. Based on the images and description, I estimate the repair will cost ${selected_price['Price']}. Reasoning: {selected_price['reasoning']}. Thoughts?"
    st.session_state[f"chat_{selected_tendor}"] = [
        {"sender": "system", "msg": initial_message, "time": datetime.now().strftime("%H:%M")}
    ]

# Show chat title
st.title(f"{selected_tendor}")

# Scrollable chat window
chat_container = st.container()
with chat_container:
    for message in st.session_state[f"chat_{selected_tendor}"]:
        align = "right" if message["sender"] == "mechanic" else "left"
        bubble_color = "#DCF8C6" if align == "right" else "#FFFFFF"

        # Display the message bubble
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
                    {message["msg"]} </span>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Display the time separately, styled with <small>
        st.markdown(
            f"<div style='text-align: {align};'><small>{message['time']}</small></div>",
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

        # ----- Gemini AI Response -----
        # Construct a Prompt for Gemini AI
        user_message = new_msg
        context = f"""You are a mechanic negotiating with a customer about a car repair. Your initial estimate was ${selected_price['Price']} because {selected_price['reasoning']}. Be human-like, respond briefly, and decide whether to take the job or not. If the customer asks for a discount, you can offer a small discount, reject it, or suggest alternative solutions. If you don't want the job anymore, politely say you cannot do the repair at this moment."""

        prompt = f"{context}\nCustomer: {user_message}"

        # Generate the Gemini response
        ai_response = generate_response(prompt)

        # No need to escape if it doesn't fix the issue, and risks double escaping.
        #If that also doesn't work, try to add the line below
        #ai_response = ai_response.replace("</span","").replace("</div","")
        st.session_state[f"chat_{selected_tendor}"].append({
            "sender": "system",  # SYSTEM for AI messages
            "msg": ai_response,
            "time": datetime.now().strftime("%H:%M")  # ADD THE TIMESTAMPS
        })
        st.rerun()