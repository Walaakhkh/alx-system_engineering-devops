exec { 'fix--for-nginx':
  command => '/bin/sed -i "s/worker_connections.*/worker_connections 1024;/g" /etc/nginx/nginx.conf && /usr/sbin/service nginx restart',
}
