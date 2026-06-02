
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# PAGE CONFIG

st.set_page_config(
    page_title="CYBERPUNK AI",
    page_icon="⚡️",
    layout="wide"
)

# LOAD DATA
df = pd.read_csv("Vote Ai.csv")

# CUSTOM CSS
st.markdown("""
<style>

/* ANIMATED BACKGROUND */
@keyframes gradientBG {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(
        -45deg,
        #050816,
        #0f172a,
        #111827,
        #020617
    );

    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    color: white;
}

/* REMOVE STREAMLIT HEADER */
header {
    visibility: hidden;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.95);
    border-right: 1px solid #00F5FF;
}

/* SIDEBAR LABELS */
[data-testid="stSidebar"] label {
    color: white !important;
    font-weight: bold !important;
    font-size: 16px !important;
}

/* SIDEBAR INPUTS */
.stTextInput input,
.stSelectbox div,
.stSlider {
    background-color: rgba(17,25,40,0.8) !important;
    color: white !important;
    border-radius: 10px !important;
}

/* SIDEBAR METRICS */
[data-testid="stMetricLabel"] {
    color: white !important;
    font-weight: bold !important;
}

[data-testid="stMetricValue"] {
    color: #00F5FF !important;
    font-weight: bold !important;
}

/* TITLE */
.cyber-title {
    font-size: 60px;
    font-weight: bold;
    text-align: center;
    color: #00F5FF;
    text-shadow: 0px 0px 20px #00F5FF;
    margin-bottom: 10px;
}

/* SUBTITLE */
.cyber-subtitle {
    text-align: center;
    color: #94A3B8;
    font-size: 20px;
    margin-bottom: 40px;
}

/* CARDS */
.cyber-card {
    background: rgba(17, 25, 40, 0.75);
    border: 1px solid rgba(0, 245, 255, 0.4);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    box-shadow: 0px 0px 20px rgba(0,245,255,0.3);
    transition: 0.3s;
}

.cyber-card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 0px 40px rgba(0,245,255,0.7);
}

/* METRIC TEXT */
.metric-title {
    color: #94A3B8;
    font-size: 18px;
}

.metric-value {
    font-size: 40px;
    font-weight: bold;
    color: #00F5FF;
    text-shadow: 0px 0px 15px #00F5FF;
}

/* SECTION TITLES */
.section-title {
    color: white;
    font-size: 28px;
    margin-top: 30px;
    text-shadow: 0px 0px 10px rgba(255,255,255,0.3);
}

</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
<div class="cyber-title">
⚡ CYBERPUNK VOTE AI
</div>

<div class="cyber-subtitle">
AI Powered Election Intelligence & Fraud Detection System
</div>
""", unsafe_allow_html=True)

# AI SCANNER
st.markdown("""
<div style='
text-align:center;
color:#00F5FF;
font-size:18px;
margin-bottom:20px;
'>
🧠 AI SYSTEM SCANNING ELECTION DATA...
</div>
""", unsafe_allow_html=True)

# CYBER SIDEBAR

