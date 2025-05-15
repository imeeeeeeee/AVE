import streamlit as st
import pandas as pd
from ave_functions import ave_simulator
from config import  SECTOR_CODES, BENCHMARKS, ISO_COUNTRY_CODES, INVERSE_ISO_COUNTRY_CODES
import plotly.graph_objects as go
# Sample dataset
df = pd.read_csv("stri_ave_data.csv")

st.set_page_config(layout="wide", page_title="AVE Trade Cost Simulation", page_icon="📊")

st.title("📊 STRI-based Trade Cost Simulation")

# User inputs for authentication
authenticator = st.text_input("Enter the authentication password", type="password")

# Set your desired password here
AUTH_PASSWORD = st.secrets["AUTH_PASSWORD"]

if authenticator != AUTH_PASSWORD:
    st.warning("Please enter the correct password to access the app.")
    st.stop()

# Create two columns for filters
col1, col2 = st.columns(2)

with col1:
    selected_country = st.selectbox("Select a country:", list(ISO_COUNTRY_CODES.keys()))

with col2:
    selected_sector = st.selectbox("Select a sector:", list(SECTOR_CODES.keys()))

# Filter the dataframe
if selected_sector in SECTOR_CODES:
    filtered_df = df[(df['COU'] == ISO_COUNTRY_CODES[selected_country]) & (df['SECT'] == SECTOR_CODES[selected_sector][0]) & (df['CLASS'] == 'STRI')]
else:
    filtered_df = pd.DataFrame()  # Empty DataFrame if sector is invalid

