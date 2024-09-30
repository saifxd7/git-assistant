
# GIT-ASSISTANT

**GIT-ASSISTANT** is a command-line tool designed to help you generate meaningful commit messages using the Groq API. It simplifies the process of creating well-structured commit messages, making it easier for teams to maintain consistency across projects.

## Prerequisites

Ensure that you have the following installed before using the tool:

- Python 3.8 or later
- Git
- Poetry (for dependency management)

## Installation

### Step 1: Clone the Repository

Clone the repository to your local machine using the following commands:

```bash
git clone https://github.com/saifxd7/git-assistant.git
cd git-assistant
```

### Step 2: Run the Setup Script

Run the provided setup script to install dependencies and configure your environment:

```bash
./setup.sh
```

The setup script will:

- Install Poetry if not already installed
- Install the required dependencies
- Prompt you to enter your GROQ API key and save it to a `.env` file

### Step 3: Verify Installation

After running the setup script, you should see a confirmation message. The CLI tool is now ready to use.

## Usage

### Generating a Commit Message

To generate a commit message using the Groq API, run the following command:

```bash
git-assistant commit --use-groq
```

### Command Options

- `--use-groq`: Use the Groq API for generating the commit message.
- `--model-name`: (Optional) Specify the model name to use (default is `llama-3.1-8b-instant`).

## Troubleshooting

### Common Issues

- **API Key Not Set**: If you receive an error stating that the `GROQ_API_KEY` is not set, ensure that you entered the correct API key during the setup process.
- **Dependency Installation**: If you experience issues with dependency installation, verify that Poetry is installed correctly and that your environment is properly configured.

### Logs

Logs are stored in the `logs/` directory. If you encounter any issues, check the logs for more details.

## Contributing

Contributions are welcome! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes.
4. Commit your changes:
   ```bash
   git commit -am 'Add some feature'
   ```
5. Push the branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
6. Create a pull request on the main repository.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
