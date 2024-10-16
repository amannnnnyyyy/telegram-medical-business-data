import pandas as pd
import logging
import psycopg2
import sys
sys.path.append('../')
# Setup logging
logging.basicConfig(filename='logs/csv_to_db.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def insert_data(csv_file_path):
    # Connect to PostgreSQL
    try:
        conn = psycopg2.connect(
            dbname="tenacad",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )
        logging.info("Connected to the database.")
        cursor = conn.cursor()

        insert_query = """
            INSERT INTO custom_yolo_detections (
                image_file, label, bbox_x_min, bbox_y_min, bbox_width, bbox_height, image_width, image_height
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        detections_df = pd.read_csv(csv_file_path)
        logging.info(f'Read CSV with {len(detections_df)} records.')
        logging.info(f'Columns in CSV: {detections_df.columns.tolist()}')

        for _, row in detections_df.iterrows():
            cursor.execute(insert_query, (
                row['image_file'], row['label'], row['bbox_x_min'],  
                row['bbox_y_min'], row['bbox_width'], row['bbox_height'], 
                row['image_width'], row['image_height']
            ))
            logging.info(f'Inserted row: {row.to_dict()}')

        conn.commit()
        logging.info(f'Successfully inserted {len(detections_df)} records into the database.')

    except Exception as e:
        logging.error(f'Error occurred: {e}')

    finally:
        cursor.close()
        conn.close()

# Call the function to insert data
insert_data('docs/yolo_output/custom_labeled_data.csv')



def insert_data_new(csv_file_path):
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname="tenacad",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO custom_yolo_detections (
            image_file, label, bbox_x_min, bbox_y_min, bbox_width, bbox_height, image_width, image_height
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:
        detections_df = pd.read_csv(csv_file_path)
        
        logging.info(f'Read CSV with columns: {detections_df.columns.tolist()}')

        for _, row in detections_df.iterrows():
            cursor.execute(insert_query, (
                row['image_file'], row['label'], row['xmin'],  
                row['ymin'], row['width'], row['height'], 
                row['image_width'], row['image_height']
            ))
            logging.info(f'Inserted row: {row.to_dict()}')

        conn.commit()
        logging.info(f'Successfully inserted {len(detections_df)} records into the database.')

    except Exception as e:
        logging.error(f'Error occurred: {e}')

    finally:
        cursor.close()
        conn.close()