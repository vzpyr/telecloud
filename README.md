# telecloud
telecloud is a simple app which allows you to save unlimited files on telegram's cloud storage

# features
- uploading, downloading, removing and listing files
- infinite storage
- free & open-source
- easy to setup

# forked ?
telecloud was forked by [telesync](https://github.com/FujiwaraChoki/TeleSync), make sure to check out his project too.
i wanted to add an account system to this, so i could host a public instance ([keqing.cloud](https://keqing.cloud/)) and everyone had access to free storage.
telecloud is currently only a backend which can be used for other things.

# requirements
- api id and hash from [here](https://my.telegram.org/apps)
- python3 and the required modules

# config
| entry          | description                                                              |
| -------------- | ------------------------------------------------------------------------ |
| `api_id`       | your telegram api id                                                     |
| `api_hash`     | your telegram api hash                                                   |
| `phone_number` | your telegram phone number                                               |
| `db_file`      | any name for the database `files.db`)                                    |
| `verbose`      | set to `true` if you want telecloud to log everything, otherwise `false` |

# commands
| command                        | description                                  |
| ------------------------------ | -------------------------------------------- |
| `register`                     | create a local telecloud account             |
| `viewtoken <user> <pass>`      | view your token if you didn't save it        |
| `<token> upload [FILE_NAME]`   | upload a file to telegram & your account     |
| `<token> download [FILE_NAME]` | download a file from telegram & your account |
| `<token> remove [FILE_NAME]`   | remove a file from telegram & your account   |
| `<token> list`                 | list all files in your account               |

# how to setup
1. clone this repo
2. open the folder and run ```pip install -r requirements.txt```
3. fill in everything in ```example.json``` and rename the file to ```config.json```
4. run ```python3 run.py register``` and create a local telecloud account, securely save your token somewhere
5. then you can use ```python3 run.py <token> <command>``` to run commands

# problems
if you have a problem with telecloud, open an [issue](https://github.com/v1peeer/telecloud/issues)
