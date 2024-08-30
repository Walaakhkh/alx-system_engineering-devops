# 0-strace_is_your_friend.pp

# Ensure the necessary PHP module is installed
package { 'php-mysql':
  ensure => installed,
}

# Ensure correct file permissions for the web directory
file { '/var/www/html/':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

# Ensure the Apache service is running and enabled
service { 'apache2':
  ensure => running,
  enable => true,
}
