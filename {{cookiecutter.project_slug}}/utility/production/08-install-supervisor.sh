#!/usr/bin/env bash

if [ ! -f /etc/supervisor/supervisord.conf ]; then

    echo "=> Installing Supervisor..."
    sudo apt-get -y install supervisor

    echo '==> Create Supervisord conf...'
    echo_supervisord_conf > supervisord.conf
    sudo mv supervisord.conf /etc/supervisor/supervisord.conf

    sh -c "cat >> /etc/supervisor/supervisord.conf" <<EOF
[include]
files = /etc/supervisor/conf.d/*.conf
EOF

    # Make sure Supervisor comes up after a reboot
    sudo systemctl enable supervisor

    # Bring Supervisor up right now
    sudo systemctl start supervisor

    sudo service supervisor restart

fi
