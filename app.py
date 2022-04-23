#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request


# In[2]:


app = Flask(__name__)


# In[3]:


import joblib

@app.route("/", methods =("GET", "POST"))
def index():
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        print(rate)
        model = joblib.load("DBS prediction")
        pred = model.prediction([[rate]])
        return(render_template("Index.html", results=pred))
    else:
        return(render_template("Index.html", results='Waiting'))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




