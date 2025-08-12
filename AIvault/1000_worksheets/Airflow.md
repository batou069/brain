# Keywords

### 1. ETL/ELT

**ETL (Extract, Transform, Load)** and **ELT (Extract, Load, Transform)** are two approaches for moving data from a source system to a data warehouse.

- **ETL**: Data is **extracted** from a source, **transformed** in a staging area (e.g., on a dedicated processing engine like Spark), and then **loaded** into the destination warehouse. The transformation happens _before_ loading.
    
- **ELT**: Data is **extracted** from a source and immediately **loaded** into the destination warehouse. The **transformation** logic is then run directly on the data within the powerful warehouse itself (e.g., using SQL).
    
- Airflow is a tool to **orchestrate** these workflows, not to perform the E, T, or L itself. It triggers the tools that do the work.
    
- The ELT approach has become more popular with the rise of powerful, scalable cloud data warehouses like BigQuery, Snowflake, and Redshift.
    

Python

```python
# Conceptual DAG structure for an ELT pipeline in Airflow
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from dbt.airflow import DbtTaskGroup

# In a real DAG file...
# 1. Extract & Load: A task to load raw data from a file into BigQuery
load_raw_data = GCSToBigQueryOperator(
    task_id='extract_and_load_to_bigquery',
    bucket='my-raw-data-bucket',
    source_objects=['new_sales_data.csv'],
    destination_project_dataset_table='my_project.my_raw_dataset.sales'
)

# 2. Transform: A task group to run dbt models that transform the raw data
# within BigQuery
transform_data = DbtTaskGroup(
    group_id='run_dbt_transformations',
    project_config='/path/to/dbt/project',
    profile_config='/path/to/dbt/profiles'
)

load_raw_data >> transform_data
```

**ETL** and **ELT** are blueprints for data integration pipelines. The traditional method, **ETL**, is like preparing ingredients in your kitchen before cooking. You extract raw data (veggies), transform it in a separate staging area (chop, peel, and season them), and then load the prepared data into your destination (the pot). In contrast, the modern **ELT** approach is like having a powerful, all-in-one cooking machine. You extract the raw data and immediately load it into your high-performance cloud data warehouse. You then leverage the massive computational power of the warehouse itself to run transformations on the data in-place, often using SQL. Airflow acts as the head chef, directing when each of these steps should happen, regardless of whether you choose an ETL or ELT recipe.

---

### 2. DAG

A **DAG (Directed Acyclic Graph)** in Airflow is a collection of tasks with defined dependencies, representing a complete workflow.

- **Directed**: Data flows in one direction. A task dependency goes from a parent (upstream) to a child (downstream), not the other way around.
    
- **Acyclic**: The graph has no loops or circular dependencies. A task cannot depend on a downstream task that eventually depends back on the original task.
    
- A DAG is defined as Python code, which makes it dynamic, versionable, and testable.
    
- The DAG itself doesn't do any work; it's a declaration of the workflow's structure, schedule, and properties.
    

Python

```python
# A simple DAG definition in an Airflow DAG file (e.g., my_dag.py)
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
import pendulum

with DAG(
    dag_id='my_first_dag',
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule='@daily',
    catchup=False,
    tags=['example']
) as dag:
    task_a = BashOperator(task_id='task_a', bash_command='echo "Task A done"')
    task_b = BashOperator(task_id='task_b', bash_command='echo "Task B done"')
    task_c = BashOperator(task_id='task_c', bash_command='echo "Task C done"')

    # Define dependencies: A runs first, then B and C run in parallel
    task_a >> [task_b, task_c]
```

A **DAG** is the heart of Airflow; it's the blueprint for your entire data workflow. Think of it as a recipe. The recipe has a name (`dag_id`), a time to start cooking (`start_date`), and instructions on how often to make it (`schedule`). The individual steps in the recipe are the **tasks**. The "Directed" part means the steps have an order—you must chop vegetables before you cook them. The "Acyclic" part means you can't have a circular instruction like "to make the sauce, first make the sauce." In Airflow, you define this entire structure in a Python file, which gives you the power to create complex, dynamic, and version-controlled workflows programmatically.

