# 🌾 AgriDrone Intelligence Platform

A smart agriculture and drone zone information system that analyzes agricultural regions across Tamil Nadu and identifies drone-operational zones based on proximity to airports and regulatory restrictions.

## 📋 Overview

The **AgriDrone Intelligence Platform** is an intelligent system designed to:

- Analyze agricultural data across different districts and taluks in Tamil Nadu
- Classify drone operation zones (Red, Yellow, Green) based on airport proximity
- Calculate drone readiness scores for agricultural operations
- Provide smart recommendations for drone-based agricultural activities
- Visualize agricultural and drone zone distributions
- Display real-time agricultural location mapping

## 🎯 Key Features

### 1. **Smart Zone Classification**
   - **Red Zone** (< 5 km from airport): Restricted drone operations (Score: 20/100)
   - **Inner Yellow Zone** (5-12 km): Limited operations with prior permission (Score: 50/100)
   - **Outer Yellow Zone** (12-25 km): Regulated agricultural operations (Score: 75/100)
   - **Green Zone** (> 25 km): Unrestricted drone operations (Score: 75-100/100)

### 2. **Intelligent Recommendations**
   - **Score ≥ 90**: Full drone capabilities (Spraying, Monitoring, NDVI Analysis, Yield Estimation)
   - **Score 70-89**: Limited agricultural operations with altitude monitoring
   - **Score 40-69**: Requires prior permission for controlled operations
   - **Score < 40**: Drone operations restricted

### 3. **District & Taluk Explorer**
   - Browse agricultural data by district and taluk
   - View detailed agricultural information (crop type, soil composition, irrigation)
   - Check nearest airport and distance
   - Real-time drone readiness assessment

### 4. **Data Visualizations**
   - Drone Zone Distribution (Pie Chart)
   - Crop Distribution across Tamil Nadu (Bar Chart)
   - Agricultural Location Mapping
   - Complete dataset table with filtering options

### 5. **Data Export**
   - Download enhanced dataset with drone zone classifications in CSV format

## 🚀 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Interactive web application framework
- **Data Processing**: [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis
- **Visualization**: [Plotly](https://plotly.com/) - Interactive charts and graphs
- **Geospatial**: [GeoPy](https://geopy.readthedocs.io/) - Distance calculations and geocoding

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/RashilKumar513/Agri_Drone_Intelligent_System.git
cd Agri_Drone_Intelligent_System
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Open in browser**
   - The application will automatically open at `http://localhost:8501`

## 📊 Dataset

The system uses `tamilnadu_agriculture.csv` containing agricultural data with the following key columns:

| Column | Description |
|--------|-------------|
| `District` | Agricultural district in Tamil Nadu |
| `Taluk` | Sub-district/administrative division |
| `Latitude` | Geographic latitude coordinate |
| `Longitude` | Geographic longitude coordinate |
| `Crop` | Primary crop cultivated |
| `Soil` | Soil type classification |
| `Irrigation` | Irrigation method/availability |
| `DroneZone` | Calculated drone operation zone (Red/Yellow/Green) |
| `ReadinessScore` | Drone readiness score (0-100) |
| `NearestAirport` | Closest airport location |
| `AirportDistanceKM` | Distance to nearest airport |

## 🗺️ Supported Airports (Tamil Nadu)

The system tracks these major airports for zone classification:

- Chennai (12.9941°N, 80.1709°E)
- Coimbatore (11.0300°N, 77.0434°E)
- Madurai (9.8345°N, 78.0934°E)
- Trichy (10.7654°N, 78.7097°E)
- Salem (11.7833°N, 78.0656°E)
- Tuticorin (8.7242°N, 78.0258°E)

## 🎮 Usage Guide

### 1. **View Dashboard Metrics**
   - See total districts, taluks, and green zones at a glance
   - Monitor total agricultural records in the system

### 2. **Explore by Location**
   - Select a district from the dropdown
   - Choose a specific taluk
   - View agricultural and drone intelligence for that location

### 3. **Analyze Visualizations**
   - Check drone zone distribution across regions
   - Review crop diversity and distribution
   - Explore geographic locations on the map

### 4. **Export Data**
   - Download the enhanced dataset with drone classifications
   - Use for further analysis or reporting

## 📁 File Structure

```
Agri_Drone_Intelligent_System/
├── app.py                           # Main Streamlit application
├── requirements.txt                 # Python dependencies
├── tamilnadu_agriculture.csv       # Agricultural dataset
└── README.md                        # Documentation
```

## 🔧 How It Works

### Drone Zone Classification Algorithm

1. **Input**: Agricultural location (latitude, longitude)
2. **Process**: 
   - Calculate distance to all known airports using GeoPy
   - Identify the nearest airport
   - Apply zone classification rules based on distance
   - Calculate readiness score
3. **Output**: Zone classification, readiness score, and recommendations

### Recommendation Engine

The system generates recommendations based on the drone readiness score:
- Evaluates agricultural operations feasibility
- Considers regulatory restrictions from airport proximity
- Suggests appropriate drone-based interventions
- Flags areas requiring special permissions

## 🌐 Use Cases

- **Agricultural Planning**: Identify suitable areas for drone-based farming operations
- **Regulatory Compliance**: Ensure drone operations comply with airspace restrictions
- **Resource Optimization**: Plan crop monitoring and pesticide spraying operations
- **Data Analytics**: Analyze agricultural patterns and drone capabilities across regions
- **Government Planning**: Support policy decisions on agricultural drone usage

## 📈 Future Enhancements

- Real-time weather integration for optimal drone operations
- Historical trend analysis for crop yields
- Machine learning-based yield predictions
- Integration with drone fleet management systems
- Multi-state coverage expansion
- Drone path optimization algorithms
- Integration with agricultural IoT sensors

## ⚠️ Regulatory Disclaimer

This system is designed to assist in drone operation planning. Users must comply with:
- DGCA (Directorate General of Civil Aviation) regulations
- Local airport authority guidelines
- State and local drone operation laws
- Environmental regulations

Always obtain necessary approvals before conducting drone operations.

## 👤 Author

**Rashil Kumar**
- GitHub: [@RashilKumar513](https://github.com/RashilKumar513)

## 📞 Support & Contact

For issues, suggestions, or contributions:
- Open an issue on the GitHub repository
- Check existing documentation
- Review the code comments for implementation details

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests with improvements
- Improve documentation

---

**Made with ❤️ for Smart Agriculture & Precision Farming**
