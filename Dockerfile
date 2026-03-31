# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy your requirements file first (if you have one) to cache dependencies
# If you don't have a requirements.txt, you can skip this step
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

# Command to run the bot (replace 'bot.py' with your actual file name)
CMD ["python", "bot.py"]