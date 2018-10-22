
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <meta name="viewport" content="initial-scale=1.0,user-scalable=no,maximum-scale=1,width=device-width">
  <meta name="viewport" content="initial-scale=1.0,user-scalable=no,maximum-scale=1" media="(device-height: 568px)">
  <meta name="selected-link" value="repo_source">

  
<meta name="octolytics-dimension-device" content="mobile" />
<meta name="octolytics-dimension-user_id" content="4343403" /><meta name="octolytics-dimension-user_login" content="chinoogawa" /><meta name="octolytics-dimension-repository_id" content="15218683" /><meta name="octolytics-dimension-repository_nwo" content="chinoogawa/fbht" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="15218683" /><meta name="octolytics-dimension-repository_network_root_nwo" content="chinoogawa/fbht" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


<meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="6456:7D42:B7B17:154E9C:5BCD4DFF" /><meta name="octolytics-dimension-region_edge" content="iad" /><meta name="octolytics-dimension-region_render" content="iad" /><meta name="octolytics-actor-id" content="44348666" /><meta name="octolytics-actor-login" content="Laratutors" /><meta name="octolytics-actor-hash" content="bb32af2019db588506bafd15a9671875bbc989f3831d2e1b7696d17bc381294d" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">

  <meta class="js-ga-set" name="userId" content="101ec04cc1511d3ae6d6b2eec576e026" %>

<meta class="js-ga-set" name="dimension1" content="Logged In">

  <meta class="js-ga-set" name="dimension3" content="mobile">


  

  <title>fbht/database.py at master · chinoogawa/fbht</title>

  <link crossorigin="anonymous" media="all" integrity="sha512-bx1vLXTAi7xgAHHOuC1IUjb8oPPfUtFE44qrR8cDqaMKnyuyw+uI/AIxSwMpDXUcg6Dg1wsAzQucOzyoW+nXgA==" rel="stylesheet" href="https://assets-cdn.github.com/assets/mobile-8f356e9dba0dd50a11d4f9f905dbb30b.css" />


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">



  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="page-responsive">
    


  <header class="Header f5 lh-default clearfix">
    <div class="p-responsive flex-justify-between">
        <div class="d-flex flex-justify-between flex-items-center position-absolute right-0 left-0 px-3 mt-1">
          <div class="d-flex mx-2"><!-- placeholder for hamburger --></div>
          <div class="px-3 overflow-hidden">
                <div class="css-truncate css-truncate-target width-fit">
    <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
    <strong>
      <a class="text-white" href="/chinoogawa">chinoogawa</a>
    </strong> /
    <strong>
      <a class="text-white" href="/chinoogawa/fbht">fbht</a>
    </strong>
  </div>

          </div>

          <div class="d-flex">
            
              <a class="position-relative notification-indicator ml-3" href="/notifications"
                    aria-label="You have no unread notifications"
                  data-ga-click="Mobile, tap, location:header; text:Notifications">
                <span class="mail-status "></span>
                <svg height="16" class="octicon octicon-bell" viewBox="0 0 14 16" version="1.1" width="14" aria-hidden="true"><path fill-rule="evenodd" d="M13.99 11.991v1H0v-1l.73-.58c.769-.769.809-2.547 1.189-4.416.77-3.767 4.077-4.996 4.077-4.996 0-.55.45-1 .999-1 .55 0 1 .45 1 1 0 0 3.387 1.229 4.156 4.996.38 1.879.42 3.657 1.19 4.417l.659.58h-.01zM6.995 15.99c1.11 0 1.999-.89 1.999-1.999H4.996c0 1.11.89 1.999 1.999 1.999z"/></svg>
              </a>
          </div>
        </div>


        <details class="details-reset">
          <summary class="mt-1 float-left position-relative user-select-none" data-ga-click="Mobile, tap, location:header; text:Hamburger">
            <svg height="24" class="octicon octicon-three-bars notification-indicator" viewBox="0 0 12 16" version="1.1" width="18" aria-hidden="true"><path fill-rule="evenodd" d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"/></svg>
          </summary>
              <div style="clear: both;">
        <div class="py-3">
          <div class="header-search scoped-search site-scoped-search js-site-search position-relative "
  role="search"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" data-scope-type="Repository" data-scope-id="15218683" data-scoped-search-url="/chinoogawa/fbht/search" data-unscoped-search-url="/search" action="/chinoogawa/fbht/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control header-search-wrapper  js-chromeless-input-container">
            <a class="header-search-scope no-underline" href="/chinoogawa/fbht/blob/master/database.py">This repository</a>
        <input type="text"
          class="form-control header-search-input  js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search"
          data-unscoped-placeholder="Search GitHub"
          data-scoped-placeholder="Search"
          autocapitalize="off"
          aria-label="Search this repository"
          >
          <input type="hidden" class="js-site-search-type-field" name="type" >
      </label>
