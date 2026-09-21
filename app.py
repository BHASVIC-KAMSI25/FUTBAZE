import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="FUTBAZE 24/25",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #092328;
    --card: #12544F;
    --accent: #2A835F;
    --light: #8BBB92;
    --white: #FFFFFF;
    --border: rgba(139, 187, 146, 0.18);
    --border-strong: rgba(139, 187, 146, 0.30);
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp,
[data-testid="stAppViewContainer"] {
    background: var(--bg);
    color: var(--white);
}

[data-testid="stHeader"],
[data-testid="stToolbar"] {
    background: transparent;
}

[data-testid="stSidebar"],
[data-testid="stSidebar"] > div:first-child {
    background: var(--card);
}

[data-testid="stSidebar"] {
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] * {
    color: var(--white);
}

.block-container {
    max-width: 1500px;
    padding-top: 2.5rem;
    padding-bottom: 4rem;
}

h1, h2, h3, h4, h5, h6 {
    color: var(--white) !important;
    font-weight: 700 !important;
    letter-spacing: -0.025em;
}

p, span, label, div {
    color: var(--white);
}

.stCaption,
[data-testid="stCaptionContainer"] {
    color: var(--light) !important;
}

[data-testid="stCaptionContainer"] p {
    color: var(--light) !important;
}

.futbaze-hero {
    padding: 1.5rem 0 2.4rem 0;
    margin-bottom: 0.5rem;
}

.futbaze-brand {
    font-size: clamp(2.8rem, 6vw, 5rem);
    line-height: 0.9;
    font-weight: 800;
    letter-spacing: -0.07em;
    color: var(--white);
}

.futbaze-season {
    margin-top: 0.7rem;
    color: var(--light);
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.16em;
}

.futbaze-tagline {
    margin-top: 1.15rem;
    color: var(--white);
    font-size: 1rem;
    font-weight: 500;
    opacity: 0.85;
}

.futbaze-line {
    width: 58px;
    height: 4px;
    margin-top: 1.15rem;
    border-radius: 99px;
    background: var(--accent);
}

.sidebar-brand {
    padding: 1rem 0 1.3rem 0.2rem;
}

.sidebar-brand-main {
    font-size: 1.7rem;
    font-weight: 800;
    letter-spacing: -0.05em;
}

.sidebar-brand-sub {
    margin-top: 0.3rem;
    color: var(--light);
    font-size: 0.63rem;
    font-weight: 700;
    letter-spacing: 0.12em;
}

.sidebar-label {
    margin: 0.5rem 0 0.65rem 0.2rem;
    color: var(--light);
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
}

.page-header {
    padding: 0.3rem 0 1.7rem 0;
}

.page-eyebrow {
    color: var(--light);
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 0.45rem;
}

.page-title {
    color: var(--white);
    font-size: clamp(2rem, 4vw, 3rem);
    line-height: 1;
    font-weight: 800;
    letter-spacing: -0.045em;
}

.page-description {
    max-width: 760px;
    margin-top: 0.75rem;
    color: var(--light);
    font-size: 0.92rem;
    line-height: 1.65;
}

.section-heading {
    margin-top: 2.2rem;
    margin-bottom: 1rem;
    color: var(--white);
    font-size: 1.15rem;
    font-weight: 700;
    letter-spacing: -0.02em;
    display: flex;
    align-items: center;
    gap: 0.65rem;
}

.section-heading::before {
    content: "";
    width: 4px;
    height: 19px;
    border-radius: 99px;
    background: var(--accent);
    display: inline-block;
}

.player-identity {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 1.4rem 1.5rem;
    margin: 0.4rem 0 1.4rem 0;
}

.player-name {
    font-size: 1.45rem;
    font-weight: 800;
    letter-spacing: -0.035em;
}

.player-meta {
    margin-top: 0.35rem;
    color: var(--light);
    font-size: 0.82rem;
}

.position-badge {
    display: inline-block;
    margin-top: 0.9rem;
    padding: 0.32rem 0.65rem;
    border-radius: 999px;
    background: rgba(42, 131, 95, 0.22);
    border: 1px solid rgba(139, 187, 146, 0.3);
    color: var(--light);
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.rating-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.25rem;
    min-height: 130px;
}

