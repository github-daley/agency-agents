---
layout: default
title: Agency Agents Catalog
---

<div class="hero">
  <div class="container">
    <h1 class="hero-title">Agency Agents</h1>
    <p class="hero-subtitle">A comprehensive catalog of specialized AI agents for software development, design, marketing, and more.</p>

    <div class="search-container">
      <input type="text" id="search-input" class="search-input" placeholder="Search agents by name or description...">
      <span class="search-icon">🔍</span>
    </div>

    <div class="category-filters">
      <button class="filter-btn active" data-category="all">All</button>
      {% for category in site.data.categories %}
      <button class="filter-btn" data-category="{{ category.id }}">{{ category.name_en }}</button>
      {% endfor %}
    </div>
  </div>
</div>

<div class="container">
  <div class="agents-grid" id="agents-grid">
    {% for agent in site.data.agents %}
    <a href="{{ agent.url }}" class="agent-card" data-category="{{ agent.category }}" data-name="{{ agent.name | downcase | escape }}" data-description="{{ agent.description_en | downcase | replace: '"', '&quot;' }} {{ agent.description_zh | downcase | replace: '"', '&quot;' }}">
      <div class="card-header" style="background-color: {{ agent.color }}20;">
        <span class="card-emoji">{{ agent.emoji }}</span>
      </div>
      <div class="card-body">
        <span class="card-category">{{ agent.category_name }}</span>
        <h3 class="card-title">{{ agent.name }}</h3>
        <p class="card-description" lang="en">{{ agent.description_en }}</p>
        <p class="card-description zh-only" lang="zh">{{ agent.description_zh }}</p>
      </div>
    </a>
    {% endfor %}
  </div>

  <div class="no-results" id="no-results" style="display: none;">
    <p>No agents found matching your search.</p>
  </div>
</div>

<script>
  // Pass agents data to JavaScript
  window.agentsData = {{ site.data.agents | jsonify }};
  window.categoriesData = {{ site.data.categories | jsonify }};
</script>
