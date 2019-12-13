---
layout: page
title: Download
sorted: 3

sources:
  - name: Linux
    icon: /assets/img/tux.png
    description: >
        !SITE_TITLE! is already available on majority of Linux distriutions. You
        can install it from the KDE Software Center.
  - name: Release Sources
    icon: /assets/img/ark.svg
    description: >
        !SITE_TITLE! is released regularily as part of KDE Applications. You can 
        find !SITE_TITLE! latest stable realease among the 
        <a href="https://download.kde.org/stable/applications">tarballs from
        the latest KDE Applications release</a>.

        If you want to build !SITE_TITLE! from sources, we recommend checking our
        <a href="get-involved.html">Getting Involved</a> page which contains
        links to full guide how to compile !SITE_TITLE!.
  - name: Git
    icon: /assets/img/git.svg
    description: >
        !SITE_TITLE! git repository can be viewed
        <a href="!SITE_GIT!">using cgit</a>.

        To clone !SITE_TITLE! uses <code>git clone !SITE_GIT!</code>. for
        detailed instructions how to build !SITE_TITLE! from source, check
        the <a href="get-involved.html">Getting Involved page</a>
---

<h1>Download</h1>

<table class="distribution-table">
{% for source in page.sources %}
    <tr class="title-row">
        <td rowspan="2" width="100">
            <img src="{{ source.icon }}" alt="{{ source.name }}">
        </td>
        <th>{{ source.name }}</th>
    </tr>
    <tr>
        <td>{{ source.description | replace: '!SITE_TITLE!', site.title | replace: '!SITE_GIT!', site.git}}</td>
    </tr>
{% endfor %}
</table>
