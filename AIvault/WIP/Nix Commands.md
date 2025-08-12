# Find packages with updates on unstable
```shell
  
  

packages=(

bc isd erdtree baobab btrfs-progs clang curl cpufrequtils duf findutils

ffmpeg glib gsettings-qt git killall libappindicator libnotify openssl

pciutils wget xdg-user-dirs xdg-utils sof-firmware linux-firmware

fastfetch mpv nix-your-shell btop brightnessctl cava cliphist loupe

gnome-system-monitor grim gtk-engine-murrine hypridle imagemagick inxi

jq ijq manix mediainfo networkmanagerapplet nwg-displays nwg-look

pamixer pavucontrol playerctl polkit_gnome rofi-wayland slurp swappy

swaynotificationcenter swww unzip wallust wl-clipboard wlogout xarchiver

yad yt-dlp nix-search-tv claude-code lutris heroic bottles stow

gnome-font-viewer fx yq-go figlet bitwarden-cli ghostty uv ruff tmux

gedit bitwarden-desktop twingate vlc obsidian foot calibre rstudioWrapper

hyprls lazygit lazycli lazydocker lazyjournal bitwarden-menu chromedriver

google-chrome lagrange appimage-run hyprpicker lm_sensors lshw ncdu

picard usbutils gcr nixd

dejavu_fonts ibm-plex inter roboto fira-code jetbrains-mono

hackgen-nf-font roboto-mono terminus_font victor-mono font-awesome

fira-code-symbols material-icons powerline-fonts symbola noto-fonts

noto-fonts-emoji noto-fonts-cjk-sans gemini-cli

dejavu_fonts ibm-plex inter roboto fira-code jetbrains-mono

hackgen-nf-font roboto-mono terminus_font victor-mono font-awesome

fira-code-symbols material-icons powerline-fonts symbola noto-fonts

noto-fonts-emoji noto-fonts-cjk-sans noto-fonts-cjk-serif

noto-fonts-monochrome-emoji minecraftia fpp igrep ladybird meld normcap

fd repgrep alejandra pre-commit vgrep xonsh vimPluginsUpdater vimgolf

rofi-obsidian tradingview neovide home-manager)

  

for pkg in "${packages[@]}"; do

stable_version=$(nix eval .#nixosConfigurations.lf-nix.pkgs.$pkg.version --raw 2>/dev/null)

unstable_version=$(nix eval .#nixosConfigurations.lf-nix.pkgs.unstable.$pkg.version --raw 2>/dev/null)

if [ -n "$unstable_version" ] && [ "$stable_version" != "$unstable_version" ]; then

echo "$pkg: $stable_version -> $unstable_version (Update available)"

else

echo "$pkg: No update ($stable_version)"

fi

done
```