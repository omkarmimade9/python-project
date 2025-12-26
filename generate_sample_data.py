import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

class RestaurantDataGenerator:
    """Generate sample restaurant data for analysis"""
    
    def __init__(self):
        self.cuisines = ['Indian', 'Chinese', 'Italian', 'Continental', 'Fast Food', 
                        'Cafe', 'North Indian', 'South Indian', 'Desserts', 'Seafood',
                        'Mexican', 'Thai', 'Japanese', 'Korean', 'Vietnamese']
        
        self.restaurants = [
            'Spice Garden', 'Dragon Palace', 'Pasta House', 'The Burger King',
            'Taj Express', 'Noodle House', 'Pizza Corner', 'Desi Dhaba',
            'Curry King', 'Wok Express', 'The Good Fork', 'Samosa Junction',
            'Biryani Palace', 'Tandoori Nights', 'Sweet Escapes'
        ]
    
    def generate_sample_data(self, num_records=1000, seed=42):
        """Generate synthetic restaurant data"""
        np.random.seed(seed)
        random.seed(seed)
        
        data = {
            'restaurant_id': range(1, num_records + 1),
            'restaurant_name': [random.choice(self.restaurants) for _ in range(num_records)],
            'cuisine': [random.choice(self.cuisines) for _ in range(num_records)],
            'rating': np.round(np.random.uniform(2.0, 5.0, num_records), 1),
            'num_reviews': np.random.randint(10, 500, num_records),
            'price_range': np.random.randint(1, 5, num_records),
            'delivery_time': np.random.randint(15, 60, num_records),
            'cost_for_two': np.random.randint(200, 2000, num_records),
            'city': [random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Pune', 'Hyderabad']) 
                    for _ in range(num_records)],
            'vegetarian': [random.choice([True, False]) for _ in range(num_records)],
            'has_online_delivery': [random.choice([True, False]) for _ in range(num_records)]
        }
        
        df = pd.DataFrame(data)
        
        # Add correlation between rating and other features
        df['rating'] = df['rating'] + (df['num_reviews'] / 100) * 0.1
        df['rating'] = df['rating'].clip(lower=1.0, upper=5.0)
        df['rating'] = np.round(df['rating'], 1)
        
        return df
    
    def save_data(self, df, filename='restaurant_data.csv'):
        """Save data to CSV"""
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
        print(f"Shape: {df.shape}")
        print(f"\nFirst few rows:\n{df.head()}")


if __name__ == "__main__":
    generator = RestaurantDataGenerator()
    df = generator.generate_sample_data(num_records=1000)
    generator.save_data(df, 'restaurant_data.csv')
    
    print("\nDataset Summary:")
    print(f"Total Restaurants: {len(df)}")
    print(f"Cuisines: {df['cuisine'].nunique()}")
    print(f"Cities: {df['city'].nunique()}")
    print(f"Average Rating: {df['rating'].mean():.2f}")
    print(f"Price Range: {df['price_range'].min()}-{df['price_range'].max()}")
