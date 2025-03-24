# Model Context Protocol Server

A FastAPI-based implementation of a Model Context Protocol (MCP) server that handles model context management, session handling, and protocol operations.

## Features

- FastAPI-based REST API server
- Model context management
- Session handling and persistence
- WebSocket support for real-time updates
- Authentication and authorization
- Request validation and error handling
- Swagger/OpenAPI documentation
- Docker support

## Project Structure

```
mcp-protocol-server/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── context.py
│   │   ├── session.py
│   │   └── protocol.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   ├── context.py
│   │   │   └── session.py
│   │   └── dependencies.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── context.py
│   │   └── session.py
│   └── utils/
│       ├── __init__.py
│       └── security.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_context.py
│   └── test_session.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tian1ll1/mcp-protocol-server.git
cd mcp-protocol-server
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy the example environment file and configure your settings:
```bash
cp .env.example .env
```

## Running the Server

### Development Mode

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Using Docker

```bash
docker-compose up -d
```

## API Documentation

Once the server is running, you can access the API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Testing

Run the test suite:

```bash
pytest
```

## Configuration

The server can be configured using environment variables or a `.env` file. See `.env.example` for available options.

## License

This project is licensed under the MIT License - see the LICENSE file for details.