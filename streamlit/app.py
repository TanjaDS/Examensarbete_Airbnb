import streamlit as st
from pathlib import Path

BASE_DIR = Path.cwd().parent
st.set_page_config(layout="wide")

# Create the first page
def page_topic():
    st.subheader("Interactive Topic Exploration with LDA Visualization")
    html_file_path = BASE_DIR / 'models' / 'lda_visualization.html'
    with open(html_file_path, 'r') as file:
        html_content = file.read()
    st.components.v1.html(html_content, width=4000, height=10000)

def page_topic_neg():
    st.subheader("Interactive Topic Exploration with LDA Visualization on Negative Reviews")
    # Specify the path to your Plotly HTML file

    html_file_path = BASE_DIR / 'models' / 'lda_visualization_neg.html'
    with open(html_file_path, 'r') as file:
        html_content = file.read()
    st.components.v1.html(html_content, width=4000, height=10000)

def page_umap():
    st.subheader("Interactive UMAP Visualization")
    # Specify the path to your Plotly HTML file
    html_file_path = BASE_DIR / 'models' / 'umap.html'

    # Read the HTML content
    with open(html_file_path, 'r') as file:
        html_content = file.read()
    st.components.v1.html(html_content, width=1500, height=10000)

# Main function to manage the pages
def main():
    st.sidebar.title("Airbnb Stockholm NLP")
    st.markdown("""
    <style>
    [data-testid=stSidebar] {
        background-color: #c7c1c1;
    }
    </style>
    """, unsafe_allow_html=True)
    # Add navigation buttons in the sidebar
    if st.sidebar.button("Topic Modeling"):
        page_topic()
    if st.sidebar.button("Topic Modeling Negative Reviews"):
        page_topic_neg()
    if st.sidebar.button("UMAP"):
        page_umap()


# Run the app
if __name__ == "__main__":
    main()