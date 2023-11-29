#!/usr/bin/pup
# install a esesific version of flask 2.1.0

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  require => Package['python3-pip'],
}

file { '/usr/local/bin/flask':
  ensure => link,
  target => '/usr/local/bin/flask',
  require => Exec['install_flask'],
}

