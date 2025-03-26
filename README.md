# Install dependencies
pip install -r requirements.txt

# To check API docs
make doc

# Document can be viewed on URL
http://localhost:8001/

# Execute using:
uvicorn app.main:app --reload

# On browser:
http://127.0.0.1:8000/shopping/
http://127.0.0.1:8000/auth/login

# Check elasticsearch data using:
curl -X GET "localhost:9200/items/_search?pretty"

# Create docker image:
docker build -t fastapi-microservice .

# Run container:
docker-compose up --build

# On browser:
http://127.0.0.1:8000/auth/register

