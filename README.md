# RotMGAutostart
Launches Realm of the Mad God (Steam version) using Python. After successful launch script will kill Steam and launcher processes. You can also configure killing steam app. **Why?** This saves a lot of time.

## How to install & Use:
1. Download files `update.png` & `play.png` & `RotMGAutostart.pyw` & `requirements.txt`, then put them in _one_ folder. If you are an advanced user with git intalled you can clone this repo.
2. Make sure [Python](https://www.python.org/) and [pip](https://pip.pypa.io/) installed on your machine.
3. Open console. (Win+R, then `cmd`)
4. Move to the folder with downloaded files and run `pip install -r requirements.txt` command. For example using `cd path/to/the/folder/with/downloaded/files` command (You can copy folder path using file explorer).
5. Run `.pyw` file and have fun!

### To disable killing steam app (if you want to keep steam overlay for example):
1. Open the `RotMGAutostart.pyw` file with any kind or text editor (it can be even a default Windows notepad)
2. Change `KILL_STEAM` value to `False`, this is all thing!

## troubleshooting:
If steam force you to choose an account, you can try disable following setting:

`Steam > Settings > Interface > Ask which account to use each time Steam starts`

_Works fine on Windows 11 with python version 3.12_
