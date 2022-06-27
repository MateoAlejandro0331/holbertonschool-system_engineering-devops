<h1 class="gap">0x06. Regular expression</h1>
<div data-react-class="tags/Tags" data-react-props="{&quot;tags&quot;:[]}" data-react-cache-id="tags/Tags-0">&nbsp;</div>
<ul id="project-metadata" class="list-group metadata">
<li class="list-group-item">&nbsp;By Sylvain Kalache</li>
<li class="list-group-item">&nbsp;Weight: 1</li>
<li class="list-group-item">&nbsp;Ongoing project - started&nbsp;
<div class="d-inline-block" data-react-class="common/DateTime" data-react-props="{&quot;showDate&quot;:true,&quot;showTime&quot;:false,&quot;value&quot;:&quot;2022-06-27T00:00:00.000-05:00&quot;}" data-react-cache-id="common/DateTime-0"><span title="" data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" data-original-title="2022-06-27 00:00 (GMT-05:00)"><span class="datetime">Jun 27, 2022</span></span></div>
, must end by&nbsp;
<div class="d-inline-block" data-react-class="common/DateTime" data-react-props="{&quot;showDate&quot;:true,&quot;showTime&quot;:false,&quot;value&quot;:&quot;2022-06-29T00:00:00.000-05:00&quot;}" data-react-cache-id="common/DateTime-0"><span title="" data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" data-original-title="2022-06-29 00:00 (GMT-05:00)"><span class="datetime">Jun 29, 2022</span></span></div>
&nbsp;- you're done with&nbsp;<span id="student_task_done_percentage">0</span>% of tasks.</li>
<li class="list-group-item">&nbsp;Checker will be released at&nbsp;
<div class="d-inline-block" data-react-class="common/DateTime" data-react-props="{&quot;showDate&quot;:true,&quot;showTime&quot;:true,&quot;value&quot;:&quot;2022-06-28T12:00:00.000-05:00&quot;}" data-react-cache-id="common/DateTime-0"><span title="" data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" data-original-title="2022-06-28 12:00 (GMT-05:00)"><span class="datetime">Jun 28, 2022 12:00 PM</span></span></div>
</li>
<li class="list-group-item">&nbsp;<strong>Manual QA review must be done</strong>&nbsp;(request it when you are done with the project)</li>
<li class="list-group-item">&nbsp;An auto review will be launched at the deadline</li>
</ul>
<div class="panel panel-default">
<div class="panel-heading">
<h3 class="panel-title">Concepts</h3>
</div>
<div class="panel-body">
<p><em>For this project, we expect you to look at this concept:</em></p>
<ul>
<li><a href="https://intranet.hbtn.io/concepts/29">Regular Expression</a></li>
</ul>
</div>
</div>
<div id="project-description" class="panel panel-default">
<div class="panel-body">
<h2>Background Context</h2>
<p>For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.</p>
<p>Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the&nbsp;<code>//</code>:</p>
<pre><code>sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
</code></pre>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="Regular expressions - basics" href="https://intranet.hbtn.io/rltoken/SJ2eQ7V2iQlCgLc-L96zWg" target="_blank">Regular expressions - basics</a></li>
<li><a title="Regular expressions - advanced" href="https://intranet.hbtn.io/rltoken/qyjWL-J1_qUaZGR690gH1Q" target="_blank">Regular expressions - advanced</a></li>
<li><a title="Rubular is your best friend" href="https://intranet.hbtn.io/rltoken/WCjn8NgohbQ5NGXEObWZvQ" target="_blank">Rubular is your best friend</a></li>
<li><a title="Use a regular expression against a problem: now you have 2 problems" href="https://intranet.hbtn.io/rltoken/Zfvv_ydOCvJ_YaBB6eDqVw" target="_blank">Use a regular expression against a problem: now you have 2 problems</a></li>
<li><a title="Learn Regular Expressions with simple, interactive exercises" href="https://intranet.hbtn.io/rltoken/Y-OVGcJ5cskdXWIBowiE_A" target="_blank">Learn Regular Expressions with simple, interactive exercises</a></li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
<li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A&nbsp;<code>README.md</code>&nbsp;file, at the root of the folder of the project, is mandatory</li>
<li><strong>All your script files must be executable</strong></li>
<li>The first line of all your Bash scripts should be exactly&nbsp;<code>#!/usr/bin/env ruby</code></li>
<li>All your regex must be built for the Oniguruma library</li>
</ul>
</div>
</div>