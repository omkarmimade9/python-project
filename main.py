#!/usr/bin/env python3
"""
Main script to demonstrate Zomato/Swiggy Restaurant Analysis
This script shows how to use all the modules together
"""

import sys
from generate_sample_data import RestaurantDataGenerator
from restaurant_analysis import RestaurantAnalysis
from visualizations import RestaurantVisualizations


def main():
    """Main execution function"""
    
    print("\n" + "="*70)
    print("ZOMATO/SWIGGY RESTAURANT ANALYSIS SYSTEM")
    print("="*70)
    
    # Step 1: Generate sample data
    print("\n[Step 1] Generating sample restaurant data...")
    try:
        generator = RestaurantDataGenerator()
        df = generator.generate_sample_data(num_records=1000)
        generator.save_data(df, 'restaurant_data.csv')
        print(f"✓ Sample data generated successfully")
        print(f"  Total records: {len(df)}")
        print(f"  Cuisines: {df['cuisine'].nunique()}")
        print(f"  Cities: {df['city'].nunique()}")
    except Exception as e:
        print(f"✗ Error generating data: {e}")
        return
    
    # Step 2: Load and analyze data
    print("\n[Step 2] Loading and analyzing data...")
    try:
        analysis = RestaurantAnalysis(data_path='restaurant_data.csv')
        print("✓ Data loaded successfully")
    except Exception as e:
        print(f"✗ Error loading data: {e}")
        return
    
    # Step 3: Generate analysis report
    print("\n[Step 3] Generating analysis report...")
    try:
        analysis.generate_report()
        print("\n✓ Analysis report generated")
    except Exception as e:
        print(f"✗ Error generating report: {e}")
        return
    
    # Step 4: Perform detailed analysis
    print("\n[Step 4] Performing detailed analysis...")
    try:
        # Rating Analysis
        print("\n  Rating Analysis:")
        rating_stats = analysis.rating_analysis()
        if rating_stats:
            for metric, value in rating_stats.items():
                print(f"    • {metric}: {value:.2f}")
        
        # Cuisine Analysis
        print("\n  Cuisine Analysis:")
        cuisine_data = analysis.cuisine_analysis()
        if cuisine_data:
            print(f"    • Total unique cuisines: {len(cuisine_data['cuisine_count'])}")
            print(f"    • Top 5 cuisines:")
            for cuisine, count in cuisine_data['cuisine_count'].head(5).items():
                print(f"      - {cuisine}: {count} restaurants")
        
        # Price Analysis
        print("\n  Price Analysis:")
        price_data = analysis.price_analysis()
        if price_data:
            print(f"    • Mean Price Range: {price_data['Mean Price']:.2f}")
            print(f"    • Median Price Range: {price_data['Median Price']:.2f}")
    
    except Exception as e:
        print(f"✗ Error in detailed analysis: {e}")
        return
    
    # Step 5: Create visualizations
    print("\n[Step 5] Creating visualizations...")
    try:
        viz = RestaurantVisualizations(df)
        print("✓ Creating visualization charts...")
        
        # Create individual visualizations
        fig1 = viz.plot_rating_distribution()
        print("  • Rating distribution chart created")
        
        fig2 = viz.plot_cuisine_analysis()
        print("  • Cuisine analysis chart created")
        
        fig3 = viz.plot_price_analysis()
        print("  • Price analysis chart created")
        
        fig4 = viz.plot_city_analysis()
        print("  • City analysis chart created")
        
        fig5 = viz.plot_correlation_heatmap()
        print("  • Correlation heatmap created")
        
        print("\n✓ All visualizations created successfully")
        print("  Note: To save visualizations, use viz.create_all_visualizations(save_path='./plots')")
    
    except Exception as e:
        print(f"✗ Error creating visualizations: {e}")
        return
    
    # Summary
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE!")
    print("="*70)
    print("\nKey Files Generated:")
    print("  • restaurant_data.csv - Sample dataset")
    print("\nFor more information, see PROJECT_INFO.md")
    print("\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAnalysis interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\nFatal error: {e}")
        sys.exit(1)
