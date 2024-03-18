import logging
logging.info('First test')

# workflow
    # Set of Jobs
        # Job
        # Defines a runner (execution environment)
        # Contains one or more steps
        # Step
            # Execute a shell script or an action
            # Can use custom or third party actions
            # Steps are executed in order
            # Steps can be conditional
        # Jobs are executed parallel by default (can be executed sequentially)
        # Conditional jobs (runs only when a certain condition is met)
