# Setting Environment Variables in VSCode for Jupyter Development

When developing Jupyter Notebooks in VSCode, you may need to set environment variables such as an API key. Here's how you can do it:

1. Open the VSCode terminal: Click on the "Terminal" menu in VSCode and select "New Terminal".

2. Set the environment variable: In the terminal, enter the following command to set the environment variable:

  - For Windows:

  ```shell
  setx OPENAI_API_KEY "your_api_key"
  ```

  - For Mac/Linux:
    
  ```shell
  export OPENAI_API_KEY="your_api_key"
  ```
  Note that you should replace "your_api_key" with your actual API key.

3. Launch Jupyter in VSCode: To launch Jupyter in VSCode, go to the "View" menu and select "Command Palette". In the Command Palette, type "Jupyter: Create New Blank Notebook" and select it. This will launch Jupyter in VSCode.


