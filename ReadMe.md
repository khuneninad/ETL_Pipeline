# Cloud-Based ETL Pipeline

## Overview
A robust Python-based ETL (Extract, Transform, Load) pipeline designed to process banking transaction data with comprehensive error handling and data validation.

## Project Description
This pipeline demonstrates core data engineering concepts by extracting sample banking data, performing transformation and validation checks, and loading cleaned data to CSV format. The architecture supports easy integration with AWS S3 for cloud deployment.

## Features
✅ **Data Extraction** - Generates realistic banking transaction data  
✅ **Data Transformation** - Removes duplicates, filters failed transactions  
✅ **Data Validation** - Quality checks for data integrity  
✅ **Error Handling** - Try-except blocks and logging throughout  
✅ **Logging** - Comprehensive logging for debugging and monitoring  
✅ **Cloud Ready** - Easy integration with AWS S3  

## Technical Stack
- **Language:** Python 3
- **Libraries:** Pandas, Logging
- **Output Format:** CSV
- **Cloud Support:** AWS S3 (Boto3)

## Installation

```bash
pip install pandas
```

## Usage

```bash
python etl_pipeline.py
```

## Output
- `banking_transactions_cleaned.csv` - Cleaned and validated transaction data

## Project Structure
- Extract: Generates 100 banking transactions
- Transform: Cleans data, removes duplicates and failed transactions
- Validate: Checks data quality
- Load: Saves to CSV file

## Error Handling
All functions include try-except blocks with detailed error logging for production reliability.

## Future Enhancements
- AWS S3 integration
- Real-time data streaming
- Data quality metrics dashboard