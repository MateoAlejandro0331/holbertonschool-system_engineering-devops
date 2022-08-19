# Using Puppet to create a file
node default {
file { '/tmp/school': #Path file
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
   }
}
