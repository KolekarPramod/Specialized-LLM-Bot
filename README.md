
1. **Install the required Python packages:**

   ```bash
   git clone git@github.com:KolekarPramod/hrChatBot.git
   cd hrChatBot
   pip install -r requirements.txt
   ```

2. **Run the FastAPI application:**

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

### Running the Frontend Locally

If you want to run the frontend locally without Docker, follow these steps:

1. **Navigate to the frontend directory:**

   ```bash
   cd frontend
   ```

2. **Install the required Node packages:**

   ```bash
   npm install
   ```

3. **Start the React application:**

   ```bash
   npm start
   ```

## Contributing

Feel free to submit issues or pull requests to improve this application!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/) - A modern, fast (high-performance), web framework for building APIs with Python 3.6+.
- [React](https://reactjs.org/) - A JavaScript library for building user interfaces.
- [Ollama](https://ollama.com/) - A platform for running large language models.
```

### Notes:
- Make sure to replace `<repository-url>` with the actual URL of your Git repository if you’re using version control.
- Adjust any sections based on additional features or instructions specific to your project.

You can copy and paste this directly into a `README.md` file in your project directory! If you need further modifications or additions, let me know!
