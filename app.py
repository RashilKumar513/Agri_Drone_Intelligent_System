import streamlit as st
import pandas as pd
import plotly.express as px
from geopy.distance import geodesic

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="AgriDrone Intelligence Platform",
    page_icon="🌾",
    layout="wide"
)

# ----------------------------------
# AIRPORT DATABASE (Tamil Nadu)
# ----------------------------------

AIRPORTS = {
    "Chennai": (12.9941, 80.1709),
    "Coimbatore": (11.0300, 77.0434),
    "Madurai": (9.8345, 78.0934),
    "Trichy": (10.7654, 78.7097),
    "Salem": (11.7833, 78.0656),
    "Tuticorin": (8.7242, 78.0258)
}

# ----------------------------------
# FUNCTIONS
# ----------------------------------

def nearest_airport(lat, lon):
    nearest_name = None
    nearest_distance = float("inf")

    for airport, coords in AIRPORTS.items():

        distance = geodesic(
            (lat, lon),
            coords
        ).km

        if distance < nearest_distance:
            nearest_distance = distance
            nearest_name = airport

    return nearest_name, nearest_distance


def classify_drone_zone(lat, lon):

    airport_name, airport_distance = nearest_airport(
        lat,
        lon
    )

    # Classification Logic

    if airport_distance < 5:

        zone = "Red"
        score = 20

    elif airport_distance < 12:

        zone = "Inner Yellow"
        score = 50

    elif airport_distance < 25:

        zone = "Outer Yellow"
        score = 75

    else:

        zone = "Green"
        score = min(
            100,
            round(75 + (airport_distance / 20))
        )

    return pd.Series([
        zone,
        score,
        airport_name,
        round(airport_distance, 2)
    ])


def display_value(value, fallback="Not specified"):
    if pd.isna(value):
        return fallback

    text = str(value).strip()

    if text.lower() in {"", "none", "nan"}:
        return fallback

    return text


# ----------------------------------
# LOAD DATA
# ----------------------------------

df = pd.read_csv(
    "tamilnadu_agriculture.csv"
)

# Ensure coordinates exist

required_columns = [
    "Latitude",
    "Longitude"
]

for col in required_columns:
    if col not in df.columns:
        st.error(
            f"Missing column: {col}"
        )
        st.stop()

# ----------------------------------
# CALCULATE DRONE ZONES
# ----------------------------------

df[
    [
        "DroneZone",
        "ReadinessScore",
        "NearestAirport",
        "AirportDistanceKM"
    ]
] = df.apply(
    lambda row:
    classify_drone_zone(
        row["Latitude"],
        row["Longitude"]
    ),
    axis=1
)

# ----------------------------------
# HEADER
# ----------------------------------

st.title(
    "🌾 AgriDrone Intelligence Platform"
)

st.markdown("""
### Smart Agriculture & Drone Zone Information System

Analyze agricultural regions, identify drone-operational zones,
and explore district-wise agricultural insights across Tamil Nadu.
""")

# ----------------------------------
# METRICS
# ----------------------------------

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Districts",
        df["District"].nunique()
    )

with col2:
    st.metric(
        "Taluks",
        df["Taluk"].nunique()
    )

with col3:
    st.metric(
        "Green Zones",
        len(
            df[
                df["DroneZone"] == "Green"
            ]
        )
    )

with col4:
    st.metric(
        "Records",
        len(df)
    )

# ----------------------------------
# DISTRICT EXPLORER
# ----------------------------------

st.markdown("---")
st.header("📍 District Explorer")

district = st.selectbox(
    "Select District",
    sorted(
        df["District"].unique()
    )
)

filtered = df[
    df["District"] == district
]

taluk = st.selectbox(
    "Select Taluk",
    sorted(
        filtered["Taluk"].unique()
    )
)

selected = filtered[
    filtered["Taluk"] == taluk
].iloc[0]

# ----------------------------------
# DETAILS
# ----------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader(
        "🌾 Agriculture Information"
    )

    st.write(
        "**District:**",
        selected["District"]
    )

    st.write(
        "**Taluk:**",
        selected["Taluk"]
    )

    st.write(
        "**Crop:**",
        selected["Crop"]
    )

    st.write(
        "**Soil:**",
        selected["Soil"]
    )

    st.write(
        "**Irrigation:**",
        display_value(
            selected["Irrigation"],
            "No major irrigation data available"
        )
    )

with col2:

    st.subheader(
        "🚁 Drone Intelligence"
    )

    zone = selected["DroneZone"]
    score = selected["ReadinessScore"]

    if zone == "Green":
        st.success(
            f"🟢 {zone} Zone"
        )

    elif zone in [
        "Outer Yellow",
        "Inner Yellow"
    ]:
        st.warning(
            f"🟡 {zone} Zone"
        )

    else:
        st.error(
            f"🔴 {zone} Zone"
        )

    st.progress(
        score / 100
    )

    st.write(
        f"Drone Readiness Score: {score}/100"
    )

    st.write(
        f"Nearest Airport: {selected['NearestAirport']}"
    )

    st.write(
        f"Airport Distance: {selected['AirportDistanceKM']} km"
    )

# ----------------------------------
# RECOMMENDATIONS
# ----------------------------------

st.markdown("---")
st.header("🤖 Smart Recommendations")

if score >= 90:

    st.success(
        "✅ Drone Spraying"
    )

    st.success(
        "✅ Crop Monitoring"
    )

    st.success(
        "✅ NDVI Analysis"
    )

    st.success(
        "✅ Yield Estimation"
    )

elif score >= 70:

    st.warning(
        "⚠ Limited Agricultural Operations"
    )

    st.warning(
        "⚠ Altitude Monitoring Recommended"
    )

elif score >= 40:

    st.warning(
        "⚠ Prior Permission Required"
    )

    st.warning(
        "⚠ Controlled Operations Only"
    )

else:

    st.error(
        "❌ Drone Operations Restricted"
    )

# ----------------------------------
# ZONE DISTRIBUTION
# ----------------------------------

st.markdown("---")
st.header(
    "🚁 Drone Zone Distribution"
)

zone_count = (
    df["DroneZone"]
    .value_counts()
    .reset_index()
)

zone_count.columns = [
    "Zone",
    "Count"
]

zone_fig = px.pie(
    zone_count,
    names="Zone",
    values="Count",
    title="Drone Zone Distribution"
)

st.plotly_chart(
    zone_fig,
    use_container_width=True
)

# ----------------------------------
# CROP DISTRIBUTION
# ----------------------------------

st.markdown("---")
st.header(
    "📊 Crop Distribution"
)

crop_count = (
    df["Crop"]
    .value_counts()
    .reset_index()
)

crop_count.columns = [
    "Crop",
    "Count"
]

fig = px.bar(
    crop_count,
    x="Crop",
    y="Count",
    color="Crop",
    title="Crop Distribution Across Tamil Nadu"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------------
# MAP
# ----------------------------------

st.markdown("---")
st.header(
    "🗺 Agricultural Locations"
)

map_df = df.rename(
    columns={
        "Latitude": "latitude",
        "Longitude": "longitude"
    }
)

st.map(map_df)

# ----------------------------------
# DATA TABLE
# ----------------------------------

st.markdown("---")
st.header(
    "📋 Complete Dataset"
)

st.dataframe(
    df,
    use_container_width=True
)

# ----------------------------------
# DOWNLOAD
# ----------------------------------

csv = df.to_csv(
    index=False
)

st.download_button(
    label="⬇ Download Enhanced Dataset",
    data=csv,
    file_name="tamilnadu_agriculture_drone.csv",
    mime="text/csv"
)