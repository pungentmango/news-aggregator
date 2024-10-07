# Dockerfile for React frontend
FROM node:14
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Install `serve` globally to serve the built app
RUN npm install -g serve

# Serve the app using `serve`
CMD ["serve", "-s", "build"]
EXPOSE 3000
