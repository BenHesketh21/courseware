# Overview
Key Pairs in EC2 can be used for securely connecting to EC2 instances in AWS.
Connections are usually over SSH, which uses public and private keys.
This handout discusses how to manage these Key Pairs, and how to locally store the private keys that are generated.



<!--TOC_START-->
## Contents
- [Creating Key Pairs](#creating-key-pairs)
	- [Basic Usage](#basic-usage)
	- [The Private Key](#the-private-key)
	- [Locally Storing the Private Key](#locally-storing-the-private-key)
	- [Private Key Permissions](#private-key-permissions)
- [Deleting Key Pairs](#deleting-key-pairs)
		- [Basic Usage](#basic-usage-1)
- [Tasks](#tasks)

<!--TOC_END-->
## Creating Key Pairs

### Basic Usage
The create-key-pair command can be used to create our key pair. We specify the name of the Key Pair so that it can be easily referenced later on, such as when we want to add a key pair to an EC2 instance:
```bash
# aws ec2 create-key-pair --key-name [KEY_PAIR_NAME]
aws ec2 create-key-pair --key-name MyKeyPair
```

### The Private Key
Once a new Key Pair has been created, the AWS CLI will print out the private key, along with some other information about the Key Pair.
The private key is what we can use on the client side, to authenticate with an EC2 instance.

Here is an example output when creating a new key pair:
```
{
    "KeyFingerprint": "69:bc:f4:ae:0e:ab:98:cb:6d:b7:ec:32:58:3a:00:82:c0:46:c7:c0",
    "KeyMaterial": "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAmJuYixAl4YlYRIVQxZUZ+Fb0vZpRFG342ju8AuY90npucDFyzMfTBhprMrKK\nM3zXhUCkXCdciza2qIQF4UZEJItmPt7hDhnaFy7R12Ta9Av2xBZZCXnNijeaFzGxgI8Yk42VxLLZ\n9Tlm1hKq7x+aVVfjQQkrJVUM4NN5z7skyHM7B+9mW8uVSnamtGTyVo1lUQcrcc+YN2iKElAFiQ6u\nIKndmtjg9ufIYBkx631sSBAuNHaPpAITpaYfr/E+ecz0BekHyGHgKUmmFh6Rklia+kxttJYfSJfR\nxLvOwIwyj+knRAJ2VyWsX1TfxZ6aYBdW2n2NQ8ym5p2WMPsxAwO3kQIDAQABAoIBAEXJkd62Sbxz\n5IuhM6jHYJLyoQU71qwzBkQ2YOoqhEcGeg6QbmE7WENIPZF3mD+nbZ+gSglibq2zHaC+jznPukXE\nAcPqhJzAMb28SXXox0AnYHeXiKwOqXH1r1+/995EkgaYDs9ewtGjqGVpMAYeO6Ofh2ssWDDATh1a\nWDAo8s8/ODQb4c1ewkFNxAwEV5m5bAcF2pG5/TUDt8ctV3RZCHEHryoNKWN44L3Yi7OqJjBGStQT\nKLSiwItmDi0+CNyl43sPqW6BjDc5VY79LNOFgbwIqv+Bxt7uDIrhUfXPIAsdgdeU0ktHw+lbK0fZ\nUtlWmJog9o28+qwCZNSLl46SkAECgYEA/sGKtt73VEwpWHl9BDBjVblSurWzikRm7nsh1wqIoVDE\nnpL/3xq0OikS9SwlQTGvJckslGOsHiycz3LZWUjoIGuFtCaSRceFdaArJfQpESFBhr8Xgxi/7W8W\nQjkMpD/S33WVq0J3dTZOkDl3HqnHQAdmlxyBg+GnAYtwG6BiDxECgYEAmVpdDMES65dWiU68pLA5\n987nSPwIPxcy55sIIXZEnM98Ajb6naQ3NanmzptQ6LJDn1EVJt4tW5khshDydsF7+4UKZsxxkWOm\nQHuH7lY54WfteaN4B5Ydqp4iWwuL3+K834AxXCe2GRVRXw0DBUPOIjI3OhbuZxb12yBNs2Q4IIEC\ngYEAmhfFaNG69qFOzPZHOTZvj1WWhdsMK1EulYejM2hqtnCdTXGLFY8YfqmDjwrRyfpcf9WMgoE7\nhdDkVNKaR1hDGAERkaNXDKAfyMNF9iIWiQb9lJyXgzOAPATaiNnrHJqCWanNCxccHKjponEv7Tsy\nizcuxa53ZKckFloaSIudZJECgYEAiuT7bjfZSSSTLl3wIkGy3y248bPETFBYvMj//j6+OkD6ko71\nQp6fmq097VdjWr9K3Bt2SvPkpRf3Gu6ajNEF2HNRTnZRTluxEqpQHaBfYDbfMdLLPiPKzuPXPhsh\nHzCf3Nag3lTha6qRPsPsPnKBWxucRbLLTvfOyh9iAN7+rwECgYB4hFe+i5ioxP+SC6cr0kMlZ92n\nu3nscQO5Q3DFZY4w5s6C9qI/rqd2FOtvLwxokF6u/tpQRCc0crLGhaJUvXYqKABkS6tTKmSGY/ro\nuQRyT9Xu9DMGKzzHXp/fTEBHZxATPLLzJRpnupgvFKryhEHKVv9zN7LJXe/ojUplB+RY0A==\n-----END RSA PRIVATE KEY-----",
    "KeyName": "MyKeyPair"
}
```

### Locally Storing the Private Key
It is important that we save the private key somewhere, because we will not be able to gain access to it again.
To do this, we can add a query to our command that gets the `KeyMaterial` property when the key information is returned. We can then specify that we would like a text output, and then redirect the output to a file for the key to be stored in.

**Make sure that you do not put your key somewhere publicly accessible, such as a GitHub repository**
```bash
# aws ec2 create-key-pair --key-name [KEY_PAIR_NAME] --query [QUERY] --output [OUTPUT_TYPE]
aws ec2 create-key-pair --key-name MyKeyPair --query ‘KeyMaterial’ --output text > ~/.ssh/MyKeyPair.pem
```

### Private Key Permissions
When storing a private key, it is important that only you, as the owner, can read it. Make sure you change the file permissions to allow this:
```bash
chmod 400 ~/.ssh/MyKeyPair.pem
```

## Deleting Key Pairs

#### Basic Usage
Deleting key pairs is very easy - just be 100% sure that you want to delete them!

Provide the name of the Key Pair to delete it:
```bash
# aws ec2 delete-key-pair --key-name [KEY_PAIR_NAME]
aws ec2 delete-key-pair --key-name MyKeyPair
```

## Tasks
Try to complete the following tasks:
- Create a new key pair called `MyKeyPair`, and make sure the value of the key gets saved to a file: `~/ssh/MyKeyPair.pem`
- Verify the key has been saved properly by viewing the contents of the file
- Delete the key pair that you created and also the file that you saved

[Go Back](../README.md#tasks)
