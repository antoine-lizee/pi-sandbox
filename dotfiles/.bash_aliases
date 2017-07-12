alias ll='ls -l'

alias sshpm='ssh pi@pi-main.local'
alias sshpzr='ssh pi@pi-zero-redbear.local'

alias act='source ./env/bin/activate'
alias create_env='python3 -m venv env --without-pip; act; curl https://bootstrap.pypa.io/get-pip.py | python;'
