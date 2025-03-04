import streamlit as st
from crew import BrdToSrs

import sqlite3
#StreamLit page config
st.set_page_config(page_title="BRD to SRS converter", page_icon="📝", layout="wide")

#Title and description
st.title("BRD to SRS converter, powered by CrewAI.")
st.markdown("Generate an SRS from a BRD using AI agents.")



#Sidebar
with st.sidebar:
    st.header("Content Settings")

    #Make the text input take up more space
    # topic = st.text_area(
    #     "Enter Your Topic",
    #     height=100,
    #     placeholder="Enter the topic"
    # )

    #Add more sidebar controls if needed
    # st.markdown("### LLM Settings")
    # temperature = st.slider("Temperature", 0.0, 1.0, 0.7)

    #Add more spacing
    st.markdown("----")

    #Make the generate button more prominent in the sidebar
    generate_button = st.button("Generate SRS", type="primary", use_container_width=True)

    #Add some helpful information
    with st.expander("ℹ How to use"):
        st.markdown("""
            1. Enter your decider content topic
            2. Play with the temperature
            3. Click 'Generate Content' to start
            4. Wait for the AI to generate your article
            5. Download the result as a markdown file
            """)


def generate_content():
    #Create a new instance of the crew
    crewNew = BrdToSrs().crew().kickoff()

    return crewNew
    # #Get the result
    # result = crewNew

    # #Display the result
    # st.markdown(result)



#Main content area
if generate_button:
    with st.spinner("Generating Content...This may take a moment.."):
        try:
            result = generate_content()
            st.markdown("### Generated Content")
            st.markdown(result)

            #Add download button
            st.download_button(
                label="Download Content",
                data=result.raw,
                file_name=f"article.md",
                mime="text/markdown"
            )
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")


#Footer
st.markdown("----")
st.markdown("Built by Team AgenticAI")
