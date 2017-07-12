alias ll='ls -l'

alias sshpm='ssh pi@pi-main.local'
alias sshpzr='ssh pi@pi-zero-redbear.local'

alias act='source ./env/bin/activate'
alias create_env='python3 -m venv env --without-pip; act; curl https://bootstrap.pypa.io/get-pip.py | python;'
alias ssh_agent='eval `ssh-agent`; ssh-add ~/.ssh/id_rsa'
alias start_j='cd /home/pi/pi-sandbox; act; jupyter notebook --config=jupyter_notebook_config.py'
