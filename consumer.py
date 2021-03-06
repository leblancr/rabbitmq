import pika, os, time

def pdf_process_function(msg):
    print(" PDF processing")
    print(" Received %r" % msg)
    
    #time.sleep(5) # delays for 5 seconds
    print(" PDF processing finished");
    return;

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://bierhrnn:kIYntLtzZ4TIbRCsUiPLDpNywzbdZfLB@otter.rmq.cloudamqp.com/bierhrnn')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='pdfprocess') # Declare a queue

# create a function which is called on incoming messages
def callback(ch, method, properties, body):
    print("In callback function");
    print("ch: {}\n" \
    "method: {}\n" \
    "properties: {}\n" \
    "body: {}\n" \
    .format(ch, method, properties, body))
     
    #pdf_process_function(body)
    
    
# set up subscription on the queue
channel.basic_consume(callback, queue='pdfprocess', no_ack=True)

# start consuming (blocks)
print("start_consuming");
channel.start_consuming()
print("done consuming");
connection.close()
