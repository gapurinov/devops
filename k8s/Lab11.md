# Lab11
- Creating secret
  [![name](https://github.com/gapurinov/devops/blob/main/k8s/screenshots/Screen%20Shot%202021-09-27%20at%2021.47.33.png)]
- Listing secrets
  [![name](https://github.com/gapurinov/devops/blob/main/k8s/screenshots/Screen%20Shot%202021-09-27%20at%2021.47.48.png]
- decoding secrets
  [![name](https://github.com/gapurinov/devops/blob/main/k8s/screenshots/Screen%20Shot%202021-09-27%20at%2021.47.59.png)]
  [![name](https://github.com/gapurinov/devops/blob/main/k8s/screenshots/Screen%20Shot%202021-09-27%20at%2021.54.50.png)]
- Creating secret by using helm
After changing helm secret related files we need to upgrade it
  [![name](https://github.com/gapurinov/devops/blob/main/k8s/screenshots/Screen%20Shot%202021-09-27%20at%2022.55.38.png)]
- Get pods
  [![name](https://github.com/gapurinov/devops/blob/main/k8s/screenshots/Screen%20Shot%202021-09-27%20at%2022.57.12.png)]
- Checking secret inside pod
  [![name](https://github.com/gapurinov/devops/blob/main/k8s/screenshots/Screen%20Shot%202021-09-27%20at%2022.58.38.png)]
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
  [![name](https://github.com/gapurinov/devops/blob/main/k8s/screenshots/Screen%20Shot%202021-09-27%20at%2023.06.51.png)]