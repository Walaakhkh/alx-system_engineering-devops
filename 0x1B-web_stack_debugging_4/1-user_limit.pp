# Enable the user holberton to login and open files without error

# Increase file descriptor limit for the holberton user
file { '/etc/security/limits.conf':
  ensure  => file,
  content => "holberton soft nofile 1024\nholberton hard nofile 4096\n",
  notify  => Exec['apply-limits'],
}

exec { 'apply-limits':
  command     => '/bin/bash -c "ulimit -n 4096"',
  refreshonly => true,
}
