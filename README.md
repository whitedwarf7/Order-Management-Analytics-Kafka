# Order-Management-Analytics-Kafka
FastAPI and Kafka

## Setup

1. `docker-compose up -d`
2. Install required packages in virtual environment `pip install -r requirements.txt`
3. Open new terminal and run Uvicorn server `uvicorn producers:app --reload`
4. Open new terminal and start the consumers `python3 consumers.py`
5. Open new terminal to start the script that will generate order every 3 seconds `python3 data_generator.py`
