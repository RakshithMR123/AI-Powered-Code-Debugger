import streamlit as st
import importlib
import back as bk  # Your backend code

# Force reload backend
importlib.reload(bk)

# Page setup
st.set_page_config(
    page_title="AI Code Debugger",
    layout="wide",
    page_icon="🛠️"
)

# ----------------- Custom CSS for Stylish UI -----------------
st.markdown("""
    <style>
        /* Background gradient */
        body, .block-container {
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            color: #ffffff;
        }
        /* Title styling */
        .stMarkdown h1 {
            font-size: 3rem;
            color: #ffffff;
            text-align: center;
            font-weight: bold;
        }
        .stMarkdown p {
            font-size: 1.2rem;
            text-align: center;
            color: #e0e0e0;
        }
        hr {
            border: 2px solid #ffffff;
            margin: 20px 0;
        }
        /* Text area styling */
        .stTextArea>div>div>textarea {
            font-family: 'Courier New', monospace;
            font-size: 16px;
            border-radius: 12px;
            border: 1px solid #ffffff;
            padding: 15px;
            background-color: #f0f0f5;
            color: #000000;
        }
        /* Button styling */
        div.stButton > button {
            background-color: #ffffff;
            color: #2575fc;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 25px;
            border: none;
            transition: 0.3s;
            font-weight: bold;
        }
        div.stButton > button:hover {
            background-color: #e0e0e0;
            cursor: pointer;
        }
        /* Output container */
        .output-container {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            margin-top: 20px;
            color: #000000;
        }
        /* Code block styling */
        .stCodeBlock {
            border-radius: 12px;
            background-color: #e8e8f0;
            padding: 15px;
            color: #000000;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------- Title & Description -----------------
st.markdown("""
    <h1>🛠️ AI CODE DEBUGGER</h1>
    <p>Paste your code below and get instant AI-powered debugging help.</p>
    <hr>
""", unsafe_allow_html=True)

# ----------------- Input Container -----------------
st.markdown("""
    <div style="background-color: #f0f0f5; padding: 25px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
""", unsafe_allow_html=True)

code_input = st.text_area(
    "Paste your code here 👇",
    height=300,
    placeholder="Enter your code...",
    key="code_input"
)

st.markdown("</div>", unsafe_allow_html=True)

# ----------------- Submit Button & Output -----------------
if st.button("🚀 Debug Code", use_container_width=True):
    if code_input.strip() == "":
        st.warning("⚠️ Please enter some code before submitting.")
    else:
        # Call backend for debugging
        output = bk.get_text_output(code_input)
        st.markdown(f"""
            <div class="output-container">
                <h3 style="color: #2575fc;">🧠 Debugging Output</h3>
            </div>
        """, unsafe_allow_html=True)
        st.code(output, language="python")