</form>  </div>
</div>

        </div>
      <ul class="text-bold list-style-none p-0 m-0">
            <li>
              <a href="/" data-ga-click="Mobile, tap, location:header; text:Dashboard" class="js-selected-navigation-item HeaderNavlink py-2 mt-3">
                Dashboard
              </a>
            </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink py-2" href="/pulls">
                Pull requests
</a>            </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink py-2" href="/issues">
                Issues
</a>            </li>
              <li>
                <a class="js-selected-navigation-item HeaderNavlink py-2" data-ga-click="Mobile, tap, location:header; text:Marketplace" href="/marketplace">
                  Marketplace
</a>              </li>
          <li>
            <a href="/explore" data-ga-click="Mobile, tap, location:header; text:Explore" class="js-selected-navigation-item HeaderNavlink py-2">
              Explore
            </a>
          </li>
            <li>
              <a href="/Laratutors" data-ga-click="Mobile, tap, location:header; text:User avatar" class="js-selected-navigation-item HeaderNavlink py-2">
                <img class="avatar" src="https://avatars2.githubusercontent.com/u/44348666?s=40&amp;v=4" width="20" height="20" alt="@Laratutors" />
                Laratutors
              </a>
            </li>
            <li>
              <a href="/logout" data-ga-click="Mobile, tap, location:header; text:Sign out" class="HeaderNavlink py-2" style="padding-left: 2px;">
                <svg style="margin-right: 2px;" class="octicon octicon-sign-out v-align-middle" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11.992 8.994V6.996H7.995v-2h3.997V2.999l3.998 2.998-3.998 2.998zm-1.998 2.998H5.996V2.998L2 1h7.995v2.998h1V1c0-.55-.45-.999-1-.999H.999A1.001 1.001 0 0 0 0 1v11.372c0 .39.22.73.55.91L5.996 16v-3.008h3.998c.55 0 1-.45 1-1V7.995h-1v3.997z"/></svg>
                Sign out
              </a>
            </li>
      </ul>
    </div>

        </details>
    </div>
  </header>

    



    




<div class="reponav-wrapper lh-default">
  <nav class="reponav js-reponav"
       itemscope
       itemtype="http://schema.org/BreadcrumbList">

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /chinoogawa/fbht" href="/chinoogawa/fbht">
        <span itemprop="name">Code</span>
        <meta itemprop="position" content="1">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /chinoogawa/fbht/issues" href="/chinoogawa/fbht/issues">
          <span itemprop="name">Issues</span>
          <span class="Counter">3</span>
          <meta itemprop="position" content="2">
</a>      </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /chinoogawa/fbht/pulls" href="/chinoogawa/fbht/pulls">
        <span itemprop="name">Pull requests</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="3">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links=" /chinoogawa/fbht/projects" href="/chinoogawa/fbht/projects">
          <span itemprop="name">Projects</span>
          <span class="Counter">0</span>
          <meta itemprop="position" content="4">
</a>      </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links=" /chinoogawa/fbht/wiki" href="/chinoogawa/fbht/wiki">
          <span itemprop="name">Wiki</span>
          <meta itemprop="position" content="5">
</a>      </span>

    <a class="js-selected-navigation-item reponav-item" data-selected-links="pulse /chinoogawa/fbht/pulse" href="/chinoogawa/fbht/pulse">
      Pulse
