<h2>Background Context</h2>
<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/244/zPVRKhPsUP5lK.gif" alt="" /></p>
<p>Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using&nbsp;<code>ssh</code>. But contrary to level 2, you will not connect using a password but an RSA key. We&rsquo;ve configured your server with the public key you created in the first task of&nbsp;<a title="a previous project" href="https://intranet.hbtn.io/rltoken/LZ_8pMANOAmpn5-tiwqiJQ" target="_blank">a previous project</a>&nbsp;shared in your&nbsp;<a title="intranet profile" href="https://intranet.hbtn.io/rltoken/l4Ao4ESbI_hMB6s4mjBKRw" target="_blank">intranet profile</a>.</p>
<p>You can access your server information in the&nbsp;<a title="my servers" href="https://intranet.hbtn.io/rltoken/owYhGMuyPTY4OyvSGJljGQ" target="_blank">my servers</a>&nbsp;section of the intranet, each line with contains the IP and username you should use to connect via&nbsp;<code>ssh</code>.</p>
<p><strong>Note:</strong>&nbsp;Your server is configured with an Ubuntu 20.04 LTS environment.</p>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="What is a (physical) server - text" href="https://intranet.hbtn.io/rltoken/PXE-o9DWronMp4ETwADOpg" target="_blank">What is a (physical) server - text</a></li>
<li><a title="What is a (physical) server - video" href="https://intranet.hbtn.io/rltoken/IfLc3lxSs4w5xdsFlRDPWw" target="_blank">What is a (physical) server - video</a></li>
<li><a title="SSH essentials" href="https://intranet.hbtn.io/rltoken/qKJi0RXLqaCLkHLCLhiYNA" target="_blank">SSH essentials</a></li>
<li><a title="SSH Config File" href="https://intranet.hbtn.io/rltoken/hnb0XaZQ0Nb_7QmSC6aV-w" target="_blank">SSH Config File</a></li>
<li><a title="Public Key Authentication for SSH" href="https://intranet.hbtn.io/rltoken/zaO_H74BXLfsrQHzDW-QGQ" target="_blank">Public Key Authentication for SSH</a></li>
<li><a title="How Secure Shell Works" href="https://intranet.hbtn.io/rltoken/SW2m2e0KMA2K1dXk_0M0CA" target="_blank">How Secure Shell Works</a></li>
<li><a title="SSH Crash Course" href="https://intranet.hbtn.io/rltoken/8N-RlUma9lwGfyZp1_C-Wg" target="_blank">SSH Crash Course</a>&nbsp;(Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)</li>
</ul>
<p><strong>For reference:</strong></p>
<ul>
<li><a title="Understanding the SSH Encryption and Connection Process" href="https://intranet.hbtn.io/rltoken/6mtNBCxYkoBQJ2vJ6TcRYA" target="_blank">Understanding the SSH Encryption and Connection Process</a></li>
<li><a title="Secure Shell Wiki" href="https://intranet.hbtn.io/rltoken/c1Yj55AE6gGkDxpACdY1vg" target="_blank">Secure Shell Wiki</a></li>
<li><a title="IETF RFC 4251 (Description of the SSH Protocol)" href="https://www.ietf.org/rfc/rfc4251.txt" target="_blank">IETF RFC 4251 (Description of the SSH Protocol)</a></li>
<li><a title="Internet Engineering Task Force" href="https://intranet.hbtn.io/rltoken/bH7JrEiKN4Q6-J58d9pAsw" target="_blank">Internet Engineering Task Force</a></li>
<li><a title="Request for Comments" href="https://intranet.hbtn.io/rltoken/lDe2f7hVqQPPCNr5i2zE-g" target="_blank">Request for Comments</a></li>
</ul>
<p><strong>man or help</strong>:</p>
<ul>
<li><code>ssh</code></li>
<li><code>ssh-keygen</code></li>
<li><code>env</code></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/kSsEz3TOFnxP9C6paL8FfQ" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>What is a server</li>
<li>Where servers usually live</li>
<li>What is SSH</li>
<li>How to create an SSH RSA key pair</li>
<li>How to connect to a remote host using an SSH RSA key pair</li>
<li>The advantage of using&nbsp;<code>#!/usr/bin/env bash</code>&nbsp;instead of&nbsp;<code>/bin/bash</code></li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
<li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A&nbsp;<code>README.md</code>&nbsp;file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>The first line of all your Bash scripts should be exactly&nbsp;<code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>