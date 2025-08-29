FROM node:18

WORKDIR /app

COPY package*.json ./
RUN npm install

# Copy rest of the source
COPY . .

# Expose port
EXPOSE 3000

# Start React with hot reload
CMD ["npm", "start"]
