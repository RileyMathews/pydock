# pydock
A script that lets you easily mount your working directory into any docker image you wish!

## Explanation
This script works by creating a temporary dockerfile (with a parent image of your choice) that has a directory ready for volume mounting. It then will run that image with your current working directory mounted into it.

## Requiremments
This script was developed using python 3.7.3 installed via asdf and has not been tested with any other versions.

## Setup
1. Clone this repository anywhere on your machine
2. (optional) I recommend creating a bash alias for easier running of this script. For example with this script copied into `~/scripts/pydock/pydock.py`. Add the following alias to your shell of choice.
```
alias pydock="python3 ~/scripts/pydock/pydock.py"
```

## WARNINGS
This script will overwrite, and delete anything named `Dockerfile` living in your working directory. DO NOT run this script from a directory where you already have a working dockerfile.

This script assumes the image you are using has bash installed. If your image uses another command to start the shell prompt. You may pass in the relevant command as an optional second argument


## Use
Once the script is installed on your computer. Go to any directory you wish to mount into an arbitrary docker image and run the following command.
```
pydock node:latest
```
After building a very simple image, you should find yourself sitting in the shell of the node image with whatever directory you were in mounted as a volume.

For images that use another type of shell command you can pass in the command as an optional second argument.
```
pydock alpine sh
```

## Example
Lets say you want to start a new rails project, but don't have ruby or rails installed locally as you develop in docker. One solution may be that you create a temporary dockerfile pulling from ruby's latest image. Build that image. Run it while mounting your directory as a volume. Run rails new. Leave the container. Delete your temporary docker file. Create a new dockerfile that actually interacts with and runs your rails project. And now you are ready to start development. Well, this script won't automate all of that for you, but it makes the startup much simpler.

(This guide assumes you have setup an alias for running the script named `pydock`)
1. Move to any empty directory on your computer
```
mkdir pydock-test && cd pydock-test
```

2. Run pydock while passing it the rails image as an argument.
```
pydock rails:latest
```

3. If you do not have the latest rails image, docker may spend some time pulling this image before building your dockerfile.
4. You should now find yourself inside the container. You may now create your rails project by running
```
rails new .
```
5. A rails project should now be created inside your directory.
6. Leave your container by running.
```
exit
```
7. You should now be back into your hosts machine shell. If you `ls` in the directory you should see all of the boilerplate code for your rails project. You may now continue making your production/development dockerfiles based on this boilerplate code!