---

### 3. Airflow task

An **Airflow task** is a single, defined unit of work within a DAG.

- A task is an instance of an **Operator** (e.g., `BashOperator`, `PythonOperator`, `BigQueryOperator`).
    
- Tasks are arranged within a DAG and have upstream (parent) and downstream (child) dependencies.
    
- An ideal task is **idempotent**, meaning running it multiple times with the same input produces the same result. This is crucial for safely retrying failed tasks.
    
- The state of a task (e.g., `running`, `success`, `failed`) is tracked by Airflow's metadata database.
    

Python

```python
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import pendulum

def my_python_function():
    print("Executing Python function!")
    return "Success"

with DAG(
    dag_id='task_example_dag',
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False
) as dag:
    # This is a task that runs a bash command
    bash_task = BashOperator(
        task_id='run_bash_script',
        bash_command='echo "Hello from Bash! Today is $(date)"'
    )

    # This is a task that runs a Python function
    python_task = PythonOperator(
        task_id='run_python_function',
        python_callable=my_python_function
    )

    bash_task >> python_task
```

An **Airflow task** is a single step in your workflow's recipe. It's the action item. A task is created by using an **Operator**, which is a template for a specific kind of work. For example, a `BashOperator` is a task that runs a shell command, a `PythonOperator` is a task that executes a Python function, and a `BigQueryOperator` is a task that runs a query in Google BigQuery. Each task has a unique ID within the DAG and is responsible for executing one atomic piece of work. The power of Airflow comes from arranging these individual tasks into a graph, defining their dependencies, and letting the Airflow scheduler execute them in the correct order.

## Airflow

### 1. `with DAG`

The `with DAG(...) as dag:` syntax is the classic context manager approach for declaring a DAG and associating tasks with it.

- Any task instantiated inside the `with` block is automatically assigned to that DAG.
    
- It provides a clear, indented scope that visually groups all components of a single DAG.
    
- This is the traditional and still very common way to define DAGs, especially when using standard Operators.
    
- It is an alternative to the newer `@dag` decorator (TaskFlow API).
    

Python

```python
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
import pendulum

# Using the 'with' statement as a context manager
with DAG(
    dag_id='context_manager_dag',
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule='@daily'
) as dag:
    # These tasks are automatically part of the 'dag' object
    start = BashOperator(task_id='start', bash_command='echo "start"')
    end = BashOperator(task_id='end', bash_command='echo "end"')

    start >> end
```

The `with DAG(...) as dag:` syntax is a clean and explicit way to build a DAG in Airflow. It works just like opening a file in Python using `with open(...)`. Everything indented inside the `with` block "belongs" to the DAG being defined. This approach makes your code highly readable because it creates a clear visual container for all the tasks and dependencies that make up a single workflow. It's the foundational pattern for DAG authoring and is especially useful when you're working with traditional operators that need to be explicitly instantiated.

---

### 2. `@dag` / `@task`

The `@dag` and `@task` decorators are part of Airflow's **TaskFlow API**, offering a more Python-native way to create DAGs and tasks.

- `@dag`: A decorator placed above a Python function that turns the entire function into a DAG generator.
    
- `@task`: A decorator placed above a Python function to turn it into an Airflow task (`PythonOperator`).
    
- This API automatically handles passing data between tasks using **XComs**, making pipelines look like simple Python function calls.
    
- It simplifies DAG authoring by reducing boilerplate code and focusing on the core logic.
    

Python

```python
from airflow.decorators import dag, task
import pendulum

@dag(
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule='@daily',
    catchup=False,
    tags=['taskflow_api']
)
def my_taskflow_dag():
    """A DAG created using the TaskFlow API."""

    @task
    def extract():
        """Returns a value that is automatically passed via XComs."""
        return 42

    @task
    def process(value: int):
        """Receives the value from the upstream task."""
        return value * 10

    # The dependencies are inferred from the function calls
    extracted_value = extract()
    processed_value = process(extracted_value)

# This line instantiates the DAG
my_taskflow_dag()
```

