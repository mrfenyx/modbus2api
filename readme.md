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

### Limitations

1. Currently only extracts 1 register
2. Multi-register values are not supported (no Hi/Low bytes)
3. GET route name is fixed (/regval)
4. There is no authentication, security, etc.

# Example for using the value

You can use the value through a simple JavaScript call and display it on a website. Here's an example (save it as an HTML file):

```html
<script>
    window.onload = function() {
        fetch('http://<DOCKER_HOST_IP>:<PORT>/regval')
        .then(response => response.json())
        .then(data => {
            document.getElementById('apiValue').innerHTML = data.value;
        })
        .catch(error => console.error('Error:', error));
    };
    </script>
    

<p id="apiValue">Loading...</p>

```

# License

This project is licensed under the MIT License - see the [license.md](/license.md)