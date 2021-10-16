# cat-facts
This was a fun weekend project to get my feet wet with several AWS services including Lambda, API Gateway, IAM, and CloudWatch.

On the Slack API side, there's a slash command that sends an API request with a token to AWS API Gateway. The API Gateway forwards that to Lambda, and the python script here decodes the request and checks to make sure the token is valid. The script then grabs a random cat fact by sending an API request to catfact.ninja, then returns the cat fact to Slack via an incoming web hook configured in the Slack API.

Note that since the requests library isn't included in Lambda by default, I had to use pip to install it to a local directory, then package and upload it to Lambda.
