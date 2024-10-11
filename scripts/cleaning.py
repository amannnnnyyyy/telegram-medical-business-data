import pandas as pd
def cleaning(data):
    data.drop_duplicates(subset=['message_id', 'channel_name', 'date'], inplace=True)

    data['text'].fillna('No text', inplace=True)

    data['image_path'].fillna('No image', inplace=True)

    data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d %H:%M:%S')


    data.to_csv('../my_project/data/all_scraped_messages.csv', index=False)