import streamlit as st
import streamlit.components.v1 as components

# Styling to remove unnecessary padding and center the plots
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
st.title("🌍 Economics by Country")

# Function to load and display the plot from a path
def display_plot(plot_path, plot_title):
    try:
        with open(plot_path, "rb") as f:
            html_content = f.read().decode(errors="ignore")  # Ignore problematic bytes
        st.markdown(f"### {plot_title}")
        # Display the plot using an iframe in Streamlit
        st.components.v1.html(html_content, height=600, width=1200, scrolling=True)
    except Exception as e:
        st.error(f"Error loading the plot: {e}")

# Plot 1: GDP Growth
display_plot("plots/GDP_CTRY.html", "GDP Growth by Country")

# Plot 2: CPI Growth
display_plot("plots/CPI_CTRY.html", "CPI Growth by Country")

# Plot 3: PPI
display_plot("plots/PPI_CTRY.html", "PPI by Country")

# Plot 4: PPI Growth
display_plot("plots/PPI_YoY_CTRY.html", "PPI Growth by Country")

# Plot 5: Unemployment
display_plot("plots/UNEMP_CTRY.html", "Unemployment by Country")

# Plot 6: Unemployment Growth
display_plot("plots/UNEMP_YoY_CTRY.html", "Unemployment Growth by Country")

# Plot 7: Interest Rate
display_plot("plots/IR_CTRY.html", "Interest Rate by Country")

# Plot 8: Interest Rate Growth
display_plot("plots/IR_YoY_CTRY.html", "Interest Rate Growth by Country")
