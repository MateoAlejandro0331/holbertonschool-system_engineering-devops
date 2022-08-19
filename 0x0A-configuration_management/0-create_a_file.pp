# Using Puppet to create a file
file { '/tmp/school': #Path file
  path    => '/tmp/school'
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
  }
