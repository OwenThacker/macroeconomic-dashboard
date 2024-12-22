import streamlit as st
import streamlit.components.v1 as components

# Initialize session state for navigation
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Home"

# Function to change the page
def set_page(page):
    st.session_state["current_page"] = page
    st.rerun()

# Sidebar Navigation
st.sidebar.title("Navigation")
st.sidebar.button("🏠 Home", on_click=lambda: set_page("Home"))
st.sidebar.button("🌍 Economics by Country", on_click=lambda: set_page("Country"))
st.sidebar.button("📊 USA Economic Insights", on_click=lambda: set_page("USA"))
st.sidebar.button("💹 Yield Curve Analysis", on_click=lambda: set_page("Yield"))


# Plot Display Function
def display_plot(plot_path, plot_title):
    try:
        with open(plot_path, "rb") as f:
            html_content = f.read().decode(errors="ignore")
        st.markdown(f"### {plot_title}")
        html = f'''
            <div style="width: 1200px; height: 600px;">
                {html_content}
            </div>
        '''
        components.html(html, height=600, width=1200, scrolling=False)
    except Exception as e:
        st.error(f"Error loading the plot: {e}")

# 🏠 Home Page
def show_home_page():
    st.title("📊 Macroeconomic Data Dashboard")
    st.write("""
    Welcome to the **Macroeconomic Data Dashboard**.  
    Explore interactive insights and visualizations across various economic categories using the sidebar.
    """)
    st.header("Project Highlights")
    st.write("- 📈 Interactive Economic Visualizations")
    st.write("- 🏦 Yield Analysis")
    st.write("- 💱 Currency Performance Scoring")
    st.write("- 🔄 Sector Analysis")
    st.write("- 📝 Blog with Key Insights")

# 📊 USA Economic Insights Page
def show_usa_page():
    st.title("📊 USA Economic Insights")
    display_plot("plots/EI_ASSETS.html", "Economic Indicator vs Assets")
    display_plot("plots/SP500_DR.html", "S&P 500 Daily Returns")
    display_plot("plots/GDP_SP500_ST.html", "Simple GDP-SP500 Trading Strategy")

# 💹 Yield Curve Page
def show_yield_page():
    st.title("💹 Yield Curve and Treasury Securities")
    display_plot("plots/Yield_Curve.html", "Yield Curve")
    display_plot("plots/Yields_TS.html", "Treasury Security Yields")
    display_plot("plots/10_2_Spread.html", "10 Year - 2 Year Spread")
    display_plot("plots/Spread_VS_EI_SP500.html", "Evaluating Spread Against Economic Indicators & S&P 500")
    display_plot("plots/GDP_10_5_2_Spread.html", "GDP YoY vs 10 Year - 5 Year Spread vs 5 Year - 2 Year Spread")
    display_plot("plots/VM_IR_Model.html", "Change In Interest Rates - Actual vs Vasicek Model - MLE Method")

# 🌍 Economics by Country Page
def show_country_page():
    st.title("🌍 Economics by Country")
    display_plot("plots/GDP_CTRY.html", "GDP Growth by Country")
    display_plot("plots/CPI_CTRY.html", "CPI Growth by Country")
    display_plot("plots/PPI_CTRY.html", "PPI by Country")
    display_plot("plots/PPI_YoY_CTRY.html", "PPI Growth by Country")
    display_plot("plots/UNEMP_CTRY.html", "Unemployment by Country")
    display_plot("plots/UNEMP_YoY_CTRY.html", "Unemployment Growth by Country")
    display_plot("plots/IR_CTRY.html", "Interest Rate by Country")
    display_plot("plots/IR_YoY_CTRY.html", "Interest Rate Growth by Country")

# 🚀 Render the Selected Page
if st.session_state["current_page"] == "Home":
    show_home_page()
elif st.session_state["current_page"] == "USA":
    show_usa_page()
elif st.session_state["current_page"] == "Yield":
    show_yield_page()
elif st.session_state["current_page"] == "Country":
    show_country_page()
