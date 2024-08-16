#!/usr/bin/env puppet

# Ensure the Apache service is running
service { 'apache2':
  ensure => running,
  enable => true,
}

# Ensure the necessary directory and file permissions are set
file { '/var/www/html/wp-config.php':
  ensure  => file,
  source  => 'puppet:///modules/my_module/wp-config.php',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  require => File['/var/www/html'],
}

file { '/var/www/html':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
}

# Ensure the correct PHP version is installed
package { 'php':
  ensure => installed,
}

# Restart Apache to apply changes
exec { 'restart_apache':
  command => '/usr/sbin/service apache2 restart',
  path    => ['/usr/sbin', '/usr/bin'],
  notify  => Service['apache2'],
}
