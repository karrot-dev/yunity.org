FROM php:7

RUN <<EOF
set -eu
apt-get update
apt-get install -y libzip-dev libpng-dev libjpeg-dev libfreetype-dev wget
docker-php-ext-configure gd --with-freetype --with-jpeg
docker-php-ext-install -j$(nproc) gd
docker-php-ext-install -j$(nproc) zip
EOF

RUN <<EOF
set -eu
wget https://getcomposer.org/download/2.7.2/composer.phar -O /usr/local/bin/composer
chmod +x /usr/local/bin/composer
EOF

WORKDIR /site
