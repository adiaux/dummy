import requests
import json
import collections
import re 

from secret import accessToken
from werkzeug.utils import secure_filename
from flask import Flask, render_template,request

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
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(secure_filename(f.filename))
        list=upload_file(f.filename)
        infile=[x.replace('\n', '') for x in open("{}".format(f.filename), "r").readlines()]
        #infile = open('{}'.format(f.filename),'r').readlines()
        #content = f.read()
        print(request.files["file"])
    return render_template("upload_file.html", totalPRCount=list[0],totalAddCount=list[1],totalDelCount=list[2])

"""@app.errorhandler(500)
def not_found(e):
  nouser={
      "id":"None"
  }
  return render_template('prs.html',nouser=nouser), 500
"""



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

def getpullRequests(username):
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

class pullRequestsData:
    def __init__(self, username):
        self.variables=dict({
            "name":str(username)
        })
        self.data = {}
    def getPRData(self):
        request = requests.post('https://api.github.com/graphql', json={'query': topic_query,"variables":self.variables},headers=headers)
        if(request.status_code == 200):
            result = request.json()           
            if(result['data']['repositoryOwner'] != None):
                self.data['username'] = result['data']['repositoryOwner']['login']
                self.data['name'] = result['data']['repositoryOwner']['name']
                prsdata = {}
                for pr in result['data']['repositoryOwner']['pullRequests']['nodes']:
                    prdata = {}
                    if(re.match(r'^2019-10', pr['createdAt'])):
                        prdata['createdAt'] = pr['createdAt']
                        prdata['additions'] = pr['additions']
                        prdata['deletions'] = pr['deletions']
                        prsdata[pr['id']] = prdata
                self.data['prsdata'] = prsdata
            else:
                self.data['username'] = result['data']['repositoryOwner']
                
    def displayData(self):
        if(self.data['username'] != None):
            if(self.data['prsdata']):
                print(self.data)
            else:
                print("No PRs for Hacktoberfest")
        else:
            print("User doesn't exist")
        
    def returnsData(self):
        return self.data



def upload_file(text):
    usernames = [x.replace('\n', '') for x in open("{}".format(text), "r").readlines()]
    data=[]
    for username in usernames:
        prData = pullRequestsData(username)
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
    return [totalPRCount,totalAddCount,totalDelCount]


if __name__ == "__main__":
    app.run(debug=True)    

