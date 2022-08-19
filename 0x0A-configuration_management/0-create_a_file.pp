# Using Puppet to create a file
node default {
file { '/tmp/school':
  content => 'I love Puppet',
  ensure  => 'present',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
   }
}
