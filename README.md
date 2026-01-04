<!--
  Auto-generated file. Do not edit directly.
  Edit /home/jcook/Documents/git_repo/python3-cookiecutter/docs/jekyll/README.md instead.
  Run ```make readme``` to regenerate this file
-->
<h1 id="python3-cookiecutter">python3-cookiecutter</h1>

<p><strong>Author:</strong> Jared Cook<br />
<strong>Version:</strong> 0.1.0</p>

<h2 id="overview">Overview</h2>
<p>Python3 cookiecutter template project + Github docs template generation + Sphinx docs template generation.</p>

<hr />

<p><img src="https://github.com/jcook3701/python3-cookiecutter/actions/workflows/dependency-check.yml/badge.svg" alt="dependency-check" />
<img src="https://github.com/jcook3701/python3-cookiecutter/actions/workflows/format-check.yml/badge.svg" alt="format-check" />
<img src="https://github.com/jcook3701/python3-cookiecutter/actions/workflows/lint-check.yml/badge.svg" alt="lint-check" />
<img src="https://github.com/jcook3701/python3-cookiecutter/actions/workflows/security-audit.yml/badge.svg" alt="security-audit" />
<img src="https://github.com/jcook3701/python3-cookiecutter/actions/workflows/spellcheck.yml/badge.svg" alt="spellcheck" />
<img src="https://github.com/jcook3701/python3-cookiecutter/actions/workflows/tests.yml/badge.svg" alt="tests" />
<img src="https://github.com/jcook3701/python3-cookiecutter/actions/workflows/typecheck.yml/badge.svg" alt="typecheck" /></p>

<hr />

<p><strong>Note:</strong> Unless you are using a newer version of cookiecutter &gt;= 2, <code class="language-plaintext highlighter-rouge">--no-input</code> is necessary for template generation without error.</p>

<ol>
  <li>Pull Project with cookiecutter command:
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cookiecutter git@github.com:jcook3701/python3-cookiecutter.git <span class="se">\</span>
 <span class="nt">--no-input</span> <span class="se">\</span>
 <span class="nv">project_name</span><span class="o">=</span><span class="s2">"test-project"</span>  
</code></pre></div>    </div>
  </li>
</ol>

<h2 id="development">Development</h2>

<ol>
  <li>Pull code from development branch while testing updates.</li>
</ol>

<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cookiecutter git@github.com:jcook3701/python3-cookiecutter.git <span class="se">\</span>
	 <span class="nt">--checkout</span> develop <span class="se">\</span>
	  <span class="nt">--no-input</span> <span class="se">\</span>
	  <span class="nv">project_name</span><span class="o">=</span><span class="s2">"test-project"</span>
</code></pre></div></div>
<p>replace <code class="language-plaintext highlighter-rouge">test-project</code> or any of the other variables with real context configuration variables:</p>

<h3 id="future-ideas">Future Ideas:</h3>
<ol>
  <li><a href="https://cookiecutter.readthedocs.io/en/latest/advanced/directories.html#organizing-cookiecutters-in-directories">Organizing cookiecutters in directories</a>
    <ul>
      <li>Add freecad paths for freecad projects.</li>
      <li>etc.</li>
    </ul>
  </li>
  <li>Create python repository to make it easy to swap nested vars but might eventually use newer version of cookiecutter from pypi.</li>
  <li>Update configuration file to include or disclude the Dockerfile (Only needed for webapps)</li>
  <li>Create seperate repo to utilze cookiecutter 1.7 with custom json config inorder to update pyproject.toml variables in ‘config’ variable.</li>
</ol>

<h3 id="authors-notes">Authors Notes:</h3>
<ol>
  <li>This code currently works with cookiecutter 1.7 from Ubuntu’s apt repositories.</li>
</ol>
