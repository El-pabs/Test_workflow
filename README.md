## Projet github workflow

Se connecter a aws en ssh en utilisant la clé pem 

```powershell
ssh -i .\ssh.pem ubuntu@3.236.5.210 #ip publique instance ec2
```

installer kubernetes : 

```powershell
curl -sfL https://get.k3s.io | sh -s - --tls-san $(curl -s http://checkip.amazonaws.com)
```

Récupéré la clé de connexion du kubernetes et mettre dans un fichier `config-aws.yaml`

```powershell
sudo cat /etc/rancher/k3s/k3s.yaml #copier coller
```

Tester connexion 

```powershell
$env:KUBECONFIG=".\config-aws.yaml"
kubectl get nodes
```

Connecter argocd au cluster aws : 

```powershell
argocd login localhost:8080  # (User: admin, Password: ******)
argocd cluster add default --name aws-prod --kubeconfig .\config-aws.yaml 
#donne les credentials aws pour dire a argocd "tu peux piloter"
```

Enfin créer une nouvelle app sur argocd avec source le github et destination le clusteraws (PAS DEFAULT)