# Using Puppet to install flask from pip3.
if ($need_to_install == undef) {
  exec { 'install python packages':
  command => 'pip3 install flask flask_restful apiai; touch /root/installed.txt',
  path    => ['/usr/bin/'],
  before  => Exec['create custom facter'],
  }
exec { 'create custom facter':
  command  => "mkdir -p /etc/facter/facts.d; echo 'need_to_install=false' > /etc/facter/facts.d/check_pip_install.txt",
  provider => shell,
  }
}
