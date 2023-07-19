
```node
const { Configuration, OpenAIApi } = require("openai");
const fs = require('fs');

const configuration = new Configuration({
  //   apiKey: process.env.OPENAI_API_KEY,
      apiKey: "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"
  });

// Load your key from an environment variable or secret management service
// (do not include your key directly in your code)
const OPENAI_API_KEY = "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";

// const openai = new OpenAI(OPENAI_API_KEY);
const openai = new OpenAIApi(configuration);

const targetLang = "persian";

const messages1 =  [
  {
      role: "system",
      content: `You are a helpful assistant that translates a i18n locale array content to ${targetLang}. 
      It's a array structure, contains many strings for software program, this is for kibana software , dont translate keywords, translate each of them and make a new array of translated strings.
      Consider all the string as a context to make better translation .\n`,
  },
];

const jsonInputFilePath = 'd:/temp/input.json';
const jsonFilePath = 'd:/temp/output.json';

const jsonData = fs.readFileSync(jsonInputFilePath);
const jsonObject = JSON.parse(jsonData);


(async ()=>{
  const response = await openai.createChatCompletion(
    {
      
        model: "gpt-3.5-turbo",
        messages: [
            ...messages1,
            {
                role: "user",
                content: JSON.stringify(jsonObject)
            },
        ]
    })
    
    console.log(response.data.choices[0].message.content);

    fs.writeFileSync(jsonFilePath, response.data.choices[0].message.content.replaceAll('",','",\r\n'));
    console.log('Translation completed successfully!');

})();

```

translate  with file split 

```node
const { Configuration, OpenAIApi } = require("openai");
const fs = require('fs');
const readline = require('readline')

const configuration = new Configuration({
  //   apiKey: process.env.OPENAI_API_KEY,
      apiKey: "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"
  });


// const openai = new OpenAI(OPENAI_API_KEY);
const openai = new OpenAIApi(configuration);
const targetLang = "persian";

const messages1 =  [
  {
      role: "system",
      content: `You are a helpful assistant that translates a i18n locale array content to ${targetLang}. 
      It's a array structure, contains many strings for software program, this is for kibana software , dont translate keywords, translate each of them and make a new array of translated strings.
      Consider all the string as a context to make better translation .\n`,
  },
];

const jsonInputFilePath = 'd:/temp/input.json';
const jsonFilePath = 'd:/temp/output.json';

function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

let start = 550;
const numRowsToRead = 40;

// read the file as a string
const fileData = fs.readFileSync(jsonInputFilePath, 'utf8');
// parse the file data as JSON
const jsonData = JSON.parse(fileData);
// convert the JSON data to an array of key-value pairs
const dataEntries = Object.entries(jsonData);

readAndWriteData(dataEntries,start);

async function readAndWriteData(dataEntries,start) {
    // get the current set of rows
    const selectedEntries = dataEntries.slice(start, start + numRowsToRead);
    // convert the selected entries back to a JSON object and output it
    const selectedJsonData = Object.fromEntries(selectedEntries);
    
    console.log(selectedJsonData);
    console.log("start= ",start)
    
   start += numRowsToRead;
   if (start < 800){
    await tranlateJson(selectedJsonData,start);
   }
}

  async function tranlateJson(selectedJsonData,start) {
	   try {
	    const response = await openai.createChatCompletion(
	    {
	      
	        model: "gpt-3.5-turbo",
	        messages: [
	            ...messages1,
	            {
	                role: "user",
	                content: JSON.stringify(selectedJsonData),
	            },
	        ]
	    })
	    //console.log(response.data.choices[0].message.content);
	    fs.writeFileSync(jsonFilePath, response.data.choices[0].message.content, { flag: 'a' });
	    fs.writeFileSync(jsonFilePath, "\r\n", { flag: 'a' });
	    console.log('Translation completed successfully!');
	    
	    await readAndWriteData(dataEntries,start);
	
	  } catch (error) {
	    console.error(error);
	  }
	}

```