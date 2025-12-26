# Zomato/Swiggy Restaurant Analysis Project

## Project Overview

This project provides comprehensive analysis of restaurant data from food delivery platforms like Zomato and Swiggy. The analysis explores restaurant ratings, cuisine popularity, pricing patterns, and other key metrics to provide insights into the food delivery market.

## Objectives

1. **Rating Analysis**: Understand the distribution of restaurant ratings and identify quality trends
2. **Cuisine Popularity**: Determine which cuisines are most popular and highly rated
3. **Pricing Analysis**: Analyze pricing patterns across different price ranges and cuisines
4. **Geographic Insights**: Explore restaurant distribution and ratings across different cities
5. **Correlation Analysis**: Identify relationships between ratings, prices, and delivery times

## Project Structure

```
restaurant-analysis/
├── restaurant_analysis.py          # Main analysis class
├── generate_sample_data.py         # Data generation utility
├── visualizations.py               # Visualization module
├── requirements.txt                # Python dependencies
├── PROJECT_INFO.md                 # Project documentation
└── README.md                       # Quick start guide
```

## Key Features

### 1. Data Loading and Processing
- Load restaurant data from CSV files
- Handle missing values and data validation
- Generate synthetic sample datasets

### 2. Statistical Analysis
- Rating distribution analysis
- Cuisine popularity metrics
- Price range analysis
- City-wise comparisons

### 3. Visualization
- Rating distribution histograms and box plots
- Cuisine popularity bar charts
- Price range analysis
- City-wise restaurant distribution
- Correlation heatmaps

## Dataset Schema

The project expects restaurant data with the following columns:

| Column | Type | Description |
|--------|------|-------------|
| restaurant_id | int | Unique restaurant identifier |
| restaurant_name | string | Name of the restaurant |
| cuisine | string | Type of cuisine |
| rating | float | Customer rating (1-5) |
| num_reviews | int | Number of reviews |
| price_range | int | Price range (1-4) |
| delivery_time | int | Average delivery time in minutes |
| cost_for_two | int | Cost for two people |
| city | string | City where restaurant operates |
| vegetarian | boolean | Has vegetarian options |
| has_online_delivery | boolean | Offers online delivery |

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Generate Sample Data

```python
from generate_sample_data import RestaurantDataGenerator

generator = RestaurantDataGenerator()
df = generator.generate_sample_data(num_records=1000)
generator.save_data(df, 'restaurant_data.csv')
```

### Perform Analysis

```python
from restaurant_analysis import RestaurantAnalysis

analysis = RestaurantAnalysis(data_path='restaurant_data.csv')
analysis.generate_report()
```

### Create Visualizations

```python
from visualizations import RestaurantVisualizations

viz = RestaurantVisualizations(df)
fig1 = viz.plot_rating_distribution()
fig2 = viz.plot_cuisine_analysis()
fig3 = viz.plot_price_analysis()
viz.create_all_visualizations(save_path='./plots')
```

## Analysis Capabilities

### Rating Analysis
- Mean, median, and standard deviation of ratings
- Rating distribution patterns
- Identifies highly-rated restaurants

### Cuisine Analysis
- Most popular cuisines by restaurant count
- Average ratings by cuisine type
- Cuisine distribution across cities

### Price Analysis
- Distribution of restaurants across price ranges
- Average ratings by price range
- Relationship between price and quality

### Geographic Analysis
- Restaurant count by city
- Average ratings by city
- Cuisine preferences by location

### Correlation Analysis
- Relationship between ratings and reviews
- Delivery time vs. ratings correlation
- Price vs. rating correlation

## Key Insights & Findings

The analysis typically reveals:

1. **Quality Consistency**: Higher-priced restaurants generally receive better ratings
2. **Popular Cuisines**: North Indian, Chinese, and Continental cuisines dominate the market
3. **Review Correlation**: Restaurants with more reviews tend to have higher ratings
4. **Urban Distribution**: Major cities like Mumbai, Delhi, and Bangalore have the most restaurants
5. **Delivery Efficiency**: Shorter delivery times often correlate with better ratings

## Technologies Used

- **Python 3.x**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib**: Static visualizations
- **Seaborn**: Statistical data visualization
- **SciPy**: Statistical analysis

## Dependencies

See `requirements.txt` for full list:
- pandas>=1.3.0
- numpy>=1.21.0
- matplotlib>=3.4.0
- seaborn>=0.11.0
- scipy>=1.7.0
- pytest>=6.2.0
- requests>=2.26.0

## Future Enhancements

1. Machine Learning: Predict restaurant success based on features
2. Time Series Analysis: Track trends over time
3. NLP Analysis: Analyze customer review sentiments
4. Interactive Dashboard: Plotly/Dash for interactive visualizations
5. API Integration: Real-time data from Zomato/Swiggy APIs
6. Recommendation System: Suggest restaurants based on preferences

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - Feel free to use this project for educational purposes

## Author

Omkar Mimade (@omkarmimade9)

## Contact & Support

For questions or support, please open an issue on the GitHub repository.
