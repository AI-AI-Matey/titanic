{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: flask in /Users/aakashp/anaconda3/lib/python3.6/site-packages (0.12.2)\n",
      "Requirement already satisfied: Werkzeug>=0.7 in /Users/aakashp/anaconda3/lib/python3.6/site-packages (from flask) (0.14.1)\n",
      "Requirement already satisfied: Jinja2>=2.4 in /Users/aakashp/anaconda3/lib/python3.6/site-packages (from flask) (2.10)\n",
      "Requirement already satisfied: itsdangerous>=0.21 in /Users/aakashp/anaconda3/lib/python3.6/site-packages (from flask) (0.24)\n",
      "Requirement already satisfied: click>=2.0 in /Users/aakashp/anaconda3/lib/python3.6/site-packages (from flask) (6.7)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in /Users/aakashp/anaconda3/lib/python3.6/site-packages (from Jinja2>=2.4->flask) (1.0)\n",
      "\u001b[33mWARNING: You are using pip version 20.1.1; however, version 20.2.2 is available.\n",
      "You should consider upgrading via the '/Users/aakashp/anaconda3/bin/python -m pip install --upgrade pip' command.\u001b[0m\n"
     ]
    }
   ],
   "source": [
    "# import sys\n",
    "# !{sys.executable} -m pip install flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5003/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [16/Aug/2020 02:18:50] \"\u001b[1m\u001b[31mGET / HTTP/1.1\u001b[0m\" 405 -\n",
      "127.0.0.1 - - [16/Aug/2020 02:18:51] \"\u001b[33mGET /favicon.ico HTTP/1.1\u001b[0m\" 404 -\n",
      "127.0.0.1 - - [16/Aug/2020 02:21:27] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from flask import Flask, jsonify, request\n",
    "import pickle\n",
    "\n",
    "# load model\n",
    "model = pickle.load(open('model.pkl','rb'))\n",
    "\n",
    "# app\n",
    "app = Flask(__name__)\n",
    "\n",
    "# routes\n",
    "@app.route('/', methods=['POST'])\n",
    "\n",
    "def predict():\n",
    "    # get data\n",
    "    data = request.get_json(force=True)\n",
    "\n",
    "    # convert data into dataframe\n",
    "    data.update((x, [y]) for x, y in data.items())\n",
    "    data_df = pd.DataFrame.from_dict(data)\n",
    "\n",
    "    # predictions\n",
    "    result = model.predict(data_df)\n",
    "\n",
    "    # send back to browser\n",
    "    output = {'results': int(result[0])}\n",
    "\n",
    "    # return data\n",
    "    return jsonify(results=output)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(port = 5000, debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
