Edit your crontab (`crontab -e`) and enter the following line:

```
@reboot cd /home/ubuntu && export LAMBDA_URL=https://PATH_TO_YOUR_LAMBDA_WITHOUT_TRAILING_SLASH && nohup python countdown.py &
```
