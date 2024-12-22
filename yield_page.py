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
st.title("💹 Yield Curve and Treasury Securities")

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

# Plot 1: Yield Curve
display_plot("plots/Yield_Curve.html", "Yield Curve")

# Plot 2: Treasury Security Yields (Yields_TS)
display_plot("plots/Yields_TS.html", "Treasury Security Yields")

# Plot 3: 10 Year - 2 Year Spread (10_2_Spread)
display_plot("plots/10_2_Spread.html", "10 Year - 2 Year Spread")

# Plot 4: Evaluating Spread Against Economic Indicators & S&P 500 (Spread_VS_EI_SP500)
display_plot("plots/Spread_VS_EI_SP500.html", "Evaluating Spread Against Economic Indicators & S&P 500")

# Plot 5: GDP YoY vs 10 Year - 5 Year Spread vs 5 Year - 2 Year Spread (GDP_10_5_2_Spread)
display_plot("plots/GDP_10_5_2_Spread.html", "GDP YoY vs 10 Year - 5 Year Spread vs 5 Year - 2 Year Spread")

# Plot 6: Change In Interest Rates - Actual vs Vasicek Model - MLE Method (VM_IR_Model)
display_plot("plots/VM_IR_Model.html", "Change In Interest Rates - Actual vs Vasicek Model - MLE Method")
