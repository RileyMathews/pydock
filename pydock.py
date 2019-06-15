import os
import subprocess
import sys

# define exception class
class ArgumentException(Exception):
    """Exception raised when given invalid arguments"""
    pass

if len(sys.argv) < 2: raise ArgumentException("you must call pydock with an image name")

# assign arguments
image = str(sys.argv[1])
if len(sys.argv) == 3:
    command = sys.argv[2]
else:
    command = "bash"

# get working directory
working_directory = os.path.abspath(os.path.curdir)

# write dockerfile
with open(f"{working_directory}/Dockerfile", "w") as f:
    f.write(f'FROM {image}\n')
    f.write('WORKDIR /workspace\n')
    f.write('ENTRYPOINT [""]\n')
    f.write(f'CMD ["{command}"]\n')
    # print(f"Your docker file is \n {f.read()}")

# print out dockerfile
print("\nYour dockerfile is...\n")
print(open(f"{working_directory}/Dockerfile", "r").read())
print("\n\n")

# build the docker image
print("building your docker image!")
subprocess.check_call("docker build -t temp .", shell=True)
print("\n\n")

# remove dockerfile
os.remove(f"{working_directory}/Dockerfile")

# start container
print("Starting your container, happy sailing!\n\n\n")
subprocess.check_call(f"docker run -v {working_directory}:/workspace -it temp", shell=True)