The **TaskFlow API**, with its `@dag` and `@task` decorators, lets you write Airflow workflows as if you were writing a regular Python script. Instead of manually instantiating operators and setting dependencies with `>>`, you simply decorate your Python functions. A function decorated with `@task` becomes a task. When you call one decorated function with the output of another, Airflow automatically understands this is a dependency and handles passing the data between them behind the scenes. This approach feels more intuitive to Python developers, reduces boilerplate, and makes data-sharing between tasks seamless.

---

### 3. `>>`, `<<`

The bit-shift operators, `>>` and `<<`, are the primary way to set dependencies between Airflow tasks.

- `task_a >> task_b` means "run task A, and then upon its successful completion, run task B."
    
- `task_b << task_a` is exactly the same as `task_a >> task_b`. The direction of the arrows indicates the flow of execution.
    
- These operators can be used to chain multiple tasks together (e.g., `task_a >> task_b >> task_c`).
    
- They can also be used with lists of tasks to define complex dependency structures.
    

Python

```python
from airflow.models.dag import DAG
from airflow.operators.dummy import DummyOperator
import pendulum

with DAG(
    dag_id='dependency_operators_dag',
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule=None
) as dag:
    start = DummyOperator(task_id='start')
    middle_task = DummyOperator(task_id='middle_task')
    end = DummyOperator(task_id='end')
    parallel_task_1 = DummyOperator(task_id='parallel_task_1')
    parallel_task_2 = DummyOperator(task_id='parallel_task_2')

    # Simple chain: start -> middle_task -> end
    start >> middle_task >> end

    # Complex dependency: start also triggers two parallel tasks
    start >> [parallel_task_1, parallel_task_2]
```

The bit-shift operators, `>>` (right-shift) and `<<` (left-shift), are an elegant and intuitive way to draw the dependency lines in your DAG. Think of `>>` as a "then" operator. The statement `extract_task >> transform_task` reads naturally as "run the extract task, _then_ run the transform task." The `<<` operator simply reverses the relationship, so `transform_task << extract_task` means the same thing. These operators are the syntactic sugar that makes defining the flow of your workflow concise and highly readable, allowing you to visually map out the relationships between your tasks directly in the code.

---

### 4. `set_downstream` ,`set_upstream`

The `set_downstream()` and `set_upstream()` methods are the explicit function calls for setting dependencies between tasks, serving as an alternative to the bit-shift operators.

- `task_a.set_downstream(task_b)` is equivalent to `task_a >> task_b`.
    
- `task_b.set_upstream(task_a)` is equivalent to `task_b << task_a`.
    
- These methods can be useful for setting dependencies programmatically, for example, inside a loop.
    
- While functionally identical to the bit-shift operators, they are more verbose and less commonly used for static dependency definitions.
    

Python

```python
from airflow.models.dag import DAG
from airflow.operators.dummy import DummyOperator
import pendulum

with DAG(
    dag_id='dependency_methods_dag',
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule=None
) as dag:
    tasks = [DummyOperator(task_id=f'task_{i}') for i in range(4)]

    # Using methods is more verbose for simple cases:
    # tasks[0].set_downstream(tasks[1]) is the same as tasks[0] >> tasks[1]

    # But they can be useful inside loops:
    for i in range(len(tasks) - 1):
        # Programmatically set task i to run before task i+1
        tasks[i].set_downstream(tasks[i+1])
```

Before the convenient bit-shift operators (`>>`, `<<`) were introduced, `set_downstream()` and `set_upstream()` were the original methods for defining task dependencies. Calling `task_a.set_downstream(task_b)` explicitly tells Airflow that `task_b` is a child of `task_a`. While these methods are more verbose for simple, one-to-one dependencies, they can be very powerful when you need to create dependencies dynamically. For instance, if you're generating a list of tasks inside a `for` loop, using these methods is a clean way to programmatically chain them together based on the loop's logic.

---

### 5. `cross_downstream`

The `cross_downstream()` function is a utility for creating an "all-to-all" dependency relationship between two groups of tasks.

