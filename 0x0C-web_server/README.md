<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png" alt="" /></p>
<h2>Background Context</h2>
<p><a href="https://www.youtube.com/watch?v=AZg4uJkEa-4&amp;feature=youtu.be&amp;hd=1" target="_blank"><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/Screenshot+2017-07-06+19.24.05.png" alt="" /></a></p>
<p>In this project, some of the tasks will be graded on 2 aspects:</p>
<ol>
<li>Is your&nbsp;<code>web-01</code>&nbsp;server configured according to requirements</li>
<li>Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)</li>
</ol>
<p>For example, if I need to create a file&nbsp;<code>/tmp/test</code>&nbsp;containing the string&nbsp;<code>hello world</code>&nbsp;and modify the configuration of Nginx to listen on port&nbsp;<code>8080</code>&nbsp;instead of&nbsp;<code>80</code>, I can use&nbsp;<code>emacs</code>&nbsp;on my server to create the file and to modify the Nginx configuration file&nbsp;<code>/etc/nginx/sites-enabled/default</code>.</p>
<p>But my answer file would contain:</p>
<pre><code>sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world &gt; /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu
</code></pre>
<p>As you can tell, I am not using&nbsp;<code>emacs</code>&nbsp;to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an&nbsp;<a title="SRE" href="https://intranet.hbtn.io/rltoken/Hjv9yJQtW6X7VRa2ByMeEg" target="_blank">SRE</a>, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the&nbsp;<code>root</code>&nbsp;user, you do not need to use the&nbsp;<code>sudo</code>&nbsp;command.</p>
<p>A good Software Engineer is a&nbsp;<a title="lazy Software Engineer" href="https://intranet.hbtn.io/rltoken/y1MX-uAX-0a4bgXfH3uweQ" target="_blank">lazy Software Engineer</a>.&nbsp;<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg" alt="" /></p>
<p>Tips: to test your answer Bash script, feel free to reproduce the checker environment:</p>
<ul>
<li>start a&nbsp;<code>Ubuntu 16.04</code>&nbsp;sandbox</li>
<li>run your script on it</li>
<li>see how it behaves</li>
</ul>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="How the web works" href="https://intranet.hbtn.io/rltoken/4tRRzyyETAySzU-bgNGLSw" target="_blank">How the web works</a></li>
<li><a title="Nginx" href="https://intranet.hbtn.io/rltoken/H9OfhUnBDdxV-QQnIucMlA" target="_blank">Nginx</a></li>
<li><a title="How to Configure Nginx" href="https://intranet.hbtn.io/rltoken/wePwmjbJDgJZO7YPvffWxQ" target="_blank">How to Configure Nginx</a></li>
<li><strong>Child process</strong>&nbsp;concept page</li>
<li><a title="Root and sub domain" href="https://intranet.hbtn.io/rltoken/S2JO8E1CftLXOgvCfYf78A" target="_blank">Root and sub domain</a></li>
<li><a title="HTTP requests" href="https://intranet.hbtn.io/rltoken/C9s3U62JbiOAvn9WCoxKsA" target="_blank">HTTP requests</a></li>
<li><a title="HTTP redirection" href="https://intranet.hbtn.io/rltoken/kI4vRQ6vc45Wfbdo3UD8Lw" target="_blank">HTTP redirection</a></li>
<li><a title="Not found HTTP response code" href="https://intranet.hbtn.io/rltoken/5UvC588x2hZR7dm6eRFPoQ" target="_blank">Not found HTTP response code</a></li>
<li><a title="Logs files on Linux" href="https://intranet.hbtn.io/rltoken/bkqQ72HZVAV65G8nB503Pw" target="_blank">Logs files on Linux</a></li>
</ul>
<p><strong>For reference:</strong></p>
<ul>
<li><a title="RFC 7231 (HTTP/1.1)" href="https://intranet.hbtn.io/rltoken/Ip0atFgh-X8dcQxQdUyVUA" target="_blank">RFC 7231 (HTTP/1.1)</a></li>
<li><a title="RFC 7540 (HTTP/2)" href="https://intranet.hbtn.io/rltoken/cwfqkSHy98XGvyezL5KIIA" target="_blank">RFC 7540 (HTTP/2)</a></li>
</ul>
<p><strong>man or help</strong>:</p>
<ul>
<li><code>scp</code></li>
<li><code>curl</code></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/HLB_f8cKD3VOdBgXcaHTdA" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>What is the main role of a web server</li>
<li>What is a child process</li>
<li>Why web servers usually have a parent process and child processes</li>
<li>What are the main HTTP requests</li>
</ul>
<h3>DNS</h3>
<ul>
<li>What DNS stands for</li>
<li>What is DNS main role</li>
</ul>
<h3>DNS Record Types</h3>
<ul>
<li><code>A</code></li>
<li><code>CNAME</code></li>
<li><code>TXT</code></li>
<li><code>MX</code></li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
<li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 16.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A&nbsp;<code>README.md</code>&nbsp;file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass&nbsp;<code>Shellcheck</code>&nbsp;(version&nbsp;<code>0.3.7</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly&nbsp;<code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
<li>You can&rsquo;t use&nbsp;<code>systemctl</code>&nbsp;for restarting a process</li>
</ul>