
import os
from google.genai import types
from google import genai
from .CMDTOOL.createfolder import CREATE_FOLDER_TOOL
from .CMDTOOL.createfile import CREATE_FILE_TOOL
from .CMDTOOL.deletePath import DELETE_PATH_TOOL
from .CMDTOOL.appendTOfile import APPPEND_TO_FILE_TOOL
from .CMDTOOL.executeCommand import EXECUTE_COMMAND_TOOL


def make_client(api_key: str = None):
    api_key = api_key or os.getenv("PO_GENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Set PO_GENAI_API_KEY env var or pass api_key")
    return genai.Client(api_key=api_key)

sys_ins = os.getenv("SYSTEM_INSTRUCTION") # from .env file
create_file_tool = CREATE_FILE_TOOL()
create_folder_tool = CREATE_FOLDER_TOOL()
delete_path_tool = DELETE_PATH_TOOL()
append_to_file_tool = APPPEND_TO_FILE_TOOL()
execute_command_tool = EXECUTE_COMMAND_TOOL()

def create_folder(folder_name: str) -> dict:
    """
    Creates a new folder in the current working directory.

    Args:
        folder_name: The name of the folder to create. Can include subdirectories.

    Returns:
        A dictionary containing a confirmation message with the folder path.
    """
    return create_folder_tool.create_folder(folder_name)


def create_file(file_path: str, content: str = "") -> dict:
    """
    Creates a file with optional content. Also creates parent folders if needed.

    Args:
        file_path: Relative path to the file including filename (e.g., 'dir/notes.txt').
        content: The content to write into the file. If omitted, creates an empty file.

    Returns:
        A dictionary containing a confirmation message with the file path.
    """    
    return create_file_tool.create_file(file_path, content)


def execute_command(command: str) -> dict:
    """
    Executes a shell command on the system (CMD, PowerShell, or terminal).

    Args:
        command: The shell command string to execute (e.g., 'ls', 'dir', 'python script.py').

    Returns:
        A dictionary containing the command's output and any error messages.
    """
    return execute_command_tool.execute_command(command)


def append_to_file(file_path: str, content: str) -> dict:
    """
    Appends new content to an existing file or creates the file if it does not exist.

    Args:
        file_path: The path to the target file where content should be appended.
        content: The string data to append to the file.

    Returns:
        A dictionary containing the operation's success status and any error messages encountered.
    """
    return append_to_file_tool.append_to_file(file_path, content)


def delete_path(path_str: str) -> dict:
    """
    Deletes a file or folder at the specified path.

    Args:
        path_str: The absolute or relative path to the file or folder to delete.

    Returns:
        A dictionary containing the operation's success status and any error messages encountered.
    """
    return delete_path_tool.delete_path(path_str)

def repl_loop(client=None):
    if client is None:
        client = make_client()
    history = []
    config = types.GenerateContentConfig(
        tools=[create_folder, create_file, execute_command, append_to_file, delete_path],
        system_instruction='''You are an AI agent built by ARYAN, your name is PO. You are an expert Frontend Developer. You can build scalable and roubust frontends. You can manage the device's filesystem, therefore you can also act as a File Manager. If u want to find any location of folder, subfolder or a file then use, "cd C:\\ & dir filename_or_foldername /s /b", this command on cmd to get its actual path.'''+sys_ins
    )
    print("\nPO IS TURNED ON!! 🥵  :  LESGO!!💦\nType 'over n out' to exit!🫡 \n")


    while True:
        try:
            inp = input("\nUSER : ")
        except (EOFError, KeyboardInterrupt):
            print("\nbye")
            break
        if inp.lower() == "over n out":
          print("PO   : HOPE, You are satisfied!! 😘")
          break
        history.append(types.Content(role="user", parts=[types.Part(text=inp)]))
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=history,
            config=config
        )
        history.append(response.candidates[0].content)
        print("PO   :", response.text)
if __name__ == "__main__": # just if locally run krna hai toh keep it either ways pip package wont exectute this line
    repl_loop()# Just for local testing 
