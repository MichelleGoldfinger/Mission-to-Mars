{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "white-simpson",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Use Flask to render a template\n",
    "from flask import Flask, render_template\n",
    "#Use PyMongo to interact with MongoDB\n",
    "from flask_pymongo import PyMongo\n",
    "#Use scraping code from JN to Python\n",
    "import Scraping "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "black-intermediate",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Set up Flask\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "inappropriate-compilation",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use flask_pymongo to set up mongo connection\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars_app\"\n",
    "mongo = PyMongo(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "special-style",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Define the route for the HTML page\n",
    "@app.route(\"/\")\n",
    "def index():\n",
    "   mars = mongo.db.mars.find_one()\n",
    "   return render_template(\"index.html\", mars=mars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "irish-evans",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Set up scrapping route/button\n",
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "   mars = mongo.db.mars\n",
    "   mars_data = scraping.scrape_all()\n",
    "   mars.update({}, mars_data, upsert=True)\n",
    "   return redirect('/', code=302)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "specialized-operator",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Update the databse\n",
    ".update(query_parameter, data, options)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "significant-virus",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "#Tell Flask to run\n",
    "if __name__ == \"__main__\":\n",
    "   app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "normal-marina",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
