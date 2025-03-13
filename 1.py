import streamlit as st
from datetime import datetime
import json

class ConfigurationManagementTool:
    def __init__(self):
        self.configurations = {}
        self.change_history = []

    def create_configuration(self, config_id, config_data):
        if config_id in self.configurations:
            st.error(f"Configuration ID {config_id} already exists.")
            return
        try:
            json.loads(config_data)  # Validate JSON
            self.configurations[config_id] = config_data
            self.track_change_history(f"Configuration created: {config_id}")
            st.success(f"Configuration {config_id} created successfully.")
        except json.JSONDecodeError:
            st.error("Invalid JSON format.")

    def read_configuration(self, config_id):
        config = self.configurations.get(config_id, None)
        if config:
            self.track_change_history(f"Configuration read: {config_id}")
            return config
        else:
            st.error(f"Configuration ID {config_id} not found.")
            return None

    def update_configuration(self, config_id, new_config_data):
        if config_id not in self.configurations:
            st.error(f"Configuration ID {config_id} not found.")
            return
        try:
            json.loads(new_config_data)  # Validate JSON
            self.configurations[config_id] = new_config_data
            self.track_change_history(f"Configuration updated: {config_id}")
            st.success(f"Configuration {config_id} updated successfully.")
        except json.JSONDecodeError:
            st.error("Invalid JSON format.")

    def delete_configuration(self, config_id):
        if config_id in self.configurations:
            del self.configurations[config_id]
            self.track_change_history(f"Configuration deleted: {config_id}")
            st.success(f"Configuration {config_id} deleted successfully.")
        else:
            st.error(f"Configuration ID {config_id} not found.")

    def deploy_configuration_changes(self, config_id):
        if config_id in self.configurations:
            self.track_change_history(f"Configuration changes deployed: {config_id}")
            st.success(f"Configuration {config_id} changes deployed successfully.")
        else:
            st.error(f"Configuration ID {config_id} not found.")

    def rollback_configuration(self, config_id, previous_config_data):
        if config_id in self.configurations:
            self.configurations[config_id] = previous_config_data
            self.track_change_history(f"Configuration rolled back: {config_id}")
            st.success(f"Configuration {config_id} rolled back successfully.")
        else:
            st.error(f"Configuration ID {config_id} not found.")

    def track_change_history(self, history_details):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.change_history.append(f"[{current_time}] {history_details}")
        with open("changes_config.log", "a") as log_file:
            log_file.write(f"[{current_time}] {history_details}\n")

def main():
    st.title("Configuration Management Tool")
    cm_tool = ConfigurationManagementTool()

    menu = ["Create Configuration", "Read Configuration", "Update Configuration", 
            "Delete Configuration", "Deploy Configuration Changes", "Rollback Configuration", "View Change History"]
    choice = st.sidebar.selectbox("Select Operation", menu)

    if choice == "Create Configuration":
        st.subheader("Create a New Configuration")
        config_id = st.text_input("Enter Configuration ID")
        config_data = st.text_area("Enter Configuration Data (in JSON format)")
        if st.button("Create"):
            if config_id and config_data:
                cm_tool.create_configuration(config_id, config_data)
            else:
                st.error("Configuration ID and Data are required.")

    elif choice == "Read Configuration":
        st.subheader("Read a Configuration")
        config_id = st.text_input("Enter Configuration ID")
        if st.button("Read"):
            if config_id:
                config = cm_tool.read_configuration(config_id)
                if config:
                    st.json(config)
            else:
                st.error("Configuration ID is required.")

    elif choice == "Update Configuration":
        st.subheader("Update a Configuration")
        config_id = st.text_input("Enter Configuration ID")
        new_config_data = st.text_area("Enter New Configuration Data (in JSON format)")
        if st.button("Update"):
            if config_id and new_config_data:
                cm_tool.update_configuration(config_id, new_config_data)
            else:
                st.error("Configuration ID and New Data are required.")

    elif choice == "Delete Configuration":
        st.subheader("Delete a Configuration")
        config_id = st.text_input("Enter Configuration ID")
        if st.button("Delete"):
            if config_id:
                cm_tool.delete_configuration(config_id)
            else:
                st.error("Configuration ID is required.")

    elif choice == "Deploy Configuration Changes":
        st.subheader("Deploy Configuration Changes")
        config_id = st.text_input("Enter Configuration ID")
        if st.button("Deploy"):
            if config_id:
                cm_tool.deploy_configuration_changes(config_id)
            else:
                st.error("Configuration ID is required.")

    elif choice == "Rollback Configuration":
        st.subheader("Rollback a Configuration")
        config_id = st.text_input("Enter Configuration ID")
        previous_config_data = st.text_area("Enter Previous Configuration Data (in JSON format)")
        if st.button("Rollback"):
            if config_id and previous_config_data:
                cm_tool.rollback_configuration(config_id, previous_config_data)
            else:
                st.error("Configuration ID and Previous Data are required.")

    elif choice == "View Change History":
        st.subheader("Configuration Change History")
        if cm_tool.change_history:
            for entry in cm_tool.change_history:
                st.write(entry)
        else:
            st.info("No change history available.")

if __name__ == "__main__":
    main()