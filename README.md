

# Server Configuration Management Tool

A simple web-based tool built with Streamlit to manage application or server configurations. It provides a user-friendly interface for performing CRUD (Create, Read, Update, Delete) operations on configuration data, along with features for deployment simulation, rollback, and change tracking.

-----

## 📋 Overview

This tool is designed to provide a centralized and straightforward way to handle configuration files. Instead of manually editing JSON files on a server, you can use this interface to manage them. All actions are logged, providing a clear history of every change, deployment, or rollback.

-----

## ✨ Features

  * **Create Configuration**: Add new configurations with a unique ID and JSON data.
  * **Read Configuration**: View the data of an existing configuration by its ID.
  * **Update Configuration**: Modify the data of an existing configuration.
  * **Delete Configuration**: Remove a configuration from the system.
  * **Deploy Changes**: Simulate the deployment of a specific configuration to a target environment.
  * **Rollback Configuration**: Revert a configuration to a previous state by providing the old data.
  * **Change History**: View a timestamped log of all activities performed through the tool.
  * **Persistent Logging**: All change history is automatically saved to a `changes_config.log` file.

-----

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

You need to have Python 3.8 or newer installed on your system. You can check your Python version with:

```bash
python --version
```

### Installation & Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/server-configuration-management.git
    cd server-configuration-management
    ```

2.  **Create a `requirements.txt` file** with the following content:

    ```
    streamlit
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    Save your Python code as `app.py` (or any other name) and run the following command in your terminal:

    ```bash
    streamlit run app.py
    ```

    Your web browser should automatically open with the application running.

-----

## 💻 How to Use

The application interface is straightforward. Use the sidebar on the left to navigate between different operations.

1.  **Select Operation**: Choose an action from the sidebar menu (e.g., "Create Configuration", "Read Configuration").

2.  **Create Configuration**:

      * Enter a unique **Configuration ID**.
      * Enter the configuration data in the text area, ensuring it's valid **JSON format**.
      * Example JSON: `{"database": "mysql", "port": 3306, "user": "admin"}`
      * Click the "Create" button.

3.  **Read, Update, Delete, or Deploy**:

      * Select the desired operation.
      * Enter the **Configuration ID** of the configuration you want to manage.
      * For updates, provide the new JSON data.
      * Click the corresponding button (e.g., "Read", "Update").

4.  **Rollback Configuration**:

      * Enter the **Configuration ID**.
      * Paste the **previous configuration data** (the state you want to revert to) into the text area.
      * Click the "Rollback" button.

5.  **View Change History**:

      * This section displays the in-memory log of all actions taken during the current session.
      * A persistent log is also saved in the `changes_config.log` file in the project directory.

-----

## ⚠️ Important Notes & Limitations

  * **In-Memory Storage**: The configurations themselves are stored **in-memory**. This means all created and updated configurations will be **lost** when the Streamlit application is stopped or reloaded. Only the change history is persisted to a file.
  * **Simulated Actions**: The "Deploy" and "Rollback" features are currently **simulations**. They log the action to the history but do not perform actual deployment to a server or automatically fetch a previous version. The rollback requires manual input of the previous data.

-----

## 🔧 Future Improvements

  * **Persistent Storage**: Integrate a database (like SQLite, MongoDB) or a file-based system to persistently store configurations.
  * **Automatic Versioning**: Store a history of changes for each configuration to enable one-click rollbacks to any previous version.
  * **Real Deployment Logic**: Implement SSH or API calls to actual servers (e.g., using libraries like `paramiko` or `fabric`) to make the "Deploy" feature functional.
  * **User Authentication**: Add a login system to control access.

-----

## 📜 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
