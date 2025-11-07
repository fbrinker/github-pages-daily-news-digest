---
layout: default
---

Welcome to the Daily News Digest! Below you'll find links to all available articles.

## Recent Articles

{% if site.posts.size > 0 %}
  {% for post in site.posts %}
  <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
  <p><small>{{ post.date | date: "%B %d, %Y" }}</small></p>
  {% endfor %}
{% else %}
  <p>No posts found. Total posts: {{ site.posts.size }}</p>
{% endif %}
