#!/usr/bin/env python3
"""
Comprehensive Visualization Script
Generates and displays all charts from the Restaurant Analysis Project
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from generate_sample_data import RestaurantDataGenerator
from visualizations import RestaurantVisualizations


def create_all_visualizations():
    """
    Generate sample data and create all visualization charts
    """
    
    print("\n" + "="*70)
    print("RESTAURANT ANALYSIS - COMPREHENSIVE VISUALIZATIONS")
    print("="*70)
    
    # Step 1: Generate sample data
    print("\n[1] Generating Sample Restaurant Data...")
    generator = RestaurantDataGenerator()
    df = generator.generate_sample_data(num_records=1000)
    print(f"    ✓ Generated {len(df)} restaurant records")
    print(f"    ✓ Cuisines: {df['cuisine'].nunique()}")
    print(f"    ✓ Cities: {df['city'].nunique()}")
    
    # Step 2: Initialize visualization class
    print("\n[2] Initializing Visualization Module...")
    viz = RestaurantVisualizations(df)
    print("    ✓ Visualization module ready")
    
    # Step 3: Create Rating Distribution Chart
    print("\n[3] Creating Rating Distribution Charts...")
    fig1 = viz.plot_rating_distribution()
    fig1.suptitle('CHART 1: Rating Distribution Analysis', 
                  fontsize=16, fontweight='bold', y=1.00)
    print("    ✓ Rating histogram and box plot created")
    plt.tight_layout()
    
    # Step 4: Create Cuisine Analysis Chart
    print("\n[4] Creating Cuisine Popularity Charts...")
    fig2 = viz.plot_cuisine_analysis()
    fig2.suptitle('CHART 2: Cuisine Analysis - Popularity & Ratings', 
                  fontsize=16, fontweight='bold', y=1.00)
    print("    ✓ Top cuisines by count and rating created")
    plt.tight_layout()
    
    # Step 5: Create Price Analysis Chart
    print("\n[5] Creating Price Range Analysis Charts...")
    fig3 = viz.plot_price_analysis()
    fig3.suptitle('CHART 3: Price Range Distribution & Quality', 
                  fontsize=16, fontweight='bold', y=1.00)
    print("    ✓ Price distribution and rating correlation created")
    plt.tight_layout()
    
    # Step 6: Create City Analysis Chart
    print("\n[6] Creating City-wise Analysis Charts...")
    fig4 = viz.plot_city_analysis()
    fig4.suptitle('CHART 4: Geographic Distribution & Ratings', 
                  fontsize=16, fontweight='bold', y=1.00)
    print("    ✓ City distribution and average ratings created")
    plt.tight_layout()
    
    # Step 7: Create Correlation Heatmap
    print("\n[7] Creating Correlation Heatmap...")
    fig5 = viz.plot_correlation_heatmap()
    print("    ✓ Correlation analysis heatmap created")
    plt.tight_layout()
    
    # Step 8: Create Additional Statistics Visualizations
    print("\n[8] Creating Additional Statistical Visualizations...")
    fig6, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig6.suptitle('CHART 5: Additional Restaurant Statistics', 
                  fontsize=16, fontweight='bold')
    
    # 8.1: Delivery Time Distribution
    axes[0, 0].hist(df['delivery_time'], bins=20, color='steelblue', edgecolor='black')
    axes[0, 0].set_title('Delivery Time Distribution', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('Delivery Time (minutes)')
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].grid(alpha=0.3)
    
    # 8.2: Cost for Two Distribution
    axes[0, 1].hist(df['cost_for_two'], bins=20, color='coral', edgecolor='black')
    axes[0, 1].set_title('Cost for Two Distribution', fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('Cost for Two (INR)')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].grid(alpha=0.3)
    
    # 8.3: Vegetarian vs Non-Vegetarian
    veg_counts = df['vegetarian'].value_counts()
    colors_veg = ['#ff9999', '#66b3ff']
    axes[1, 0].pie(veg_counts, labels=['Non-Vegetarian', 'Vegetarian'], 
                   autopct='%1.1f%%', colors=colors_veg, startangle=90)
    axes[1, 0].set_title('Vegetarian Option Availability', fontsize=12, fontweight='bold')
    
    # 8.4: Online Delivery Availability
    delivery_counts = df['has_online_delivery'].value_counts()
    colors_delivery = ['#ffcc99', '#99ff99']
    axes[1, 1].pie(delivery_counts, labels=['No Online Delivery', 'Has Online Delivery'], 
                   autopct='%1.1f%%', colors=colors_delivery, startangle=90)
    axes[1, 1].set_title('Online Delivery Availability', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    print("    ✓ Delivery time, cost, vegetarian, and delivery status charts created")
    
    # Step 9: Create Advanced Analysis Visualizations
    print("\n[9] Creating Advanced Analysis Visualizations...")
    fig7, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig7.suptitle('CHART 6: Advanced Restaurant Metrics', 
                  fontsize=16, fontweight='bold')
    
    # 9.1: Rating vs Review Count Scatter
    scatter = axes[0, 0].scatter(df['num_reviews'], df['rating'], 
                                alpha=0.5, c=df['rating'], cmap='viridis', s=50)
    axes[0, 0].set_title('Rating vs Review Count', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('Number of Reviews')
    axes[0, 0].set_ylabel('Rating')
    axes[0, 0].grid(alpha=0.3)
    plt.colorbar(scatter, ax=axes[0, 0])
    
    # 9.2: Average Rating by Delivery Time
    delivery_bins = pd.cut(df['delivery_time'], bins=5)
    rating_by_delivery = df.groupby(delivery_bins)['rating'].mean()
    axes[0, 1].plot(range(len(rating_by_delivery)), rating_by_delivery.values, 
                   marker='o', linewidth=2, markersize=8, color='green')
    axes[0, 1].set_title('Average Rating by Delivery Time Bins', fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('Delivery Time Categories')
    axes[0, 1].set_ylabel('Average Rating')
    axes[0, 1].grid(alpha=0.3)
    axes[0, 1].set_xticks(range(len(rating_by_delivery)))
    axes[0, 1].set_xticklabels([f'Bin {i+1}' for i in range(len(rating_by_delivery))], 
                              rotation=45)
    
    # 9.3: Top Restaurants by Rating
    top_restaurants = df.nlargest(10, 'rating')[['restaurant_name', 'rating']].reset_index(drop=True)
    axes[1, 0].barh(range(len(top_restaurants)), top_restaurants['rating'].values, color='gold')
    axes[1, 0].set_yticks(range(len(top_restaurants)))
    axes[1, 0].set_yticklabels(top_restaurants['restaurant_name'].values)
    axes[1, 0].set_title('Top 10 Highest Rated Restaurants', fontsize=12, fontweight='bold')
    axes[1, 0].set_xlabel('Rating')
    axes[1, 0].invert_yaxis()
    axes[1, 0].grid(alpha=0.3, axis='x')
    
    # 9.4: Price Range vs Average Rating
    price_rating = df.groupby('price_range')['rating'].agg(['mean', 'std', 'count'])
    axes[1, 1].errorbar(price_rating.index, price_rating['mean'], 
                       yerr=price_rating['std'], marker='o', linewidth=2, 
                       markersize=10, capsize=5, color='purple')
    axes[1, 1].set_title('Price Range vs Average Rating (with Std Dev)', 
                        fontsize=12, fontweight='bold')
    axes[1, 1].set_xlabel('Price Range')
    axes[1, 1].set_ylabel('Average Rating')
    axes[1, 1].grid(alpha=0.3)
    axes[1, 1].set_xticks([1, 2, 3, 4])
    
    plt.tight_layout()
    print("    ✓ Rating vs reviews, delivery time, top restaurants, and price vs rating created")
    
    # Step 10: Summary Statistics
    print("\n[10] Generating Summary Statistics...")
    print("\n" + "-"*70)
    print("DATASET SUMMARY STATISTICS")
    print("-"*70)
    print(f"\nTotal Restaurants: {len(df)}")
    print(f"Unique Cuisines: {df['cuisine'].nunique()}")
    print(f"Cities Covered: {df['city'].nunique()}")
    print(f"\nRating Statistics:")
    print(f"  • Mean Rating: {df['rating'].mean():.2f}")
    print(f"  • Median Rating: {df['rating'].median():.2f}")
    print(f"  • Std Dev: {df['rating'].std():.2f}")
    print(f"  • Min Rating: {df['rating'].min():.2f}")
    print(f"  • Max Rating: {df['rating'].max():.2f}")
    
    print(f"\nReview Statistics:")
    print(f"  • Mean Reviews: {df['num_reviews'].mean():.0f}")
    print(f"  • Median Reviews: {df['num_reviews'].median():.0f}")
    print(f"  • Max Reviews: {df['num_reviews'].max()}")
    
    print(f"\nDelivery Statistics:")
    print(f"  • Mean Delivery Time: {df['delivery_time'].mean():.1f} minutes")
    print(f"  • Min Delivery Time: {df['delivery_time'].min()} minutes")
    print(f"  • Max Delivery Time: {df['delivery_time'].max()} minutes")
    
    print(f"\nPrice Statistics:")
    print(f"  • Mean Cost for Two: ₹{df['cost_for_two'].mean():.0f}")
    print(f"  • Min Cost for Two: ₹{df['cost_for_two'].min()}")
    print(f"  • Max Cost for Two: ₹{df['cost_for_two'].max()}")
    
    print(f"\nService Availability:")
    print(f"  • Vegetarian Options: {df['vegetarian'].sum()} ({df['vegetarian'].sum()/len(df)*100:.1f}%)")
    print(f"  • Online Delivery: {df['has_online_delivery'].sum()} ({df['has_online_delivery'].sum()/len(df)*100:.1f}%)")
    
    print("\n" + "="*70)
    print("ALL VISUALIZATIONS GENERATED SUCCESSFULLY!")
    print("="*70)
    print("\nCharts Generated:")
    print("  1. Rating Distribution Analysis")
    print("  2. Cuisine Analysis - Popularity & Ratings")
    print("  3. Price Range Distribution & Quality")
    print("  4. Geographic Distribution & Ratings")
    print("  5. Correlation Heatmap")
    print("  6. Additional Statistics (Delivery, Cost, Vegetarian, Delivery Service)")
    print("  7. Advanced Metrics (Ratings vs Reviews, Delivery Impact, Top Restaurants)")
    print("\nPress ENTER to display all charts...\n")
    
    # Display all figures
    plt.show()


if __name__ == "__main__":
    try:
        create_all_visualizations()
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