.rating-label {
    color: var(--light);
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.rating-value {
    margin-top: 0.55rem;
    color: var(--white);
    font-size: 1.45rem;
    font-weight: 800;
}

.rating-score {
    margin-top: 0.25rem;
    color: var(--light);
    font-size: 0.78rem;
}

div[data-testid="stMetric"] {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1rem 1.1rem;
    min-height: 105px;
    transition: border-color 0.2s ease, transform 0.2s ease;
}

div[data-testid="stMetric"]:hover {
    border-color: var(--border-strong);
    transform: translateY(-1px);
}

div[data-testid="stMetricLabel"] {
    color: var(--light) !important;
    font-size: 0.72rem !important;
    font-weight: 600 !important;
}

div[data-testid="stMetricValue"] {
    color: var(--white) !important;
    font-weight: 800 !important;
    letter-spacing: -0.025em;
}

div[data-testid="stMetricDelta"] {
    color: var(--light) !important;
}

.stButton {
    margin-top: 0.35rem;
}

.stButton > button {
    min-height: 42px;
    background: var(--accent);
    color: var(--white);
    border: 1px solid var(--accent);
    border-radius: 10px;
    font-weight: 700;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: var(--light);
    color: var(--bg);
    border-color: var(--light);
    transform: translateY(-1px);
}

.stButton > button:focus {
    box-shadow: 0 0 0 2px rgba(139, 187, 146, 0.25);
}

.stSelectbox > div > div,
.stMultiSelect > div > div,
.stTextInput > div > div,
.stNumberInput > div > div {
    background: var(--card);
    color: var(--white);
    border-radius: 10px;
    border: 1px solid var(--border-strong);
}

.stSelectbox label,
.stMultiSelect label,
.stTextInput label,
.stNumberInput label,
.stDateInput label {
    color: var(--white) !important;
    font-weight: 600;
    font-size: 0.78rem;
}

[data-baseweb="select"] > div {
    background: var(--card);
    color: var(--white);
    border-color: var(--border-strong);
}

[data-baseweb="popover"] {
    background: var(--card);
}

[data-baseweb="menu"] {
    background: var(--card);
}

[data-baseweb="menu"] li {
    color: var(--white);
}

[data-baseweb="menu"] li:hover {
    background: var(--accent);
}

[data-baseweb="input"] {
    background: var(--card);
}

input {
    color: var(--white) !important;
}

input::placeholder {
    color: rgba(139, 187, 146, 0.65) !important;
}

[data-testid="stDataFrame"] {
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
    background: var(--card);
}

[data-testid="stDataFrame"] > div {
    border-radius: 14px;
}

div[data-testid="stExpander"] {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
}

div[data-testid="stExpander"] summary {
    color: var(--white);
    font-weight: 600;
}

hr {
    border-color: var(--border);
    margin: 1.7rem 0;
}

.stProgress > div > div > div > div {
    background: var(--accent);
}

[data-testid="stAlert"] {
    background: var(--card);
    border-radius: 12px;
    border: 1px solid var(--border);
}

[data-testid="stMarkdownContainer"] a {
    color: var(--light) !important;
}

[data-testid="stSidebarNav"] {
    padding-top: 1rem;
}

[data-testid="stSidebarNav"] span {
    color: var(--white) !important;
}

[data-testid="stSidebar"] .stRadio label {
    font-size: 0.82rem;
    font-weight: 600;
}

[data-testid="stSidebar"] [data-baseweb="radio"] {
    padding: 0.15rem 0;
}

[data-testid="stSidebar"] [data-baseweb="radio"] > div:first-child {
    border-color: var(--light);
}

[data-testid="stSidebar"] [data-baseweb="radio"] [aria-checked="true"] > div:first-child {
    background: var(--accent);
    border-color: var(--accent);
}

.stPlotlyChart {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 0.4rem;
    overflow: hidden;
}

[data-testid="stDateInput"] > div > div {
    background: var(--card);
    border-radius: 10px;
}

[data-testid="stDateInput"] input {
    color: var(--white) !important;
}

[data-testid="stNumberInput"] button {
    background: var(--card);
    color: var(--light);
    border-color: var(--border);
}

[data-testid="stNumberInput"] button:hover {
    background: var(--accent);
    color: var(--white);
}

[data-testid="stMarkdownContainer"] table {
    background: var(--card);
    border-radius: 12px;
}

[data-testid="stMarkdownContainer"] th {
    background: var(--accent);
    color: var(--white);
}

[data-testid="stMarkdownContainer"] td {
    background: var(--card);
    color: var(--white);
}

@media (max-width: 768px) {
    .block-container {
        padding-top: 1.4rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .futbaze-hero {
        padding-bottom: 1.6rem;
    }

    .page-header {
        padding-bottom: 1.2rem;
    }

    .player-identity {
        padding: 1.1rem;
    }

    div[data-testid="stMetric"] {
        min-height: 95px;
        padding: 0.85rem;
    }
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="futbaze-hero">
    <div class="futbaze-brand">FUTBAZE</div>
    <div class="futbaze-season">24/25 ENGLISH PREMIER LEAGUE FOOTBALL ANALYTICS</div>
    <div class="futbaze-tagline">Turn football data into insight.</div>
    <div class="futbaze-line"></div>
</div>
""", unsafe_allow_html=True)

players = pd.read_csv("data/players_full.csv")

percentage_columns = [
    "Conversion %",
    "Passes%",
    "Crosses %",
    "fThird Passes %",
    "gDuels %",
    "aDuels %",
    "Saves %"
]

for column in percentage_columns:
    if column in players.columns:
        players[column] = (
            players[column]
            .astype(str)
            .str.replace("%", "", regex=False)
            .str.strip()
        )
        players[column] = pd.to_numeric(
            players[column],
            errors="coerce"
        )

numeric_columns = [
    "Appearances",
    "Minutes",
    "Goals",
    "Assists",
    "Shots",
    "Shots On Target",
    "Big Chances Missed",
    "Hit Woodwork",
    "Offsides",
    "Touches",
    "Passes",
    "Successful Passes",
    "Crosses",
    "Successful Crosses",
    "fThird Passes",
    "Successful fThird Passes",
    "Through Balls",
    "Carries",
    "Progressive Carries",
    "Carries Ended with Goal",
    "Carries Ended with Assist",
    "Carries Ended with Shot",
    "Carries Ended with Chance",
    "Possession Won",
    "Dispossessed",
    "Clean Sheets",
    "Clearances",
    "Interceptions",
    "Blocks",
    "Tackles",
    "Ground Duels",
    "gDuels Won",
    "Aerial Duels",
    "aDuels Won",
    "Goals Conceded",
    "xGoT Conceded",
    "Own Goals",
    "Fouls",
    "Yellow Cards",
    "Red Cards",
    "Saves",
    "Penalties Saved",
    "Clearances Off Line",
    "Punches",
    "High Claims",
    "Goals Prevented"
]

for column in numeric_columns:
    if column in players.columns:
        players[column] = pd.to_numeric(
            players[column],
            errors="coerce"
        )

st.sidebar.markdown("""
<div class="sidebar-brand">
    <div class="sidebar-brand-main">FUTBAZE</div>
    <div class="sidebar-brand-sub">24/25 FOOTBALL ANALYTICS</div>
</div>
<div class="sidebar-label">Dashboard</div>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state["page"] = "Player Analysis"

pages = [
    "Player Analysis",
    "Player Comparison",
    "My FUTBAZE",
    "Rating Methodology"
]

page = st.sidebar.radio(
    "Go to",
    pages,
    index=pages.index(st.session_state["page"])
)

st.session_state["page"] = page


def get_rating(score):
    if score >= 64:
        return "Elite"
    elif score >= 50:
        return "High Standard"
    elif score >= 30:
        return "Standard"
    elif score >= 20:
        return "Mediocre"
    else:
        return "Poor"


def percentile_score(value, series):
    values = pd.to_numeric(
        series,
        errors="coerce"
    ).dropna()

    if pd.isna(value) or values.empty:
        return 50

    return (values <= value).mean() * 100


def get_position_group(position):
    position = str(position).upper()

    if "GK" in position:
        return "GK"
    elif "DF" in position:
        return "DF"
    elif "MF" in position:
        return "MF"
    elif "FW" in position:
        return "FW"
    else:
        return "MF"


def calculate_productivity(
    player,
    players,
    category
):
    position_group = get_position_group(
        player["Position"]
    )

    position_players = players[
        players["Position"].apply(
            get_position_group
        ) == position_group
    ].copy()

    position_players = position_players[
        position_players["Minutes"] >= 900
    ]

    if len(position_players) < 10:
        position_players = players.copy()

    minutes = max(
        player["Minutes"],
        1
    )

    per90_columns = [
        "Goals",
        "Assists",
        "Shots On Target",
        "Carries Ended with Goal",
        "Carries Ended with Assist",
        "Carries Ended with Shot",
        "Carries Ended with Chance",
        "Progressive Carries",
        "fThird Passes",
        "Through Balls",
        "Tackles",
        "Interceptions",
        "Blocks",
        "Clearances",
        "Possession Won"
    ]

    for column in per90_columns:
        if column in position_players.columns:
            position_players[column + " Per 90"] = (
                position_players[column]
                / position_players["Minutes"].clip(lower=1)
                * 90
            )

    if category == "attacking":

        if position_group == "FW":
            metrics = [
                ("Goals Per 90", 0.25),
                ("Assists Per 90", 0.20),
                ("Shots On Target Per 90", 0.15),
                ("Conversion %", 0.10),
                ("Carries Ended with Goal Per 90", 0.10),
                ("Carries Ended with Assist Per 90", 0.10),
                ("Carries Ended with Chance Per 90", 0.10)
            ]

        elif position_group == "MF":
            metrics = [
                ("Goals Per 90", 0.15),
                ("Assists Per 90", 0.15),
                ("Shots On Target Per 90", 0.10),
                ("Progressive Carries Per 90", 0.15),
                ("fThird Passes Per 90", 0.15),
                ("Through Balls Per 90", 0.10),
                ("Carries Ended with Chance Per 90", 0.10),
                ("Passes%", 0.10)
            ]

        elif position_group == "DF":
            metrics = [
                ("Goals Per 90", 0.10),
                ("Assists Per 90", 0.10),
                ("Progressive Carries Per 90", 0.15),
                ("fThird Passes Per 90", 0.15),
                ("Crosses", 0.15),
                ("Carries Ended with Chance Per 90", 0.10),
                ("Passes%", 0.15),
                ("Successful Passes", 0.10)
            ]

        else:
            metrics = [
                ("Passes%", 0.30),
                ("Successful Passes", 0.25),
                ("Touches", 0.20),
                ("Carries", 0.15),
                ("Through Balls Per 90", 0.10)
            ]

    else:

        if position_group == "GK":
            metrics = [
                ("Saves %", 0.30),
                ("Goals Prevented", 0.25),
                ("Clean Sheets", 0.20),
                ("Saves", 0.15),
                ("High Claims", 0.10)
            ]

        elif position_group == "DF":
            metrics = [
                ("Tackles Per 90", 0.20),
                ("Interceptions Per 90", 0.20),
                ("Blocks Per 90", 0.15),
                ("Clearances Per 90", 0.15),
                ("Ground Duels Won", 0.10),
                ("gDuels %", 0.10),
                ("Aerial Duels Won", 0.10)
            ]

        elif position_group == "MF":
            metrics = [
                ("Tackles Per 90", 0.15),
                ("Interceptions Per 90", 0.15),
                ("Possession Won Per 90", 0.20),
                ("Ground Duels Won", 0.15),
                ("gDuels %", 0.10),
                ("Aerial Duels Won", 0.10),
                ("Dispossessed", 0.15)
            ]

        else:
            metrics = [
                ("Possession Won Per 90", 0.25),
                ("Tackles Per 90", 0.15),
                ("Interceptions Per 90", 0.15),
                ("Ground Duels Won", 0.15),
                ("gDuels %", 0.10),
                ("Dispossessed", 0.20)
            ]

    scores = []
    total_weight = 0

    for metric, weight in metrics:

        if metric not in position_players.columns:
            continue

        base_column = metric.replace(
            " Per 90",
            ""
        )

        if "Per 90" in metric:
            value = (
                player[base_column]
                / minutes
                * 90
            )
        else:
            value = player[base_column]

        if metric == "Dispossessed":
            percentile = (
                100
                - percentile_score(
                    value,
                    position_players[metric]
                )
            )
        else:
            percentile = percentile_score(
                value,
                position_players[metric]
            )

        scores.append(
            percentile * weight
        )

        total_weight += weight

    if total_weight == 0:
        return 50

    score = (
        sum(scores)
        / total_weight
    )

    reliability = min(
        minutes / 900,
        1
    )

    score = (
        50
        + (score - 50)
        * reliability
    )

    return score


def calculate_my_performance_score(match):

    position = match["Position"]

    minutes = max(
        match["Minutes"],
        1
    )

    def per90(column):
        return (
            match[column]
            / minutes
            * 90
        )

    def capped_score(
        value,
        benchmark
    ):
        return min(
            value / benchmark * 100,
            100
        )

    scores = []

    if position == "GK":

        save_attempts = (
            match["Saves"]
            + match["Goals Conceded"]
        )

        save_percentage = (
            match["Saves"]
            / save_attempts
            * 100
            if save_attempts > 0
            else 100
        )

        metrics = [
            (
                per90("Saves"),
                4.0,
                0.25
            ),
            (
                save_percentage,
                75,
                0.25
            ),
            (
                per90("Goals Prevented"),
                0.15,
                0.20
            ),
            (
                match["Clean Sheets"],
                1,
                0.15
            ),
            (
                per90("High Claims"),
                1.5,
                0.10
            ),
            (
                match["Penalties Saved"],
                0.5,
                0.05
            )
        ]

    elif position == "FW":

        metrics = [
            (
                per90("Goals"),
                0.75,
                0.30
            ),
            (
                per90("Assists"),
                0.35,
                0.20
            ),
            (
                per90("Shots On Target"),
                2.0,
                0.20
            ),
            (
                per90("Shots"),
                4.0,
                0.15
            ),
            (
                per90("Progressive Carries"),
                5.0,
                0.15
            )
        ]

    elif position == "MF":

        pass_accuracy = (
            match["Successful Passes"]
            / max(match["Passes"], 1)
            * 100
        )

        metrics = [
            (
                per90("Assists"),
                0.30,
                0.15
            ),
            (
                per90("Progressive Carries"),
                5.0,
                0.20
            ),
            (
                per90("Through Balls"),
                0.30,
                0.15
            ),
            (
                per90("Tackles"),
                2.5,
                0.20
            ),
            (
                per90("Interceptions"),
                1.5,
                0.15
            ),
            (
                pass_accuracy,
                90,
                0.15
            )
        ]

    else:

        pass_accuracy = (
            match["Successful Passes"]
            / max(match["Passes"], 1)
            * 100
        )

        metrics = [
            (
                per90("Tackles"),
                3.0,
                0.20
            ),
            (
                per90("Interceptions"),
                2.0,
                0.20
            ),
            (
                per90("Blocks"),
                1.0,
                0.15
            ),
            (
                per90("Progressive Carries"),
                3.0,
                0.10
            ),
            (
                pass_accuracy,
                90,
                0.20
            ),
            (
                per90("Possession Won"),
                5.0,
                0.15
            )
        ]

    for value, benchmark, weight in metrics:
        scores.append(
            capped_score(
                value,
                benchmark
            ) * weight
        )

    return min(
        sum(scores),
        100
    )


def calculate_radar_score(
    player,
    players,
    metrics
):

    position_group = get_position_group(
        player["Position"]
    )

    comparison_players = players[
        players["Position"].apply(
            get_position_group
        ) == position_group
    ].copy()

    comparison_players = comparison_players[
        comparison_players["Minutes"] >= 900
    ]

    if len(comparison_players) < 10:
        comparison_players = players.copy()

    minutes = max(
        float(player["Minutes"]),
        1
    )

    scores = []
    weights = []

    for column, weight, per90, lower_is_better in metrics:

        if column not in comparison_players.columns:
            continue

        if per90:

            comparison_values = (
                comparison_players[column]
                / comparison_players["Minutes"].clip(lower=1)
                * 90
            )

            player_value = (
                player[column]
                / minutes
                * 90
            )

        else:

            comparison_values = comparison_players[column]
            player_value = player[column]

        percentile = percentile_score(
            player_value,
            comparison_values
        )

        if lower_is_better:
            percentile = 100 - percentile

        scores.append(
            percentile * weight
        )

        weights.append(weight)

    if not weights:
        return 50

    score = (
        sum(scores)
        / sum(weights)
    )

    reliability = min(
        minutes / 900,
        1
    )

    return (
        50
        + (score - 50)
        * reliability
    )


def get_player_radar_data(
    player,
    players
):

    position = get_position_group(
        player["Position"]
    )

    attacking_metrics = [
        ("Goals", 0.25, True, False),
        ("Assists", 0.20, True, False),
        ("Shots On Target", 0.15, True, False),
        ("Conversion %", 0.10, False, False),
        ("Carries Ended with Goal", 0.10, True, False),
        ("Carries Ended with Assist", 0.10, True, False),
        ("Carries Ended with Chance", 0.10, True, False)
    ]

    passing_metrics = [
        ("Passes%", 0.35, False, False),
        ("Successful Passes", 0.25, False, False),
        ("Through Balls", 0.15, True, False),
        ("fThird Passes", 0.15, True, False),
        ("Progressive Carries", 0.10, True, False)
    ]

    progression_metrics = [
        ("Progressive Carries", 0.35, True, False),
        ("fThird Passes", 0.25, True, False),
        ("Through Balls", 0.20, True, False),
        ("Carries Ended with Chance", 0.20, True, False)
    ]

    defensive_metrics = [
        ("Tackles", 0.20, True, False),
        ("Interceptions", 0.20, True, False),
        ("Blocks", 0.15, True, False),
        ("Clearances", 0.15, True, False),
        ("gDuels Won", 0.10, False, False),
        ("gDuels %", 0.10, False, False),
        ("Possession Won", 0.10, True, False)
    ]

    creativity_metrics = [
        ("Assists", 0.25, True, False),
        ("Through Balls", 0.25, True, False),
        ("Carries Ended with Chance", 0.25, True, False),
        ("fThird Passes", 0.25, True, False)
    ]

    radar_data = {
        "Attacking": calculate_radar_score(
            player,
            players,
            attacking_metrics
        ),
        "Passing": calculate_radar_score(
            player,
            players,
            passing_metrics
        ),
        "Progression": calculate_radar_score(
            player,
            players,
            progression_metrics
        ),
        "Defensive": calculate_radar_score(
            player,
            players,
            defensive_metrics
        ),
        "Creativity": calculate_radar_score(
            player,
            players,
            creativity_metrics
        )
    }

    if position == "GK":

        goalkeeping_metrics = [
            ("Saves %", 0.30, False, False),
            ("Goals Prevented", 0.25, False, False),
            ("Clean Sheets", 0.20, False, False),
            ("Saves", 0.15, False, False),
            ("High Claims", 0.10, False, False)
        ]

        radar_data["Goalkeeping"] = calculate_radar_score(
            player,
            players,
            goalkeeping_metrics
        )

    return radar_data


def calculate_my_radar_data(match):

    position = match["Position"]

    minutes = max(
        float(match["Minutes"]),
        1
    )

    def per90(column):
        return (
            match[column]
            / minutes
            * 90
        )

    def score(value, benchmark):
        return min(
            max(value / benchmark * 100, 0),
            100
        )

    if position == "GK":

        save_attempts = (
            match["Saves"]
            + match["Goals Conceded"]
        )

        save_percentage = (
            match["Saves"]
            / save_attempts
            * 100
            if save_attempts > 0
            else 100
        )

        return {
            "Shot Stopping": score(
                per90("Saves"),
                4.0
            ),
            "Save %": score(
                save_percentage,
                75
            ),
            "Clean Sheets": score(
                match["Clean Sheets"],
                1
            ),
            "Command": score(
                per90("High Claims"),
                1.5
            ),
            "Distribution": score(
                match["Successful Passes"]
                / max(match["Passes"], 1)
                * 100,
                85
            )
        }

    if position == "FW":

        return {
            "Attacking": score(
                per90("Goals"),
                0.75
            ),
            "Creativity": score(
                per90("Assists"),
                0.35
            ),
            "Shooting": score(
                per90("Shots On Target"),
                2.0
            ),
            "Progression": score(
                per90("Progressive Carries"),
                5.0
            ),
            "Defensive": score(
                per90("Tackles"),
                1.5
            )
        }

    if position == "MF":

        return {
            "Attacking": score(
                per90("Assists"),
                0.30
            ),
            "Passing": score(
                match["Successful Passes"]
                / max(match["Passes"], 1)
                * 100,
                90
            ),
            "Progression": score(
                per90("Progressive Carries"),
                5.0
            ),
            "Defensive": score(
                per90("Tackles"),
                2.5
            ),
            "Interceptions": score(
                per90("Interceptions"),
                1.5
            )
        }

    return {
        "Defensive": score(
            per90("Tackles"),
            3.0
        ),
        "Interceptions": score(
            per90("Interceptions"),
            2.0
        ),
        "Passing": score(
            match["Successful Passes"]
            / max(match["Passes"], 1)
            * 100,
            90
        ),
        "Progression": score(
            per90("Progressive Carries"),
            3.0
        ),
        "Possession": score(
            per90("Possession Won"),
            5.0
        )
    }


def create_radar_chart(
    radar_data,
    title=None,
    player_name=None,
    player2_data=None,
    player2_name=None
):

    categories = list(
        radar_data.keys()
    )

    values = list(
        radar_data.values()
    )

    categories_closed = (
        categories
        + categories[:1]
    )

    values_closed = (
        values
        + values[:1]
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values_closed,
            theta=categories_closed,
            fill="toself",
            name=player_name or "Player",
            line=dict(
                color="#8BBB92",
                width=3
            ),
            fillcolor="rgba(42, 131, 95, 0.28)"
        )
    )

    if (
        player2_data is not None
        and player2_name is not None
    ):

        values2 = list(
            player2_data.values()
        )

        values2_closed = (
            values2
            + values2[:1]
        )

        fig.add_trace(
            go.Scatterpolar(
                r=values2_closed,
                theta=categories_closed,
                fill="toself",
                name=player2_name,
                line=dict(
                    color="#2A835F",
                    width=3
                ),
                fillcolor="rgba(139, 187, 146, 0.16)"
            )
        )

    fig.update_layout(
        polar=dict(
            bgcolor="#12544F",
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(
                    color="#8BBB92",
                    size=10
                ),
                gridcolor="rgba(139, 187, 146, 0.22)",
                linecolor="rgba(139, 187, 146, 0.22)"
            ),
            angularaxis=dict(
                tickfont=dict(
                    color="#FFFFFF",
                    size=11
                ),
                gridcolor="rgba(139, 187, 146, 0.18)",
                linecolor="rgba(139, 187, 146, 0.18)"
            )
        ),
        paper_bgcolor="#12544F",
        plot_bgcolor="#12544F",
        font=dict(
            family="Inter",
            color="#FFFFFF"
        ),
        showlegend=True,
        legend=dict(
            font=dict(
                color="#FFFFFF",
                size=11
            ),
            bgcolor="rgba(0,0,0,0)"
        ),
        title=dict(
            text=title or "",
            font=dict(
                color="#FFFFFF",
                size=16
            )
        ),
        height=500,
        margin=dict(
            l=40,
            r=40,
            t=55,
            b=30
        )
    )

    return fig


if page == "Player Analysis":

    st.markdown("""
    <div class="page-header">
        <div class="page-eyebrow">Professional Football</div>
        <div class="page-title">Player Analysis</div>
        <div class="page-description">
            Explore player performance, productivity ratings and detailed statistical profiles.
        </div>
    </div>
    """, unsafe_allow_html=True)

    player_name = st.selectbox(
        "Select a player",
        sorted(
            players["Player Name"]
            .dropna()
            .unique()
        )
    )

    player = players[
        players["Player Name"] == player_name
    ].iloc[0]

    st.markdown(f"""
    <div class="player-identity">
        <div class="player-name">{player_name}</div>
        <div class="player-meta">{player['Club']} · {player['Nationality']}</div>
        <div class="position-badge">{player['Position']}</div>
    </div>
    """, unsafe_allow_html=True)

    attacking_score = calculate_productivity(
        player,
        players,
        "attacking"
    )

    defensive_score = calculate_productivity(
        player,
        players,
        "defensive"
    )

    attacking_rating = get_rating(
        attacking_score
    )

    defensive_rating = get_rating(
        defensive_score
    )

    st.markdown(
        '<div class="section-heading">Productivity</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Attacking Productivity",
            attacking_rating,
            f"{attacking_score:.0f} / 100"
        )

    with col2:
        st.metric(
            "Defensive Productivity",
            defensive_rating,
            f"{defensive_score:.0f} / 100"
        )

    st.caption(
        "Scores use position-adjusted percentile rankings, "
        "weighted performance metrics and playing-time reliability."
    )

    st.markdown(
        '<div class="section-heading">Player Profile</div>',
        unsafe_allow_html=True
    )

    radar_data = get_player_radar_data(
        player,
        players
    )

    radar_chart = create_radar_chart(
        radar_data,
        title="Performance Profile",
        player_name=player_name
    )

    st.plotly_chart(
        radar_chart,
        use_container_width=True
    )

    st.caption(
        "Radar scores are normalised to 0–100 and compare "
        "the player with others in their position group."
    )

    if st.button(
        "Click here to learn more →"
    ):

        st.session_state["page"] = (
            "Rating Methodology"
        )

        st.rerun()

    st.markdown(
        '<div class="section-heading">Basic Statistics</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Appearances",
        player["Appearances"]
    )

    col2.metric(
        "Minutes",
        player["Minutes"]
    )

    col3.metric(
        "Goals",
        player["Goals"]
    )

    col4.metric(
        "Assists",
        player["Assists"]
    )

    st.markdown(
        '<div class="section-heading">Attacking</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Shots",
        player["Shots"]
    )

    col2.metric(
        "Shots On Target",
        player["Shots On Target"]
    )

    col3.metric(
        "Conversion",
        f"{player['Conversion %']:.1f}%"
    )

    col4.metric(
        "Big Chances Missed",
        player["Big Chances Missed"]
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Hit Woodwork",
        player["Hit Woodwork"]
    )

    col2.metric(
        "Offsides",
        player["Offsides"]
    )

    col3.metric(
        "Carries Ended With Goal",
        player["Carries Ended with Goal"]
    )

    col4.metric(
        "Carries Ended With Assist",
        player["Carries Ended with Assist"]
    )

    st.markdown(
        '<div class="section-heading">Passing & Progression</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Passes",
        player["Passes"]
    )

    col2.metric(
        "Successful Passes",
        player["Successful Passes"]
    )

    col3.metric(
        "Pass Accuracy",
        f"{player['Passes%']:.1f}%"
    )

    col4.metric(
        "Through Balls",
        player["Through Balls"]
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Progressive Carries",
        player["Progressive Carries"]
    )

    col2.metric(
        "Progressive Passes",
        player["fThird Passes"]
    )

    col3.metric(
        "Successful Crosses",
        player["Successful Crosses"]
    )

    col4.metric(
        "Cross Accuracy",
        f"{player['Crosses %']:.1f}%"
    )

    st.markdown(
        '<div class="section-heading">Defensive</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Tackles",
        player["Tackles"]
    )

    col2.metric(
        "Interceptions",
        player["Interceptions"]
    )

    col3.metric(
        "Blocks",
        player["Blocks"]
    )

    col4.metric(
        "Clearances",
        player["Clearances"]
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Ground Duels Won",
        player["gDuels Won"]
    )

    col2.metric(
        "Ground Duel %",
        f"{player['gDuels %']:.1f}%"
    )

    col3.metric(
        "Aerial Duels Won",
        player["aDuels Won"]
    )

    col4.metric(
        "Aerial Duel %",
        f"{player['aDuels %']:.1f}%"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Possession Won",
        player["Possession Won"]
    )

    col2.metric(
        "Fouls",
        player["Fouls"]
    )

    col3.metric(
        "Dispossessed",
        player["Dispossessed"]
    )

    if str(
        player["Position"]
    ).upper() == "GK":

        st.markdown(
            '<div class="section-heading">Goalkeeping</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Saves",
            player["Saves"]
        )

        col2.metric(
            "Save %",
            f"{player['Saves %']:.1f}%"
        )

        col3.metric(
            "Penalties Saved",
            player["Penalties Saved"]
        )

        col4.metric(
            "Goals Prevented",
            player["Goals Prevented"]
        )

    st.markdown(
        '<div class="section-heading">Discipline</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    col1.metric(
        "Yellow Cards",
        player["Yellow Cards"]
    )

    col2.metric(
        "Red Cards",
        player["Red Cards"]
    )

    st.markdown(
        '<div class="section-heading">Per 90 Statistics</div>',
        unsafe_allow_html=True
    )

    minutes = float(
        player["Minutes"]
    )

    def player_per90(column):

        value = pd.to_numeric(
            player[column],
            errors="coerce"
        )

        if pd.isna(value) or minutes <= 0:
            return 0

        return (
            value
            / minutes
            * 90
        )

    st.caption(
        "Per-90 statistics normalise a player's output to 90 "
        "minutes, making players with different amounts of "
        "playing time easier to compare."
    )

    st.markdown("**Attacking**")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Goals / 90",
        f"{player_per90('Goals'):.2f}"
    )

    col2.metric(
        "Assists / 90",
        f"{player_per90('Assists'):.2f}"
    )

    col3.metric(
        "Shots / 90",
        f"{player_per90('Shots'):.2f}"
    )

    col4.metric(
        "Shots On Target / 90",
        f"{player_per90('Shots On Target'):.2f}"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Goal Carries / 90",
        f"{player_per90('Carries Ended with Goal'):.2f}"
    )

    col2.metric(
        "Assist Carries / 90",
        f"{player_per90('Carries Ended with Assist'):.2f}"
    )

    col3.metric(
        "Shot Carries / 90",
        f"{player_per90('Carries Ended with Shot'):.2f}"
    )

    col4.metric(
        "Chance Carries / 90",
        f"{player_per90('Carries Ended with Chance'):.2f}"
    )

    st.markdown(
        "**Passing & Progression**"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Passes / 90",
        f"{player_per90('Passes'):.2f}"
    )

    col2.metric(
        "Successful Passes / 90",
        f"{player_per90('Successful Passes'):.2f}"
    )

    col3.metric(
        "Through Balls / 90",
        f"{player_per90('Through Balls'):.2f}"
    )

    col4.metric(
        "Progressive Carries / 90",
        f"{player_per90('Progressive Carries'):.2f}"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Final Third Passes / 90",
        f"{player_per90('fThird Passes'):.2f}"
    )

    col2.metric(
        "Successful Final Third Passes / 90",
        f"{player_per90('Successful fThird Passes'):.2f}"
    )

    col3.metric(
        "Crosses / 90",
        f"{player_per90('Crosses'):.2f}"
    )

    col4.metric(
        "Successful Crosses / 90",
        f"{player_per90('Successful Crosses'):.2f}"
    )

    st.markdown("**Defensive**")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Tackles / 90",
        f"{player_per90('Tackles'):.2f}"
    )

    col2.metric(
        "Interceptions / 90",
        f"{player_per90('Interceptions'):.2f}"
    )

    col3.metric(
        "Blocks / 90",
        f"{player_per90('Blocks'):.2f}"
    )

    col4.metric(
        "Clearances / 90",
        f"{player_per90('Clearances'):.2f}"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Possession Won / 90",
        f"{player_per90('Possession Won'):.2f}"
    )

    col2.metric(
        "Ground Duels Won / 90",
        f"{player_per90('gDuels Won'):.2f}"
    )

    col3.metric(
        "Aerial Duels Won / 90",
        f"{player_per90('aDuels Won'):.2f}"
    )

    if str(
        player["Position"]
    ).upper() == "GK":

        st.markdown(
            "**Goalkeeping**"
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Saves / 90",
            f"{player_per90('Saves'):.2f}"
        )

        col2.metric(
            "Goals Conceded / 90",
            f"{player_per90('Goals Conceded'):.2f}"
        )

        col3.metric(
            "High Claims / 90",
            f"{player_per90('High Claims'):.2f}"
        )


