# Restaurant Analysis - Visualizations Guide

## Complete Guide to All Charts and Visualizations

This document provides a comprehensive overview of all visualizations available in the Zomato/Swiggy Restaurant Analysis project.

---

## Quick Start: Run All Visualizations

To generate and display all charts at once:

```bash
python show_visualizations.py
```

This will:
1. Generate 1000 sample restaurant records
2. Create 6 comprehensive visualization groups
3. Display summary statistics
4. Show all charts in an interactive window

---

## Visualization Overview

### CHART 1: Rating Distribution Analysis

**Purpose**: Understand how restaurant ratings are distributed

**Components**:
- **Histogram**: Shows frequency of ratings across 1-5 scale
- **Box Plot**: Displays median, quartiles, and outliers

**Key Insights**:
- Identifies rating trends
- Shows spread and concentration of ratings
- Reveals average quality in the market
- Highlights highly-rated vs low-rated restaurants

**Data Shown**:
- Mean rating: ~3.5 stars
- Most restaurants: 3.0-4.5 stars
- Distribution shape: Normal/Bimodal

---

### CHART 2: Cuisine Analysis - Popularity & Ratings

**Purpose**: Compare cuisines by popularity and quality

**Left Panel - Top 10 Cuisines by Count**:
- Horizontal bar chart
- Shows which cuisines have most restaurants
- Color: Coral

**Right Panel - Top 10 Cuisines by Average Rating**:
- Shows which cuisines are highest-rated
- Helps identify quality vs popularity gap
- Color: Light Green

**Key Insights**:
- Most popular cuisines (Indian, Chinese, Continental)
- Highest-rated cuisines (may differ from most popular)
- Market gaps and opportunities
- Consumer preferences by cuisine

---

### CHART 3: Price Range Distribution & Quality

**Purpose**: Analyze relationship between pricing and customer satisfaction

**Left Panel - Price Range Distribution**:
- Bar chart of restaurants per price range
- Range 1 (cheapest) to 4 (most expensive)
- Color: Purple

**Right Panel - Average Rating by Price Range**:
- Shows quality correlation with price
- Helps understand value proposition
- Color: Gold

**Key Insights**:
- Price elasticity of ratings
- Which price ranges offer best value
- Premium pricing and quality relationship
- Most competitive price segments

---

### CHART 4: Geographic Distribution & Ratings

**Purpose**: Compare restaurant landscape across cities

**Left Panel - Restaurants by City**:
- Count of restaurants in each city
- Market size comparison
- Color: Teal

**Right Panel - Average Rating by City**:
- Quality standards vary by location
- City-wise competitiveness
- Color: Salmon

**Key Insights**:
- Largest markets (Mumbai, Delhi, Bangalore)
- Quality standards by city
- Regional preferences and standards
- Market concentration vs distributed

---

### CHART 5: Correlation Heatmap

**Purpose**: Identify relationships between numerical variables

**Shows Correlations Between**:
- Rating vs Number of Reviews
- Rating vs Price Range
- Rating vs Delivery Time
- Rating vs Cost for Two
- And more...

**Color Scale**:
- Red: Positive correlation
- Blue: Negative correlation
- White: No correlation

**Key Insights**:
- Strong positive: More reviews → Higher ratings
- Weak/Moderate: Price → Quality relationship
- Impact of delivery time on ratings

---

### CHART 6: Additional Restaurant Statistics (2x2 Grid)

#### 6.1 Delivery Time Distribution
**Chart Type**: Histogram
**Color**: Steel Blue
- Distribution of delivery times (15-60 minutes)
- Most restaurants: 30-40 minute delivery
- Impacts customer satisfaction

#### 6.2 Cost for Two Distribution
**Chart Type**: Histogram  
**Color**: Coral
- Price distribution in INR
- Most common price points
- Market segmentation visible

#### 6.3 Vegetarian Option Availability
**Chart Type**: Pie Chart
**Colors**: Red, Blue
- Percentage with/without vegetarian options
- Market requirement analysis

#### 6.4 Online Delivery Availability
**Chart Type**: Pie Chart
**Colors**: Orange, Green
- Percentage offering online delivery
- Digital adoption metrics

---

### CHART 7: Advanced Restaurant Metrics (2x2 Grid)

#### 7.1 Rating vs Review Count
**Chart Type**: Scatter Plot
**Color Scale**: Viridis
- Each point = one restaurant
- X-axis: Number of reviews
- Y-axis: Rating (1-5)
- Shows maturation effect (more reviews = better ratings)

