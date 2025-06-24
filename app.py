import streamlit as st
def get_ai_response(user_input):
    responses = {
        "air pollution": "Use electric public transport and promote carpooling.",
        "water waste": "Implement smart meters and public awareness campaigns.",
        "waste management": "Use IoT-enabled bins and automated waste segregation.",
    }
    for key in responses:
        if key in user_input.lower():
            return responses[key]
    return "Try promoting green energy, smart buildings, and sustainable mobility."
st.title("Sustainable Smart City Assistant")
user_input = st.text_input("Ask your question related to sustainability:")
if user_input:
    response = get_ai_response(user_input)
    st.markdown(f"*AI Assistant:* {response}")