</a>
  </nav>
</div>

<div id="js-flash-container">


</div>




<div class="breadcrumb blob-breadcrumb">
  <label for="blob-history-checkbox" class="blob-history-label">
    <svg class="octicon octicon-history" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 13H6V6h5v2H8v5zM7 1C4.81 1 2.87 2.02 1.59 3.59L0 2v4h4L2.5 4.5C3.55 3.17 5.17 2.3 7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-.34.03-.67.09-1H.08C.03 7.33 0 7.66 0 8c0 3.86 3.14 7 7 7s7-3.14 7-7-3.14-7-7-7z"/></svg>
  </label>
  <span class="filetype-icon"><svg class="octicon octicon-file" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z"/></svg></span>
  <strong class="final-path">database.py</strong>
</div>


<input id="blob-history-checkbox"
       class="js-blob-history-checkbox blob-history-checkbox"
       type="checkbox"
       data-url="/chinoogawa/fbht/latest_commit/master/database.py">

<div class="blob-history">
  <a class="js-blob-history-link" href="/chinoogawa/fbht/commits/master/database.py">
    Loading latest commit…
</a></div>

  <div class="blob-file-content js-file-line-container">
    <div class="highlighted-blob tab-size" data-tab-size="8"><div class="code-body highlight"><pre><div class='line js-file-line' id='LC1'><span class="pl-k">import</span> sqlite3 <span class="pl-k">as</span> db</div><div class='line js-file-line' id='LC2'><br></div><div class='line js-file-line' id='LC3'><span class="pl-k">try</span>:</div><div class='line js-file-line' id='LC4'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">global</span> connect, cursor, rows</div><div class='line js-file-line' id='LC5'>&nbsp;&nbsp;&nbsp;&nbsp;connect <span class="pl-k">=</span> db.connect(<span class="pl-s"><span class="pl-pds">&quot;</span>fb_db.db<span class="pl-pds">&quot;</span></span>,<span class="pl-v">check_same_thread</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>)</div><div class='line js-file-line' id='LC6'>&nbsp;&nbsp;&nbsp;&nbsp;cursor <span class="pl-k">=</span> connect.cursor()</div><div class='line js-file-line' id='LC7'><span class="pl-k">except</span>:</div><div class='line js-file-line' id='LC8'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Error handling Database<span class="pl-pds">&#39;</span></span></div><div class='line js-file-line' id='LC9'><br></div><div class='line js-file-line' id='LC10'><span class="pl-k">def</span> <span class="pl-en">insertTestUsers</span>(<span class="pl-smi">userId</span>,<span class="pl-smi">name</span>,<span class="pl-smi">email</span>,<span class="pl-smi">password</span>):</div><div class='line js-file-line' id='LC11'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">len</span>(email)):</div><div class='line js-file-line' id='LC12'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">try</span>:</div><div class='line js-file-line' id='LC13'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(<span class="pl-s"><span class="pl-pds">&quot;</span>INSERT INTO testUsers (id, name, email, password,logged, blocked) VALUES(?, ?, ?, ?,0,0)<span class="pl-pds">&quot;</span></span>, (userId[i], name[i], email[i], password[i]))</div><div class='line js-file-line' id='LC14'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">except</span>:</div><div class='line js-file-line' id='LC15'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>No se realizo la iteracion <span class="pl-c1">%d</span> <span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> i</div><div class='line js-file-line' id='LC16'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line js-file-line' id='LC17'>&nbsp;&nbsp;&nbsp;&nbsp;connect.commit()</div><div class='line js-file-line' id='LC18'><br></div><div class='line js-file-line' id='LC19'><span class="pl-k">def</span> <span class="pl-en">insertTestUsersDev</span>(<span class="pl-smi">userId</span>,<span class="pl-smi">name</span>):</div><div class='line js-file-line' id='LC20'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">len</span>(userId)):</div><div class='line js-file-line' id='LC21'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">try</span>:</div><div class='line js-file-line' id='LC22'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(<span class="pl-s"><span class="pl-pds">&quot;</span>INSERT INTO testUsers (id, name, email, password,logged, blocked) VALUES(?, ?, 0, 1234567890,0,0)<span class="pl-pds">&quot;</span></span>, (userId[i], name[i]))</div><div class='line js-file-line' id='LC23'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">except</span>:</div><div class='line js-file-line' id='LC24'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>No se realizo la iteracion <span class="pl-c1">%d</span> <span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> i</div><div class='line js-file-line' id='LC25'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line js-file-line' id='LC26'>&nbsp;&nbsp;&nbsp;&nbsp;connect.commit()</div><div class='line js-file-line' id='LC27'><br></div><div class='line js-file-line' id='LC28'><span class="pl-k">def</span> <span class="pl-en">removeTestUsers</span>(<span class="pl-smi">userId</span>):</div><div class='line js-file-line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;query <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>DELETE FROM testUsers WHERE id = <span class="pl-c1">%d</span>;<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> <span class="pl-c1">int</span>(userId)</div><div class='line js-file-line' id='LC30'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">try</span>:</div><div class='line js-file-line' id='LC31'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(query)</div><div class='line js-file-line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\r</span>Succesfull deleted <span class="pl-c1">%d</span>                                    <span class="pl-cce">\r</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> <span class="pl-c1">int</span>(userId),</div><div class='line js-file-line' id='LC33'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">except</span>:</div><div class='line js-file-line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>No se pudo eliminar el id de usuario <span class="pl-c1">%d</span>                    <span class="pl-cce">\r</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> <span class="pl-c1">int</span>(userId),</div><div class='line js-file-line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>             </div><div class='line js-file-line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;connect.commit()</div><div class='line js-file-line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line js-file-line' id='LC38'><span class="pl-k">def</span> <span class="pl-en">getUsers</span>():</div><div class='line js-file-line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(<span class="pl-s"><span class="pl-pds">&quot;</span>SELECT * FROM testUsers;<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;rows <span class="pl-k">=</span> cursor.fetchall()</div><div class='line js-file-line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">return</span> rows</div><div class='line js-file-line' id='LC42'><br></div><div class='line js-file-line' id='LC43'><span class="pl-k">def</span> <span class="pl-en">setLogged</span>(<span class="pl-smi">c_user</span>):</div><div class='line js-file-line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;query <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>UPDATE testUsers SET logged=1 WHERE id = <span class="pl-c1">%d</span>;<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> <span class="pl-c1">int</span>(c_user)</div><div class='line js-file-line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">try</span>:</div><div class='line js-file-line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(query)</div><div class='line js-file-line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">except</span>:</div><div class='line js-file-line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Error en setLogged() <span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>  </div><div class='line js-file-line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line js-file-line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;connect.commit()</div><div class='line js-file-line' id='LC51'><br></div><div class='line js-file-line' id='LC52'><span class="pl-k">def</span> <span class="pl-en">setLoggedOut</span>(<span class="pl-smi">c_user</span>):</div><div class='line js-file-line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;query <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>UPDATE testUsers SET logged=0 WHERE id = <span class="pl-c1">%d</span>;<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> <span class="pl-c1">int</span>(c_user)</div><div class='line js-file-line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">try</span>:</div><div class='line js-file-line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(query)</div><div class='line js-file-line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">except</span>:</div><div class='line js-file-line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Error en setLogged() <span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>  </div><div class='line js-file-line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line js-file-line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;connect.commit()</div><div class='line js-file-line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line js-file-line' id='LC61'><span class="pl-k">def</span> <span class="pl-en">status</span>():</div><div class='line js-file-line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;queries <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>SELECT count(*) FROM testUsers;<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>SELECT count(*) FROM testUsers WHERE logged=0;<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>SELECT count(*) FROM testUsers WHERE logged=1;<span class="pl-pds">&quot;</span></span>,</div><div class='line js-file-line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-s"><span class="pl-pds">&quot;</span>SELECT count(*) FROM testUsers WHERE blocked=1;<span class="pl-pds">&quot;</span></span>]</div><div class='line js-file-line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">try</span>:</div><div class='line js-file-line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">for</span> query <span class="pl-k">in</span> queries:</div><div class='line js-file-line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(query)</div><div class='line js-file-line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;row <span class="pl-k">=</span> cursor.fetchall()</div><div class='line js-file-line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">for</span> rows <span class="pl-k">in</span> row:</div><div class='line js-file-line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>The query: <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> query <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span> dump the result: <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (rows,) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span></div><div class='line js-file-line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">except</span>:</div><div class='line js-file-line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Error in status() <span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span> </div><div class='line js-file-line' id='LC72'><br></div><div class='line js-file-line' id='LC73'><span class="pl-k">def</span> <span class="pl-en">getUsersNotLogged</span>():</div><div class='line js-file-line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(<span class="pl-s"><span class="pl-pds">&quot;</span>SELECT * FROM testUsers WHERE logged=0;<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;rows <span class="pl-k">=</span> cursor.fetchall()</div><div class='line js-file-line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">return</span> rows</div><div class='line js-file-line' id='LC77'><br></div><div class='line js-file-line' id='LC78'><span class="pl-k">def</span> <span class="pl-en">createVictimTable</span>(<span class="pl-smi">victim</span>):</div><div class='line js-file-line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">try</span>:</div><div class='line js-file-line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;victim <span class="pl-k">=</span> victim.replace(<span class="pl-s"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>_<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(<span class="pl-s"><span class="pl-pds">&quot;</span>CREATE TABLE <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(victim)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>_nodes(friendName text, friendId text)<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(<span class="pl-s"><span class="pl-pds">&quot;</span>CREATE TABLE <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(victim)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>_friends_edges(friendName text, friendId text, edges text, edgesIDS text)<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">except</span>:</div><div class='line js-file-line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Error al crear la tabla<span class="pl-pds">&#39;</span></span></div><div class='line js-file-line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">return</span> <span class="pl-k">-</span><span class="pl-c1">1</span></div><div class='line js-file-line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;connect.commit()</div><div class='line js-file-line' id='LC87'><br></div><div class='line js-file-line' id='LC88'><span class="pl-k">def</span> <span class="pl-en">addNode</span>(<span class="pl-smi">victim</span>,<span class="pl-smi">friendName</span>, <span class="pl-smi">friendId</span>):</div><div class='line js-file-line' id='LC89'><br></div><div class='line js-file-line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">try</span>:</div><div class='line js-file-line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;victim <span class="pl-k">=</span> victim.replace(<span class="pl-s"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>_<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">if</span> (checkNodeExistence(victim, friendName, friendId) <span class="pl-k">==</span> <span class="pl-c1">False</span>):</div><div class='line js-file-line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(<span class="pl-s"><span class="pl-pds">&quot;</span>INSERT INTO <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(victim)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>_nodes (friendName, friendId) VALUES(?, ?)<span class="pl-pds">&quot;</span></span>, (friendName, friendId))</div><div class='line js-file-line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(<span class="pl-s"><span class="pl-pds">&quot;</span>INSERT INTO <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(victim)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>_friends_edges (friendName, friendId) VALUES(?, ?)<span class="pl-pds">&quot;</span></span>, (friendName, friendId))</div><div class='line js-file-line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">except</span>:</div><div class='line js-file-line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Error al ingresar el nodo <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span>friendName</div><div class='line js-file-line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line js-file-line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;connect.commit()</div><div class='line js-file-line' id='LC99'><br></div><div class='line js-file-line' id='LC100'><span class="pl-k">def</span> <span class="pl-en">addEdge</span>(<span class="pl-smi">victim</span>,<span class="pl-smi">friendName</span>, <span class="pl-smi">friendId</span>, <span class="pl-smi">edge</span>, <span class="pl-smi">edgeID</span>):</div><div class='line js-file-line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">if</span> checkNodeExistence(victim,friendName, friendId) <span class="pl-k">==</span> <span class="pl-c1">True</span>:</div><div class='line js-file-line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">try</span>:</div><div class='line js-file-line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;victim <span class="pl-k">=</span> victim.replace(<span class="pl-s"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>_<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(<span class="pl-s"><span class="pl-pds">&quot;</span>SELECT edges FROM <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(victim)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>_friends_edges WHERE friendName=<span class="pl-cce">\&quot;</span><span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(friendName)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\&quot;</span> OR friendId=<span class="pl-cce">\&quot;</span><span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(friendId)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\&quot;</span>;<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rows <span class="pl-k">=</span> <span class="pl-c1">str</span>(cursor.fetchone()).strip(<span class="pl-s"><span class="pl-pds">&quot;</span>(None,)<span class="pl-pds">&quot;</span></span>).strip(<span class="pl-s"><span class="pl-pds">&quot;</span>&#39;<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rows <span class="pl-k">=</span> rows.encode(<span class="pl-s"><span class="pl-pds">&#39;</span>ascii<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>replace<span class="pl-pds">&#39;</span></span>) <span class="pl-k">+</span> edge <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>;<span class="pl-pds">&quot;</span></span></div><div class='line js-file-line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(<span class="pl-s"><span class="pl-pds">&quot;</span>UPDATE <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(victim)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>_friends_edges SET edges=<span class="pl-cce">\&quot;</span><span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>rows<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\&quot;</span> WHERE friendName=<span class="pl-cce">\&quot;</span><span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(friendName)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\&quot;</span> OR friendId=<span class="pl-cce">\&quot;</span><span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(friendId)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\&quot;</span>;<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(<span class="pl-s"><span class="pl-pds">&quot;</span>SELECT edgesIDS FROM <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(victim)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>_friends_edges WHERE friendName=<span class="pl-cce">\&quot;</span><span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(friendName)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\&quot;</span> OR friendId=<span class="pl-cce">\&quot;</span><span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(friendId)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\&quot;</span>;<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rows <span class="pl-k">=</span> <span class="pl-c1">str</span>(cursor.fetchone()).strip(<span class="pl-s"><span class="pl-pds">&quot;</span>(None,)<span class="pl-pds">&quot;</span></span>).strip(<span class="pl-s"><span class="pl-pds">&quot;</span>&#39;<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rows <span class="pl-k">=</span> rows.encode(<span class="pl-s"><span class="pl-pds">&#39;</span>ascii<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>replace<span class="pl-pds">&#39;</span></span>) <span class="pl-k">+</span> edgeID <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>;<span class="pl-pds">&quot;</span></span></div><div class='line js-file-line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(<span class="pl-s"><span class="pl-pds">&quot;</span>UPDATE <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(victim)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>_friends_edges SET edgesIDS=<span class="pl-cce">\&quot;</span><span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>rows<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\&quot;</span> WHERE friendName=<span class="pl-cce">\&quot;</span><span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(friendName)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\&quot;</span> OR friendId=<span class="pl-cce">\&quot;</span><span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(friendId)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\&quot;</span>;<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line js-file-line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">except</span> db.Error <span class="pl-k">as</span> e:</div><div class='line js-file-line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>An error occurred:<span class="pl-pds">&quot;</span></span>, e.args[<span class="pl-c1">0</span>]</div><div class='line js-file-line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line js-file-line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">except</span>:</div><div class='line js-file-line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Error al hacer update para el nodo <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span>edge</div><div class='line js-file-line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line js-file-line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connect.commit()</div><div class='line js-file-line' id='LC120'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">else</span>:</div><div class='line js-file-line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">return</span> <span class="pl-k">-</span><span class="pl-c1">1</span></div><div class='line js-file-line' id='LC122'><br></div><div class='line js-file-line' id='LC123'><span class="pl-k">def</span> <span class="pl-en">getNodes</span>(<span class="pl-smi">victim</span>):</div><div class='line js-file-line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;victim <span class="pl-k">=</span> victim.replace(<span class="pl-s"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>_<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(<span class="pl-s"><span class="pl-pds">&quot;</span>SELECT * FROM <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(victim)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>_nodes;<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;rows <span class="pl-k">=</span> cursor.fetchall()</div><div class='line js-file-line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">return</span> rows</div><div class='line js-file-line' id='LC128'><br></div><div class='line js-file-line' id='LC129'><span class="pl-k">def</span> <span class="pl-en">getEdges</span>(<span class="pl-smi">victim</span>, <span class="pl-smi">friendName</span>, <span class="pl-smi">friendId</span>):</div><div class='line js-file-line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;victim <span class="pl-k">=</span> victim.replace(<span class="pl-s"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>_<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(<span class="pl-s"><span class="pl-pds">&quot;</span>SELECT * FROM <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(victim)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>_friends_edges WHERE friendName=<span class="pl-cce">\&quot;</span><span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(friendName)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\&quot;</span> OR friendId=<span class="pl-cce">\&quot;</span><span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(friendId)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\&quot;</span>;<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;rows <span class="pl-k">=</span> cursor.fetchall()</div><div class='line js-file-line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">return</span> rows    </div><div class='line js-file-line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line js-file-line' id='LC135'><span class="pl-k">def</span> <span class="pl-en">checkNodeExistence</span>(<span class="pl-smi">victim</span>, <span class="pl-smi">friendName</span>, <span class="pl-smi">friendId</span>):</div><div class='line js-file-line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;victim <span class="pl-k">=</span> victim.replace(<span class="pl-s"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>_<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(<span class="pl-s"><span class="pl-pds">&quot;</span>SELECT * FROM <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(victim)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>_nodes WHERE friendName=<span class="pl-cce">\&quot;</span><span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(friendName)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\&quot;</span> OR friendId=<span class="pl-cce">\&quot;</span><span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(friendId)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\&quot;</span>;<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;rows <span class="pl-k">=</span> cursor.fetchall()</div><div class='line js-file-line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">if</span> rows <span class="pl-k">!=</span> []:</div><div class='line js-file-line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">return</span> <span class="pl-c1">True</span></div><div class='line js-file-line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">else</span>:</div><div class='line js-file-line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">return</span> <span class="pl-c1">False</span></div><div class='line js-file-line' id='LC143'><br></div><div class='line js-file-line' id='LC144'><span class="pl-k">def</span> <span class="pl-en">checkTableExistence</span>(<span class="pl-smi">victim</span>):</div><div class='line js-file-line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">try</span>:</div><div class='line js-file-line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(<span class="pl-s"><span class="pl-pds">&quot;</span>SELECT count(*) FROM <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>victim.replace(<span class="pl-s"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>_<span class="pl-pds">&quot;</span></span>)<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>_nodes;<span class="pl-pds">&quot;</span></span>)</div><div class='line js-file-line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;res <span class="pl-k">=</span> cursor.fetchone()</div><div class='line js-file-line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">return</span> <span class="pl-c1">bool</span>(res[<span class="pl-c1">0</span>])</div><div class='line js-file-line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">except</span>:</div><div class='line js-file-line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">return</span> <span class="pl-c1">False</span></div></pre></div></div>
  </div>


  <footer class="clearfix">
    <div class="container">
      <a href="#"><svg height="32" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg></a>

      <ul class="clearfix">
        <li>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-mobile-preference-form" action="/site/mobile_preference" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="R37wJ9RaWfu3eZJkVMa+5dNduC32ciOwMhFT1DUarECtJ4r7hvpuvHPYPLPq29ai2RmcGaF0QLBC7QeizZcd0A==" />
            <input type="hidden" name="mobile" value="false">
            <input type="hidden" name="anchor" class="js-mobile-preference-anchor-field">

            <button type="submit" class="switch-to-desktop" data-ga-click="Mobile, switch to desktop, switch button">
              Desktop version
            </button>
</form>        </li>
        <li>
          <a href="/logout" data-ga-click="Mobile, tap, location:header; text:Sign out">
            Sign out
          </a>
        </li>
      </ul>
    </div>
  </footer>
  
    <script crossorigin="anonymous" async="async" integrity="sha512-mIReH+yA7eVQ/ft+uEISUOeBTAulN6Y03IPf4vZttq4l6FlOt3sl8uJ0s/7fQE2cqCSKbsJRtatRji3l+LZFFQ==" type="application/javascript" src="https://assets-cdn.github.com/assets/mobile-5be8a940455efa95c152e49c8abca017.js"></script>

  </body>
</html>