- `cross_downstream(group_a, group_b)` makes every task in `group_b` dependent on _every_ task in `group_a`.
    
- This means that no task in `group_b` will start until all tasks in `group_a` have completed successfully.
    
- It's a powerful shortcut for creating complex fan-out/fan-in dependency patterns.
    
- It helps avoid writing many individual dependency lines manually.
    

Python

```python
from airflow.models.dag import DAG
from airflow.operators.dummy import DummyOperator
from airflow.models.baseoperator import cross_downstream
import pendulum

with DAG(
    dag_id='cross_downstream_dag',
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule=None
) as dag:
    # Group A: A list of extraction tasks
    extract_tasks = [DummyOperator(task_id=f'extract_{i}') for i in ['a', 'b']]
    
    # Group B: A list of loading tasks
    load_tasks = [DummyOperator(task_id=f'load_{i}') for i in ['x', 'y']]

    # A single "report" task that runs after everything is loaded
    report_task = DummyOperator(task_id='report')

    # This single line creates 4 dependency links:
    # extract_a >> load_x, extract_a >> load_y
    # extract_b >> load_x, extract_b >> load_y
    cross_downstream(extract_tasks, load_tasks)

    # The report task depends on all load tasks completing
    load_tasks >> report_task
```

The `cross_downstream()` function is a massive time-saver for creating fan-in dependencies. Imagine you have a set of "extract" tasks that pull data from various sources and a set of "load" tasks that load that data. You need to ensure that _all_ extraction is finished before _any_ loading begins. Instead of writing out every single dependency line (`extract_a >> load_x`, `extract_a >> load_y`, `extract_b >> load_x`, etc.), you can use a single command: `cross_downstream(extract_tasks, load_tasks)`. This creates the complete, many-to-many dependency structure for you, making your DAG code cleaner and less error-prone.

---

### 6. `chain`

The `chain()` function is a utility for creating a simple, linear sequence of dependencies between multiple tasks.

- `chain(task_a, task_b, task_c)` is equivalent to `task_a >> task_b >> task_c`.
    
- It's particularly useful for creating long, straight-line workflows without having to repeat the `>>` operator.
    
- You can chain together individual tasks, or lists of tasks, to create more complex linear flows.
    
- It improves the readability of long, sequential dependency chains.
    

Python

```python
from airflow.models.dag import DAG
from airflow.operators.dummy import DummyOperator
from airflow.models.baseoperator import chain
import pendulum

with DAG(
    dag_id='chain_dag',
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule=None
) as dag:
    tasks = [DummyOperator(task_id=f'task_{i}') for i in range(5)]

    # Instead of writing:
    # tasks[0] >> tasks[1] >> tasks[2] >> tasks[3] >> tasks[4]

    # You can write this much cleaner line:
    chain(*tasks)
```

The `chain()` function is a convenience utility designed to make your DAG definitions cleaner. When you have a workflow where several tasks need to run one after the other in a straight line, writing `task1 >> task2 >> task3 >> task4` can become long and repetitive. `chain()` allows you to express this linear dependency more concisely. By passing a list of tasks to the function, like `chain(task1, task2, task3, task4)`, you achieve the exact same sequential workflow with less code, improving the readability and maintainability of your DAG file.

## Questions

### 1. Why is Airflow better than a simple scheduler? When would you prefer the cron utility over Airflow?

Airflow is better than a simple scheduler because it's a full-featured **workflow orchestration platform**, not just a trigger.

- **Airflow's Advantages**:
    
    - **Dependency Management**: It manages complex relationships between tasks (e.g., A must finish before B and C can start).
        
    - **Monitoring & UI**: It provides a rich user interface to visualize workflows, check logs, and see task statuses.
        
    - **Scalability**: It can distribute tasks across multiple worker machines.
        
    - **Resilience**: It has built-in mechanisms for retrying failed tasks and sending alerts.
        
    - **Dynamic Pipelines**: DAGs are defined in Python, allowing for dynamic and complex logic.
        
