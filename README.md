<!--
  Auto-generated file. Do not edit directly.
  Edit /home/jcook/Documents/git_repo/python3-cookiecutter/docs/jekyll/README.md instead.
  Run ```make readme``` to regenerate this file
-->
<h1 id="python3-cookiecutter">python3-cookiecutter</h1>

<p><a href="LICENSE.md"><img src="https://img.shields.io/github/license/jcook3701/python3-cookiecutter" alt="License" /></a></p>

<p><strong>Author:</strong> Jared Cook<br />
<strong>Version:</strong> 0.1.0</p>

<h2 id="overview">Overview</h2>
<p>Python3 cookiecutter template project + Github docs template generation + Sphinx docs template generation.</p>

<p><strong>Utilizes:</strong><br />
The <strong>python3-cookiecutter</strong> depends on the following repositories for its documentation and sub-features.</p>

<ul>
  <li><a href="https://github.com/jcook3701/cookiecutter-cookiecutter">cookiecutter-cookiecutter</a> is the the parent repository for python3-cookiecutter.  Updates from <code class="language-plaintext highlighter-rouge">cookiecutter_project_upgrader</code> are pulled from this repository.</li>
  <li><a href="https://github.com/jcook3701/github-docs-cookiecutter">Github docs</a> cookiecutter template generation for Github Pages (Jekyll).</li>
  <li><a href="https://github.com/jcook3701/sphinx-cookiecutter">Sphinx docs</a> cookiecutter template generation for Python Sphinx Documentation.</li>
  <li><a href="https://github.com/jcook3701/nutri-matic">Nutri-Matic</a> cookiecutter utilities for streamlining development and utilization of Cookiecutter templates.</li>
</ul>

<p><strong>Maintains:</strong><br />
The <strong>python3-cookiecutter</strong> is used to maintain the build and ci/cd structure for the following projects.</p>

<ul>
  <li><strong><a href="https://github.com/jcook3701/nutri-matic">Nutri-Matic</a></strong> cookiecutter utilities for streamlining development and utilization of Cookiecutter templates.</li>
</ul>

<hr />

<p>🛠️ <strong>CI/CD Check List:</strong></p>

<ul>
  <li><img src="https://github.com/jcook3701/python3-cookiecutter/actions/workflows/dependency-check.yml/badge.svg" alt="dependency-check" /></li>
  <li><img src="https://github.com/jcook3701/python3-cookiecutter/actions/workflows/format-check.yml/badge.svg" alt="format-check" /></li>
  <li><img src="https://github.com/jcook3701/python3-cookiecutter/actions/workflows/lint-check.yml/badge.svg" alt="lint-check" /></li>
  <li><img src="https://github.com/jcook3701/python3-cookiecutter/actions/workflows/security-audit.yml/badge.svg" alt="security-audit" /></li>
  <li><img src="https://github.com/jcook3701/python3-cookiecutter/actions/workflows/spellcheck.yml/badge.svg" alt="spellcheck" /></li>
  <li><img src="https://github.com/jcook3701/python3-cookiecutter/actions/workflows/tests.yml/badge.svg" alt="tests" /></li>
  <li><img src="https://github.com/jcook3701/python3-cookiecutter/actions/workflows/typecheck.yml/badge.svg" alt="typecheck" /></li>
</ul>

<hr />

<p><strong>Note:</strong> Unless you are using a newer version of cookiecutter &gt;= 2, <code class="language-plaintext highlighter-rouge">--no-input</code> is necessary for template generation without error.</p>

<h2 id="usage-examples">Usage Examples</h2>

<p><strong>Example:</strong> Pull from main branch.<br />
<strong>Note:</strong> <a href="https://github.com/jcook3701/nutri-matic">Nutri-Matic</a> is needed in active python environment.</p>

<ol>
  <li>Pull Project with cookiecutter command:</li>
</ol>

<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cookiecutter git@github.com:jcook3701/python3-cookiecutter.git <span class="se">\</span>
	<span class="nt">--no-input</span> <span class="se">\</span>
	<span class="nv">project_name</span><span class="o">=</span><span class="s2">"test-project"</span>  
</code></pre></div></div>

<p><strong>Example:</strong> Pull from develop branch.</p>

<ol>
  <li>Pull code from development branch while testing updates.</li>
</ol>

<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cookiecutter git@github.com:jcook3701/python3-cookiecutter.git <span class="se">\</span>
	  <span class="nt">--checkout</span> develop <span class="se">\</span>
	  <span class="nt">--no-input</span> <span class="se">\</span>
	  <span class="nv">project_name</span><span class="o">=</span><span class="s2">"test-project"</span>
</code></pre></div></div>
<p>replace <code class="language-plaintext highlighter-rouge">test-project</code> or any of the other variables with real context configuration variables:</p>

<p><strong>Note:</strong> replace <code class="language-plaintext highlighter-rouge">test-project</code> or any of the other variables with real context configuration variables.</p>

<hr />

<h2 id="-getting-started">🌱 Getting Started</h2>

<ul>
  <li><a href="https://jcook3701.github.io/python3-cookiecutter/manual/setup-guide/requirements">Requirements</a></li>
  <li><a href="https://jcook3701.github.io/python3-cookiecutter/manual/introduction/installation-guide">Installation guide</a></li>
</ul>

<h2 id="-documentation">📚 Documentation</h2>

<p>The python3-cookiecutter documentation is available at <a href="https://jcook3701.github.io/python3-cookiecutter">docs</a>.</p>

<h2 id="-contributing">🤝 Contributing</h2>

<p>If you’re interested in contributing to the python3-cookiecutter project:</p>
<ul>
  <li>Start by reading the <a href="https://jcook3701.github.io/python3-cookiecutter/manual/developer-resources/contribute">contributing guide</a>.</li>
  <li>Learn how to setup your local environment, in our <a href="https://jcook3701.github.io/python3-cookiecutter/manual/contribute/developer-guide">developer guide</a>.</li>
  <li>Look through our <a href="https://jcook3701.github.io/python3-cookiecutter/manual/contribute/style-guides/index">style guide</a>.</li>
</ul>

<hr />

<h2 id="-authors-notes">🍹 Authors Notes</h2>

<ol>
  <li>This code currently works with cookiecutter (V2.6) from PyPi’s repositories.</li>
</ol>

<h2 id="️-license">⚖️ License</h2>

<p>Copyright (c) 2025-2026, Jared Cook</p>

<p>This project is licensed under the <strong>AGPL-3.0-or-later License</strong>.<br />
See the <a href="https://github.com/jcook3701/python3-cookiecutter/blob/master/LICENSE.md">LICENSE</a> file for the full license text.</p>

<p>SPDX-License-Identifier: AGPL-3.0-or-later</p>

<hr />

<!--
1. [Organizing cookiecutters in directories](https://cookiecutter.readthedocs.io/en/latest/advanced/directories.html#organizing-cookiecutters-in-directories)  
   * Add freecad paths for freecad projects.  
   * etc.  
2. Create python repository to make it easy to swap nested vars but might eventually use newer version of cookiecutter from pypi.  
3. Update configuration file to include or disclude the Dockerfile (Only needed for a webapp)
4. Create separate repo to utilize cookiecutter 1.7 with custom json config in order to update pyproject.toml variables in 'config' variable.  

-->
