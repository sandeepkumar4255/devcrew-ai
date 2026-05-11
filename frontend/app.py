import streamlit as st
import requests

# Page Title
st.set_page_config(
    page_title="Multi-Agent AI Software Planner",
    layout="wide"
)

# Title
st.title("Multi-Agent AI Software Planning System")

st.write(
    "Enter your software idea and let AI agents analyze it."
)

# User Input
idea = st.text_area(
    "Enter Your Software Idea",
    placeholder="Example: Build an AI-powered hospital management system"
)

# Button
if st.button("Analyze Project"):

    if idea.strip() == "":
        st.warning("Please enter a software idea.")

    else:

        with st.spinner("AI Agents Working..."):

            try:

                # Send Request To FastAPI
                response = requests.post(
                    "https://devcrew-ai-production.up.railway.app/analyze",
                    json={"idea": idea}
                )

                # Get JSON Response
                data = response.json()

                # Display Result
                st.subheader("AI Generated Result")

                st.write(data["result"])

            except Exception as e:

                st.error(f"Error: {e}")