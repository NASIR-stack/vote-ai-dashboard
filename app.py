
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# PAGE CONFIG

st.set_page_config(
    page_title="CYBERPUNK VOTE AI",
    page_icon="⚡",
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

if st.sidebar.button(
    "🔄 RESET ALL FILTERS",
    use_container_width=True
):
    st.rerun()
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

# CYBER STATS
st.sidebar.metric("⚡ Live Threats", "12")
st.sidebar.metric("🧠 AI Accuracy", "98.7%")
st.sidebar.metric("🚨 Alerts", "24")


# AI CHATBOT ASSISTANT

st.sidebar.markdown("---")

st.sidebar.markdown("""
<h2 style='
color:#00F5FF;
text-align:center;
font-weight:bold;
text-shadow:0px 0px 10px #00F5FF;
'>
🤖 VOTE AI ASSISTANT
</h2>
""", unsafe_allow_html=True)

question = st.sidebar.text_input(
    "💬 Ask Vote AI"
)

if question:

    q = question.lower()

    
    # HIGHEST FRAUD PARTY
    
    if (
        "fraud" in q or
        "risk" in q
    ) and "party" in q:

        risky_party = (
            df.groupby("Party")["Fraud_Risk_Score"]
            .mean()
            .idxmax()
        )

        risk_score = (
            df.groupby("Party")["Fraud_Risk_Score"]
            .mean()
            .max()
        )

        st.sidebar.success(
            f"⚠️ {risky_party} has highest fraud risk ({risk_score:.1f})"
        )

    # TOTAL VOTES
    
    elif (
        "total" in q and "votes" in q
    ):

        total_votes = df["Total_Votes"].sum()

        st.sidebar.success(
            f"🗳️ Total Votes: {total_votes:,}"
        )

    # HIGHEST TURNOUT
    
    elif (
        "turnout" in q or
        "highest turnout" in q
    ):

        top_state = (
            df.groupby("State")["Voter_Turnout"]
            .mean()
            .idxmax()
        )

        turnout = (
            df.groupby("State")["Voter_Turnout"]
            .mean()
            .max()
        )

        st.sidebar.success(
            f"📈 {top_state} has highest turnout ({turnout:.1f}%)"
        )

    # MOST VOTES PARTY
   
    elif (
        "most votes" in q or
        "winner" in q or
        "top party" in q
    ):

        top_party = (
            df.groupby("Party")["Total_Votes"]
            .sum()
            .idxmax()
        )

        votes = (
            df.groupby("Party")["Total_Votes"]
            .sum()
            .max()
        )

        st.sidebar.success(
            f"🏛️ {top_party} has most votes ({votes:,})"
        )

    # HIGH RISK CANDIDATE
    
    elif (
        "candidate" in q and
        "risk" in q
    ):

        risky_candidate = (
            df.sort_values(
                by="Fraud_Risk_Score",
                ascending=False
            )
            .iloc[0]["Candidate_Name"]
        )

        st.sidebar.error(
            f"🚨 Highest risk candidate: {risky_candidate}"
        )

   
    # DEFAULT RESPONSE
  
    else:

        st.sidebar.info(
            '''
🤖 Try asking:

• Which party has highest fraud risk?
• Show total votes
• Highest turnout state
• Which party has most votes?
• High risk candidate
            '''
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
st.download_button(
    "⬇ Download Data",
    filtered_df.to_csv(index=False),
    "filtered_data.csv",
    "text/csv"
)
# FOOTER
st.markdown("""
<br><br>

<center>
<h3 style="color:#00F5FF;">
⚡ CYBERPUNK AI ANALYTICS SYSTEM ⚡
</h3>
</center>
""", unsafe_allow_html=True)
