---
layout: page
title: Download
sorted: 3

sources:
  - name: Debian
    icon: /assets/img/debian.png
    description: >
         <pre><code># apt-get install krusader </code></pre>
                <p class="important"><span class="normal"><b>Note:</b></span>This is supposed to work on any <a class="external" href="http://www.debian.org">Debian</a> based system like <a class="external" href="http://www.ubuntu.com">Ubuntu</a> or <a class="external" href="http://www.mepis.org/">Mepis</a> as well as other apt-get aware distributions such as <a class="external" href="http://altlinux.org/">ALT Linux</a>.</p>
                <p class="small">Related links: <a class="external" href="http://packages.debian.org/search?suite=default&amp;section=all&amp;arch=any&amp;searchon=names&amp;keywords=krusader">Packages.debian.org</a>, <a class="external" href="http://packages.ubuntu.com/search?searchon=names&amp;keywords=krusader">Packages.ubuntu.com</a></p> 
  - name: Gentoo
    icon: /assets/img/gentoo.svg
    description: >
        <pre><code># emerge krusader </code></pre>
                <p class="important"><span class="normal"><b>Note:</b></span>Refer to the official <a class="external" href='http://www.gentoo.org/doc/en/handbookhandbook-x86.xml?part=3&amp;chap=3'>Gentoo Handbook</a> if you intend to try the testing branch.</p>
                <p class="small">Related links: <a class="external" href="http://packages.gentoo.org/package/kde-misc/krusader">Packages.gentoo.org</a></p>
  - name: Fedora
    icon: /assets/img/fedoara.png
    description: >
        <pre><code># dnf install krusader </code></pre>
                    <p class="small">Related links: <a class="external" href="https://admin.fedoraproject.org/pkgdb/acls/name/krusader">Fedora package database</a></p> 
  - name: Mageia
    icon: /assets/img/mageia.png
    description: >
        <pre><code># urpmi krusader </code></pre>
                    <p class="small">Related links: <a class="external" href="https://wiki.mageia.org/en/URPMI">Mageia wiki</a></p>
                    <p class="normal small">                        More systems known to include Krusader:
                        <br /><a class="external" href="http://www.archlinux.org/packages/?q=krusader">Arch Linux</a>,&nbsp;
                        <a class="external" href="http://www.arc-team.com/archeos/">ArcheOS</a>,&nbsp;
                        <a class="external" href="http://www.arklinux.org">Ark Linux</a>,&nbsp;
                        <a class="external" href="http://www.freebsd.org/cgi/ports.cgi?query=krusader&amp;stype=all">FreeBSD</a>,&nbsp;
                        <a class="external" href="http://frugalware.org/packages.php?id=280">Frugalware Linux</a>,&nbsp;
                        <a class="external" href="http://kanotix.com/">Kanotix</a>,&nbsp;
                        <a class="external" href="http://www.lunar-linux.org">Lunar Linux</a>,&nbsp;
                        <a class="external" href="http://www.rocklinux.net/packages/krusader.html">ROCK Linux</a>,&nbsp;
                        <a class="external" href="http://www.openlx.com/">OpenLX</a>,&nbsp;
                        <a class="external" href="http://www.opensuse.org">openSUSE</a>,&nbsp;
                        <a class="external" href="http://www.knoppix.org/">Knoppix</a>,&nbsp;
                        <a class="external" href="http://www.linspire.com/lindows_products_details.php?package_name=krusader">Linspire</a>,&nbsp;
                        <a class="external" href="http://www.pclinuxos.com/">PCLinuxOS</a>,&nbsp;
                        <a class="external" href="http://www.altlinux.ru/">ALT Linux</a>,&nbsp;
                        <a class="external" href="http://www.sourcemage.org/">Source Mage</a></p>
        <h1>Extensions</h1>
        <p>Krusader can be extended with custom add-ons called <b>User Actions</b>. You can find existing extensions and share your own ones in the <a     class="external" href="https://store.kde.org/browse/cat/370/ord/top/">KDE store</a>. Note that all add-ons there are unofficial, use them with caution.</p>

---

<h1>Get your copy of the Krusader file manager</h1>
<div id="content">
                <p>Looking for a quick source download? Krusader comes in different flavors:</p>
                    <div id="branches" class="clearfix">
                        <div id="branch-stable" class="branch">
                            <div class="clearfix">
                                <div class="download-button">
                                    <div class="button">
                                        <div class="button-inner"><a class="stable" href="https://download.kde.org/stable/krusader/2.7.2/krusader-2.7.2.tar.xz.mirrorlist">Download stable version<br/><span class="release"><span class="important">Release</span>: 2.7.2</span></a></div> 
                                    </div>
                                    <p class="release-meta"><a href="../release/2.7.2/release_notes.txt">Release notes</a> | <a href="../release/2.7.2/changelog.txt">Changelog</a></p>
                                </div>
                                <p class="release-desc">The latest stable version of Krusader.
                                    <br />Mature and safe for everyday use.</p>
                            </div>
                        </div>
                        <div id="branch-unstable" class="branch">
                            <div class="clearfix">
                                <div class="download-button">
                                    <div class="button">
                                        <div class="button-inner"><a class="devel" href="https://phabricator.kde.org/source/krusader/clone/">Latest Git version<br /><span class="release"><span class="important">Development version</span>: 2.8.0-dev</span></a></div>
                                    </div>
                                </div>
                                <p class="release-desc">This version is a (possibly) unstable but may include new features<br/> and bug fixes that haven't been released yet.</p>
                            </div>
                        </div>
                    </div>
<p>Chances are good, that Krusader is already part of your distribution and can be installed without major effort. In a perfect world Krusader is only one command away ...</p>
                    
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
