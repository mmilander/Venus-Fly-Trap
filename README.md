# Venus-Fly-Trap
## Project summary

### One-sentence description of the project
TODO: A 20-second elevator pitch of your project - its core idea summarized in one
sentence.
### Additional information about the project
TODO: Write a compelling/creative/informative project description / summary
## Installation
### Prerequisites
- Docker Desktop with Docker Compose
- Python 3.10 or newer
- Available ports 5678 and 8000
### Add-ons
- **n8n:** Runs the workflow that retrieves webpage content and generates structured output.
- **Docker Compose:** Configures and runs n8n locally.
- **Python HTTP Server:** Hosts the test webpage on port 8000.
- **Python harness:** Sends requests to n8n, collects output, and records results in CSV.
### Installation Steps
1. Clone the GitHub repo
2. Start n8n through Docker
    ```
    docker compose up -d
    ```
3. Open ```http://localhost:5678``` and create a local n8n account if prompted.
4. Import ```workflows/venus-fly-trap-workflow.json``` into n8n.
5. Save and publish the imported workflow to enable its production webhook.
6. Open a seperate terminal in the repo's root and start the local test webpage:
    ```
    python -m http.server 8000 --directory website
    ```
7. Open another terminal in the repo's root and run:
    ```
    python scripts/run_harness.py
    ```
8. View the generated file at *results/results.csv*
9. To stop n8n:
    ```
    docker compose down
    ```
## Functionality
TODO: Write usage instructions. Structuring it as a walkthrough can help structure
this section,
and showcase your features.
## Known Problems
TODO: Describe any known issues, bugs, odd behaviors or code smells.
Provide steps to reproduce the problem and/or name a file or a function where the
problem lives.

## Additional Documentation
* [D1 Assignment](https://github.com/mmilander/Venus-Fly-Trap/blob/main/Documents/D1-Team%2C%20Track%2C%20Target%2C%20and%20Scope.pdf)
## License
* [MIT](https://github.com/mmilander/Venus-Fly-Trap/blob/main/LICENSE.txt)