elif page == "Player Comparison":

    st.markdown("""
    <div class="page-header">
        <div class="page-eyebrow">Head To Head</div>
        <div class="page-title">Player Comparison</div>
        <div class="page-description">
            Compare two players across performance profiles, statistics and per-90 output.
        </div>
    </div>
    """, unsafe_allow_html=True)

    positions = sorted(
        players["Position"]
        .dropna()
        .unique()
    )

    selected_position = st.selectbox(
        "Filter by position",
        positions
    )

    position_players = sorted(
        players[
            players["Position"]
            == selected_position
        ]["Player Name"]
        .dropna()
        .unique()
    )

    player1_name = st.selectbox(
        "First player",
        position_players,
        key="comparison_player1"
    )

    player2_name = st.selectbox(
        "Second player",
        position_players,
        key="comparison_player2"
    )

    player1 = players[
        players["Player Name"]
        == player1_name
    ].iloc[0]

    player2 = players[
        players["Player Name"]
        == player2_name
    ].iloc[0]

    st.markdown(
        '<div class="section-heading">Players</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="player-identity">
            <div class="player-name">{player1_name}</div>
            <div class="player-meta">{player1['Club']} · {player1['Nationality']}</div>
            <div class="position-badge">{player1['Position']}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="player-identity">
            <div class="player-name">{player2_name}</div>
            <div class="player-meta">{player2['Club']} · {player2['Nationality']}</div>
            <div class="position-badge">{player2['Position']}</div>
        </div>
        """, unsafe_allow_html=True)

    radar1 = get_player_radar_data(
        player1,
        players
    )

    radar2 = get_player_radar_data(
        player2,
        players
    )

    st.markdown(
        '<div class="section-heading">Performance Profile</div>',
        unsafe_allow_html=True
    )

    comparison_radar = create_radar_chart(
        radar1,
        title="Player Profile Comparison",
        player_name=player1_name,
        player2_data=radar2,
        player2_name=player2_name
    )

    st.plotly_chart(
        comparison_radar,
        use_container_width=True
    )

    st.caption(
        "Both players are scored on the same normalised 0–100 scale "
        "using position-adjusted percentile rankings."
    )

    def create_comparison(
        metrics
    ):

        data = []

        for metric, column, lower_is_better in metrics:

            value1 = player1[column]
            value2 = player2[column]

            data.append({
                "Metric": metric,
                player1_name: value1,
                player2_name: value2
            })

        comparison = pd.DataFrame(
            data
        )

        styles = pd.DataFrame(
            "",
            index=comparison.index,
            columns=comparison.columns
        )

        for i, row in comparison.iterrows():

            value1 = pd.to_numeric(
                row[player1_name],
                errors="coerce"
            )

            value2 = pd.to_numeric(
                row[player2_name],
                errors="coerce"
            )

            lower_is_better = metrics[i][2]

            if pd.notna(value1) and pd.notna(value2):

                if lower_is_better:

                    if value1 < value2:
                        styles.loc[
                            i,
                            player1_name
                        ] = (
                            "background-color: #2A835F; "
                            "color: white; "
                            "font-weight: bold"
                        )

                    elif value2 < value1:
                        styles.loc[
                            i,
                            player2_name
                        ] = (
                            "background-color: #2A835F; "
                            "color: white; "
                            "font-weight: bold"
                        )

                else:

                    if value1 > value2:
                        styles.loc[
                            i,
                            player1_name
                        ] = (
                            "background-color: #2A835F; "
                            "color: white; "
                            "font-weight: bold"
                        )

                    elif value2 > value1:
                        styles.loc[
                            i,
                            player2_name
                        ] = (
                            "background-color: #2A835F; "
                            "color: white; "
                            "font-weight: bold"
                        )

        return comparison.style.apply(
            lambda x: styles,
            axis=None
        )

    attacking_metrics = [
        ("Goals", "Goals", False),
        ("Assists", "Assists", False),
        ("Shots", "Shots", False),
        ("Shots On Target", "Shots On Target", False),
        ("Conversion %", "Conversion %", False),
        ("Big Chances Missed", "Big Chances Missed", True),
        ("Hit Woodwork", "Hit Woodwork", False),
        ("Offsides", "Offsides", True),
        ("Carries Ended With Goal", "Carries Ended with Goal", False),
        ("Carries Ended With Assist", "Carries Ended with Assist", False)
    ]

    passing_metrics = [
        ("Passes", "Passes", False),
        ("Successful Passes", "Successful Passes", False),
        ("Pass Accuracy %", "Passes%", False),
        ("Through Balls", "Through Balls", False),
        ("Progressive Carries", "Progressive Carries", False),
        ("Final Third Passes", "fThird Passes", False),
        ("Successful Final Third Passes", "Successful fThird Passes", False),
        ("Crosses", "Crosses", False),
        ("Successful Crosses", "Successful Crosses", False),
        ("Cross Accuracy %", "Crosses %", False)
    ]

    defensive_metrics = [
        ("Tackles", "Tackles", False),
        ("Interceptions", "Interceptions", False),
        ("Blocks", "Blocks", False),
        ("Clearances", "Clearances", False),
        ("Ground Duels Won", "gDuels Won", False),
        ("Ground Duel %", "gDuels %", False),
        ("Aerial Duels Won", "aDuels Won", False),
        ("Aerial Duel %", "aDuels %", False),
        ("Possession Won", "Possession Won", False),
        ("Dispossessed", "Dispossessed", True),
        ("Fouls", "Fouls", True)
    ]

    st.markdown(
        '<div class="section-heading">Attacking</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        create_comparison(
            attacking_metrics
        ),
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        '<div class="section-heading">Attacking Comparison</div>',
        unsafe_allow_html=True
    )

    attacking_chart = pd.DataFrame(
        {
            player1_name: [
                player1["Goals"],
                player1["Assists"],
                player1["Shots"],
                player1["Shots On Target"],
                player1["Carries Ended with Goal"],
                player1["Carries Ended with Assist"]
            ],
            player2_name: [
                player2["Goals"],
                player2["Assists"],
                player2["Shots"],
                player2["Shots On Target"],
                player2["Carries Ended with Goal"],
                player2["Carries Ended with Assist"]
            ]
        },
        index=[
            "Goals",
            "Assists",
            "Shots",
            "Shots On Target",
            "Goal Carries",
            "Assist Carries"
        ]
    )

    st.bar_chart(
        attacking_chart
    )

    st.markdown(
        '<div class="section-heading">Passing & Progression</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        create_comparison(
            passing_metrics
        ),
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        '<div class="section-heading">Passing Comparison</div>',
        unsafe_allow_html=True
    )

    passing_chart = pd.DataFrame(
        {
            player1_name: [
                player1["Passes"],
                player1["Successful Passes"],
                player1["Through Balls"],
                player1["Progressive Carries"],
                player1["fThird Passes"],
                player1["Successful Crosses"]
            ],
            player2_name: [
                player2["Passes"],
                player2["Successful Passes"],
                player2["Through Balls"],
                player2["Progressive Carries"],
                player2["fThird Passes"],
                player2["Successful Crosses"]
            ]
        },
        index=[
            "Passes",
            "Successful Passes",
            "Through Balls",
            "Progressive Carries",
            "Final Third Passes",
            "Successful Crosses"
        ]
    )

    st.bar_chart(
        passing_chart
    )

    st.markdown(
        '<div class="section-heading">Defensive</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        create_comparison(
            defensive_metrics
        ),
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        '<div class="section-heading">Defensive Comparison</div>',
        unsafe_allow_html=True
    )

    defensive_chart = pd.DataFrame(
        {
            player1_name: [
                player1["Tackles"],
                player1["Interceptions"],
                player1["Blocks"],
                player1["Clearances"],
                player1["Possession Won"]
            ],
            player2_name: [
                player2["Tackles"],
                player2["Interceptions"],
                player2["Blocks"],
                player2["Clearances"],
                player2["Possession Won"]
            ]
        },
        index=[
            "Tackles",
            "Interceptions",
            "Blocks",
            "Clearances",
            "Possession Won"
        ]
    )

    st.bar_chart(
        defensive_chart
    )

    st.markdown(
        '<div class="section-heading">Per 90 Comparison</div>',
        unsafe_allow_html=True
    )

    def calculate_comparison_per90(
        player,
        column
    ):

        minutes = pd.to_numeric(
            player["Minutes"],
            errors="coerce"
        )

        value = pd.to_numeric(
            player[column],
            errors="coerce"
        )

        if (
            pd.isna(minutes)
            or minutes <= 0
            or pd.isna(value)
        ):
            return 0

        return (
            value
            / minutes
            * 90
        )

    per90_metrics = [
        ("Goals / 90", "Goals"),
        ("Assists / 90", "Assists"),
        ("Shots / 90", "Shots"),
        ("Shots On Target / 90", "Shots On Target"),
        ("Progressive Carries / 90", "Progressive Carries"),
        ("Final Third Passes / 90", "fThird Passes"),
        ("Through Balls / 90", "Through Balls"),
        ("Tackles / 90", "Tackles"),
        ("Interceptions / 90", "Interceptions"),
        ("Blocks / 90", "Blocks"),
        ("Clearances / 90", "Clearances"),
        ("Possession Won / 90", "Possession Won")
    ]

    per90_data = []

    for metric, column in per90_metrics:

        value1 = calculate_comparison_per90(
            player1,
            column
        )

        value2 = calculate_comparison_per90(
            player2,
            column
        )

        per90_data.append({
            "Metric": metric,
            player1_name: f"{value1:.2f}",
            player2_name: f"{value2:.2f}"
        })

    per90_comparison = pd.DataFrame(
        per90_data
    )

    styles = pd.DataFrame(
        "",
        index=per90_comparison.index,
        columns=per90_comparison.columns
    )

    for i, row in per90_comparison.iterrows():

        value1 = float(
            row[player1_name]
        )

        value2 = float(
            row[player2_name]
        )

        if value1 > value2:
            styles.loc[
                i,
                player1_name
            ] = (
                "background-color: #2A835F; "
                "color: white; "
                "font-weight: bold"
            )

        elif value2 > value1:
            styles.loc[
                i,
                player2_name
            ] = (
                "background-color: #2A835F; "
                "color: white; "
                "font-weight: bold"
            )

    st.dataframe(
        per90_comparison.style.apply(
            lambda x: styles,
            axis=None
        ),
        use_container_width=True,
        hide_index=True
    )


elif page == "My FUTBAZE":

    st.markdown("""
    <div class="page-header">
        <div class="page-eyebrow">Personal Performance</div>
        <div class="page-title">My FUTBAZE</div>
        <div class="page-description">
            Track your own football performances and monitor how your statistics change from match to match.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if "my_matches" not in st.session_state:
        st.session_state["my_matches"] = []

    st.markdown(
        '<div class="section-heading">Add Match</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        match_name = st.text_input(
            "Match",
            placeholder="e.g. Brighton vs Arsenal"
        )

    with col2:
        match_date = st.date_input(
            "Date"
        )

    with col3:
        match_position = st.selectbox(
            "Position",
            [
                "GK",
                "DF",
                "MF",
                "FW"
            ]
        )

    match_minutes = st.number_input(
        "Minutes Played",
        min_value=1,
        max_value=120,
        value=90
    )

    st.markdown(
        '<div class="section-heading">Attacking</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        match_goals = st.number_input(
            "Goals",
            min_value=0,
            value=0,
            key="my_goals"
        )

    with col2:
        match_assists = st.number_input(
            "Assists",
            min_value=0,
            value=0,
            key="my_assists"
        )

    with col3:
        match_shots = st.number_input(
            "Shots",
            min_value=0,
            value=0,
            key="my_shots"
        )

    with col4:
        match_shots_on_target = st.number_input(
            "Shots On Target",
            min_value=0,
            value=0,
            key="my_shots_on_target"
        )

    st.markdown(
        '<div class="section-heading">Passing & Progression</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        match_passes = st.number_input(
            "Passes",
            min_value=0,
            value=0,
            key="my_passes"
        )

    with col2:
        match_successful_passes = st.number_input(
            "Successful Passes",
            min_value=0,
            value=0,
            key="my_successful_passes"
        )

    with col3:
        match_progressive_carries = st.number_input(
            "Progressive Carries",
            min_value=0,
            value=0,
            key="my_progressive_carries"
        )

    with col4:
        match_through_balls = st.number_input(
            "Through Balls",
            min_value=0,
            value=0,
            key="my_through_balls"
        )

    st.markdown(
        '<div class="section-heading">Defensive</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        match_tackles = st.number_input(
            "Tackles",
            min_value=0,
            value=0,
            key="my_tackles"
        )

    with col2:
        match_interceptions = st.number_input(
            "Interceptions",
            min_value=0,
            value=0,
            key="my_interceptions"
        )

    with col3:
        match_blocks = st.number_input(
            "Blocks",
            min_value=0,
            value=0,
            key="my_blocks"
        )

    with col4:
        match_possession_won = st.number_input(
            "Possession Won",
            min_value=0,
            value=0,
            key="my_possession_won"
        )

    match_goals_conceded = 0
    match_saves = 0
    match_clean_sheets = 0
    match_high_claims = 0
    match_penalties_saved = 0

    if match_position == "GK":

        st.markdown(
            '<div class="section-heading">Goalkeeping</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            match_saves = st.number_input(
                "Saves",
                min_value=0,
                value=0,
                key="my_saves"
            )

        with col2:
            match_goals_conceded = st.number_input(
                "Goals Conceded",
                min_value=0,
                value=0,
                key="my_goals_conceded"
            )

        with col3:
            match_clean_sheets = st.selectbox(
                "Clean Sheet",
                [0, 1],
                key="my_clean_sheet"
            )

        with col4:
            match_high_claims = st.number_input(
                "High Claims",
                min_value=0,
                value=0,
                key="my_high_claims"
            )

        with col5:
            match_penalties_saved = st.number_input(
                "Penalties Saved",
                min_value=0,
                value=0,
                key="my_penalties_saved"
            )

    if st.button(
        "Save Match"
    ):

        if not match_name.strip():

            st.warning(
                "Please enter a match name."
            )

        elif (
            match_successful_passes
            > match_passes
        ):

            st.warning(
                "Successful passes cannot be greater "
                "than total passes."
            )

        elif (
            match_shots_on_target
            > match_shots
        ):

            st.warning(
                "Shots on target cannot be greater "
                "than total shots."
            )

        else:

            match_data = {
                "Date": match_date,
                "Match": match_name,
                "Position": match_position,
                "Minutes": match_minutes,
                "Goals": match_goals,
                "Assists": match_assists,
                "Shots": match_shots,
                "Shots On Target": match_shots_on_target,
                "Passes": match_passes,
                "Successful Passes": match_successful_passes,
                "Progressive Carries": match_progressive_carries,
                "Through Balls": match_through_balls,
                "Tackles": match_tackles,
                "Interceptions": match_interceptions,
                "Blocks": match_blocks,
                "Possession Won": match_possession_won,
                "Saves": match_saves,
                "Goals Conceded": match_goals_conceded,
                "Clean Sheets": match_clean_sheets,
                "High Claims": match_high_claims,
                "Penalties Saved": match_penalties_saved,
                "Goals Prevented": 0
            }

            match_score = calculate_my_performance_score(
                match_data
            )

            match_data["Performance Score"] = round(
                match_score,
                2
            )

            st.session_state[
                "my_matches"
            ].append(
                match_data
            )

            st.success(
                "Match saved successfully!"
            )

    if st.session_state["my_matches"]:

        st.markdown(
            '<div class="section-heading">Match History</div>',
            unsafe_allow_html=True
        )

        match_history = pd.DataFrame(
            st.session_state[
                "my_matches"
            ]
        )

        st.dataframe(
            match_history,
            use_container_width=True,
            hide_index=True
        )

        latest_match = match_history.iloc[-1].to_dict()

        st.markdown(
            '<div class="section-heading">Latest Performance Profile</div>',
            unsafe_allow_html=True
        )

        my_radar_data = calculate_my_radar_data(
            latest_match
        )

        my_radar_chart = create_radar_chart(
            my_radar_data,
            title="Latest Match Profile",
            player_name="My FUTBAZE"
        )

        st.plotly_chart(
            my_radar_chart,
            use_container_width=True
        )

        st.caption(
            "Radar scores are based on position-specific "
            "performance benchmarks."
        )

        st.markdown(
            '<div class="section-heading">Performance Trends</div>',
            unsafe_allow_html=True
        )

        trend_data = (
            match_history.copy()
        )

        trend_data["Goals / 90"] = (
            trend_data["Goals"]
            / trend_data["Minutes"]
            * 90
        )

        trend_data["Assists / 90"] = (
            trend_data["Assists"]
            / trend_data["Minutes"]
            * 90
        )

        trend_data["Tackles / 90"] = (
            trend_data["Tackles"]
            / trend_data["Minutes"]
            * 90
        )

        trend_data["Interceptions / 90"] = (
            trend_data["Interceptions"]
            / trend_data["Minutes"]
            * 90
        )

        trend_data["Progressive Carries / 90"] = (
            trend_data["Progressive Carries"]
            / trend_data["Minutes"]
            * 90
        )

        chart_data = trend_data[
            [
                "Goals / 90",
                "Assists / 90",
                "Tackles / 90",
                "Interceptions / 90",
                "Progressive Carries / 90"
            ]
        ]

        st.line_chart(
            chart_data
        )

        st.markdown(
            '<div class="section-heading">Latest Match</div>',
            unsafe_allow_html=True
        )

        latest = trend_data.iloc[-1]

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Goals / 90",
            f"{latest['Goals / 90']:.2f}"
        )

        col2.metric(
            "Assists / 90",
            f"{latest['Assists / 90']:.2f}"
        )

        col3.metric(
            "Tackles / 90",
            f"{latest['Tackles / 90']:.2f}"
        )

        col4.metric(
            "Progressive Carries / 90",
            f"{latest['Progressive Carries / 90']:.2f}"
        )

        st.markdown(
            '<div class="section-heading">Latest Performance Score</div>',
            unsafe_allow_html=True
        )

        latest_score = latest.get(
            "Performance Score",
            None
        )

        if (
            latest_score is not None
            and pd.notna(latest_score)
        ):

            latest_rating = get_rating(
                latest_score
            )

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Performance Score",
                    f"{latest_score:.0f} / 100"
                )

            with col2:
                st.metric(
                    "Rating",
                    latest_rating
                )

            st.caption(
                "Your score is calculated using "
                "position-specific performance benchmarks "
                "and weighted statistics."
            )

        else:

            st.info(
                "Performance Score is not available for "
                "this match."
            )

        st.markdown(
            '<div class="section-heading">Career Statistics</div>',
            unsafe_allow_html=True
        )

        career_minutes = (
            match_history["Minutes"].sum()
        )

        career_goals = (
            match_history["Goals"].sum()
        )

        career_assists = (
            match_history["Assists"].sum()
        )

        career_shots = (
            match_history["Shots"].sum()
        )

        career_shots_on_target = (
            match_history[
                "Shots On Target"
            ].sum()
        )

        career_passes = (
            match_history["Passes"].sum()
        )

        career_successful_passes = (
            match_history[
                "Successful Passes"
            ].sum()
        )

        career_progressive_carries = (
            match_history[
                "Progressive Carries"
            ].sum()
        )

        career_through_balls = (
            match_history[
                "Through Balls"
            ].sum()
        )

        career_tackles = (
            match_history[
                "Tackles"
            ].sum()
        )

        career_interceptions = (
            match_history[
                "Interceptions"
            ].sum()
        )

        career_blocks = (
            match_history[
                "Blocks"
            ].sum()
        )

        career_possession_won = (
            match_history[
                "Possession Won"
            ].sum()
        )

        st.markdown(
            '<div class="section-heading">Overall</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Matches",
            len(match_history)
        )

        col2.metric(
            "Minutes",
            career_minutes
        )

        col3.metric(
            "Goals",
            career_goals
        )

        col4.metric(
            "Assists",
            career_assists
        )

        st.markdown(
            '<div class="section-heading">Attacking</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Shots",
            career_shots
        )

        col2.metric(
            "Shots On Target",
            career_shots_on_target
        )

        col3.metric(
            "Goals / 90",
            (
                f"{career_goals / career_minutes * 90:.2f}"
                if career_minutes > 0
                else "0.00"
            )
        )

        col4.metric(
            "Assists / 90",
            (
                f"{career_assists / career_minutes * 90:.2f}"
                if career_minutes > 0
                else "0.00"
            )
        )

        st.markdown(
            '<div class="section-heading">Passing & Progression</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Passes",
            career_passes
        )

        col2.metric(
            "Successful Passes",
            career_successful_passes
        )

        col3.metric(
            "Pass Accuracy",
            (
                f"{career_successful_passes / career_passes * 100:.1f}%"
                if career_passes > 0
                else "0.0%"
            )
        )

        col4.metric(
            "Progressive Carries",
            career_progressive_carries
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Through Balls",
            career_through_balls
        )

        col2.metric(
            "Tackles",
            career_tackles
        )

        col3.metric(
            "Interceptions",
            career_interceptions
        )

        st.markdown(
            '<div class="section-heading">Defensive</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Tackles",
            career_tackles
        )

        col2.metric(
            "Interceptions",
            career_interceptions
        )

        col3.metric(
            "Blocks",
            career_blocks
        )

        col4.metric(
            "Possession Won",
            career_possession_won
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Tackles / 90",
            (
                f"{career_tackles / career_minutes * 90:.2f}"
                if career_minutes > 0
                else "0.00"
            )
        )

        col2.metric(
            "Interceptions / 90",
            (
                f"{career_interceptions / career_minutes * 90:.2f}"
                if career_minutes > 0
                else "0.00"
            )
        )

        col3.metric(
            "Possession Won / 90",
            (
                f"{career_possession_won / career_minutes * 90:.2f}"
                if career_minutes > 0
                else "0.00"
            )
        )

    else:

        st.info(
            "No matches recorded yet. Add your first "
            "match above to start building your FUTBAZE "
            "performance history."
        )


