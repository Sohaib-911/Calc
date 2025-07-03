import streamlit as st

# Set full-width layout for flexibility
st.set_page_config(page_title="Simple Calculator", layout="wide")

# Optional: Reduce padding if needed
st.markdown("""
    <style>
    .center-vertically {
        height: 14vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        overflow-y: hidden;
    }
    
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
    }
    
    button {
        border: 1px solid #555 !important;
        color: #ffffff !important;
        border-radius: 6px !important;
        transition: all 0.2s ease-in-out;
    }

    /* Hover effect */
    button:hover {
        background-color: #4B0082 !important; /* indigo */
        color: #ffffff !important;
        transform: scale(1.05);
        border: 1px solid #ffffff33 !important;
    }

    /* Active / clicked state */
    button:active {
        background-color: #6200ea !important;  /* darker purple */
        transform: scale(0.97);
        box-shadow: 0 0 0 2px rgba(255,255,255,0.2);
    }

    /* Selected (focused) state */
    button:focus {
        outline: none;
        box-shadow: 0 0 0 3px rgba(75, 0, 130, 0.5);  /* indigo glow */
    }
    
    </style>
""", unsafe_allow_html=True)

# State Handling for the btns
if "expression" not in st.session_state:
    st.session_state.expression = ""


# Function to handle button press
def press(btn):
    icon_to_op = {
        "➕": "+",
        "➖": "-",
        "✖️": "*",
        "％": "/100*",
        "🟰": "=",
        "⌫": "⌫",
        "🗑️": "C"
    }

    op = icon_to_op.get(btn, btn)
    expr = st.session_state.expression

    if op == "C":
        st.session_state.expression = ""
    elif op == "⌫":
        st.session_state.expression = expr[:-1]
    elif op == "=":
        try:
            st.session_state.expression = str(eval(expr))
        except:
            st.session_state.expression = "Error"
    elif op in "+-*/":
        if expr:
            if expr[-1] in "+-*/":
                st.session_state.expression = expr[:-1] + op
            else:
                st.session_state.expression += op
        elif op == "-":
            st.session_state.expression += op
    else:
        st.session_state.expression += op


# Create 3 columns, render calculator only in the rightmost one
left, middle, right = st.columns([0.3, 0.1, 0.4])

with left:
    st.markdown('<div class="center-vertically">', unsafe_allow_html=True)
    st.image("thumbnail_corner_illustr.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="center-vertically">', unsafe_allow_html=True)

    st.title("Corvit Calculator")
    st.markdown("###### Sohaib Asgher")
    st.text_input("Result", value=st.session_state.expression, key="display", disabled=True)

    buttons = [
        ["7", "8", "9", "➕"],
        ["4", "5", "6", "➖"],
        ["1", "2", "3", "✖️"],
        ["％", "0", "🗑️", "⌫"],
        ["🟰"]
    ]

    for row in buttons:
        cols = st.columns(len(row))
        for i, btn in enumerate(row):
            with cols[i]:
                st.button(btn, key=btn + str(i), on_click=press, args=(btn,), use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)
