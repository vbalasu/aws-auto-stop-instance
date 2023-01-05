# aws-auto-stop-instance

AWS EC2 instances do not have an auto-stop feature. This means that you can unintentionally rack up large costs if you forget to stop your instance after you are done.

This convenience script sets up a timer on your instance that counts down 60 minutes, and stops (but does not terminate) your instance.

The initial set up is as follows:
1. Create an EC2 instance the normal way (preferably Ubuntu)
2. Set up an Elastic IP so that the IP address remains the same
3. Connect to your EC2 instance using ssh
4. Once you have successfully connected, copy countdown.py and place it in your home directory (eg. /home/ubuntu). Log out to return to your local machine.
5. Modify app.py to set the correct InstanceId
6. Configure your AWS CLI and run `source deploy.sh` to deploy your Lambda function. Note the resulting Lambda URL. You can also get this by running `chalice url` (remember to remove the trailing slash if you do this)
7. Now reconnect to the EC2 instance and ensure that Python is installed (this should be installed by default)
8. Edit your crontab (`crontab -e`) and enter the following line:
```
@reboot cd /home/ubuntu && export LAMBDA_URL=https://PATH_TO_YOUR_LAMBDA_WITHOUT_TRAILING_SLASH && nohup python countdown.py &
```
9. Log out to return to your local machine
10. Set the `LAMBDA_URL` environment variable and run `./stop.sh` followed by `./start.sh` to restart your instance

The countdown has begun! Your instance will now auto-stop after 60 minutes.

Peace of mind at last!