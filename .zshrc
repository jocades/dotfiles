# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Theme
source ~/powerlevel10k/powerlevel10k.zsh-theme

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# Fetch system
#neofetch

# PATH variables
export TERM='xterm-256color'
export EDITOR='nvim'
export VISUAL='nvim'
export BROWSER='brave'
export ANDROID_HOME=/home/j0rdi/Android/Sdk
export HISTCONTROL=ignoreboth:erasedups

# format `time` command
export TIMEFMT=$'%J\n%U user\n%s system\n%P cpu\n%*E total'

# Keep N lines of history within the shell and save it to ~/.zsh_history:
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.zsh_history

# Use modern completion system
autoload -Uz compinit
compinit

# auto CD
setopt autocd
bindkey -e

zstyle ':completion:*' auto-description 'specify: %d'
zstyle ':completion:*' completer _expand _complete _correct _approximate
zstyle ':completion:*' format 'Completing %d'
zstyle ':completion:*' group-name ''
zstyle ':completion:*' menu select=2
eval "$(dircolors -b)"
zstyle ':completion:*:default' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*' list-colors ''
zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
zstyle ':completion:*' matcher-list '' 'm:{a-z}={A-Z}' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=* l:|=*'
zstyle ':completion:*' menu select=long
zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
zstyle ':completion:*' use-compctl false
zstyle ':completion:*' verbose true

zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#)*=0=01;31'
zstyle ':completion:*:kill:*' command 'ps -u $USER -o pid,%cpu,tty,cputime,cmd'

# ----Manual configuration---- #

PATH=/snap/bin:/usr/sandbox/:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/usr/share/games:/usr/local/sbin:/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/home/j0rdi/.local/bin:/home/j0rdi/.local/scripts:$ANDROID_HOME/platform-tools:/home/j0rdi/.deno/bin


# ---- ALIASES ---- #

# ls and cat 
alias ll='lsd -lh --group-dirs=first'
alias la='lsd -a --group-dirs=first'
alias l='lsd --group-dirs=first'
alias lla='lsd -lha --group-dirs=first'
alias ls='lsd --group-dirs=first'
alias cat='bat'
alias cl='clear'

# File explorer
alias e='ranger'

# Python
alias py="python"
alias pm="python manage.py"
alias bpy='bpython'

# Open img in terminal
alias icat="kitty +kitten icat"

# Railway
alias rw='/usr/bin/railway'

# Neovim
alias v='nvim'
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# Git
alias g='git'
alias glog='git log --oneline'
alias gstat='git status --short'
alias gch='git checkout'
alias gb='git branch'
alias gp='git push'
alias gf='git fetch'
alias gl='git pull'

function gcom() {
  git add .
  git commit -m "$1"
}

function gcomp() {
  git add .
  git commit -m "$1"
  git push
}

# Tmux
alias t='tmux'

function ts() {
  tmux new -s "$1"
}

function ta() {
  tmux a -t "$1"
}

function ide() {
  tmux split-window -v -p 25
  tmux split-window -h -p 66
  tmux split-window -h -p 50
}

function pide() {
  tmux split-window -v -p 25
  tmux split-window -h
}

# Docker
alias d='docker'
alias dco='docker-compose'

# NPM
alias nr='npm run'

# Set keyboard layout
alias qwerty-gb="sudo localectl set-x11-keymap gb"
alias qwerty-us="sudo localectl set-x11-keymap us"

# which graphical card is working
alias whichvga="/usr/local/bin/arcolinux-which-vga"

# add new fonts
alias fontcache='sudo fc-cache -fv'

#copy shell configs
alias cpcommands='cp /etc/skel/.zshrc ~/.zshrc && echo "Copied."'

#hardware info --short
alias hw="hwinfo --short"

# -- Aliases for software managment
# pacman
alias update='sudo pacman -Syyu'

# paru as aur helper - updates everything
alias updateall="paru -Syu"

#get fastest mirrors in your neighborhood
alias getmirrors="sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist"

#Recent Installed Packages
alias rip="expac --timefmt='%Y-%m-%d %T' '%l\t%n %v' | sort | tail -200 | nl"

#Cleanup orphaned packages
alias cleanup='sudo pacman -Rns $(pacman -Qtdq)'

# FIX DB & KEYS!
alias fixkeys="/usr/local/bin/arcolinux-fix-pacman-databases-and-keys"

#systeminfo
alias probe="sudo -E hw-probe -all -upload"
alias sysfailed="systemctl list-units --failed"

#shutdown or reboot
alias ssn="sudo shutdown now"
alias sr="sudo reboot"

# -- EDIT IMPORTANT CONFIG FILES -- #
# know what you do in these files
alias npacman="sudo $EDITOR /etc/pacman.conf"
alias ngrub="sudo $EDITOR /etc/default/grub"
alias nconfgrub="sudo $EDITOR /boot/grub/grub.cfg"
alias nlxdm="sudo $EDITOR /etc/lxdm/lxdm.conf"
alias nlightdm="sudo $EDITOR /etc/lightdm/lightdm.conf"
alias nmkinitcpio="sudo $EDITOR /etc/mkinitcpio.conf"
alias nmirrorlist="sudo $EDITOR /etc/pacman.d/mirrorlist"
alias narcomirrorlist='sudo nano /etc/pacman.d/arcolinux-mirrorlist'
alias nsddm="sudo $EDITOR /etc/sddm.conf"
alias nsddmk="sudo $EDITOR /etc/sddm.conf.d/kde_settings.conf"
alias nfstab="sudo $EDITOR /etc/fstab"
alias nnsswitch="sudo $EDITOR /etc/nsswitch.conf"
alias nsamba="sudo $EDITOR /etc/samba/smb.conf"
alias ngnupgconf="sudo nano /etc/pacman.d/gnupg/gpg.conf"
alias nhosts="sudo $EDITOR /etc/hosts"

# FIX KEYS
	# Fix 'end', 'home', 'del' keys
bindkey "^[[H" beginning-of-line
bindkey "^[[F" end-of-line
bindkey "^[[3~" delete-char
	# skip word = alt + {arrowKeys}
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word

# ---- Plugins ---- #
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh-sudo/sudo.plugin.zsh

# Z history
[[ -r "/usr/share/z/z.sh" ]] && source /usr/share/z/z.sh

# Fzf:
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

# --- Functions ---- #
# Beautify 'man' colors
function man() {
    env \
    LESS_TERMCAP_mb=$'\e[01;31m' \
    LESS_TERMCAP_md=$'\e[01;31m' \
    LESS_TERMCAP_me=$'\e[0m' \
    LESS_TERMCAP_se=$'\e[0m' \
    LESS_TERMCAP_so=$'\e[01;44;33m' \
    LESS_TERMCAP_ue=$'\e[0m' \
    LESS_TERMCAP_us=$'\e[01;32m' \
    man "$@"
}

# fzf improvement
function fzf-lovely(){

	if [ "$1" = "h" ]; then
		fzf -m --reverse --preview-window down:20 --preview '[[ $(file --mime {}) =~ binary ]] &&
 	                echo {} is a binary file ||
	                 (bat --style=numbers --color=always {} ||
	                  highlight -O ansi -l {} ||
	                  coderay {} ||
	                  rougify {} ||
	                  cat {}) 2> /dev/null | head -500'

	else
	        fzf -m --preview '[[ $(file --mime {}) =~ binary ]] &&
	                         echo {} is a binary file ||
	                         (bat --style=numbers --color=always {} ||
	                          highlight -O ansi -l {} ||
	                          coderay {} ||
	                          rougify {} ||
	                          cat {}) 2> /dev/null | head -500'
	fi
}

