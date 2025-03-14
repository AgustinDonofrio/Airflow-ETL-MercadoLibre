from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from operators.PostgresFileOperator import PostgresFileOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'Agustin',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id="test_postgres_v1",
    default_args=default_args,
    start_date=datetime(2025, 3, 13),
    schedule_interval='0 0 * * *',
) as dag:
    create_table = SQLExecuteQueryOperator(
        task_id="create_postgres_table",
        conn_id="postgres_localhost",
        sql="""
            CREATE TABLE IF NOT EXISTS tecnica_ml (
                id VARCHAR(30) PRIMARY KEY,
                site_id VARCHAR(30),
                title VARCHAR(150),
                price DECIMAL(10, 2),
                thumbnail VARCHAR(150),
                created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
    )

    run_api_script = BashOperator(
        task_id="run_api_script",
        bash_command="python /opt/airflow/tmp/consult_api.py",
    )

    # Insertar datos en la tabla "tecnica_ml" de la base de datos
    insert_data = PostgresFileOperator(
        task_id="insert_data",
        operation="write",
        config={"table_name":"tecnica_ml"}
    )

    create_table >> run_api_script >> insert_data
