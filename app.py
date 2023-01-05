from chalice import Chalice

app = Chalice(app_name='stop-temp-instance')


@app.route('/')
def index():
    return {'Please specify command': 'start OR stop'}

@app.route('/stop')
def stop():
    import boto3
    ec2 = boto3.client('ec2')
    ec2.stop_instances(InstanceIds=['i-0c596d0193929b7b6'])
    return {'success': 'instance stopped'}

@app.route('/start')
def start():
    import boto3
    ec2 = boto3.client('ec2')
    ec2.start_instances(InstanceIds=['i-0c596d0193929b7b6'])
    return {'success': 'instance started'}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
