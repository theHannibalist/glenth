# Attention :
glenth is a project I loved so much , but it clearly it has no clear code in it ! it's just shell script run by python in a messed up way ! <br>
I have entirely rewritten this little guy for a better performance and quality. check it out : https://github.com/theHannibalist/glenth2



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
## Installing systemwide :

You can install `glenth` systemwide , and it's easy!

```bash
sudo ln -s PATH_TO_GLENTH/main.py /usr/bin/glenth ; sudo chmod +x /usr/bin/glenth
```
###
Have fun!
Let me know if you have any problems.
