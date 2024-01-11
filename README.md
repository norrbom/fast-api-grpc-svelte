# FastAPI gRPC Svelte example

## Prerequisites

pipx and poetry, Ubuntu users gets the option to let make install them for you when you start the server.

## Start the server

```sh
make run
```

The run target performs the following:

- installs and updates the python packages required using poetry
- generates python code from .proto files
- starts the gRPC server
