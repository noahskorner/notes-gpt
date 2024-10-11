# NotesGPT

## Prerequisites

- Docker
- Python

## Setup

1. **Clone the repository:**

    ```sh
    git clone noahskorner/notes.new
    cd notes.new
    ```

2. **Set up the virtual environment:**

    ```sh
    python -m venv venv
    source venv/Scripts/activate  # On Windows
    source venv/bin/activate    # On Unix or MacOS
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Start the Docker containers:**

    ```sh
    ./dev.sh
    ```

    This script will:
    - Start the Docker containers defined in [docker-compose.yml](./docker-compose.yml).
    - Execute the ollama container and pull the `llama3.2` model.

## Usage

1. **Embed Documents:**

    To embed documents from a specified folder into the Chroma database, run the following command:

    ```sh
    python embed.py PATH_TO_FOLDER
    ```

    Replace `PATH_TO_FOLDER` with the path to the folder containing your markdown files. This script will read all `.md` files in the folder and embed their contents into the Chroma database.

2. **Prompt the LLM:**

    To interact with the LLM using your embedded documents, run the following command:

    ```sh
    python prompt.py
    ```

    This will start a prompt where you can enter your queries. The LLM will analyze and reference your notes to provide comprehensive and accurate responses.

