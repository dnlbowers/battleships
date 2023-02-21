# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory to /app
WORKDIR /app

# Copy package.json and package-lock.json to /app
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application to /app
COPY . .

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose port 3000
EXPOSE 3000

# Start both Node.js and Python apps
CMD ["bash", "-c", "node index.js & python run.py"]