# Display the score
st.markdown("---")
if not filtered_df.empty:
    score = filtered_df.iloc[0]['STRI']
    stri_now = {selected_sector: [selected_country, score]}
    result = ave_simulator(stri_now, BENCHMARKS)

    # Get benchmark info
    benchmark_score = result['STRI_benchmark'].iloc[0]
    benchmark_country_code = result['STRI_benchmark_country'].iloc[0]
    benchmark_country = INVERSE_ISO_COUNTRY_CODES[benchmark_country_code]
    is_benchmark = selected_country == benchmark_country
    stri_simulated = result['STRI_simulated'].iloc[0]

    # PART 1 - Country STRI
    st.markdown("### 🌍 Current STRI Score")
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; gap: 1.5em;">
            <div style="background: #f0f2f6; border-radius: 10px; padding: 1em 2em; box-shadow: 0 2px 8px #e0e0e0;">
                <span style="font-size: 1.2em; color: #555;">Country</span><br>
                <span style="font-size: 1.6em; font-weight: bold; color: #1f77b4;">{selected_country}</span>
            </div>
            <div style="background: #f0f2f6; border-radius: 10px; padding: 1em 2em; box-shadow: 0 2px 8px #e0e0e0;">
                <span style="font-size: 1.2em; color: #555;">Sector</span><br>
                <span style="font-size: 1.3em; font-weight: bold; color: #ff7f0e;">{selected_sector}</span>
            </div>
            <div style="background: #f0f2f6; border-radius: 10px; padding: 1em 2em; box-shadow: 0 2px 8px #e0e0e0;">
                <span style="font-size: 1.2em; color: #555;">Current STRI</span><br>
                <span style="font-size: 2em; font-weight: bold; color: #1f77b4;">{score:.4f}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


    # PART 2 - Benchmark Comparison
    st.markdown("### 🏁 Benchmark Comparison")
    if is_benchmark:
        st.success(
            f"{selected_country} is the benchmark country for the {selected_sector} sector."
        )
    else:
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; gap: 1.5em;">
            <div style="background: #f0f2f6; border-radius: 10px; padding: 1em 2em; box-shadow: 0 2px 8px #e0e0e0;">
                <span style="font-size: 1.2em; color: #555;">Benchmark Country</span><br>
                <span style="font-size: 1.6em; font-weight: bold; color: #1f77b4;">{benchmark_country}</span>
            </div>
            <div style="background: #f0f2f6; border-radius: 10px; padding: 1em 2em; box-shadow: 0 2px 8px #e0e0e0;">
                <span style="font-size: 1.2em; color: #555;">Benchmark STRI</span><br>
                <span style="font-size: 2em; font-weight: bold; color: #1f77b4;">{benchmark_score:.4f}</span>
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Visual comparison of STRI and benchmark

    fig = go.Figure(data=[
        go.Bar(
            name=selected_country,
            x=[selected_country],
            y=[score],
            marker_color='royalblue',
            text=[f"{score:.4f}"],
            textposition='auto'
        ),
        go.Bar(
            name=f"{benchmark_country} (Benchmark)",
            x=[benchmark_country],
            y=[benchmark_score],
            marker_color='orange',
            text=[f"{benchmark_score:.4f}"],
            textposition='auto'
        ),
        go.Bar(
            name="STRI Simulated",
            x=["STRI Simulated"],
            y=[result['STRI_simulated'].iloc[0]],
            marker_color='green',
            text=[f"{stri_simulated:.4f}"],
            textposition='auto'
        )
    ])

    fig.update_layout(
        barmode='group',
        title="STRI Score vs Benchmark",
        xaxis_title="Country",
        yaxis_title="STRI Score",
        legend_title="Legend",
        plot_bgcolor='rgba(0,0,0,0)',
        height=500,
        width=500
    )

    st.plotly_chart(fig, use_container_width=False)

    # PART 3 - Simulated Results
    st.markdown("### 🔬 Simulation Results")

    # Calculate changes for arrow indicators
    ave = result['AVE'].iloc[0]
    ave_ci_lower = result['AVE_CI_Lower'].iloc[0]
    ave_ci_upper = result['AVE_CI_Upper'].iloc[0]

    stri_delta = stri_simulated - score
    ave_delta = ave * 100 - score * 100  # If you want to compare AVE % to STRI %, adjust as needed

    # Arrow and delta_color logic
    def get_arrow_and_color(delta, is_inverse=False):
        if (delta < 0 and not is_inverse) or (delta > 0 and is_inverse):
            return "↓", "#2ca02c"  # green
        elif (delta > 0 and not is_inverse) or (delta < 0 and is_inverse):
            return "↑", "#d62728"  # red
        else:
            return "", "#888888"   # gray

    stri_arrow, stri_color = get_arrow_and_color(stri_delta)
    ave_arrow, ave_color = get_arrow_and_color(ave_delta, is_inverse=True)  # Lower AVE is better

    # Custom HTML/CSS for metrics
    st.markdown(
        f"""
        <style>
        .metric-card {{
            background: #f8fafc;
            border-radius: 12px;
            box-shadow: 0 2px 8px #e0e0e0;
            padding: 1.2em 1.5em;
            margin: 0.5em 0.5em 1.5em 0.5em;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            min-width: 220px;
        }}
        .metric-label {{
            font-size: 1.1em;
            color: #555;
            margin-bottom: 0.2em;
        }}
        .metric-value {{
            font-size: 2em;
            font-weight: bold;
            color: #1f77b4;
            margin-bottom: 0.2em;
        }}
        .metric-delta {{
            font-size: 1.1em;
            font-weight: 500;
            color: {stri_color};
            margin-bottom: 0.2em;
        }}
        .metric-arrow {{
            font-size: 1.3em;
            font-weight: bold;
            color: {stri_color};
            margin-right: 0.2em;
        }}
        .metric-help {{
            font-size: 0.95em;
            color: #888;
            margin-top: 0.3em;
        }}
        .metric-row {{
            display: flex;
            flex-wrap: wrap;
            gap: 1.5em;
            justify-content: flex-start;
        }}
        </style>
        <div class="metric-row">
            <div class="metric-card">
                <span class="metric-label">STRI Simulated</span>
                <span class="metric-value">{stri_simulated:.4f}</span>
                <span class="metric-delta">
                    <span class="metric-arrow">{stri_arrow}</span>
                    {stri_delta:+.4f}
                </span>
                <span class="metric-help">Simulated STRI after applying benchmark-like policy</span>
            </div>
            <div class="metric-card">
                <span class="metric-label">Trade Cost Reduction (in %)</span>
                <span class="metric-value" style="color:#2ca02c;">{ave*100:.2f}%</span>
                <span class="metric-help">Ad Valorem Equivalent (estimated tariff equivalent)</span>
            </div>
            <div class="metric-card">
                <span class="metric-label">Confidence Interval</span>
                <span class="metric-value" style="color:#ff7f0e;">[{ave_ci_lower*100:.2f}%, {ave_ci_upper*100:.2f}%]</span>
                <span class="metric-help">95% confidence interval for AVE</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

else:
    st.warning("No data available for the selected country and sector.")

st.markdown("---")
st.markdown(
    """
    <div style="font-size: 1em; color: #444; margin-top: 2em;">
        <strong>References:</strong><br>
        For details regarding the methodology and simulation approach, see:<br>
        <a href="https://one.oecd.org/document/ECO/WKP(2020)25/en/pdf" target="_blank">
            SERVICES TRADE COSTS IN THE UNITED STATES: A SIMULATION BASED ON THE 
            OECD SERVICES TRADE RESTRICTIVENESS INDEX
            ECONOMICS DEPARTMENT WORKING PAPERS No.1617
            By Sebastian Benz and Alexander Jaax, paragraph 26.
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
