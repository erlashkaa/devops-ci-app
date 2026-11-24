# DevOps CI application

Flask service for Practical Work 10. The GitHub Actions pipeline checks the
source code, runs tests, builds and verifies a Docker image, and publishes the
reviewed image to GitHub Container Registry after changes reach `main`.

## Endpoints

- `GET /` - service information.
- `GET /health` - health status.

