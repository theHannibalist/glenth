# Glenth
##### GEt the LENgTH !
I've been a Linux user for a long time, and the problem I always had was that I could not get the total length of videos I had in a folder.
So I decided to make myself a tool to do that for me!
And Here it is.

## Dependencies :

To run `Glenth` you need:
* `ffpmeg`
* `python3`

By default, `python` is installed on every linux distro.

### to install `ffmpeg` :

#### Arch Linux :
```bash
sudo pacman -S ffmpeg
```

#### Fedora :
```bash
sudo dnf install ffmpeg
```

#### Debian :
```bash
sudo apt install ffmpeg
```

***

## Usage:
```bash
./main.py -h # for help 
./main.py -d # choose a directory to scan (default : current directory)
./main.py -t # choose a file type [mpg, mpeg, mov, mp4, mkv, all] (default : all)
```

Have fun!
Let me know if you have any problems.
