<h1>0x0A. Configuration management</h1>
<div id="project-description" class="panel panel-default">
<div class="panel-body">
<h2>Background Context</h2>
<p><a href="https://youtu.be/ogYLFyp68cI" target="_blank"><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/6a0a8024f2b1c47a9d1e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220819%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20220819T151903Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=f57f193da99b49222058e8af324c26eca3b45e4b07bf5fcd664667168d2b55f6" alt="" /></a></p>
<p>When I was working for SlideShare, I worked on an auto-remediation tool called&nbsp;<a title="Skynet" href="https://intranet.hbtn.io/rltoken/ftFvBjxNPLoWcF9eHaK8yw" target="_blank">Skynet</a>&nbsp;that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the server&rsquo;s hostname or any other metadata we had (server type, server environment&hellip;). At some point, a bug was present in my code that sent&nbsp;<code>nil</code>&nbsp;to the filter method.</p>
<p>There were 2 pieces of bad news:</p>
<ol>
<li>When MCollective receives&nbsp;<code>nil</code>&nbsp;as an argument for its filter method, it takes this to mean &lsquo;all servers&rsquo;</li>
<li>The action I sent was to terminate the selected servers</li>
</ol>
<p>I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShare&rsquo;s entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, powerpoints, and videos&hellip; Pretty bad!</p>
<p>Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)&hellip;</p>
<p>Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.</p>
<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/292/4i8il3B.gif" alt="" /></p>
<p>That was me ^_^&lsquo;:&nbsp;<a title="https://twitter.com/devopsreact/status/836971570136375296" href="https://intranet.hbtn.io/rltoken/uHU1llO2UZXg8_funEgpJA" target="_blank">https://twitter.com/devopsreact/status/836971570136375296</a></p>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="Intro to Configuration Management" href="https://intranet.hbtn.io/rltoken/r-NmkYO8bxIKp2qEx2ZjKQ" target="_blank">Intro to Configuration Management</a></li>
<li><a title="Puppet resource type: file" href="https://intranet.hbtn.io/rltoken/D0-IO_SIZSXYLKJs2BitYA" target="_blank">Puppet resource type: file</a>&nbsp;(<em>check &ldquo;Resource types&rdquo; for all manifest types in the left menu</em>)</li>
<li><a title="Puppet's Declarative Language: Modeling Instead of Scripting" href="https://intranet.hbtn.io/rltoken/Fqmb5rnChQgYAypvKoTxAQ" target="_blank">Puppet&rsquo;s Declarative Language: Modeling Instead of Scripting</a></li>
<li><a title="Puppet lint" href="https://intranet.hbtn.io/rltoken/oezu0m_hJ8nEVA6a9o17Tw" target="_blank">Puppet lint</a></li>
<li><a title="Puppet emacs mode" href="https://intranet.hbtn.io/rltoken/N70cVw8mG3707He-OxjP1w" target="_blank">Puppet emacs mode</a></li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
<li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A&nbsp;<code>README.md</code>&nbsp;file at the root of the folder of the project is mandatory</li>
<li>Your Puppet manifests must pass&nbsp;<code>puppet-lint</code>&nbsp;version 2.1.1 without any errors</li>
<li>Your Puppet manifests must run without error</li>
<li>Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about</li>
<li>Your Puppet manifests files must end with the extension&nbsp;<code>.pp</code></li>
</ul>
<h2>Note on Versioning</h2>
<p>Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.</p>
<h3>Install&nbsp;<code>puppet</code></h3>
<pre><code>$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
</code></pre>
<p>You do&nbsp;<strong>not</strong>&nbsp;need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.</p>
<p><a title="Puppet 5 Docs" href="https://intranet.hbtn.io/rltoken/_xOod_Lzz8WKTbhpG5SWLQ" target="_blank">Puppet 5 Docs</a></p>
<h3>Install&nbsp;<code>puppet-lint</code></h3>
<pre><code>$ gem install puppet-lint
</code></pre>
</div>
</div>
<h2 class="gap">Tasks</h2>
<div id="task-num-0" data-role="task1612" data-position="1">
<div id="task-1612" class="panel panel-default task-card "><span id="user_id" data-id="4765"></span>
<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">0. Create a file</h3>
<div><span class="label label-info">mandatory</span></div>
</div>
<div class="panel-body"><span id="user_id" data-id="4765"></span>
<p>Using Puppet, create a file in&nbsp;<code>/tmp</code>.</p>
<p>Requirements:</p>
<ul>
<li>File path is&nbsp;<code>/tmp/school</code></li>
<li>File permission is&nbsp;<code>0744</code></li>
<li>File owner is&nbsp;<code>www-data</code></li>
<li>File group is&nbsp;<code>www-data</code></li>
<li>File contains&nbsp;<code>I love Puppet</code></li>
</ul>
<p>Example:</p>
<pre><code>root@6712bef7a528:~# puppet-lint --version
puppet-lint 2.5.2
root@6712bef7a528:~# puppet-lint 0-create_a_file.pp
root@6712bef7a528:~# 
root@6712bef7a528:~# puppet apply 0-create_a_file.pp
Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
Notice: /Stage[main]/Main/File[school]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
Notice: Finished catalog run in 0.03 seconds
root@6712bef7a528:~#
root@6712bef7a528:~# ls -l /tmp/school
-rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/school
root@6712bef7a528:~# cat /tmp/school
I love Puppetroot@6712bef7a528:~#
</code></pre>
</div>
<div class="list-group">
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-system_engineering-devops</code></li>
<li>Directory:&nbsp;<code>0x0A-configuration_management</code></li>
<li>File:&nbsp;<code>0-create_a_file.pp</code></li>
</ul>
</div>
</div>
<div class="panel-footer">
<div class="align-items-center d-flex justify-content-between">
<div><button class="student_task_done btn btn-default btn-sm no" data-task-id="1612">&nbsp;Done<span class="no pending">?</span></button>&nbsp;<button class="student-task-done-by btn btn-default btn-sm" data-task-id="1612" data-batch-id="235" data-toggle="modal" data-target="#task-1612-users-done-modal">Help</button>&nbsp;<button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><span>Get a sandbox</span></button></div>
<div class="fs-4">&nbsp;</div>
</div>
</div>
</div>
</div>
<div id="task-num-1" data-role="task1613" data-position="2">
<div id="task-1613" class="panel panel-default task-card "><span id="user_id" data-id="4765"></span>
<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">1. Install a package</h3>
<div><span class="label label-info">mandatory</span></div>
</div>
<div class="panel-body"><span id="user_id" data-id="4765"></span>
<p>Using Puppet, install&nbsp;<code>flask</code>&nbsp;from&nbsp;<code>pip3</code>.</p>
<p>Requirements:</p>
<ul>
<li>Install&nbsp;<code>flask</code></li>
<li>Version must be&nbsp;<code>2.1.0</code></li>
</ul>
<p>Example:</p>
<pre><code>root@9665f0a47391:/# puppet apply 1-install_a_package.pp
Notice: Compiled catalog for 9665f0a47391 in environment production in 0.14 seconds
Notice: /Stage[main]/Main/Package[Flask]/ensure: created
Notice: Applied catalog in 0.20 seconds
root@9665f0a47391:/# flask --version
Python 3.8.10
Flask 2.1.0
Werkzeug 2.1.1
</code></pre>
</div>
<div class="list-group">
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-system_engineering-devops</code></li>
<li>Directory:&nbsp;<code>0x0A-configuration_management</code></li>
<li>File:&nbsp;<code>1-install_a_package.pp</code></li>
</ul>
</div>
</div>
<div class="panel-footer">
<div class="align-items-center d-flex justify-content-between">
<div><button class="student_task_done btn btn-default btn-sm no" data-task-id="1613">&nbsp;Done<span class="no pending">?</span></button>&nbsp;<button class="student-task-done-by btn btn-default btn-sm" data-task-id="1613" data-batch-id="235" data-toggle="modal" data-target="#task-1613-users-done-modal">Help</button>&nbsp;<button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal"><span>Get a sandbox</span></button></div>
<div class="fs-4">&nbsp;</div>
</div>
</div>
</div>
</div>
<div id="task-num-2" data-role="task1614" data-position="3">
<div id="task-1614" class="panel panel-default task-card "><span id="user_id" data-id="4765"></span>
<div class="panel-heading panel-heading-actions">
<h3 class="panel-title">2. Execute a command</h3>
<div><span class="label label-info">mandatory</span></div>
</div>
<div class="panel-body"><span id="user_id" data-id="4765"></span>
<p>Using Puppet, create a manifest that kills a process named&nbsp;<code>killmenow</code>.</p>
<p>Requirements:</p>
<ul>
<li>Must use the&nbsp;<code>exec</code>&nbsp;Puppet resource</li>
<li>Must use&nbsp;<code>pkill</code></li>
</ul>
<p>Example:</p>
<p>Terminal #0 - starting my process</p>
<pre><code>root@d391259bf577:/# cat killmenow
#!/bin/bash
while [[ true ]]
do
    sleep 2
done

root@d391259bf577:/# ./killmenow
</code></pre>
<p>Terminal #1 - executing my manifest</p>
<pre><code>root@d391259bf577:/# puppet apply 2-execute_a_command.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
Notice: Finished catalog run in 0.10 seconds
root@d391259bf577:/# 
</code></pre>
<p>Terminal #0 - process has been terminated</p>
<pre><code>root@d391259bf577:/# ./killmenow
Terminated
root@d391259bf577:/#
</code></pre>
</div>
<div class="list-group">
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-system_engineering-devops</code></li>
<li>Directory:&nbsp;<code>0x0A-configuration_management</code></li>
<li>File:&nbsp;<code>2-execute_a_command.pp</code></li>
</ul>
</div>
</div>
<div class="panel-footer">
<div class="align-items-center d-flex justify-content-between">
<div><button class="student_task_done btn btn-default btn-sm no" data-task-id="1614">&nbsp;Done<span class="no pending">?</span></button>&nbsp;<button class="student-task-done-by btn btn-default btn-sm" data-task-id="1614" data-batch-id="235" data-toggle="modal" data-target="#task-1614-users-done-modal">Help</button>&nbsp;</div>
</div>
</div>
</div>
</div>