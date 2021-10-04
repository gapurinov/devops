```bash
yerzhan@Yerzhans-MacBook-Pro k8s % kubectl get po,sts,svc,pvc
NAME               READY   STATUS    RESTARTS        AGE
pod/simple-app-0   1/1     Running   1 (3m15s ago)   4m35s
pod/simple-app-1   1/1     Running   0               4m35s
pod/simple-app-2   1/1     Running   0               4m35s

NAME                          READY   AGE
statefulset.apps/simple-app   3/3     4m35s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          14d
service/simple-app   LoadBalancer   10.108.213.222   <pending>     5000:30781/TCP   4m35s

NAME                                           STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/my-visits-simple-app-0   Bound    pvc-0469b625-f2ff-47fd-a66a-1b12ed1faa53   256M       RWO            standard       48m
persistentvolumeclaim/my-visits-simple-app-1   Bound    pvc-c378d664-8783-4dc6-8aea-70427d0351b9   256M       RWO            standard       48m
persistentvolumeclaim/my-visits-simple-app-2   Bound    pvc-757de243-ed49-468a-aaaa-2387f2b57ce3   256M       RWO            standard       48m
```

```bash
yerzhan@Yerzhans-MacBook-Pro k8s % kubectl exec pod/simple-app-0 cat my-visits.txt
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.

00:30:56
00:31:01
00:31:03
00:12:24
00:12:24
00:12:33
00:12:33
00:12:43
00:12:43%                                                                                                                                                                                                   yerzhan@Yerzhans-MacBook-Pro k8s % kubectl exec pod/simple-app-1 cat my-visits.txt
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.

00:30:56
00:31:01
00:31:03
00:11:44
00:11:44
00:11:53
00:11:53
00:12:03
00:12:03
00:12:04
00:12:05
00:12:11
00:12:13
00:12:13
00:12:23
00:12:23
00:12:33
00:12:33
00:12:43
00:12:43
00:12:53
00:12:53%                                                                                                                                                                                                   yerzhan@Yerzhans-MacBook-Pro k8s % kubectl exec pod/simple-app-2 cat my-visits.txt
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.

00:30:56
00:31:01
00:31:03
00:11:44
00:11:44
00:11:53
00:11:53
00:11:58
00:12:03
00:12:03
00:12:03
00:12:07
00:12:13
00:12:13
00:12:13
00:12:14
00:12:23
00:12:23
00:12:33
00:12:33
00:12:43
00:12:43
00:12:53
00:12:53
00:13:03
00:13:03%                 

```

Since we are using 3 different pods everytime we access our server different pod is
provided. And different my-visits.txt file are created.