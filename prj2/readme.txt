customise admin panel:
=======================
list_display = ['name', 'email', 'dob', 'gender']
search_fields = ['name', 'email']
list_filter = ['gender']
fields = ['name', 'email', 'dob', 'gender']
list_editable = ['email', 'dob', 'gender']
list_per_page = 5


 fav icon   
 ---------------------
search favicon.io:   https://favicon.io/favicon-generator/
<link rel="shortcut icon" href="{% static 'images/favicon.ico'%}" type="image/x-icon">
fontawsomeCDN: <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/fontawesome.min.css">
<a class="navbar-brand" href="{% url 'student:home' %}"><img src="{% static 'images/favicon.ico'%}" alt=""></a>

base_site.html.............
{% extends 'admin/base.html' %}   #base.html django system 
{% load static %}   

{% block extrahead %}
<link rel="shortcut icon" href="{% static 'images/favicon.ico'%}" type="image/x-icon">
{% endblock %}


{% block title %}
{{ title }} | {{site_title|default:_('Django site admin') }}
{% endblock %}

{% block branding %}
<h1 id="site-name"><a href="{% url 'student:home' %}">Lubna's web application</a></h1>
{% endblock %}

{% block nav-global %}

{% endblock%}
--------------------------------------
https://sweetalert.js.org/guides/
CDN: <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>

--datatable CDN:
<link rel="stylesheet" href="https://cdn.datatables.net/1.10.25/css/jquery.dataTables.min.css">
<script src="https://cdn.datatables.net/1.10.25/js/jquery.dataTables.min.js"></script>