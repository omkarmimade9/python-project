import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

class RestaurantAnalysis:
    """Zomato/Swiggy Restaurant Analysis System"""
    
    def __init__(self, data_path=None):
        """Initialize the analysis system"""
        self.df = None
        if data_path:
            self.load_data(data_path)
    
    def load_data(self, file_path):
        """Load restaurant data from CSV"""
        try:
            self.df = pd.read_csv(file_path)
            print(f"Data loaded successfully. Shape: {self.df.shape}")
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def rating_analysis(self):
        """Analyze restaurant ratings distribution"""
        if self.df is None:
            print("No data loaded")
            return
        
        stats_dict = {
            'Mean Rating': self.df['rating'].mean(),
            'Median Rating': self.df['rating'].median(),
            'Std Dev': self.df['rating'].std(),
            'Min Rating': self.df['rating'].min(),
            'Max Rating': self.df['rating'].max()
        }
        return stats_dict
    
    def cuisine_analysis(self):
        """Analyze cuisine popularity"""
        if self.df is None:
            print("No data loaded")
            return
        
        cuisine_counts = self.df['cuisine'].value_counts()
        cuisine_ratings = self.df.groupby('cuisine')['rating'].mean().sort_values(ascending=False)
        
        return {
            'cuisine_count': cuisine_counts,
            'cuisine_ratings': cuisine_ratings
        }
    
    def price_analysis(self):
        """Analyze pricing patterns"""
        if self.df is None:
            print("No data loaded")
            return
        
        price_stats = {
            'Mean Price': self.df['price_range'].mean(),
            'Median Price': self.df['price_range'].median(),
            'Price Distribution': self.df['price_range'].value_counts().sort_index()
        }
        return price_stats
    
    def correlation_analysis(self):
        """Analyze correlation between ratings and price"""
        if self.df is None:
            print("No data loaded")
            return
        
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        correlation = self.df[numeric_cols].corr()
        return correlation
    
    def generate_report(self):
        """Generate comprehensive analysis report"""
        print("\n" + "="*60)
        print("RESTAURANT ANALYSIS REPORT")
        print("="*60)
        
        print("\n--- RATING STATISTICS ---")
        rating_stats = self.rating_analysis()
        for key, value in rating_stats.items():
            print(f"{key}: {value:.2f}")
        
        print("\n--- CUISINE ANALYSIS ---")
        cuisine_data = self.cuisine_analysis()
        if cuisine_data:
            print("\nTop 10 Cuisines by Count:")
            print(cuisine_data['cuisine_count'].head(10))
        
        print("\n--- PRICE ANALYSIS ---")
        price_data = self.price_analysis()
        if price_data:
            for key, value in price_data.items():
                if isinstance(value, (int, float)):
                    print(f"{key}: {value:.2f}")


if __name__ == "__main__":
    analysis = RestaurantAnalysis()
    print("Restaurant Analysis System Initialized")
    print("Use load_data() to load CSV file")
    print("Available methods: rating_analysis(), cuisine_analysis(), price_analysis()")
