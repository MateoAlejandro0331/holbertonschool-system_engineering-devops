# Using Puppet to create a manifest that kills a process named killmenow.
exec {'Kill process - killmenow':
  command  => 'pkill killmenow',
  provider => shell
}
