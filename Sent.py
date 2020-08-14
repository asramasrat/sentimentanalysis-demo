from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
app = Flask(__name__)

@app.route('/')
def front():
   return render_template('front.html')

@app.route('/keyword',methods = ['POST', 'GET'])
def result():
  result = request.form["keyword"]

  sia_obj=SentimentIntensityAnalyzer()
  s_dic=sia_obj.polarity_scores(result)
  sentiment=None
  if (s_dic['compound']>=0.05):
    sentiment='Positive'
  elif (s_dic['compound']<=-0.05):
    sentiment='Negative'
  else:
    sentiment='Neutral'
  return render_template("front.html",sentiment = sentiment)

if __name__ == '__main__':
  app.run(debug = True)