- **When to prefer `cron`**: You would prefer `cron` for extremely simple, standalone tasks that have no dependencies and require no monitoring beyond basic logging. For example, running a single script every night to clean up a temporary directory is a perfect use case for `cron`. If the job fails, the consequence is low, and you don't need a complex UI to debug it.
    

Airflow is a complete orchestra conductor, while `cron` is a simple alarm clock. An alarm clock (`cron`) is great for one simple job: "run this script at 2 AM." It's lightweight, simple, and reliable for isolated tasks. An orchestra conductor (Airflow) manages dozens of musicians (tasks), ensuring they start and stop at the right times, follow the right sequence, and can recover if someone plays a wrong note (retries). You need Airflow when your jobs have dependencies, require monitoring, need to be re-run on failure, or involve complex logic. If you just need to ring a bell at midnight, `cron` is the better, simpler tool.

---

### 2. In what different ways can a task be triggered?

A task in Airflow is triggered automatically by the scheduler once all of its upstream dependencies have been met for a specific DAG run.

- A **DAG run** itself can be triggered in several ways:
    
    - **Schedule-based**: The most common way. The DAG runs automatically based on its `schedule` parameter (e.g., `'@daily'`, `'0 5 * * *'`).
        
    - **External Triggers**:
        
        - **Airflow CLI**: Using the command `airflow dags trigger <dag_id>`.
            
        - **Airflow REST API**: Sending a request to the appropriate API endpoint to create a new DAG run. This is common for event-driven workflows.
            
    - **Manual Trigger**: Clicking the "play" button next to a DAG in the Airflow UI.
        
    - **Dataset Updates (since Airflow 2.4)**: A DAG can be configured to run automatically whenever a specific dataset it consumes is updated by another DAG.
        

A task doesn't get triggered on its own; it gets triggered as part of a **DAG Run**. The DAG run is the instance of your entire workflow for a specific point in time. The DAG run itself can be kicked off in multiple ways. The most common is on a recurring **schedule**, like a cron job (`'@daily'`, `'@hourly'`). You can also trigger a run **manually** by pressing the play button in the Airflow web UI, which is useful for testing or backfilling. For integration with external systems, you can trigger a run using the **REST API** or the **command-line interface (CLI)**. Finally, a newer, more advanced method allows a DAG to be triggered automatically whenever a dataset it depends on is produced by another DAG.

---

### 3. Can Airflow run multiple tasks in parallel?

Yes, Airflow is specifically designed to run multiple tasks in parallel.

- Any tasks that do not have dependencies on each other, or whose upstream dependencies have been successfully met, are eligible to run at the same time.
    
- The number of tasks that can actually run in parallel is determined by the configuration of the **Executor** and the overall Airflow setup.
    
- For example, if you have `task_a >> [task_b, task_c]`, once `task_a` completes, `task_b` and `task_c` will be scheduled to run in parallel.
    
- This parallel execution is a key feature that allows Airflow to run complex workflows efficiently and quickly.
    

Python

```python
# In this DAG, 'process_data_a' and 'process_data_b' can run in parallel.
# Similarly, 'report_a' and 'report_b' can run in parallel.

start >> [process_data_a, process_data_b]
process_data_a >> report_a
process_data_b >> report_b
[report_a, report_b] >> end
```

Absolutely. Parallel execution is one of Airflow's core strengths. When the Airflow scheduler looks at your DAG, it identifies all tasks that are "ready" to run—meaning all their parent tasks have completed successfully. If it finds multiple ready tasks, it will send them to be executed concurrently. The degree of parallelism is limited only by your Airflow configuration, such as the number of available worker slots defined by your **Executor** (e.g., `CeleryExecutor` or `KubernetesExecutor`). This ability to run independent branches of your workflow simultaneously is what makes Airflow so efficient for complex data pipelines.

---

### 4. How can you handle dependencies between tasks?

You handle dependencies by explicitly defining the relationships between tasks in your DAG file using specific operators and functions.

- **Bit-Shift Operators (`>>`, `<<`)**: The most common method for setting a direct dependency (e.g., `task_1 >> task_2`).
    
