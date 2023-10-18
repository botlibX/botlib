.. _{{ fullname }}:

.. title:: {{ fullname }}

.. raw:: html

    <center>
    <h3>
    <b>

{{ fullname }} 

.. raw:: html

    </b>
    </h3>
    </center>

.. automodule:: {{ fullname }}
    :members:
    :private-members:
    :undoc-members:

    .. raw:: html
  
        <br>

    {% block exceptions %}
    {% if exceptions %}
    .. rubric:: exceptions

    .. autosummary::
    {% for item in exceptions %}
        {{ item }}
    {%- endfor %}
    {% endif %}
    {% endblock %}

    {% block classes %}
    {% if classes %}
    .. rubric:: classes

    .. autosummary:: 
    {% for item in classes %}
        {{ item }}
        .. raw:: html

            <br><br>

    {%- endfor %}
    {% endif %}
    {% endblock %}

    {% block functions %}
    {% if functions %}
    .. rubric:: functions

    .. autosummary::
    {% for item in functions %}
        {{ item }}
    {%- endfor %}
    {% endif %}
    {% endblock %}

    .. raw:: html

        <br><br>

.. currentmodule:: {{ fullname }}


