# Use the base Python 3.10 image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the project dependencies to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project source code to the container
COPY . .

# Set the command to run when the container starts
CMD [ "python", "bot.py" ]