- **Lists for Fan-Out/Fan-In**: You can set dependencies to or from a list of tasks to manage parallel workflows.
    
    - **Fan-Out**: `start_task >> [parallel_task_1, parallel_task_2]`
        
    - **Fan-In**: `[parallel_task_1, parallel_task_2] >> end_task`
        
- **Utility Functions (`chain`, `cross_downstream`)**:
    
    - `chain(t1, t2, t3)` creates a simple linear sequence.
        
    - `cross_downstream([t1, t2], [t3, t4])` creates an all-to-all dependency.
        
- **TaskFlow API**: Dependencies are inferred automatically from function calls. If `task_b(task_a())` is called, Airflow knows `task_b` depends on `task_a`.
    

You manage dependencies by "drawing" the lines of your workflow graph directly in your Python code. The most common way is with the bit-shift operators, `>>` and `<<`. The statement `extract >> transform` clearly defines that the `transform` task must wait for the `extract` task to finish. For more complex patterns, you can use lists. For example, `start >> [task_a, task_b]` is a "fan-out" pattern where `task_a` and `task_b` start in parallel after `start` finishes. The reverse, `[task_a, task_b] >> end`, is a "fan-in" pattern where `end` waits for both `task_a` and `task_b` to complete. For even more complex scenarios, helper functions like `chain` and `cross_downstream` provide powerful shortcuts.

---

### 5. How can you monitor your workflow?

You primarily monitor your workflows using the **Airflow Web UI**, which provides a comprehensive suite of tools for observability.

- **DAGs View**: The main dashboard showing all your DAGs, their recent run statuses, and quick links.
    
- **Graph View**: A visual representation of your DAG's structure and the status of tasks for a specific run.
    
- **Gantt Chart**: A timeline view showing how long each task took to run, helping you identify bottlenecks.
    
- **Logs**: You can access the detailed logs for every task run directly in the UI to debug errors.
    
- **Alerting**: Airflow can be configured to send alerts (e.g., via email or Slack) on task failure, retries, or SLA misses.
    
- **SLAs (Service Level Agreements)**: You can define a maximum duration for a task, and Airflow will alert you if it's not met.
    

You monitor your Airflow workflows through its powerful built-in **web interface**. The UI is your central command center. The **Graph View** gives you a live map of your workflow, showing which tasks have succeeded (green), which are running (light green), and which have failed (red). The **Gantt Chart** helps you visualize task durations and find performance bottlenecks. If a task fails, you can click on it and instantly view its **logs** to diagnose the problem. Beyond the UI, you can configure Airflow to be proactive by setting up **email or Slack alerts** for task failures or for when a task misses its **SLA (Service Level Agreement)**, ensuring you're notified immediately when something goes wrong.

---

### 6. What are the two ways to create a DAG? Are there any pros and cons?

The two main ways to create a DAG are using the **traditional context manager (`with DAG`)** and the newer **TaskFlow API (`@dag` decorator)**.

- **`with DAG` (Context Manager)**
    
    - **Pros**: Explicit and very clear about which tasks belong to which DAG. It's the classic approach, so it's well-understood and documented. Works cleanly with all operator types.
        
    - **Cons**: Can be verbose (boilerplate). Passing data between tasks requires manually pushing and pulling from XComs.
        
- **`@dag` (TaskFlow API)**
    
    - **Pros**: Less boilerplate code, feels more like writing a standard Python script. Data passing between tasks is handled automatically and magically by returning and accepting values.
        
    - **Cons**: Can feel "too magical" if you don't understand XComs. It's primarily designed for tasks that are Python functions (`@task`), so mixing it with traditional operators can sometimes be less elegant.
        

Yes, there are two primary methods for authoring DAGs. The classic approach uses a Python **context manager**: `with DAG(...) as dag:`. In this style, you explicitly instantiate operators like `BashOperator` inside the `with` block, and dependencies are set using `>>`. This method is very explicit and easy to follow. The newer, more modern approach is the **TaskFlow API**, which uses decorators. You decorate a function with `@dag` to define the workflow and other functions with `@task` to define the steps. Dependencies are created implicitly by calling one task function with the output of another. The main pro of TaskFlow is its simplicity and Pythonic feel, especially for passing data. The main con is that it can hide the underlying Airflow mechanics (like XComs), which might be confusing for beginners.

