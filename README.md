# TeleSync

An application to store your local files on Telegram.

> 📸 Watch the video on [YouTube](https://youtu.be/vCAcc_q-NNw)

## Features

- Infinite storage (No limit)
- Easy to use
- Fast and secure
- Free & Open Source

## Prerequisites

You need a Telegram API ID and API Hash.
You can create a new App [here](https://my.telegram.org/apps).

## Installation

```bash
git clone https://github.com/FujiwaraChoki/TeleSync.git
cd TeleSync
```
**Before installing dependencies you  have  to create virtual environment(mandatory)**

## linux 

```bash 
python -m venv venv
source venv/bin/activate
```
## windows 

```bash
python -m venv venv
.\venv\Scripts\activate
```

Then, continue with the installation:

```bash 
pip install -r requirements.txt
# Copy the example.config.json to config.json
cp example.config.json config.json # Edit the config.json file with your own settings
```
 **Give run.sh execution permission**
`chmod +x run.sh` ( for linux only )

## Configuration

| Option         | Description                                                                |
| -------------- | -------------------------------------------------------------------------- |
| `api_id`       | Your Telegram API ID.                                                      |
| `api_hash`     | Your Telegram API Hash.                                                    |
| `phone_number` | Your phone number, which you use for Telegram.                             |
| `db_file`      | The name of the database file. (Default: `files.db`)                       |
| `verbose`      | If `true`, the application will print more information. (Default: `false`) |


### Commands

| Command                 | Description                            |
| ----------------------- | -------------------------------------- |
| `upload [FILE_QUERY]`   | Upload a file to Telegram              |
| `download [FILE_QUERY]` | Download a file from Telegram          |
| `remove [FILE_QUERY]`   | Delete a file from Telegram            |
| `list`                  | List all files in the Telegram Channel |

`FILE_QUERY` can be the file name, file path, the ID of the file, or a part of the file name.

## Adding Script to PATH

### Linux

To add the script to the PATH in Linux, you can modify the `~/.bashrc` file:

```bash
export PATH="$PATH:/path/to/TeleSync"
```
### Windows

To add the script to the PATH in Windows, you can follow these steps:

1. Search for "Environment Variables" in the Start menu.
2. Click on "Edit the system environment variables".
3. In the System Properties window, click on the "Environment Variables..." button.
4. In the Environment Variables window, under System variables, find the Path variable and select it.
5. Click on the "Edit..." button.
6. Click on the "New" button and add the path to the TeleSync directory.
7. Click "OK" on all windows to apply the changes.


## Running

### Linux

To run TeleSync on Linux, navigate to the TeleSync directory in your terminal and execute the following command:

```bash
./run.sh [COMMAND] [ARGUMENTS]
```
or if you added to path then you can run from anywhere 

```bash
run.sh [COMMAND] [ARGUMENTS]
```

### Windows

To run TeleSync on Windows, open Command Prompt, navigate to the TeleSync directory, and execute the following command:

```bash
.\run.bat [COMMAND] [ARGUMENTS]
```
or if you have added to path you run from anywhere 
```bash
run.bat [COMMAND] [ARGUMENTS]
```


## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Issues

If you found a **bug**, please to open an [issue](https://github.com/FujiwaraChoki/TeleSync/issues). Issues that are not related to bugs will be closed.

## Contributing

> Only Pull Requests with fixes or/and improvements will be accepted.