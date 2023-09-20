FROM python:3.11.5

# Path: /app
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .
COPY requirements_dev.txt .

# Install the requirements
RUN pip install -r requirements.txt
RUN pip install -r requirements_dev.txt

# Copy the rest of the files to the working directory
COPY . .