st.sidebar.markdown("""
<h1 style='color:#00F5FF;
text-align:center;
font-weight:bold;
text-shadow:0px 0px 10px #00F5FF;'>
⚡ CONTROL PANEL
</h1>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

# SEARCH BOX
search_candidate = st.sidebar.text_input(
    "🔍 Search Candidate"
)

# STATE FILTER
state = st.sidebar.selectbox(
    "🌍 Select State",
    ["All"] + list(df["State"].unique())
)

# RISK FILTER
risk = st.sidebar.selectbox(
    "⚠️ Risk Category",
    ["All"] + list(df["Risk_Category"].unique())
)

# PARTY FILTER
party = st.sidebar.selectbox(
    "🏛️ Select Party",
    ["All"] + list(df["Party"].unique())
)

# SLIDER
risk_score = st.sidebar.slider(
    "🤖 AI Risk Score",
    0,
    100,
    (0,100)
)

st.sidebar.markdown("---")

# AI STATUS
st.sidebar.markdown("""
<div style="
background:rgba(0,245,255,0.1);
padding:15px;
border-radius:15px;
border:1px solid #00F5FF;
">

<h3 style='color:#00F5FF; font-weight:bold;'>
🟢 AI SYSTEM ACTIVE
</h3>

<p style='color:white; font-weight:bold;'>
Election monitoring running successfully.
</p>

</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<br>", unsafe_allow_html=True)

# CYBER SIDEBAR 2.0

st.sidebar.markdown("""

<div style="
text-align:center;
padding:15px;
border:1px solid #00F5FF;
border-radius:15px;
box-shadow:0 0 20px #00F5FF;
margin-bottom:15px;
">

<h2 style="color:#00F5FF;margin:0;">
⚡ CYBER CONTROL HUB
</h2>

<p style="color:white;margin:0;">
AI Election Intelligence
</p>

</div>
""", unsafe_allow_html=True)


with st.sidebar.expander("🎛 FILTERS", expanded=True):

    search_candidate = st.text_input(
        "🔍 Search Candidate"
    )

    states = st.multiselect(
        "🌍 Select State",
        sorted(df["State"].unique())
    )

parties = st.multiselect(
    "🏛 Select Party",
    sorted(df["Party"].unique())
)

risks = st.multiselect(
    "⚠ Risk Category",
    sorted(df["Risk_Category"].unique())
)

risk_score = st.slider(
    "🤖 AI Risk Score",
    0,
    100,
    (0,100)
)

vote_range = st.slider(
    "🗳 Vote Range",
    int(df["Total_Votes"].min()),
    int(df["Total_Votes"].max()),
    (
        int(df["Total_Votes"].min()),
        int(df["Total_Votes"].max())
    )
)

turnout_range = st.slider(
    "📈 Voter Turnout",
    int(df["Voter_Turnout"].min()),
    int(df["Voter_Turnout"].max()),
    (
        int(df["Voter_Turnout"].min()),
        int(df["Voter_Turnout"].max())
    )
)

with st.sidebar.expander("📊 SYSTEM STATUS", expanded=True):
  st.metric(
    "🗳 Total Votes",
    f"{df['Total_Votes'].sum():,}"
)
st.metric(
    "🚨 Fraud Cases",
    int(df["Fraud_Label"].sum())
)
st.metric(
    "🤖 Avg Risk",
    f"{df['Fraud_Risk_Score'].mean():.1f}"
)


st.sidebar.markdown("---")

if st.sidebar.button(
"🔄 RESET ALL FILTERS",
use_container_width=True
):
st.rerun()

st.sidebar.markdown("---")

st.sidebar.markdown("""

<h2 style='
color:#00F5FF;
text-align:center;
font-weight:bold;
'>
🤖 VOTE AI ASSISTANT
</h2>
""", unsafe_allow_html=True)

question = st.sidebar.text_input(
"💬 Ask Vote AI"
)


# FILTER DATA

filtered_df = df.copy()

if state != "All":
    filtered_df = filtered_df[
        filtered_df["State"] == state
    ]

if risk != "All":
    filtered_df = filtered_df[
        filtered_df["Risk_Category"] == risk
    ]

if party != "All":
    filtered_df = filtered_df[
        filtered_df["Party"] == party
    ]

filtered_df = filtered_df[
    (filtered_df["Fraud_Risk_Score"] >= risk_score[0]) &
    (filtered_df["Fraud_Risk_Score"] <= risk_score[1])
]

if search_candidate:
    filtered_df = filtered_df[
        filtered_df["Candidate_Name"]
        .str.contains(search_candidate, case=False)
    ]

# EMPTY DATA CHECK
if filtered_df.empty:
    st.warning("⚠️ No data found for selected filters")
    st.stop()

# KPI CARDS
total_votes = filtered_df["Total_Votes"].sum()
fraud_cases = filtered_df["Fraud_Label"].sum()
avg_risk = filtered_df["Fraud_Risk_Score"].mean()
avg_turnout = filtered_df["Voter_Turnout"].mean()

c1, c2, c3, c4 = st.columns(4)

cards = [
    ("TOTAL VOTES", f"{total_votes:,}"),
    ("FRAUD CASES", f"{fraud_cases}"),
    ("AI RISK SCORE", f"{avg_risk:.1f}"),
    ("AVG TURNOUT", f"{avg_turnout:.1f}%")
]

for col, card in zip([c1,c2,c3,c4], cards):

    with col:
        st.markdown(f"""
        <div class="cyber-card">
            <div class="metric-title">{card[0]}</div>
            <div class="metric-value">{card[1]}</div>
        </div>
        """, unsafe_allow_html=True)

# PARTY ANALYSIS
st.markdown("""
<div class="section-title">
🏛️ PARTY DOMINANCE ANALYSIS
</div>
""", unsafe_allow_html=True)

party_votes = (
    filtered_df.groupby("Party")["Total_Votes"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    party_votes,
    x="Party",
    y="Total_Votes",
    color="Party"
)

fig1.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="white"
)

fig1.update_traces(marker_line_width=2)

st.plotly_chart(fig1, use_container_width=True)

# FRAUD ANALYSIS
st.markdown("""
<div class="section-title">
🤖 AI FRAUD DETECTION MATRIX
</div>
""", unsafe_allow_html=True)

fig2 = px.scatter(
    filtered_df,
    x="Fraud_Risk_Score",
    y="Vote_Percentage",
    color="Risk_Category",
    size="Total_Votes",
    hover_data=["Candidate_Name"]
)

fig2.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="white"
)

