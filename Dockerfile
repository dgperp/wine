FROM digitaltoa/odoo:v18.1

USER root

# Install Package
RUN apt update
RUN apt upgrade -y
RUN apt install gcc libcairo2-dev pkg-config python3-dev -y
ADD requirements.txt /mnt/requirements.txt
RUN pip3 install -r /mnt/requirements.txt

USER odoo

# Setup Odoo
ADD --chown=odoo:odoo addons /mnt/addons
ADD --chown=odoo:odoo conf/odoo.conf /etc/odoo/odoo.conf
ADD --chown=odoo:odoo fonts /usr/share/fonts/truetype
