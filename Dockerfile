FROM digitaltoa/odoo:v18.1

USER root

# Install Package
RUN apt update
RUN apt upgrade -y

USER odoo

# Setup Odoo
ADD --chown=odoo:odoo addons /mnt/addons
ADD --chown=odoo:odoo conf/odoo.conf /etc/odoo/odoo.conf
ADD --chown=odoo:odoo fonts /usr/share/fonts/truetype
