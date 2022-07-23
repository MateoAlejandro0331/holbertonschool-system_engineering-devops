<h1 class="gap">0x09. Web infrastructure design</h1>
<div data-react-class="tags/Tags" data-react-props="{&quot;tags&quot;:[]}" data-react-cache-id="tags/Tags-0">&nbsp;</div>
<ul id="project-metadata" class="list-group metadata">
<li class="list-group-item">&nbsp;By Sylvain Kalache, co-founder at Holberton School</li>
<li class="list-group-item">&nbsp;Weight: 1</li>
<li class="list-group-item">&nbsp;Project to be done in teams of 3 people (your team: Ivan Ocampo, Jhojan Perlaza, Mateo Alejandro L&oacute;pez Samac&aacute;</li>
<li class="list-group-item">&nbsp;Ongoing project - started&nbsp;
<div class="d-inline-block" data-react-class="common/DateTime" data-react-props="{&quot;showDate&quot;:true,&quot;showTime&quot;:false,&quot;value&quot;:&quot;2022-07-19T00:00:00.000-05:00&quot;}" data-react-cache-id="common/DateTime-0"><span title="" data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" data-original-title="2022-07-19 00:00 (GMT-05:00)"><span class="datetime">Jul 19, 2022</span></span></div>
, must end by&nbsp;
<div class="d-inline-block" data-react-class="common/DateTime" data-react-props="{&quot;showDate&quot;:true,&quot;showTime&quot;:false,&quot;value&quot;:&quot;2022-07-23T00:00:00.000-05:00&quot;}" data-react-cache-id="common/DateTime-0"><span title="" data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" data-original-title="2022-07-23 00:00 (GMT-05:00)"><span class="datetime">Jul 23, 2022</span></span></div>
&nbsp;- you're done with&nbsp;<span id="student_task_done_percentage">0</span>% of tasks.</li>
<li class="list-group-item">&nbsp;<strong>Manual QA review must be done</strong>&nbsp;(request it when you are done with the project)</li>
</ul>
<div class="panel panel-default">
<div class="panel-heading">
<h3 class="panel-title">Concepts</h3>
</div>
<div class="panel-body">
<p><em>For this project, we expect you to look at these concepts:</em></p>
<ul>
<li><a href="https://intranet.hbtn.io/concepts/12">DNS</a></li>
<li><a href="https://intranet.hbtn.io/concepts/13">Monitoring</a></li>
<li><a href="https://intranet.hbtn.io/concepts/17">Web Server</a></li>
<li><a href="https://intranet.hbtn.io/concepts/33">Network basics</a></li>
<li><a href="https://intranet.hbtn.io/concepts/46">Load balancer</a></li>
<li><a href="https://intranet.hbtn.io/concepts/67">Server</a></li>
</ul>
</div>
</div>
<div id="project-description" class="panel panel-default">
<div class="panel-body"><iframe title="YouTube video player" src="https://www.youtube.com/embed/lQNEW76KdYg" frameborder="0" width="560" height="315"></iframe>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><strong>Network basics</strong>&nbsp;concept page</li>
<li><strong>Server</strong>&nbsp;concept page</li>
<li><strong>Web server</strong>&nbsp;concept page</li>
<li><strong>DNS</strong>&nbsp;concept page</li>
<li><strong>Load balancer</strong>&nbsp;concept page</li>
<li><strong>Monitoring</strong>&nbsp;concept page</li>
<li><a title="What is a database" href="https://intranet.hbtn.io/rltoken/woDFYUG0y_SrA79AaYbFCA" target="_blank">What is a database</a></li>
<li><a title="What's the difference between a web server and an app server?" href="https://intranet.hbtn.io/rltoken/Nb8B47Y2D8SLqQMOKVoQyQ" target="_blank">What&rsquo;s the difference between a web server and an app server?</a></li>
<li><a title="DNS record types" href="https://intranet.hbtn.io/rltoken/ojwHUACZEtIWfI9M6i7c3g" target="_blank">DNS record types</a></li>
<li><a title="Single point of failure" href="https://intranet.hbtn.io/rltoken/wYpewVpIp9PSqqL27RPafg" target="_blank">Single point of failure</a></li>
<li><a title="How to avoid downtime when deploying new code" href="https://intranet.hbtn.io/rltoken/Mlvynt0OgLQXrxjrC5Wlnw" target="_blank">How to avoid downtime when deploying new code</a></li>
<li><a title="High availability cluster (active-active/active-passive)" href="https://intranet.hbtn.io/rltoken/POX3jE0S6TChQHSYQraYeQ" target="_blank">High availability cluster (active-active/active-passive)</a></li>
<li><a title="What is HTTPS" href="https://intranet.hbtn.io/rltoken/N4BwU4wYDNW02kdzMiekFw" target="_blank">What is HTTPS</a></li>
<li><a title="What is a firewall" href="https://intranet.hbtn.io/rltoken/ZFTutaKN4wWzmL4fWhQmeg" target="_blank">What is a firewall</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/Dvn7v5U404zIccrJ_jDevg" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects</li>
<li>You must be able to explain what each component is doing</li>
<li>You must be able to explain system redundancy</li>
<li>Know all the mentioned acronyms: LAMP, SPOF, QPS</li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
<li>A&nbsp;<code>README.md</code>&nbsp;file, at the root of the folder of the project, is mandatory</li>
<li>For each task, once you are done whiteboarding (on a whiteboard, piece of paper or software or your choice), take a picture/screenshot of your diagram</li>
<li>This project will be manually reviewed:</li>
<li>As each task is completed, the name of that task will turn green</li>
<li>Upload a screenshot, showing that you completed the required levels, to any image hosting service (I personally use&nbsp;<a title="imgur" href="https://intranet.hbtn.io/rltoken/QorG0rvw1PzqWBVrqWW6Sg" target="_blank">imgur</a>&nbsp;but feel free to use anything you want).</li>
<li>For the following tasks, insert the link from of your screenshot into the answer file</li>
<li>After pushing your answer file to GitHub, insert the GitHub file link into the URL box</li>
<li>You will also have to whiteboard each task in front of a mentor, staff or student - no computer or notes will be allowed during the whiteboarding session</li>
<li>Focus on what you are being asked:</li>
<li>Cover what the requirements mention, we will explore details in a later project</li>
<li>Keep in mind that you will have 30 minutes to perform the exercise, you will get points for what is asked in requirements</li>
<li>Similarly in a job interview, you should answer what the interviewer asked for, be careful about being too verbose - always ask the interviewer if going into details is necessary - speaking too much can play against you</li>
<li>In this project, again, avoid going in details if not asked</li>
</ul>
</div>
</div>