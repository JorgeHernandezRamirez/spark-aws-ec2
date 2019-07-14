## Create AMI

```
$  export AWS_REGION="eu-west-1"
$  packer build -var public_ip_cidr=$(curl -s ifconfig.co)/32 spark.json
```