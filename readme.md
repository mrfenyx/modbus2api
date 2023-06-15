# Modbus2API Docker Image

This project provides a Docker image that runs a Python script as a service. The script reads data from a Modbus host and exposes it as a simple API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need Docker installed on your machine. Visit [Docker's website](https://www.docker.com/products/docker-desktop) to download and install Docker Desktop.

### Building the Docker Image

To build the Docker image, navigate to the directory containing the `Dockerfile` and run the following command:

```bash
docker build -t modbus2api .
```

### Running the Docker Image
To run the Docker image, use the following command:

```bash
docker run -d -p <PORT>:80 -e MODBUS_HOST=<HOST_IP> -e MODBUS_PORT=<HOST_PORT> -e MODBUS_REGISTER=<REGISTER> modbus2api
```

Replace <PORT> with the port on which to publish the endpoint, <HOST_IP>, <HOST_PORT> and <REGISTER> with your Modbus host, port and register, respectively.

### Accessing the API

Once the Docker container is running, you can access the API by sending a GET request to <your-docker-host-ip>:<PORT>/regval.

### License

This project is licensed under the MIT License - see the [license.md](/license.md)