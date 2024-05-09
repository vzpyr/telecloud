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

# license
so i don't really know anything about license, and if it's fine to license this fork as bsd-3 instead of gpl-3.0, but if there are any problems, please open an issue

# requirements
- api id and hash from [here](https://my.telegram.org/apps)
- python3 and the required modules

# config
| variable       | description                                                              |
| -------------- | ------------------------------------------------------------------------ |
| `api_id`       | your telegram api id                                                     |
| `api_hash`     | your telegram api hash                                                   |
| `phone_number` | your telegram phone number                                               |
| `db_file`      | any name for the database file                                           |
| `verbose`      | set to `true` if you want telecloud to log everything, otherwise `false` |

# commands
| command                        | description                                  |
| ------------------------------ | -------------------------------------------- |
| `register`                     | create a local telecloud account             |
| `viewtoken <user> <pass>`      | view your token if you didn't save it        |
| `<token> upload <file_name>`   | upload a file to telegram & your account     |
| `<token> download <file_name>` | download a file from telegram & your account |
| `<token> remove <file_name>`   | remove a file from telegram & your account   |
| `<token> list`                 | list all files in your account               |

# how to setup
1. clone this repo
2. open the folder and run ```pip install -r requirements.txt```
3. fill in everything in ```example.json``` and rename the file to ```config.json```
4. run ```python3 run.py register``` and create a local telecloud account, securely save your token somewhere
5. then you can use ```python3 run.py <token> <command>``` to run commands

# problems
if you have a problem with telecloud, open an [issue](https://github.com/v1peeer/telecloud/issues)
