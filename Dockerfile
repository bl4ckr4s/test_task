FROM python:3.12-slim

# Utilities
RUN apt-get update \
    && apt-get install -y --no-install-recommends default-jre-headless wget unzip \
    && rm -rf /var/lib/apt/lists/*

# Allure CLI
RUN wget -qO /tmp/allure.zip https://github.com/allure-framework/allure2/releases/download/2.22.1/allure-2.22.1.zip \
    && unzip /tmp/allure.zip -d /opt/ \
    && ln -s /opt/allure-2.22.1/bin/allure /usr/bin/allure \
    && rm /tmp/allure.zip

WORKDIR /app

# Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Code
COPY . /app

# Open port 8080
EXPOSE 8080

# Run: pytest + allure serve in localhost
CMD ["bash", "-lc", "pytest --alluredir=allure-results && allure serve allure-results --port 8080 "]


