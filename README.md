# spark-aws-ec2
Instalación maestro y esclavo sobre máquinas ec2 en aws. Packer + Ansible + Terraform

### Creación AMI

```
$  cd packer
$  export AWS_REGION="eu-west-1"
$  packer build -var public_ip_cidr=$(curl -s ifconfig.co)/32 spark.json
```

### Creación cluster spark sobre aws

```
$  terraform init
$  terraform apply -var PUBLIC_IP_CIDR=$(curl -s ifconfig.co)/32
```