st.plotly_chart(fig2, use_container_width=True)

# RISK DISTRIBUTION
st.markdown("""
<div class="section-title">
⚠️ RISK DISTRIBUTION
</div>
""", unsafe_allow_html=True)

risk_data = (
    filtered_df["Risk_Category"]
    .value_counts()
    .reset_index()
)

fig3 = px.pie(
    risk_data,
    names="Risk_Category",
    values="count",
    hole=0.6
)

fig3.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    font_color="white"
)

st.plotly_chart(fig3, use_container_width=True)
# HISTOGRAM

st.markdown("""
<div class="section-title">
📊 FRAUD SCORE DISTRIBUTION
</div>
""", unsafe_allow_html=True)

fig_hist = px.histogram(
    filtered_df,
    x="Fraud_Risk_Score",
    nbins=20,
    color="Risk_Category"
)

fig_hist.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="white"
)

st.plotly_chart(fig_hist, use_container_width=True)
# BOXPLOT

st.markdown("""
<div class="section-title">
📦 FRAUD RISK BOXPLOT
</div>
""", unsafe_allow_html=True)

fig_box = px.box(
    filtered_df,
    x="Risk_Category",
    y="Fraud_Risk_Score",
    color="Risk_Category"
)

fig_box.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="white"
)

st.plotly_chart(fig_box, use_container_width=True)
# PREMIUM CYBER HEATMAP

st.markdown("""
<div class="section-title">
🔥 AI CORRELATION MATRIX
</div>
""", unsafe_allow_html=True)

numeric_df = filtered_df.select_dtypes(include='number')

corr = numeric_df.corr()

fig, ax = plt.subplots(figsize=(12,6))

fig.patch.set_facecolor('#050816')
ax.set_facecolor('#050816')

sns.heatmap(
    corr,
    annot=True,
    cmap="mako",
    linewidths=1,
    linecolor="#00F5FF",
    annot_kws={"color":"white","size":10},
    cbar=True
)

plt.xticks(color='white', rotation=45)
plt.yticks(color='white', rotation=0)

st.pyplot(fig)
# HIGH RISK TABLE
st.markdown("""
<div class="section-title">
🚨 HIGH RISK CANDIDATES
</div>
""", unsafe_allow_html=True)

top_risk = filtered_df.sort_values(
    by="Fraud_Risk_Score",
    ascending=False
).head(10)

st.dataframe(
    top_risk,
    use_container_width=True,
    height=400
)
# DOWNLOAD DATA BUTTON

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download The Data",
    data=csv,
)
st.markdown("""
<style>

.section-title {
    color: white;
}

/* DOWNLOAD BUTTON */
.stDownloadButton > button {
    background-color: white !important;
    color: black !important;
    font-weight: bold !important;
}

</style>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<br><br>

<center>
<h3 style="color:#00F5FF;">
⚡ CYBERPUNK AI ANALYTICS SYSTEM ⚡
</h3>
</center>
""", unsafe_allow_html=True)
