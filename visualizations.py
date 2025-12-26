import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

class RestaurantVisualizations:
    """Create visualizations for restaurant analysis"""
    
    def __init__(self, df):
        """Initialize with dataframe"""
        self.df = df
        sns.set_style('whitegrid')
        plt.rcParams['figure.figsize'] = (12, 6)
    
    def plot_rating_distribution(self):
        """Plot histogram of rating distribution"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Histogram
        axes[0].hist(self.df['rating'], bins=20, color='skyblue', edgecolor='black')
        axes[0].set_title('Rating Distribution', fontsize=14, fontweight='bold')
        axes[0].set_xlabel('Rating')
        axes[0].set_ylabel('Frequency')
        
        # Box plot
        axes[1].boxplot(self.df['rating'])
        axes[1].set_title('Rating Box Plot', fontsize=14, fontweight='bold')
        axes[1].set_ylabel('Rating')
        
        plt.tight_layout()
        return fig
    
    def plot_cuisine_analysis(self):
        """Plot top cuisines by count and rating"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Top cuisines by count
        cuisine_counts = self.df['cuisine'].value_counts().head(10)
        axes[0].barh(range(len(cuisine_counts)), cuisine_counts.values, color='coral')
        axes[0].set_yticks(range(len(cuisine_counts)))
        axes[0].set_yticklabels(cuisine_counts.index)
        axes[0].set_title('Top 10 Cuisines by Count', fontsize=14, fontweight='bold')
        axes[0].set_xlabel('Number of Restaurants')
        axes[0].invert_yaxis()
        
        # Average rating by cuisine
        cuisine_ratings = self.df.groupby('cuisine')['rating'].mean().sort_values(ascending=False).head(10)
        axes[1].barh(range(len(cuisine_ratings)), cuisine_ratings.values, color='lightgreen')
        axes[1].set_yticks(range(len(cuisine_ratings)))
        axes[1].set_yticklabels(cuisine_ratings.index)
        axes[1].set_title('Top 10 Cuisines by Average Rating', fontsize=14, fontweight='bold')
        axes[1].set_xlabel('Average Rating')
        axes[1].invert_yaxis()
        
        plt.tight_layout()
        return fig
    
    def plot_price_analysis(self):
        """Plot price range distribution"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Price range count
        price_counts = self.df['price_range'].value_counts().sort_index()
        axes[0].bar(price_counts.index, price_counts.values, color='purple', alpha=0.7)
        axes[0].set_title('Distribution by Price Range', fontsize=14, fontweight='bold')
        axes[0].set_xlabel('Price Range')
        axes[0].set_ylabel('Count')
        axes[0].set_xticks([1, 2, 3, 4])
        
        # Average rating by price range
        price_ratings = self.df.groupby('price_range')['rating'].mean()
        axes[1].bar(price_ratings.index, price_ratings.values, color='gold', alpha=0.7)
        axes[1].set_title('Average Rating by Price Range', fontsize=14, fontweight='bold')
        axes[1].set_xlabel('Price Range')
        axes[1].set_ylabel('Average Rating')
        axes[1].set_xticks([1, 2, 3, 4])
        
        plt.tight_layout()
        return fig
    
    def plot_city_analysis(self):
        """Plot analysis by city"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Restaurants by city
        city_counts = self.df['city'].value_counts()
        axes[0].bar(city_counts.index, city_counts.values, color='teal', alpha=0.7)
        axes[0].set_title('Restaurants by City', fontsize=14, fontweight='bold')
        axes[0].set_xlabel('City')
        axes[0].set_ylabel('Count')
        axes[0].tick_params(axis='x', rotation=45)
        
        # Average rating by city
        city_ratings = self.df.groupby('city')['rating'].mean().sort_values(ascending=False)
        axes[1].bar(city_ratings.index, city_ratings.values, color='salmon', alpha=0.7)
        axes[1].set_title('Average Rating by City', fontsize=14, fontweight='bold')
        axes[1].set_xlabel('City')
        axes[1].set_ylabel('Average Rating')
        axes[1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        return fig
    
    def plot_correlation_heatmap(self):
        """Plot correlation heatmap for numeric features"""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        correlation_matrix = self.df[numeric_cols].corr()
        
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
                    square=True, ax=ax, fmt='.2f')
        ax.set_title('Correlation Heatmap', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        return fig
    
    def create_all_visualizations(self, save_path=None):
        """Create and optionally save all visualizations"""
        figures = [
            ('rating_distribution.png', self.plot_rating_distribution()),
            ('cuisine_analysis.png', self.plot_cuisine_analysis()),
            ('price_analysis.png', self.plot_price_analysis()),
            ('city_analysis.png', self.plot_city_analysis()),
            ('correlation_heatmap.png', self.plot_correlation_heatmap())
        ]
        
        if save_path:
            for filename, fig in figures:
                fig.savefig(f'{save_path}/{filename}', dpi=300, bbox_inches='tight')
        
        return figures
