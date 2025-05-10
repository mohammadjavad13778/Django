# Use the official Node.js version 18 image
FROM docker.arvancloud.ir/node:18-alpine

# Set working directory
WORKDIR /usr/src/app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the project files
COPY . .

# Open port 3000
EXPOSE 3000

# Command to run the program
CMD ["npm", "start"]
