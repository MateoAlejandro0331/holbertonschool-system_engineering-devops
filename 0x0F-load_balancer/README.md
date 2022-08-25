<div class="panel panel-default">
<div class="panel-heading">
<h3 class="panel-title">Concepts</h3>
</div>
<div class="panel-body">
<p><em>For this project, we expect you to look at these concepts:</em></p>
<ul>
<li><a href="https://intranet.hbtn.io/concepts/46">Load balancer</a></li>
<li><a href="https://intranet.hbtn.io/concepts/68">Web stack debugging</a></li>
</ul>
</div>
</div>
<div id="project-description" class="panel panel-default">
<div class="panel-body">
<p><span style="font-family: 'arial black', 'avant garde'; font-size: small;"><strong>Background Context</strong></span></p>
<p>You have been given 2 additional servers:</p>
<ul>
<li>gc-[STUDENT_ID]-web-02-XXXXXXXXXX</li>
<li>gc-[STUDENT_ID]-lb-01-XXXXXXXXXX</li>
</ul>
<p>Let&rsquo;s improve our web stack so that there is&nbsp;<a title="redundancy" href="https://intranet.hbtn.io/rltoken/QiOC_I-8BeV4aNExIucC9Q" target="_blank">redundancy</a>&nbsp;for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.</p>
<p>For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.</p>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="Introduction to load-balancing and HAproxy" href="https://intranet.hbtn.io/rltoken/ngIXarEyu8jZwOL3Y30PLQ" target="_blank">Introduction to load-balancing and HAproxy</a></li>
<li><a title="HTTP header" href="https://intranet.hbtn.io/rltoken/v32JmcDrSiOnFBfqzXvs_Q" target="_blank">HTTP header</a></li>
<li><a title="Debian/Ubuntu HAProxy packages" href="https://intranet.hbtn.io/rltoken/BXGrW_6ocecWaOJb7OK_WA" target="_blank">Debian/Ubuntu HAProxy packages</a></li>
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
</ul>
</div>
</div>