elif page == "Rating Methodology":

    st.markdown("""
    <div class="page-header">
        <div class="page-eyebrow">How FUTBAZE Works</div>
        <div class="page-title">Rating Methodology</div>
        <div class="page-description">
            Understand how FUTBAZE turns football statistics into position-aware performance ratings.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write(
        "FUTBAZE Productivity Ratings are designed to provide "
        "a position-aware measure of how effectively a player "
        "performs across important areas of their game."
    )

    st.markdown(
        '<div class="section-heading">1. Position Grouping</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Players are grouped into four main position categories: "
        "Goalkeepers (GK), Defenders (DF), Midfielders (MF) and "
        "Forwards (FW). Players are primarily compared against "
        "others within the same position group."
    )

    st.markdown(
        '<div class="section-heading">2. Minimum Playing Time</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Players with at least 900 minutes are used as the main "
        "comparison group. This reduces the impact of players "
        "with very small samples of playing time."
    )

    st.markdown(
        '<div class="section-heading">3. Per-90 Statistics</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Statistics such as goals, assists, tackles and "
        "interceptions are converted into per-90 values. "
        "This allows players who have played different amounts "
        "of time to be compared more fairly."
    )

    st.latex(
        r"\text{Per 90} = "
        r"\frac{\text{Statistic}}{\text{Minutes Played}} "
        r"\times 90"
    )

    st.markdown(
        '<div class="section-heading">4. Percentile Scores</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Each metric is converted into a percentile between "
        "0 and 100. The percentile represents how a player's "
        "value compares with the selected comparison group."
    )

    st.write(
        "For example, a player with a Goals Per 90 percentile "
        "of 90 performs better than approximately 90% of the "
        "players in the comparison group for that metric."
    )

    st.markdown(
        '<div class="section-heading">5. Position-Specific Weighting</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Different positions are judged using different "
        "combinations of statistics. The importance of each "
        "statistic is represented by a weight."
    )

    st.write(
        "For example, attacking productivity for forwards uses:"
    )

    st.table(
        pd.DataFrame({
            "Metric": [
                "Goals Per 90",
                "Assists Per 90",
                "Shots On Target Per 90",
                "Conversion %",
                "Carries Ended With Goal Per 90",
                "Carries Ended With Assist Per 90",
                "Carries Ended With Chance Per 90"
            ],
            "Weight": [
                "25%",
                "20%",
                "15%",
                "10%",
                "10%",
                "10%",
                "10%"
            ]
        })
    )

    st.markdown(
        '<div class="section-heading">6. Weighted Score</div>',
        unsafe_allow_html=True
    )

    st.write(
        "The percentile score for each metric is multiplied "
        "by its weight. These weighted values are then combined "
        "to produce the player's initial productivity score."
    )

    st.latex(
        r"\text{Initial Score} = "
        r"\sum(\text{Percentile Score} "
        r"\times \text{Metric Weight})"
    )

    st.markdown(
        '<div class="section-heading">7. Playing-Time Reliability</div>',
        unsafe_allow_html=True
    )

    st.write(
        "A player's score is adjusted according to how much "
        "they have played. Players with 900 or more minutes "
        "receive the full calculated score. Players below "
        "900 minutes are gradually pulled towards 50 to reduce "
        "the influence of small samples."
    )

    st.latex(
        r"\text{Final Score} = "
        r"50 + (\text{Initial Score} - 50) "
        r"\times \min\left(\frac{\text{Minutes}}{900},1\right)"
    )

    st.markdown(
        '<div class="section-heading">8. Rating Bands</div>',
        unsafe_allow_html=True
    )

    st.table(
        pd.DataFrame({
            "Score": [
                "64–100",
                "50–63.9",
                "30–49.9",
                "20–29.9",
                "0–19.9"
            ],
            "Rating": [
                "Elite",
                "High Standard",
                "Standard",
                "Mediocre",
                "Poor"
            ]
        })
    )

    st.markdown(
        '<div class="section-heading">9. Defensive Metrics</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Defensive productivity uses different metrics depending "
        "on position. For example, defenders are evaluated using "
        "tackles, interceptions, blocks, clearances and duel "
        "statistics, while goalkeepers use metrics such as save "
        "percentage, goals prevented and clean sheets."
    )

    st.markdown(
        '<div class="section-heading">10. Lower Is Better Metrics</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Some statistics are more positive when their value is "
        "lower. For example, being dispossessed less often is "
        "generally better. These metrics are therefore reversed "
        "when calculating their percentile contribution."
    )

    st.markdown(
        '<div class="section-heading">Radar Charts</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Radar charts provide a visual summary of performance "
        "across several areas of a player's game. Scores are "
        "normalised to a 0–100 scale so that different statistics "
        "can be displayed together."
    )

    st.write(
        "Professional player radar charts compare players with "
        "others in their position group. My FUTBAZE radar charts "
        "use position-specific performance benchmarks."
    )

    st.markdown(
        '<div class="section-heading">Important Note</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "FUTBAZE ratings are an analytical model created for "
        "this project. They are intended to provide a consistent "
        "way of comparing players using the available data and "
        "should not be treated as an official player rating."
    )