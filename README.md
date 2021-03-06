# CHIPS

Check it out [here](https://chips.dips.tips/)

Repo to setup a micro-service based machine-learning model deployment and hosting
solution on Google's cloud platform to leverage auto-scaling as well as supporting multiple environments

# Google Cloud Environment

## Micro-service approach

### Benefits

- Have different environments, versions, and packages for different models
- Allows for auto-scaling based on model usage
- Adding, removing, or updating a model is low risk for the rest of the models
- We can also use R and/or julia in this setup as long as someone figures out how to setup an endpoint and deploy it to google cloud


### Downsides

- Need to maintain multiple endpoints and multiple environments


## Diagram of CHIPS

![img](docs/chips-diagram.png)



## Explanation

### VPC and internet gateway

We will whitelist the right IPs so that we can control who pings our service

### Model scoring service

This is a simple front end that routes to the appropriate model microservice.

Ex: POST request to https://chips.dips.tips/test_model

This will forward the request to the `test_model` service for scoring

### Model instances

Each model instance has its own environment and auto-scales based on its usage (independent of other models)

### Cloud storage

The model pkl files are saved in a shared cloud storage system.  
This is VERY cheap, ~2.6 cents/GB per month.  
Each model instance will cache its data from here so there will not be dramatic performance requirements for this.

### Model pkl deployment code

This will be a simple script, file, or process to save pkl files into the cloud storage before we deploy a new endpoint


# How do I deploy my model?

Steps

1. Train model
2. Save out pickle file
3. Upload pickle file to google cloud storage
4. Create deployment scripts
    - Use generic `run.py` sample to setup logging and host endpoint
    - Create custom `model.py` to load your model file, do feature transformations, and score your model
    - Update `requirements.txt` and `app.yaml` accordingly 
5. Test this on the qa extension
6. Deploy to prod
7. Send a POST request to test it out


# Future versions

- Create shared feature transformation scripts to be shared across models
- Also deploy DIPS using this service
- Setup recurring jobs with `chron.yaml`



# Random info about google cloud

- Google domains [here](https://domains.google.com/)
- Cloud platform [here](https://console.cloud.google.com/)
- gcloud sdk download [here](https://cloud.google.com/sdk/)
- App engine micro-service docs [here](architecture https://cloud.google.com/appengine/docs/standard/python/microservices-on-app-engine)



# TODOs

- Understand logging and debugging
- Figure out real-time monitoring and alerts
- Research costs
- Figure out auto-scaling settings and how to monitor cost
- Figure out dev and QA environments for testing
- Setup repo within company
    - Create repo
    - Setup permissions
    - Define model deployment and new endpoint creation
- Setup on company Google cloud account or transfer to AWS
    - Create company cloud account
    - Figure out permissions for Dev/QA/Prod
    - Figure out change control/deployment process
    - Need to define sign-off and QA process
    - Need to figure out price estimates

