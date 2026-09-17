import pandas as pd
import json
from datetime import datetime, timedelta
import random
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Step 1: EXTRACT
def extract_data():
    """Extract banking transaction data"""
    try:
        logging.info("Starting data extraction...")
        transactions = []
        
        for i in range(100):
            transaction = {
                'transaction_id': f'TXN{str(i+1).zfill(5)}',
                'account_number': f'ACC{str(random.randint(1000, 9999))}',
                'amount': round(random.uniform(100, 50000), 2),
                'transaction_type': random.choice(['NEFT', 'RTGS', 'IMPS']),
                'status': random.choice(['SUCCESS', 'PENDING', 'FAILED']),
                'timestamp': (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d %H:%M:%S')
            }
            transactions.append(transaction)
        
        df = pd.DataFrame(transactions)
        logging.info(f"Extracted {len(df)} records")
        return df
    
    except Exception as e:
        logging.error(f"Error during extraction: {str(e)}")
        raise

# Step 2: TRANSFORM
def transform_data(df):
    """Transform and clean the data"""
    try:
        logging.info("Starting data transformation...")
        
        # Remove failed transactions
        df = df[df['status'] != 'FAILED']
        
        # Convert amount to numeric
        df['amount'] = pd.to_numeric(df['amount'])
        
        # Remove duplicates
        df = df.drop_duplicates(subset=['transaction_id'])
        
        # Add transaction date
        df['transaction_date'] = pd.to_datetime(df['timestamp']).dt.date
        
        logging.info(f"Transformed {len(df)} records")
        return df
    
    except Exception as e:
        logging.error(f"Error during transformation: {str(e)}")
        raise

# Step 2B: VALIDATE
def validate_data(df):
    """Validate data quality"""
    try:
        logging.info("Starting data validation...")
        
        # Check for nulls
        null_count = df.isnull().sum().sum()
        if null_count > 0:
            logging.warning(f"Null values found: {null_count}")
        
        # Check amount is positive
        negative_amounts = len(df[df['amount'] < 0])
        if negative_amounts > 0:
            logging.warning(f"Negative amounts found: {negative_amounts}")
        
        # Check valid transaction types
        valid_types = ['NEFT', 'RTGS', 'IMPS']
        invalid_types = len(df[~df['transaction_type'].isin(valid_types)])
        if invalid_types > 0:
            logging.warning(f"Invalid transaction types: {invalid_types}")
        
        logging.info("Data validation completed")
        return True
    
    except Exception as e:
        logging.error(f"Error during validation: {str(e)}")
        return False

# Step 3: LOAD
def load_data(df, filename='banking_transactions_cleaned.csv'):
    """Load data to CSV file"""
    try:
        logging.info(f"Starting data load to {filename}...")
        df.to_csv(filename, index=False)
        logging.info(f"Successfully loaded {len(df)} records to {filename}")
    
    except Exception as e:
        logging.error(f"Error during load: {str(e)}")
        raise

# import boto3

# s3_client = boto3.client('s3',
#     aws_access_key_id='YOUR_ACCESS_KEY',
#     aws_secret_access_key='YOUR_SECRET_KEY',
#     region_name='us-east-1'
# )

# # Convert dataframe to CSV in memory
# csv_buffer = df.to_csv(index=False)

# # Upload to S3
# s3_client.put_object(
#     Bucket='your-bucket-name',
#     Key='banking_transactions_cleaned.csv',
#     Body=csv_buffer
# )

# Main ETL Pipeline
if __name__ == "__main__":
    try:
        logging.info("=== ETL Pipeline Started ===")
        
        # Extract
        df = extract_data()
        print(df.head())
        
        # Transform
        df_transformed = transform_data(df)
        print(df_transformed.head())
        
        # Validate
        is_valid = validate_data(df_transformed)
        
        if is_valid:
            # Load
            load_data(df_transformed)
            logging.info("=== ETL Pipeline Completed Successfully ===")
        else:
            logging.error("Data validation failed. Pipeline stopped.")
    
    except Exception as e:
        logging.error(f"Pipeline failed: {str(e)}")