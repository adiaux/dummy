---
layout: page
title: Get Involved
konqi: /assets/img/konqi-dev.png
sorted: 5
---
# Participate in Krusader development

## Build {{ site.title }} from Sources

The [community wiki](https://community.kde.org/Get_Involved/development) provides ressource
about settings up your development environment.

Check out our developer site on [Phabricator](https://phabricator.kde.org/project/view/79/) where all development is taking place (you can log in with a [KDE Identity account](https://identity.kde.org/)
You can fetch the source from the KDE Git repository.

<a href='https://build.kde.org/job/Extragear/job/krusader/job/stable-kf5-qt5%20SUSEQt5.12/'>
<img src='https://build.kde.org/buildStatus/icon?job=Extragear/krusader/stable-kf5-qt5 SUSEQt5.12'>

#### Checkout (Anonymous)

<pre><code>$ git clone git://anongit.kde.org/krusader</code></pre>

#### Checkout (Developer)

<pre><code>$ git clone git@git.kde.org:krusader.git </code></pre>

**Note:** Refer to the [GitKdeOrgManual](https://community.kde.org/Sysadmin/GitKdeOrgManual) for details.

### Installation

<pre><code>$ cd krusader
$ mkdir -v build && cd build
$ cmake -DCMAKE_INSTALL_PREFIX=/usr/ ..
$ make
# At the beginning of the following command: `sudo` must be added if Kubuntu, Ubuntu, Debian, or similar is being used.
$ su -c "make install"
</code></pre>

**Note:** For the advanced and latest installation instructions please refer to the [INSTALL](https://commits.kde.org/krusader?path=INSTALL) file in the Krusader sources.

**Note:** On a multi cpu/core system you might want to speed up the compile process by increasing the number of jobs (e.g. "make -j4").

### Localization

Due to the layout of [KDE's repository](https://websvn.kde.org/trunk/l10n-kf5/), translations aren't part of the checkout. 
There is a list of translation files in the [10n.kde.org Krusader page](https://l10n.kde.org/stats/gui/trunk-kf5/po/krusader.po/index.html). In that list anyone can look for his desired translation file, hover the mouse cursor over its link, see its tooltip to look up the appropriate language code (which is shown between parentheses, e.g. if on the tooltip it's seen "German (de)" that means that the language code is: de), click on the link (in order to download the proper krusader.po file), and execute:

<pre><code>$ msgfmt krusader.po -o krusader.mo
# At the beginning of the following command: `sudo` must be added if Kubuntu, Ubuntu, Debian, or similar is being used.                    
# Replace &lt;XX&gt; with the previously found language code (e.g. de for German). 
$ su -c "cp krusader.mo /usr/share/locale/&lt;XX&gt;/LC_MESSAGES/"
</code></pre>


## Building a git snapshot with translations
In order to build a snapshot which includes translations KDE's **releaseme** script can be used. Here is how it works:

<pre><code>$ git clone git://anongit.kde.org/releaseme
$ releaseme/tarme.rb --version git`date +%Y%m%d` --origin trunk krusader
</code></pre>

**Note:** You need to have ruby installed to run the script.
The script will create a tarball in the same directory which can be installed as usual:

<pre><code>$ tar xjvf krusader-git`date +%Y%m%d`.tar.bz2
$ cd krusader-git`date +%Y%m%d`
$ cmake -DCMAKE_INSTALL_PREFIX=/usr/
$ make
$ su -c "make install"</code></pre>

---

- [Mailing Lists](../get-involved/mailing-lists/index.html)
- [Contributors](../get-involved/contributors/index.html)
- [Translation Status](https://l10n.kde.org/stats/gui/trunk-kf5/po/krusader.po/)

---