---

### 7. Can a task have more than one upstream dependency?

Yes, a task can absolutely have more than one upstream dependency.

- This is a fundamental feature for creating "fan-in" patterns in a workflow.
    
- The task will only be scheduled to run after **all** of its upstream parent tasks have completed successfully.
    
- If any one of the upstream tasks fails, the downstream task will not run and will be marked as `upstream_failed`.
    
- This is defined in code by placing a list of tasks on the upstream side of the dependency operator.
    

Python

```python
from airflow.models.dag import DAG
from airflow.operators.dummy import DummyOperator
import pendulum

with DAG(
    dag_id='fan_in_dependency_dag',
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule=None
) as dag:
    extract_a = DummyOperator(task_id='extract_from_source_A')
    extract_b = DummyOperator(task_id='extract_from_source_B')
    
    # This task depends on BOTH extract_a and extract_b completing.
    # It will only run after both have succeeded.
    generate_report = DummyOperator(task_id='generate_report')

    [extract_a, extract_b] >> generate_report
```

Yes, definitely. A task can wait for any number of upstream tasks to finish before it starts. This is a common and critical pattern known as a "fan-in." For example, you might have a final `generate_report` task that can only run after data has been successfully extracted from a database (`extract_db_task`) AND a file has been downloaded from an API (`download_api_task`). You would define this relationship in your code as `[extract_db_task, download_api_task] >> generate_report`. The Airflow scheduler will ensure that the report task is not even considered for execution until both parent tasks are marked as successful.

---

### 8. How can you test a task individually if it has upstream dependencies?

You can test a task individually, ignoring its dependencies, by using the **`airflow tasks test` CLI command**.

- This command runs a single task instance locally for a specified execution date.
    
- It **ignores all dependencies** and does not record the task's state in the metadata database.
    
- This makes it perfect for quickly testing the logic of a single task without having to run the entire DAG.
    
- You must provide the `dag_id`, `task_id`, and an `execution_date` for the test run.
    

Bash

```
# Command to run in your terminal

# Test the 'generate_report' task from the 'fan_in_dependency_dag'
# for the execution date of 2025-07-31, ignoring its upstream dependencies.

airflow tasks test fan_in_dependency_dag generate_report 2025-07-31
```

The `airflow tasks test` command in the command-line interface (CLI) is the perfect tool for this. It's designed specifically for testing. When you run this command, you're telling Airflow: "I want to run _this specific task_ from _this specific DAG_ for _this specific moment in time_, but I want you to pretend all its upstream dependencies have already succeeded." Airflow will then execute the task's logic in isolation and print the logs to your console. It doesn't write anything to the Airflow database, so it's a clean, safe, and fast way to verify that your task's code works as expected without needing to trigger and wait for an entire workflow.

---

### 9. What are the parameters to create a DAG?

When creating a DAG, you provide several key parameters to its constructor to define its behavior and properties.

- **`dag_id` (required)**: A unique string identifier for the DAG.
    
- **`start_date` (required)**: The date and time at which the DAG can begin to be scheduled. This is a fixed point in time.
    
- **`schedule`**: Defines how often the DAG should run. Can be a cron string (`'0 5 * * *'`), a timedelta object, or a preset like `'@daily'`.
    
- **`catchup`**: A boolean (`True`/`False`). If `True`, Airflow will create a DAG run for every missed schedule interval between the `start_date` and the current date. Defaults to `True`, so it's often set to `False` during development.
    
- **`tags`**: A list of strings to help organize and filter DAGs in the UI.
    
- **`default_args`**: A dictionary of default parameters that will be applied to all tasks within the DAG, reducing code repetition.
    

Python

```python
import pendulum
from datetime import timedelta
from airflow.models.dag import DAG

# A dictionary of default arguments for tasks
default_args = {
    'owner': 'data_team',
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_parameters_example',
    start_date=pendulum.datetime(2025, 7, 31, tz="Asia/Jerusalem"),
    schedule='0 9 * * 1-5',  # Run at 9 AM on weekdays
    catchup=False,
    tags=['production', 'finance'],
    default_args=default_args
) as dag:
    # Tasks instantiated here will inherit 'owner', 'retries', etc.
    pass
```

