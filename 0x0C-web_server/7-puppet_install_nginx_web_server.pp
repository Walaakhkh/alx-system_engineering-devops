# 7-puppet_install_nginx_web_server.pp

# Ensure the Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure => running,
  enable => true,
}

# Define the configuration file for Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
server {
    listen 80;
    server_name _;

    # Redirect /redirect_me to another URL with 301 Moved Permanently
    location /redirect_me {
        return 301 https://www.example.com;
    }

    # Serve content at root /
    location / {
        add_header Content-Type text/html;
        return 200 "Hello World!";
    }
}
',
  notify  => Service['nginx'],
}

# Ensure the default site configuration is enabled
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}
