# Ethiopian Medical Data Warehouse with Telegram Scraping and Object Detection
---

### **Table of Contents**

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [How to Set Up](#how-to-set-up)
- [How to Run](#how-to-run)

---
### **Project Overview**

This project is focused on building a **data warehouse** to store data about Ethiopian medical businesses that have been scraped from various **Telegram channels**. The pipeline involves data scraping, cleaning, transforming, and storing data in a structured format for easy querying and analysis. Additionally, **YOLO (You Only Look Once)** object detection is used to analyze images scraped from these channels.

The project is part of 10 Academy's Week 7 challenge, where the goal is to develop an end-to-end data engineering pipeline.



## **Key Features**

- **Telegram Scraping**: Scrapes text and images from public Telegram channels using the Telethon API.
- **Data Cleaning**: Cleans and standardizes the scraped data (handles duplicates, missing values, etc.).
- **Object Detection**: Uses YOLO to detect objects in scraped images.
- **Data Warehouse**: Stores cleaned and enriched data in PostgreSQL for easy querying and reporting.
- **API Integration**: Provides REST API access to the collected data using FastAPI.

## **Technologies Used**

- **Python**: Main language for all scripts.
- **Telethon**: Used to scrape Telegram data.
- **Pandas**: For data manipulation and cleaning.
- **YOLO (You Only Look Once)**: Object detection in images.
- **PostgreSQL**: Relational database to store cleaned data.
- **DBT (Data Build Tool)**: For transforming and loading data into the warehouse.


## **How to Set Up**

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ethiopian-medical-data-warehouse.git
cd ethiopian-medical-data-warehouse
```
## **How to Run**

```bash
pip install requirements.txt
```