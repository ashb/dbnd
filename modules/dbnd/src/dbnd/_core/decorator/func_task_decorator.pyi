from datetime import datetime
from typing import Optional

def task(
    task_class_version: Optional[str],
    task_env: Optional[str],
    task_target_date: Optional[datetime.date],
    task_airflow_op_kwargs: Optional[dict[str, object]],
    task_config: Optional[dict],
    result: Optional,
):
    """
    Used to indicate persistent changes in a code.
    :param task_class_version: Used to indicate persistent changes in a code.
    :param task_env: defines data and compute environment for a task. By default, tasks run in local environment. Part of task signature
    :param task_target_date: A date (data) associated with task execution. Part of task signature.
    Example value is 'datetime.date.today()'.
    :param task_airflow_op_kwargs:  Parameters to pass to Airflow operator that would run this task.
    :param task_config: A dictionary of arbitrary configuration params. How to override specific task sub configs
     task_config = {  "spark" : { "param" : "ss"  }
     task_config = { spark.jars = some_jars ,
                     kubernetes.gpu = some_gpu }
    :param result: Defines the name of the output of the task. When output is complex, like a tuple, we can name
    every item inside it. result=("output1", "output2")
    """
    ...