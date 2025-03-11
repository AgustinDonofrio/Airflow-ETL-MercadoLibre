from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'Agustin',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id="test_postgres_v1",
    default_args=default_args,
    start_date=datetime(2025, 3, 11),
    schedule_interval='0 0 * * *',
) as dag:
    task_1 = SQLExecuteQueryOperator(
        task_id="create_postgres_table",
        conn_id="postgres_localhost",
        sql="""
            CREATE TABLE IF NOT EXISTS tecnica_ml (
                id VARCHAR(30),
                site_id VARCHAR(30),
                title VARCHAR(50),
                price VARCHAR(10),
                sold_quantity VARCHAR(20),
                thumbnail VARCHAR(50),
                created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                primary key (id, created_date)
            )"""
    )
    task_1
    
