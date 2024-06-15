import streamlit as st
import pandas as pd
import plotly.express as px

# Language Data (Dictionary)
languages = {
    "Bhojpuri": {
        "family": "Indo-Aryan",
        "script": "Devanagari",
        "official_status": "Minority language in Nepal",
        "states": ["Bihar", "Jharkhand", "Uttar Pradesh"],
        "speakers": 80000000,
        "linguistic_features": "Subject-Object-Verb word order, rich vocabulary influenced by Hindi and Urdu.",
        "cultural_significance": "Folk songs, Bidesiya and Piya Ke Gaon films, Chhath Puja festival",
        "learning_resources": "Bhojpuri dictionaries, online tutorials, language exchange groups",
    },
    "Tamil": {
        "family": "Dravidian",
        "script": "Tamil",
        "official_status": "Official language of Tamil Nadu and Puducherry",
        "states": ["Tamil Nadu", "Puducherry"],
        "speakers": 77000000,
        "linguistic_features": "Agglutinative language, rich literary tradition.",
        "cultural_significance": "Sangam literature, Carnatic music, Pongal festival",
        "learning_resources": "Tamil dictionaries, online courses, language learning apps",
    },
    "Kannada": {
        "family": "Dravidian",
        "script": "Kannada script",
        "official_status": "Official language of Karnataka",
        "states": ["Karnataka"],
        "number_of_speakers": 43000000,
        "linguistic_features": "Subject-Object-Verb word order, extensive use of particles",
        "cultural_significance": "Yakshagana theatre, Carnatic and Hindustani music, Hampi festival",
        "learning_resources": "Kannada textbooks, online courses, language exchange groups"
    },
    "Bengali": {
        "family": "Indo-Aryan",
        "script": "Bengali script",
        "official_status": "Official language of West Bengal and Tripura, national language of Bangladesh",
        "states": ["West Bengal", "Tripura"],
        "number_of_speakers": 230000000,
        "linguistic_features": "Subject-Object-Verb word order, rich inflectional morphology",
        "cultural_significance": "Rabindra Sangeet, Durga Puja festival, Bengali literature",
        "learning_resources": "Bengali language apps, textbooks, online classes"
    },
    "Hindi": {
        "family": "Indo-Aryan",
        "script": "Devanagari",
        "official_status": "Official language of India",
        "states": ["Uttar Pradesh", "Madhya Pradesh", "Bihar", "Rajasthan", "Haryana", "Uttarakhand", "Chhattisgarh", "Jharkhand", "Himachal Pradesh", "Delhi"],
        "number_of_speakers": 600000000,
        "linguistic_features": "Subject-Object-Verb word order, rich morphology, extensive loanwords from Sanskrit, Persian, Arabic, and English",
        "cultural_significance": "Bollywood cinema, Hindi literature, major festivals like Diwali and Holi",
        "learning_resources": "Hindi textbooks, language learning apps, online courses"
    },
    "Telugu": {
        "family": "Dravidian",
        "script": "Telugu script",
        "official_status": "Official language of Andhra Pradesh and Telangana",
        "states": ["Andhra Pradesh", "Telangana"],
        "number_of_speakers": 81000000,
        "linguistic_features": "Agglutinative language, Subject-Object-Verb word order, use of vowel harmony",
        "cultural_significance": "Classical dance forms like Kuchipudi, Carnatic music, Telugu cinema",
        "learning_resources": "Telugu learning apps, textbooks, online tutorials"
    },
    "Marathi": {
        "family": "Indo-Aryan",
        "script": "Devanagari",
        "official_status": "Official language of Maharashtra",
        "states": ["Maharashtra", "Goa"],
        "number_of_speakers": 83000000,
        "linguistic_features": "Subject-Object-Verb word order, use of gender inflections, rich literary tradition",
        "cultural_significance": "Marathi literature, folk theatre (Tamasha), Ganesh Chaturthi festival",
        "learning_resources": "Marathi textbooks, online courses, language apps"
    },
    "Gujarati": {
        "family": "Indo-Aryan",
        "script": "Gujarati script",
        "official_status": "Official language of Gujarat",
        "states": ["Gujarat"],
        "number_of_speakers": 55000000,
        "linguistic_features": "Subject-Object-Verb word order, extensive use of postpositions, phonemic contrast between aspirated and unaspirated consonants",
        "cultural_significance": "Garba dance, Gujarati literature, Navratri festival",
        "learning_resources": "Gujarati learning apps, dictionaries, online courses"
    },
    "Punjabi": {
        "family": "Indo-Aryan",
        "script": "Gurmukhi",
        "official_status": "Official language of Punjab",
        "states": ["Punjab"],
        "number_of_speakers": 125000000,
        "linguistic_features": "Subject-Object-Verb word order, tonal language, use of honorifics",
        "cultural_significance": "Bhangra dance, Punjabi music and literature, Vaisakhi festival",
        "learning_resources": "Punjabi textbooks, online tutorials, language apps"
    },
    "Malayalam": {
        "family": "Dravidian",
        "script": "Malayalam script",
        "official_status": "Official language of Kerala",
        "states": ["Kerala"],
        "number_of_speakers": 35000000,
        "linguistic_features": "Agglutinative language, Subject-Object-Verb word order, extensive use of inflection",
        "cultural_significance": "Kathakali dance, Malayalam cinema, Onam festival",
        "learning_resources": "Malayalam learning apps, online courses, dictionaries"
    },
    "Odia": {
        "family": "Indo-Aryan",
        "script": "Odia script",
        "official_status": "Official language of Odisha",
        "states": ["Odisha"],
        "number_of_speakers": 37000000,
        "linguistic_features": "Subject-Object-Verb word order, rich morphology, extensive use of affixes",
        "cultural_significance": "Odissi dance, Odia literature, Rath Yatra festival",
        "learning_resources": "Odia learning apps, textbooks, online tutorials"
    }
}

