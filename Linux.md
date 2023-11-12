
## Kali PROMPT in Ubuntu

Open ~/.bashrc file and search for PS1 variable and replace the 1st PS1 variable i.e this
```shell
PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$'
```

with this
```shell
PS1='\[\033[01;32m\]┌──${debian_chroot:+($debian_chroot)}(\[\033[00m\]\u@\h\[\033[01;32m\])-[\[\033[01;34m\]\w\[\033[01;32m\]]\n└─\[\033[00m\]\$'
```

```shell
╭─user@machine ~/some/dir ‹main●› 
╰─$  
```

Install oh-my-zsh
Oh My Zsh is installed by running one of the following commands in your terminal. You can install this via the command-line with either curl or wget.
https://ohmyz.sh/#install 

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```


