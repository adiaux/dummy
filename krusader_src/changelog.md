---
layout: page
title: Changelog
css-include: /css/main.css
sorted: 2
---
{% assign sorted = site.changelogs | sort:'sorted' %}
{% assign reverse = sorted | reverse %}

{% if changelogs.size == 0 %}
    No changelog available.
{% endif %}

{% for changelog in reverse %}

## [{{ changelog.title }}]({{ changelog.url }})

{{ changelog.content | markdownify }}

{% endfor %}

