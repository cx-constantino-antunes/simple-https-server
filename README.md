# Generate self signed certificated
```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/C=XX/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=CommonNameOrHostname"
```

# Run server
```bash
python https_server.py
```

# Run test container
Runs a container:
```bash
docker run -it --rm --net=host -v $(pwd):/mnt/host checkmarx.jfrog.io/ast-docker/chainguard/wolfi-base:1-r6@sha256:91fadb8dcb6d78aaf0eadf87f5864aa4417bc98ed266d01015f380ddcc7ce53a sh
```

Installs curl:
```bash
apk add curl
```

At this point we can call the server and the request must fail:
```bash
curl https://localhost:4443
```

Trust self-signed certificate:
```bash
cat /mnt/host/cert.pem >> /etc/ssl/certs/ca-certificates.crt
```

Now the request must succeed:
```bash
curl https://localhost:4443
```
