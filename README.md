# Python backend training

In each step use a corresponding git branch (Use ssh).
1) Develop a FastAPI app consuming some endpoints from the public Google Maps API.
   1.1) Use pre-commits, pyenv(python 14), poetry, virtual envs. ruff, bandit 
   1.2) Use a build.sh script for local build
   1.3) Swagger 
   1.4) Document design pattern
   1.5) Use everything as you can regarding python language: decorators, list comprehension, context managers, etc
   1.6) Use memory improvements, like cache and generators. Try to convert traditional loops in O(1) 
2) Add unit and system tests. Use Wiremock. Automation with Github Actions. (Consider introduce Jenkins + Github Actions)
3) Dockerize. Use 2 stages (Build and running). Automation with Github actions
4) Save data from APIs in postgresql, sqlite and mongoDB databases, k-v DBs. Use public containers (most populars). Alembic for migrations
   4.1) Dockerize using compose
5) Introduce Ngnix and Apache before uvicorn. 
   5.1) Stress and document metrics
6) Introduce a visual HTTPS panel to view API results
7) Introduce Authentication using openID connect .Use auth providers like Facebook, Google, Github
8) Introduce SAAS in AWS, Azure, GC. Use S3, SQS, SNS , Dynamo, Cognito (and same for Azure and GC)
9) Deploy 
10) Introduce K8
11) Split in microservices for each cloud provider
12) Introduce a new microservice which use pandas, and LLM libraries like pytorch, 


# steps
# pip install poetry
# pip install pyenv
# pyenv install 3.13
# pyenv versions
# python global 3.13.1
# poetry env use python3.13
# poetry shell
# ln -s /Users/luisvargas/Library/Caches/pypoetry/virtualenvs/fastapi-google-maps-42h-QzWA-py3.13 venv
# source venv/bin/activate
# ./build.sh

