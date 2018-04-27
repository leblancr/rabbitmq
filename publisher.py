import pika, os, logging, time
logging.basicConfig()

# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://bierhrnn:kIYntLtzZ4TIbRCsUiPLDpNywzbdZfLB@otter.rmq.cloudamqp.com/bierhrnn')
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='pdfprocess') # Declare a queue
# send a message

num_msgs_to_send = 100

for x in range(num_msgs_to_send):
    print("Sending message {}/{}".format(x, num_msgs_to_send))
    channel.basic_publish(exchange='', routing_key='pdfprocess', body="User information {}/{}".format(x, num_msgs_to_send))
    time.sleep(5) # delays for 5 seconds
    
print ("[{}] Messages sent to consumer".format(num_msgs_to_send))
connection.close()
