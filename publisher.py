import pika, os, logging, time, sys
logging.basicConfig()

# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://bierhrnn:kIYntLtzZ4TIbRCsUiPLDpNywzbdZfLB@otter.rmq.cloudamqp.com/bierhrnn')
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='pdfprocess') # Declare a queue
# send a message

num_msgs_to_send = 2
test_list = [y for y in range(10)]
list_a = ['a', 'b', 'c', 'd', 'e']
list_b = [1, 2, 3, 4, 5]

test_dict = {k:v for k, v in zip(list_a, list_b)}

print("test_dict: {}".format(test_dict))
      
      
#sys.exit()

        
for x in range(num_msgs_to_send):
    print("Sending message {}/{}".format(x + 1, num_msgs_to_send))
    #body = "User information {}/{}\n".format(x + 1, num_msgs_to_send)
     
    body2 = "Message {}/{}\n" \
        "list: {}\n" \
        "dict: {}\n" \
        .format(x + 1, num_msgs_to_send, test_list, test_dict)    
    print("body2: {}".format(body2))
                          
    channel.basic_publish(exchange='', routing_key='pdfprocess', body=body2)
    time.sleep(1) # delays for 5 seconds
    
print ("[{}] Messages sent to consumer".format(num_msgs_to_send))
connection.close()
