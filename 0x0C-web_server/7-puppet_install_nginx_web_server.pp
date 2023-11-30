# 7-puppet_install_nginx_web_server.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Set up the default HTML page
file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

# Configure Nginx to listen on port 80 and set the root directory
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;

      root /var/www/html;
      index index.html index.htm;

      location /redirect_me {
        return 301 https://www.example.com/new_page;
      }
    }
  ",
}

# Create a symbolic link to enable the site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

# Restart Nginx service to apply changes
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-enabled/default'],
}

