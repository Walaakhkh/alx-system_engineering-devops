# Find out why Apache is returning a 500 error
# Ensure the missing PHP module is installed
package { 'php-mysql':
  ensure => installed,
}

# Ensure the Apache service is running
service { 'apache2':
  ensure => running,
  enable => true,
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
