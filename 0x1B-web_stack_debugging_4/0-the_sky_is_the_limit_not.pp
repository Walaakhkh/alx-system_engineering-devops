# Increases the amount of traffic on Nginx server can handle

# Increase the ULIMIT of the defult file
exec {  'fix--for-nginx':
# Modify the ULIMIT value
command => '/bin/sed -i "s/15/4096/" /etc/defult/nginx'
# Specify the path for the sed command
path	=> 'usr/local/bin/:/bin/',
}

# Restart Nginx
exec {  'nginx-restart':
# Restart Nginx services
command => '/etc/inti.d/nginx restart',
# Specify the path for the init.d script
path	=> '/etc/init.d/',
}
