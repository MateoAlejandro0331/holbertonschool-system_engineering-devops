# Using Puppet to create a file
file { '/tmp/school': #Path file
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  path    => '/tmp/school'
}
