
```
$  terraform init
$  terraform apply -var PUBLIC_IP_CIDR=$(curl -s ifconfig.co)/32
```