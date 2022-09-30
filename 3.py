#@title **SSH**

! pip install colab_ssh --upgrade &> /dev/null

#@markdown Choose a method (Agro Recommended)
ssh_method = "Ngrok" #@param ["Agro", "Ngrok"]


#@markdown Copy authtoken from https://dashboard.ngrok.com/auth (only for ngrok)
ngrokRegion = "us" #@param ["us", "eu", "ap", "au", "sa", "jp", "in"]

def runAgro():
    from colab_ssh import launch_ssh_cloudflared
    launch_ssh_cloudflared(password=password)

def runNgrok():
    from colab_ssh import launch_ssh
    from IPython.display import clear_output

    import getpass
    ngrokToken = getpass.getpass("Enter the ngrokToken: ")

    launch_ssh(ngrokToken, password, region=ngrokRegion)
    clear_output()

    print("ssh", user, end='@')
    ! curl -s http://localhost:4040/api/tunnels | python3 -c \
            "import sys, json; print(json.load(sys.stdin)['tunnels'][0]['public_url'][6:].replace(':', ' -p '))"

try:
    user = username
    password = password
except NameError:
    print("No user found, using username and password as 'root'")
    user='root'
    password='root'


if ssh_method == "Agro":
    runAgro()
if ssh_method == "Ngrok":
    runNgrok()
