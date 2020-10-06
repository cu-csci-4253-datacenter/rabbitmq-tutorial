# rabbitmq-tutorial
Tutorials for RabbitMQ

These are adapted from [the official RabbitMQ tutorials](https://www.rabbitmq.com/getstarted.html).

Assuming you have Docker install (*e.g.* in Google Cloud Console), you can start a rabbitmq server by running

```
docker run -d --hostname my-rabbit --name some-rabbit -p 5672:5672 rabbitmq:3
```
This will expose the RabbitMQ client TCP port 5672 to the local machine.

You will probably need to install the [`pika`](https://pika.readthedocs.io/en/stable/) library to run the examples.
You can do this using
```
pip3 install pika
```

The sample applications can then be executed.
