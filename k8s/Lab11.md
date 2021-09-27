# Lab11
- Creating secret
  ![image info](./screenshots/Screen Shot 2021-09-27 at 21.47.33.png)
- Listing secrets
  ![image_info](./screenshots/Screen Shot 2021-09-27 at 21.47.48.png)
- decoding secrets
  ![image_info](./screenshots/Screen Shot 2021-09-27 at 21.47.59.png)
  ![image_info](./screenshots/Screen Shot 2021-09-27 at 21.54.50.png)
- Creating secret by using helm
After changing helm secret related files we need to upgrade it
  ![image_info](./screenshots/Screen Shot 2021-09-27 at 22.55.38.png)
- Get pods
  ![image_info](./screenshots/Screen Shot 2021-09-27 at 22.57.12.png)
- Checking secret inside pod
  ![image_info](./screenshots/Screen Shot 2021-09-27 at 22.58.38.png)
- Set up requests and limits 
```
resources:
   limits:
     cpu: 100m
     memory: 128Mi
   requests:
     cpu: 100m
     memory: 128Mi
```
After set up, we need to upgrade helm and check. Everything works properly
![image_info](./screenshots/Screen Shot 2021-09-27 at 23.06.51.png)