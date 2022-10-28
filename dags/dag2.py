from airflow import DAG
import pendulum
import time
from airflow.decorators import task

with DAG(
    dag_id='dag2',
    description='test dag',
    schedule='@daily',
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    default_args={"owner": "@p.kozakov"},
) as dummy_dag:

    @task
    def sleeper():
        time.sleep(600) 
    sleeper()
