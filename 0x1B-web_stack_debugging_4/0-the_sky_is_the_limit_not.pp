# testing how well our web server setup featuring Nginx is doing under pressure
# and it turns out it is not doing well
exec { 'fix--for-nginx':
  command => '/bin/sed -i "s/worker_connections.*/worker_connections 1024;/g" /etc/nginx/nginx.conf && /usr/sbin/service nginx restart',
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
}
