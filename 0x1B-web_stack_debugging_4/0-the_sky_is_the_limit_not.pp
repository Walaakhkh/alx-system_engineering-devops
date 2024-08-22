# Puppet manifest to optimize Nginx server performance

# Increase Nginx worker processes and connections
exec { 'fix--for-nginx':
  command => 'sed -i "s/worker_connections.*/worker_connections 4096;/" /etc/nginx/nginx.conf &&
              sed -i "s/worker_processes.*/worker_processes auto;/" /etc/nginx/nginx.conf &&
              systemctl restart nginx',
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
}

# Ensure system limits are set to handle more connections
file { '/etc/security/limits.conf':
  ensure  => present,
  content => @("EOF")
*               soft    nofile          65535
*               hard    nofile          65535
  | EOF
}

# Increase the maximum number of open file descriptors
exec { 'increase-file-descriptors':
  command => 'echo "fs.file-max = 65535" >> /etc/sysctl.conf && sysctl -p',
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
}

# Ensure Nginx service is running after changes
service { 'nginx':
  ensure => running,
  enable => true,
  require => Exec['fix--for-nginx'],
}