When you define a DAG, you must provide a set of core parameters that act as its metadata. The most important are the `dag_id`, which is its unique name, and the `start_date`, which is the anchor point in time from which its schedule is calculated. The `schedule` parameter determines the frequency of runs, using either presets like `'@daily'` or a cron expression for more control. Another crucial parameter is `catchup=False`, which you'll almost always want to set during development to prevent Airflow from trying to run your DAG for every day since its `start_date`. Finally, you can provide `tags` for organization and a `default_args` dictionary to set common task parameters like `retries` or `owner` for all tasks in the DAG at once.

---

### 10. What are the possible states for a task?

A task instance can be in one of many states throughout its lifecycle, indicating its current status in the workflow.

- **Core Success Path**: `queued` -> `running` -> `success`
    
- **Core Failure Path**: `queued` -> `running` -> `failed`
    
- **Retry Path**: `running` -> `up_for_retry` -> `queued` -> ...
    
- **Dependency-related States**:
    
    - `upstream_failed`: An upstream parent task failed, so this task cannot run.
        
    - `skipped`: The task was skipped based on the DAG's logic (e.g., by a `BranchPythonOperator`).
        
- **Other states**: `scheduled` (the scheduler has recorded the task needs to run), `removed` (the task has been deleted from the DAG code), `restarting`.
    

The state of a task tells you its story within a workflow run. A task typically starts as `queued` once its dependencies are met. From there, it moves to `running` when a worker picks it up. If all goes well, it ends in `success`. If an error occurs, it goes to `failed`. If retries are enabled, it might go into `up_for_retry` before being `queued` again. Other important states reflect the broader workflow context: `upstream_failed` means the task never even tried to run because one of its parents failed, and `skipped` means it was intentionally bypassed by a branching decision in the DAG. These states are color-coded in the UI, giving you an immediate visual summary of your workflow's health.

---

### 11. Why is SLA important?

An **SLA (Service Level Agreement)** is important because it allows you to monitor whether your data pipelines are meeting their time-based deadlines, which is critical for business operations.

- An SLA in Airflow is a `timedelta` parameter on a task that defines the maximum allowable time from the start of a DAG run to the completion of that task.
    
- **It is not a timeout**: It does not stop the task from running.
    
- **It is an alerting mechanism**: If a task misses its SLA (i.e., it doesn't complete within the specified duration), Airflow will record an "SLA Miss" and can be configured to send out an alert.
    
- This is crucial for time-sensitive pipelines. For example, if a business report must be ready by 9 AM, you can set an SLA on the final task to ensure you are notified if the data pipeline feeding it is running late.
    

Python

```python
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
import pendulum
from datetime import timedelta

with DAG(
    dag_id='sla_example_dag',
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule='@hourly'
) as dag:
    # This task is expected to finish within 30 minutes of the DAG run's start.
    # If the DAG starts at 10:00, this task must finish by 10:30.
    # If it finishes at 10:35, an SLA Miss will be recorded and an alert can be sent.
    important_task = BashOperator(
        task_id='time_sensitive_task',
        bash_command='sleep 5 && echo "Done!"',
        sla=timedelta(minutes=30)
    )
```

An **SLA** is a promise. In Airflow, it's a promise that a task will be completed within a certain amount of time after the workflow starts. Its importance isn't in forcing the task to stop, but in **monitoring and alerting**. Imagine a pipeline that prepares data for a critical 9:00 AM financial report. By setting an SLA of 30 minutes on the final task of that pipeline (which runs at 8:00 AM), you are telling Airflow: "If this task isn't done by 8:30 AM, sound the alarm!" If the task misses this deadline, Airflow logs an "SLA Miss" and can send an email or Slack message to the data team. This allows them to investigate the delay immediately, rather than finding out at 9:01 AM that the report is missing its data. It's a critical tool for ensuring data timeliness.