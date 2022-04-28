{% extends 'blog/base_blog.html' %}

{% block title %}
    Edit tag "{{tag.title|title}}" - {{block.super}}
{% endblock %}

{% block content %}

    <form action="{{tag.get_update_url}}" method="post">
        {% csrf_token %}

        {% for field in form %}
            <div class="form-group">
                {% if field.errors %}
                    <div class="alert alert-danger">
                        {{ field.errors }}
                    </div>

                {% endif %}
                {{ field.label }}
                {{ field }}
            </div>

        {% endfor %}

        <button type="submit" class="btn btn-primary">Create </button>
    </form>

{% endblock %}