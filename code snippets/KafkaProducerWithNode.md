Create kafka producer with nodejs
this code send sample data to kafka test-topic 
Method-1
```node
const { faker } = require('@faker-js/faker');
const { Kafka } = require('kafkajs');

// Define the Kafka broker(s)
const kafka = new Kafka({
  clientId: 'my-app',
  brokers: ['localhost:29092']
});

// Define the topic to send messages to
const topic = 'test-topic';

// Create the producer instance
const producer = kafka.producer();

// Connect to the Kafka broker(s)
async function connect() {
  await producer.connect();
}

// Send a message to the Kafka broker(s)
async function sendMessage() {

    var data = {};
    let messages_array=[];
    for (let i = 0; i <= 10; i++)
    {
        data = {    
            tid : faker.string.uuid(),    
            account: faker.finance.accountName(),
            accountNumber: faker.finance.accountNumber(),
            amount: faker.finance.amount(),
            iban: faker.finance.iban(),
            pin: faker.finance.pin(),
            transactionType: faker.finance.transactionType(),
            transactionDescription: faker.finance.transactionDescription(),
            registeredAt: new Date().toISOString,
        }
        messages_array.push({ value: JSON.stringify(data)})
    }

  await producer.send({
    topic: topic,
    messages: messages_array
  });

  console.log('Message sent successfully!');
}

// Disconnect from the Kafka broker(s)
async function disconnect() {
  await producer.disconnect();
}

// Run the producer
async function runProducer() {
  await connect();
  await sendMessage();
  await disconnect();
}

runProducer();
```

Method-2
```node
const Kafka = require('kafkajs');
const logLevel = require('kafkajs');
const uuidv4 = require('uuid');

const kafka = new Kafka({
  clientId: "random-producer",
  brokers: ["localhost:29092"],
  connectionTimeout: 3000,
});
var randomstring = require("randomstring");
const randomMobile = require("random-mobile");
const producer = kafka.producer({});
const topic = "elastic-test";

const produce = async () => {
  await producer.connect();
  let i = 0;

  setInterval(async () => {
    var event = {};
    try {
      event = {
        globalId: uuidv4(),
        event: "USER-CREATED",
        data: {
          id: uuidv4(),
          firstName: randomstring.generate(8),
          lastName: randomstring.generate(6),
          country: "India",
          email: randomstring.generate(10) + "@gmail.com",
          phoneNumber: randomMobile(),
          city: "Hyderabad",
          createdAt: new Date(),
        } ,
      } ;
      await producer.send({
        topic,
        acks: 1,
        messages: [
          {
            value: JSON.stringify(event),
          },
        ],
      });

      // if the message is written successfully, log it and increment `i`
      console.log("writes: ", event);
      i++;
    } catch (err) {
      console.error("could not write message " + err);
    }
  }, 5000);
};

module.exports = produce;
```