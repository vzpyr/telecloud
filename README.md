# telecloud
free unlimited cloud storage using telegram

# features
- register: create a local telecloud account
- viewtoken <user> <pass>: view your token if you didn't save it
- <token> upload <file_name>: upload a file to telegram & your account
- <token> download <file_name>: download a file from telegram & your account
- <token> remove <file_name>: remove a file from telegram & your account
- <token> list: list all files in your account
this is basically [telesync](https://github.com/FujiwaraChoki/TeleSync) but with an user system.

# how to use
1. install python3
2. install requirements: `pip install -r requirements.txt`
3. edit the config
4. register an account: `python3 run.py register`
5. use `python3 run.py <token> <command>` to run commands

# example config
| variable       | description                                                              |
| -------------- | ------------------------------------------------------------------------ |
| `api_id`       | your telegram api id (from [here](https://my.telegram.org/apps))         |
| `api_hash`     | your telegram api hash (from [here](https://my.telegram.org/apps))       |
| `phone_number` | your telegram phone number                                               |
| `db_file`      | any name for the database file                                           |
| `verbose`      | set to `true` if you want telecloud to log everything, otherwise `false` |
