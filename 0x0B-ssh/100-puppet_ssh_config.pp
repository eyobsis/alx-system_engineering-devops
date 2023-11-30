# Puppet manifest to configure SSH client for ubuntu user on 247200-web-01

file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => '
    # SSH Client Configuration for server 247200-web-01
    # Disabling password authentication and specifying identity file
    Host 54.146.56.149
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ',
}

