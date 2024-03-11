# 🚀 Gdrive CLI

## How to Use

1. **Download** the "gdrive-executable" zip from [GitHub Releases](https://github.com/rishabh-j-23/gdrive-cli/releases) and **extract** it.

2. **Run** `gdrive.exe` once.

3. **Navigate** to `C:/Users/{User}/.gdrive-cli/` folder and **add** `credentials.json` file.
   
   Follow the instructions outlined in [this guide](https://github.com/glotlabs/gdrive/blob/main/docs/create_google_api_credentials.md) to **create** and **obtain** the `credentials.json` file.

4. After adding `credentials.json`, **navigate** to the folder containing `gdrive.exe`.
   
   - (Optional) you may **add** it to the env

5. **Open** a terminal or command prompt in this folder.

6. **Type** `.\gdrive login` to connect the CLI to your Google account.

## Commands and Features

### Commands:

- `login`:  
  - **Description:** Log in to gdrive-cli through a Google account.
  - **Arguments:** None
  
- `logout`:  
  - **Description:** Log out of gdrive-cli.
  - **Arguments:** None

- `list`:  
  - **Description:** List files from Google Drive.
  - **Arguments:**
    - `-ps PAGESIZE, --pagesize PAGESIZE`: Specify the number of files per page.
    - `-S SHOW_TYPE, --show-type SHOW_TYPE`: Show files of a specific mimetype. You can use "gdrive mimetype" to see all supported mimetypes.

- `upload`:  
  - **Description:** Upload a file to Google Drive.
  - **Arguments:**
    - `-p PATH, --path PATH`: Specify the path of the file to upload.
    - `-n NAME, --name NAME`: Specify the name of the file to upload.
    - `--parentid PARENTID`: Specify the ID of the parent folder in Google Drive where the file will be uploaded.

- `delete`:  
  - **Description:** Delete a file from Google Drive.
  - **Arguments:**
    - `-id ID, --id ID`: Specify the ID of the file to delete.

- `download`:  
  - **Description:** Download a file from Google Drive.
  - **Arguments:**
    - `-id ID, --id ID`: Specify the ID of the file to download.
    - `-d DESTINATION, --destination DESTINATION`: Specify the destination where the downloaded file will be saved.
    - `-n NAME, --name NAME`: Save the file with a specific name (provide the proper extension, e.g., `example.zip`, `example.txt`, etc.).

- `export`:  
  - **Description:** Export a file from Google Drive.
  - **Arguments:**
    - `-id ID, --id ID`: Specify the ID of the file to export.
    - `-d DESTINATION, --destination DESTINATION`: Specify the destination where the exported file will be saved.
    - `-n NAME, --name NAME`: Save the file with a specific name (provide the proper extension, e.g., `example.zip`, `example.txt`, etc.).

- `mimetypes`:  
  - **Description:** List mimetypes supported by Google Drive.
  - **Arguments:**
    - `-q QUERY, --query QUERY`: Search for a specific mimetype by providing a query.

- `me`:  
  - **Description:** View user details.
  - **Arguments:** None

- `storage`:  
  - **Description:** List storage available in Google Drive.
  - **Arguments:** None

### Additional Features:

- **Automatic Login**: Once `gdrive.exe` is run, users can seamlessly connect to their Google account by typing `.\gdrive login`.
  - **Arguments:** None

- **Customization**: Users can add `gdrive.exe` to their environment variables for easier access.
  - **Arguments:** None

## 🌟 Enjoy managing your Google Drive effortlessly with Gdrive CLI!