#### 7.2 Average Rating by Delivery Time
**Chart Type**: Line Plot
**Color**: Green
- Shows if faster delivery correlates with higher ratings
- 5 delivery time bins analyzed
- Trend visibility

#### 7.3 Top 10 Highest Rated Restaurants
**Chart Type**: Horizontal Bar Chart
**Color**: Gold
- Names and ratings of top performers
- Excellence benchmarks
- Competitor analysis

#### 7.4 Price Range vs Average Rating (with Error Bars)
**Chart Type**: Line Plot with Error Bars
**Color**: Purple
- Standard deviation shown
- Quality consistency by price range
- Statistical significance

---

## Summary Statistics Displayed

### Rating Statistics
- Mean, Median, Std Dev, Min, Max
- Data spread and consistency

### Review Statistics
- Average number of reviews
- Most reviewed restaurants
- Engagement patterns

### Delivery Statistics
- Average delivery time
- Fastest/slowest services
- Service efficiency metrics

### Price Statistics
- Average cost for two
- Price range (₹200-₹2000)
- Market segmentation

### Service Availability
- Vegetarian options percentage
- Online delivery percentage
- Digital adoption rate

---

## Using Individual Visualizations

### Method 1: Using visualizations.py directly

```python
from generate_sample_data import RestaurantDataGenerator
from visualizations import RestaurantVisualizations
import matplotlib.pyplot as plt

# Generate data
generator = RestaurantDataGenerator()
df = generator.generate_sample_data()

# Create visualization object
viz = RestaurantVisualizations(df)

# Create specific chart
fig = viz.plot_rating_distribution()
plt.show()

# Create cuisine chart
fig = viz.plot_cuisine_analysis()
plt.show()

# Save visualizations
viz.create_all_visualizations(save_path='./plots')
```

### Method 2: Quick visualization

```python
python show_visualizations.py
```

---

## Customizing Visualizations

### Change figure size
```python
viz = RestaurantVisualizations(df)
viz.fig_width = 16
viz.fig_height = 10
```

### Change color schemes
```python
import seaborn as sns
sns.set_palette("husl")  # or "Set2", "coolwarm", etc.
```

### Save individual charts
```python
fig = viz.plot_rating_distribution()
fig.savefig('rating_chart.png', dpi=300, bbox_inches='tight')
```

---

## Interpreting the Charts

### Rating Distribution
✓ **Good Sign**: Bell curve centered around 3.5-4.0
✓ **Good Sign**: Tight clustering (low std dev)
⚠ **Watch For**: Bimodal distribution (two peaks)
⚠ **Watch For**: Wide spread (inconsistent quality)

### Cuisine Analysis
✓ **Good Sign**: Multiple cuisines competing
✓ **Good Sign**: Popularity ≠ Quality relationship
⚠ **Watch For**: One cuisine dominating
⚠ **Watch For**: All top cuisines same type

### Price vs Rating
✓ **Good Sign**: Positive correlation
✓ **Good Sign**: Budget options available
⚠ **Watch For**: No quality difference across prices
⚠ **Watch For**: Premium pricing without quality

### City Analysis
✓ **Good Sign**: Similar quality standards across cities
✓ **Good Sign**: Distributed market
⚠ **Watch For**: Quality variations by city
⚠ **Watch For**: Market concentration

---

## Data Requirements

Visualizations work with any dataset containing:

| Column | Type | Range |
|--------|------|-------|
| rating | float | 1.0-5.0 |
| cuisine | string | Any |
| price_range | int | 1-4 |
| delivery_time | int | 15-60 min |
| cost_for_two | int | 200-2000 ₹ |
| city | string | Any |
| num_reviews | int | 10-500 |
| vegetarian | bool | T/F |
| has_online_delivery | bool | T/F |

---

## Troubleshooting

### Charts not displaying
```python
import matplotlib.pyplot as plt
plt.ion()  # Interactive mode
```

### Memory issues with large datasets
```python
# Sample data instead
df_sample = df.sample(n=5000, random_state=42)
viz = RestaurantVisualizations(df_sample)
```

### Colors not showing properly
```python
import seaborn as sns
sns.set_style("whitegrid")
```

---

## Next Steps

1. Run `python show_visualizations.py` to see all charts
2. Modify `show_visualizations.py` to add custom charts
3. Export charts using `savefig()` for reports
4. Combine multiple visualizations into dashboards
5. Add machine learning predictions to visualizations

---

## Additional Resources

- [Matplotlib Documentation](https://matplotlib.org/)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Pandas Visualization](https://pandas.pydata.org/docs/user_guide/visualization.html)

---

**Last Updated**: December 2025
**Project**: Zomato/Swiggy Restaurant Analysis
