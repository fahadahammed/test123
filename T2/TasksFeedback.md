# Question
Run 3 replicas using Docker Service. Use the official hello-world image from this source
https://hub.docker.com/_/hello-world. Service configuration should be written using the Docker
compose file. Establish a load balancer using HAProxy to load balance them for external traffic. 


# Answer:

I wanted to use hello-world image as base for the service. But felt not that useful on demonstrating the load balancing part.

What I did is:
- create a flask app
- use ubuntu as base and created the Dockerfile
- Then using that Dockerfile, wrote the compose file to deploy via docker stack

```
docker stack deploy -c docker-compose.yml test123
```

- Thus:
```bash
$ docker stack services test123
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
rix1zvx7gyq0        test123_test123     replicated          3/3                 test123:latest      *:30002->5100/tcp
```

- But, load balancing will be done by the machine itself. If I access http://127.0.0.1:30002/

```bash
$ curl http://127.0.0.1:30002/ && echo -e "\n"
Here for the test and I am the container: 3e79e7a3e053

$ curl http://127.0.0.1:30002/ && echo -e "\n"
Here for the test and I am the container: 9d3a13e7423f

$ curl http://127.0.0.1:30002/ && echo -e "\n"
Here for the test and I am the container: c3249dc2e1f1

```

- So, this test123 service is giving response from different containers.

- Creating another service -
```bash
$ docker stack services test123_v1
ID                  NAME                 MODE                REPLICAS            IMAGE               PORTS
vth65znryor2        test123_v1_test123   replicated          0/3                 test123:latest      *:30003->5100/tcp
```

- We have two service running with 6 containers (3 each). One with 30002 and other with 30003 port.
- For haproxy load balancing, I have used the config with port 6100

```bash
$ curl http://127.0.0.1:6100 && echo -e "\n"
Here for the test and I am the container: d3a58e466494

$ curl http://127.0.0.1:6100 && echo -e "\n"
Here for the test and I am the container: 9d3a13e7423f

$ curl http://127.0.0.1:6100 && echo -e "\n"
Here for the test and I am the container: 27743fa7d391

$ curl http://127.0.0.1:6100 && echo -e "\n"
Here for the test and I am the container: c3249dc2e1f1

$ curl http://127.0.0.1:6100 && echo -e "\n"
Here for the test and I am the container: e14214a4e2a1

$ curl http://127.0.0.1:6100 && echo -e "\n"
Here for the test and I am the container: 3e79e7a3e053

$ curl http://127.0.0.1:6100 && echo -e "\n"
Here for the test and I am the container: d3a58e466494

$ curl http://127.0.0.1:6100 && echo -e "\n"
Here for the test and I am the container: 9d3a13e7423f

$ curl http://127.0.0.1:6100 && echo -e "\n"
Here for the test and I am the container: 27743fa7d391

$ curl http://127.0.0.1:6100 && echo -e "\n"
Here for the test and I am the container: c3249dc2e1f1
```

- So, the load balancer also working. I did bind with `bind *:6100` So, all the interfaces is allowed to serve the port 6100.

