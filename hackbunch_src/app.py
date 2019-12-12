import requests
import json
import collections
import re 

from secret import accessToken

from flask import Flask, render_template,request,redirect



headers = {"Authorization": "bearer "+ accessToken }

app=Flask(__name__)
@app.route('/',methods = ['GET','POST'])
def index():    
	if request.method == 'POST': # basic Flask structure 
		username = request.form['github-username'] 
		# return in the browser
		while username!='':
			prsdata=getpullRequests(username)

			return '''{}'''.format(prsdata)
	return render_template('index.html')

@app.route("/upload-file", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        
        
        #Working upload        
        """
        
        if request.files:
            print(request.files["file"])
            request.files["file"].save(request.files["file"].filename)
            return render_template('upload_file.html',name=request.files["file"].filename)
        return render_template('upload_file.html')
        """
"""@app.errorhandler(500)
def not_found(e):
  nouser={
      "id":"None"
  }
  return render_template('prs.html',nouser=nouser), 500
"""


def getpullRequests(username):
    topic_query = """
    query ($name:String!){
    repositoryOwner(login:$name){
        login 
        ... on User {
        name
        avatarUrl
        pullRequests(last: 100){
            nodes{
            id
            createdAt
            additions
            deletions
            }
        }
        } 
    }
    } 
    """
    variables=dict({
        "name":str(username)
    })    
    request = requests.post('https://api.github.com/graphql', json={'query': topic_query,"variables":variables},headers=headers)
    if request.status_code == 200:
        result = request.json()
        prsdata = {}
        prcount=0
        for pr in result['data']['repositoryOwner']['pullRequests']['nodes']:
            prdata = {}
            if re.match(r'^2019-10', pr['createdAt']):
                prcount+=1
                prdata['createdAt'] = pr['createdAt']
                prdata['additions'] = pr['additions']
                prdata['deletions'] = pr['deletions']
                prsdata[pr['id']] = prdata
        if prsdata:
            #print(prsdata)
            return render_template('prs.html', prs=prsdata,prcount=prcount)
        else:
            print("No PRs made in Hacktoberfest")
            data={
            "id":"Null"
            }
            return render_template('prs.html',data=data)



def upload_file(data):
    usernames = [x.replace('\n', '') for x in open("{}".format(data.text), "r").readlines()]
    data=[]
    for username in usernames:
        prData = getpullRequests(username)
        prData.getPRData()
        data.append(prData.returnsData())
    totalPRCount=0
    totalAddCount=0
    totalDelCount=0
    for item in data:
        totalPRCount=totalPRCount+len(dict(dict(item)['prsdata']).keys())
        for i in dict(item)['prsdata'].values():
            totalAddCount+=int(i['additions'])
            totalDelCount+=int(i['deletions'])
    print(totalPRCount,totalAddCount,totalDelCount)







if __name__ == "__main__":
    app.run(debug=True)    

