tags = """{% extends 'base.html' %}
{% load static %}
{% block content %}







    <div class="mini-sidebar" style="margin: 2rem">
        <div class="header" style="margin-right: 60px">
            <a id="mobile_btn" class="mobile_btn float-left" href="#sidebar"><i class="fas fa-bars"
                                                                                aria-hidden="true"></i></a>
            <a id="toggle_btn" class="float-left" href="javascript:void(0);"></a>


            <ul class="nav float-left">
                <li>
                    <div class="top-nav-search">
                        <a href="#" class="responsive-search">
                            <i class="fa fa-search"></i>
                        </a>
                        <form>
                            {% csrf_token %}
                            <input class="form-control" type="text" name="keyword" placeholder="Search here">
                            <button class="btn" type="submit"><i class="fa fa-search"></i></button>
                        </form>
                    </div>
                </li>
                <li>
                    <a href="index.html" class="mobile-logo d-md-block d-lg-none d-block"><img
                            src="{% static 'assets/img/logo1.png' %}" alt="" width="30" height="30"></a>
                </li>
            </ul>

            <ul class="nav user-menu float-right">

                <li class="nav-item dropdown has-arrow">
                    <a href="#" class=" nav-link user-link" data-toggle="dropdown">
                    <span class="user-img"><img class="rounded-circle" src="{% static 'assets/img/resim.jpg' %}"
                                                width="30" alt="Admin">
                    <span class="status online"></span></span>
                        <span>{{ request.user.username }}</span>
                    </a>
                    <div class="dropdown-menu">
                        {% if request.user.is_authenticated %}
                            <a class="dropdown-item" href="{% url 'logout' %}">Logout</a>
                        {% else %}
                            <a class="dropdown-item" href="{% url 'login' %}">Login</a>
                            <a class="dropdown-item" href="{% url 'register' %}">Register</a>
                        {% endif %}

                    </div>
                </li>
            </ul>


        </div>
    </div>


    {% if request.user.is_authenticated %}
        <body class="mini-sidebar">
        <div class="main-wrapper">
            <div class="page-wrapper" style="margin-right: 60px">
                <div class="row">

                    <div class="col-md-6 col-sm-6 col-lg-6 col-xl-6">
                        <div class="dash-widget dash-widget5">
                            <div class="dash-widget-info d-inline-block text-left">
                                <span><h3 style="text-align: center">{{ keyword }} </h3></span>
                                <span><h4 style="text-align: center">Bu teg'den {{ ariyorum }} tane vardir</h4></span>
                            </div>
                            <span class="float-left"><img src="{% static 'assets/img/dash/tag.jpg' %}" alt=""
                                                          width="150"></span>
                        </div>
                    </div>


                    <div class="col-md-6 col-sm-6 col-lg-6 col-xl-6">
                        <div class="dash-widget dash-widget5">
                            <div class="dash-widget-info text-left d-inline-block">



                                {% for sahipsiz in tag_gosteriyor %}
                                    {% if sahipsiz == '' %}
                                        <span></span>



                                    {% elif '<' in sahipsiz and '/' not in sahipsiz %}
                                        <h3><span style="color: saddlebrown">{{ sahipsiz }}</span> Bu elemanin <span style="color: saddlebrown">Kapali</span> tag yoktur.</h3>


                                    {% elif '/' in sahipsiz and '<' in sahipsiz %}
                                        <h3><span style="color: #c82333">{{ sahipsiz }}</span> Bu elemanin <span style="color: #c82333">Acik</span> tag yoktur.</h3>


                                    {% else %}

                                        <span>{{ sahipsiz }}</span><br>
                                    {% endif %}



                                {% endfor %}
                            </div>
                            <span class="float-right"><img src="{% static 'assets/img/dash/MUKEMMEL.png' %}" width="160"
                                                           alt=""></span>
                        </div>
                    </div>


                </div>
            </div>
        </div>

        </div>
        </body>

    {% else %}
        <body class="mini-sidebar">
        <div class="main-wrapper">
            <div class="page-wrapper" style="margin-right: 60px">
                <div class="row">
                    <div class="col-md-12 col-sm-12 col-lg-12 col-xl-12">
                        <div class="dash-widget dash-widget5 btn-success">
                            <div class="dash-widget-info d-inline-block text-left ">
                                <h3><span style="text-align: center; margin-left: 550px">  Kayit olmalisiniz  </span>
                                </h3>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>
        </div>
        </body>
    {% endif %}






{% endblock %}
"""