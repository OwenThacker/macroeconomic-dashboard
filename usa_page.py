import streamlit as st
import streamlit.components.v1 as components

# Add custom CSS to remove indentation and adjust layout
st.markdown(
    """
    <style>
    /* Remove extra padding and margin around the body */
    .reportview-container .main .block-container {
        padding-left: 0rem;
        padding-right: 0rem;
    }
    /* Center the plots and remove indentation */
    .css-1d391kg {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-left: 0 !important;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Title of the page
st.title("📊 USA Economic Insights")

# Function to load and display the plot from a path
def display_plot(plot_path, plot_title):
    try:
        with open(plot_path, "rb") as f:
            html_content = f.read().decode(errors="ignore")  # Ignore problematic bytes
        st.markdown(f"### {plot_title}")
        # Explicit width and height adjustments using html style
        html = f'''
            <div style="width: 1200px; height: 600px;">
                {html_content}
            </div>
        '''
        st.components.v1.html(html, height=600, width=1200, scrolling=False)  # Explicit width and height
    except Exception as e:
        st.error(f"Error loading the plot: {e}")

# Plot 1: Economic Indicator vs Assets (EI_ASSETS)
display_plot("plots/EI_ASSETS.html", "Economic Indicator vs Assets")

# Plot 2: S&P 500 Daily Returns (SP500_DR)
display_plot("plots/SP500_DR.html", "S&P 500 Daily Returns")

# Plot 3: Simple GDP-SP500 Trading Strategy (GDP_SP500_ST)
display_plot("plots/GDP_SP500_ST.html", "Simple GDP-SP500 Trading Strategy")
