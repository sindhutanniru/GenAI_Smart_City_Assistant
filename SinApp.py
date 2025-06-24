import streamlit as st
st.set_page_config(page_title="Smart City Sustainability Assistant", page_icon="🌱", layout="centered")
st.markdown("<h1 style='text-align: center; color: green;'>🌆 Smart City Sustainability Assistant</h1>", unsafe_allow_html=True)
st.markdown("#### 🤖 Ask anything about making cities more sustainable!")
user_input = st.text_input("🔍 Type your question here:")
def get_suggestion(query):
    query = query.lower()
    if "pollution" in query:
        return "Switch to electric vehicles, increase green cover, and promote public transport."
    elif "waste" in query:
        return "Implement segregation at source and use smart bins with IoT sensors."
    elif "water" in query:
        return "Use smart water meters and rainwater harvesting systems."
    elif "energy" in query:
        return "Promote solar panels, LED lighting, and smart grids."
    else:
        return "Try focusing on green buildings, clean transport, and digital city planning."
if user_input:
    st.markdown("#### 💡 Suggestion:")
    st.success(get_suggestion(user_input))
