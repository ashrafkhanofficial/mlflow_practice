import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment('First_expirement')

mlflow.delete_run('a23de39ccfd84d40988a4106e74e6ac6')