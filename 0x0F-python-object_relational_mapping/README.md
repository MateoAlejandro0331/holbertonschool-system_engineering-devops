<h2>Before you start&hellip;</h2>
<p><strong>Please make sure your MySQL server is in 8.0</strong>&nbsp;-&gt;&nbsp;<a title="How to install MySQL 8.0 in Ubuntu 20.04" href="https://intranet.hbtn.io/rltoken/mqTU28SAIfz_-9w7rZipMw" target="_blank">How to install MySQL 8.0 in Ubuntu 20.04</a></p>
<h2>Background Context</h2>
<p>In this project, you will link two amazing worlds: Databases and Python!</p>
<p>In the first part, you will use the module&nbsp;<code>MySQLdb</code>&nbsp;to connect to a MySQL database and execute your SQL queries.</p>
<p>In the second part, you will use the module&nbsp;<code>SQLAlchemy</code>&nbsp;(don&rsquo;t ask me how to pronounce it&hellip;) an Object Relational Mapper (ORM).</p>
<p>The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be &ldquo;What can I do with my objects&rdquo; and not &ldquo;How this object is stored? where? when?&rdquo;. You won&rsquo;t write any SQL queries only Python code. Last thing, your code won&rsquo;t be &ldquo;storage type&rdquo; dependent. You will be able to change your storage easily without re-writing your entire project.</p>
<p>Without ORM:</p>
<pre><code>conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
</code></pre>
<p>With an ORM:</p>
<pre><code>engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
</code></pre>
<p>Do you see the difference? Cool, right?</p>
<p>The biggest difficulty with ORM is: The syntax!</p>
<p>Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don&rsquo;t read the entire documentation before starting, just jump on it if you don&rsquo;t get something.</p>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="Object-relational mappers" href="https://intranet.hbtn.io/rltoken/IqdjUaZ31ZfP6eT-lTyUkA" target="_blank">Object-relational mappers</a></li>
<li><a title="mysqlclient/MySQLdb documentation" href="https://intranet.hbtn.io/rltoken/rMJpVJ1_YjMWfvY00I7Kpw" target="_blank">mysqlclient/MySQLdb documentation</a>&nbsp;(<em>please don&rsquo;t pay attention to&nbsp;<code>_mysql</code></em>)</li>
<li><a title="MySQLdb tutorial" href="https://intranet.hbtn.io/rltoken/DJz5W6Y13-6qUSTPTGrHYw" target="_blank">MySQLdb tutorial</a></li>
<li><a title="SQLAlchemy tutorial" href="https://intranet.hbtn.io/rltoken/9JWveMwNKe3IUErdEbDsUQ" target="_blank">SQLAlchemy tutorial</a></li>
<li><a title="SQLAlchemy" href="https://intranet.hbtn.io/rltoken/E9dLS6Shaezq4ivnGxN_RA" target="_blank">SQLAlchemy</a></li>
<li><a title="mysqlclient/MySQLdb" href="https://intranet.hbtn.io/rltoken/QFgtVxz2w-C1y1OB8uls1g" target="_blank">mysqlclient/MySQLdb</a></li>
<li><a title="Introduction to SQLAlchemy" href="https://intranet.hbtn.io/rltoken/I5bvhPGTOu3_-T-4jpN-hg" target="_blank">Introduction to SQLAlchemy</a></li>
<li><a title="Flask SQLAlchemy" href="https://intranet.hbtn.io/rltoken/UvaHESHeqlRA0Z0uQFi0_A" target="_blank">Flask SQLAlchemy</a></li>
<li><a title="10 common stumbling blocks for SQLAlchemy newbies" href="https://intranet.hbtn.io/rltoken/Zb8Yc2WycLLYX8gnLlwZKw" target="_blank">10 common stumbling blocks for SQLAlchemy newbies</a></li>
<li><a title="Python SQLAlchemy Cheatsheet" href="https://intranet.hbtn.io/rltoken/XHPAX7-ydSou2BLWHII8Vw" target="_blank">Python SQLAlchemy Cheatsheet</a></li>
<li><a title="SQLAlchemy ORM Tutorial for Python Developers" href="https://intranet.hbtn.io/rltoken/aeLSQ039BhLhamU2BjqsOw" target="_blank">SQLAlchemy ORM Tutorial for Python Developers</a>&nbsp;(<em><strong>Warning:</strong>&nbsp;This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL</em>)</li>
<li><a title="SQLAlchemy Tutorial" href="https://intranet.hbtn.io/rltoken/cmfi9C_nRXrmnwaJfCPyxA" target="_blank">SQLAlchemy Tutorial</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/HgODLwDN3uGIoo-mf84jeQ" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>Why Python programming is awesome</li>
<li>How to connect to a MySQL database from a Python script</li>
<li>How to&nbsp;<code>SELECT</code>&nbsp;rows in a MySQL table from a Python script</li>
<li>How to&nbsp;<code>INSERT</code>&nbsp;rows in a MySQL table from a Python script</li>
<li>What ORM means</li>
<li>How to map a Python Class to a MySQL table</li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
<li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using&nbsp;<code>python3</code>&nbsp;(version 3.8.5)</li>
<li>Your files will be executed with&nbsp;<code>MySQLdb</code>&nbsp;version&nbsp;<code>2.0.x</code></li>
<li>Your files will be executed with&nbsp;<code>SQLAlchemy</code>&nbsp;version&nbsp;<code>1.4.x</code></li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/python3</code></li>
<li>A&nbsp;<code>README.md</code>&nbsp;file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version&nbsp;<code>2.8.*</code>)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using&nbsp;<code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code>&nbsp;and&nbsp;<code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
<li>You are not allowed to use&nbsp;<code>execute</code>&nbsp;with sqlalchemy</li>
</ul>
<h2>More Info</h2>
<h3>Install&nbsp;<code>MySQLdb</code>&nbsp;module version&nbsp;<code>2.0.x</code></h3>
<p>For installing&nbsp;<code>MySQLdb</code>, you need to have&nbsp;<code>MySQL</code>&nbsp;installed:&nbsp;<a title="How to install MySQL 8.0 in Ubuntu 20.04" href="https://intranet.hbtn.io/rltoken/mqTU28SAIfz_-9w7rZipMw" target="_blank">How to install MySQL 8.0 in Ubuntu 20.04</a></p>
<pre><code>$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
&gt;&gt;&gt; import MySQLdb
&gt;&gt;&gt; MySQLdb.version_info 
(2, 0, 3, 'final', 0)
</code></pre>
<h3>Install&nbsp;<code>SQLAlchemy</code>&nbsp;module version&nbsp;<code>1.4.x</code></h3>
<pre><code>$ sudo pip3 install SQLAlchemy
...
$ python3
&gt;&gt;&gt; import sqlalchemy
&gt;&gt;&gt; sqlalchemy.__version__ 
'1.4.22'
</code></pre>
<p>Also, you can have this warning message:</p>
<pre><code>/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
</code></pre>
<p>You can ignore it.</p>