import streamlit as st

st.set_page_config(page_title="Calcolatrice", layout="centered")
st.title("🧮 Calcolatrice Avanzata")

# Display risultato
if "display" not in st.session_state:
    st.session_state.display = ""

if "operazione" not in st.session_state:
    st.session_state.operazione = ""

if "num1" not in st.session_state:
    st.session_state.num1 = None

# Funzioni pulsanti
def click_num(n):
    st.session_state.display += str(n)

def click_oper(op):
    if st.session_state.display:
        st.session_state.num1 = float(st.session_state.display)
        st.session_state.operazione = op
        st.session_state.display = ""

def click_uguale():
    try:
        if st.session_state.display and st.session_state.num1 is not None:
            num2 = float(st.session_state.display)
            if st.session_state.operazione == "+":
                st.session_state.display = str(st.session_state.num1 + num2)
            elif st.session_state.operazione == "-":
                st.session_state.display = str(st.session_state.num1 - num2)
            elif st.session_state.operazione == "*":
                st.session_state.display = str(st.session_state.num1 * num2)
            elif st.session_state.operazione == "/":
                if num2 == 0:
                    st.session_state.display = "Errore: divisione per zero"
                else:
                    st.session_state.display = str(st.session_state.num1 / num2)
            st.session_state.num1 = None
            st.session_state.operazione = ""
    except Exception:
        st.session_state.display = "Errore"

def click_clear():
    st.session_state.display = ""
    st.session_state.num1 = None
    st.session_state.operazione = ""

# Display attuale
st.text_input("Display", value=st.session_state.display, key="display_box", disabled=True)

# Pulsanti numerici
rows = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["C","0","=","+"]
]

for r in rows:
    cols = st.columns(4)
    for i, btn in enumerate(r):
        if cols[i].button(btn):
            if btn.isdigit():
                click_num(btn)
            elif btn in "+-*/":
                click_oper(btn)
            elif btn == "=":
                click_uguale()
            elif btn == "C":
                click_clear()
