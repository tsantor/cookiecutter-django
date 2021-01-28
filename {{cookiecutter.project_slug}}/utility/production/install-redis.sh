#!/usr/bin/env bash

package_name="Redis"
package="redis-server"
systemctl_name="redis-server.service"

echo "==> Installing ${package_name}..."

if apt-cache policy ${package} | grep Installed | grep "Installed: (none)"; then

    sudo apt-get install -y ${package}

    # sudo sed -i 's/supervised no/supervised systemd/' /etc/redis/redis.conf

    # Make sure it comes up after a reboot
    sudo systemctl enable ${systemctl_name}

    # Bring it up right now
    sudo systemctl start ${systemctl_name}

    # sudo systemctl restart redis.service

else

    echo -e "$(tput setaf 2)[\u2713] ${package} already installed$(tput sgr 0)"

fi

# Configure
# sudo nano /etc/redis/redis.conf

# Stats
# redis-cli info
# redis-cli info stats
# redis-cli info server
