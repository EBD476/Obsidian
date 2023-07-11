Create node express service api for random user in postgres  database :

```node
const express = require('express');
const json = require('express');
const {faker} = require('@faker-js/faker');
const dataArray = require('./data/datasetSamples')
const { Pool } = require('pg');


const app = express();
app.use(json());
 
// Create a connection pool to the PostgreSQL database
const pool = new Pool({
    user: 'postgres',
    host: 'localhost',
    database: 'postgres',
    password: 'postgres',
    port: 5432,
  });

const api_test = [
    {name: 'name', value: 'td-name'},
    {name: 'tid', value: 1236448},
    {name: 'tdate', value: '2023-05-01'}
]

function createRandomUser() {
    return {
      datasetId: faker.number.int().toString(),
      datasetName: faker.airline.airline().name,                  
      tid : faker.string.uuid(),
      registeredAt: faker.date.past(),
    };
  }

app.get('/api/v1/rdata', (req,res)=> {

    // var randomName = faker.string.uuid();         
    const ipAddress = req.ip;
    console.log(`GET Method requeted from ${ipAddress}`);

    const randomUser= createRandomUser();

    res.send(randomUser);
});  

app.get('/api/v1/data',async (req,res)=> {
    
    const ipAddress = req.ip;
    console.log(`GET Method requeted from ${ipAddress}`);

    const user_id = Math.floor(faker.number.int()/1000000000);
    const result = await pool.query('INSERT INTO accounts (user_id, username,email,password,created_on) VALUES ($1, $2,$3,$4,$5) RETURNING user_id', 
            [user_id,faker.internet.userName(),faker.internet.email() , faker.internet.password(),faker.date.past()]);

    console.log(result);
    res.send(dataArray[0]);
});  

app.post('/api/v1/ps', (req, res)=> {
 
    const body = req.body;
    console.log(body)
    res.send(body);
 });

//PORT ENVIRONMENT VARIABLE
const port = process.env.PORT || 8085;
app.listen(port,'0.0.0.0', () => console.log(`Listening on port ${port}..`));
```