# Convert Dictionary to DataFrame
df = pd.DataFrame.from_dict(languages, orient="index").reset_index().rename(columns={"index": "language"})
df["states"] = df["states"].apply(lambda x: ", ".join(x))

# Sidebar for Search and Filter
st.sidebar.title("Search & Filter")
selected_language = st.sidebar.selectbox("Select Language", df["language"].unique())
selected_state = st.sidebar.multiselect("Select State(s)", df["states"].unique().tolist())

# Filter data based on selection
filtered_df = df[df["language"] == selected_language]
if selected_state:
    filtered_df = filtered_df[filtered_df["states"].str.contains("|".join(selected_state))]

# Main Content
st.title("Bharat Bhasha Kosha: Indian Language Treasure")
st.write(f"Details for: *{selected_language}*")

# Basic Information
st.subheader("Basic Information")
st.write(filtered_df[["family", "script", "official_status"]].iloc[0])

# Geographical Distribution (Map)
st.subheader("Geographical Distribution")
fig = px.choropleth(
    filtered_df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea05c96d1670fc/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a03/india_states.geojson",
    featureidkey="properties.ST_NM",
    locations="states",
    color="speakers",
    color_continuous_scale="Viridis",
    scope="asia",
    title=f"Speaker Distribution for {selected_language}",
)
st.plotly_chart(fig)

# Demographic Information (with Error Handling)
st.subheader("Demographic Information")
try:
    total_speakers = filtered_df["speakers"].sum()
    st.write(f"Total Speakers: {total_speakers:,}")

    # Speaker Distribution (Bar Chart - Conditional)
    if not selected_state:
        fig = px.bar(
            filtered_df, x="states", y="speakers", title=f"Speaker Distribution by State for {selected_language}"
        )
        st.plotly_chart(fig)
except KeyError:
    st.warning("Speaker data not available for the selected language and/or states.")

# Linguistic and Cultural Features
st.subheader("Linguistic & Cultural Features")
st.write(filtered_df[["linguistic_features", "cultural_significance"]].iloc[0])

# Learning Resources
st.subheader("Learning Resources")
st.write(filtered_df[["learning_resources"]].iloc[0])