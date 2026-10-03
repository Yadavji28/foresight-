import pandas as pd
import os

def run_pipeline():
    print("Starting Data Pipeline...")
    data_dir = 'data/raw/processed/'
    output_file = 'data/analysis_ready_data.csv'
    
    # 1. INGESTION
    print("Ingesting data...")
    sales = pd.read_csv(os.path.join(data_dir, 'sales_daily.csv'))
    inventory = pd.read_csv(os.path.join(data_dir, 'inventory_snapshots.csv'))
    calendar = pd.read_csv(os.path.join(data_dir, 'calendar.csv'))
    sku = pd.read_csv(os.path.join(data_dir, 'sku_master.csv'))
    
    # --- COLUMNS KE NAAM THEEK KAREIN ---
    # Sabko small letters mein badlein
    sales.columns = sales.columns.str.strip().str.lower()
    inventory.columns = inventory.columns.str.strip().str.lower()
    calendar.columns = calendar.columns.str.strip().str.lower()
    sku.columns = sku.columns.str.strip().str.lower()

    # Zidio ke standard format ke hisaab se naamon ko rename karein
    sales = sales.rename(columns={'promotion': 'promo_flag', 'price': 'unit_price', 'sku': 'sku_id'})
    
    # YAHAN FIX HAI: inventory mein 'snapshot_date' ko 'date' banayein
    inventory = inventory.rename(columns={'snapshot_date': 'date', 'sku': 'sku_id'})
    
    if 'sku' in sku.columns:
        sku = sku.rename(columns={'sku': 'sku_id'})
    
    # 2. CLEANING
    print("Cleaning data...")
    # Ab teeno files mein 'date' column maujood hai, toh error nahi aayega
    sales['date'] = pd.to_datetime(sales['date'])
    calendar['date'] = pd.to_datetime(calendar['date'])
    inventory['date'] = pd.to_datetime(inventory['date'])
    
    sales = sales.drop_duplicates()
    
    if 'promo_flag' in sales.columns:
        sales['promo_flag'] = sales['promo_flag'].fillna(0)
    
    # 3. UNIFY
    print("Unifying datasets...")
    df_merged = pd.merge(sales, sku, on='sku_id', how='left')
    df_merged = pd.merge(df_merged, calendar, on='date', how='left')
    
    # 4. OUTPUT
    print("Saving analysis-ready dataset...")
    df_merged.to_csv(output_file, index=False)
    print(f"Pipeline finished successfully! Clean data saved to: {output_file}")

if __name__ == "__main__":
    run_pipeline()
    