
#### Image generation with nodejs

```node
const { Configuration, OpenAIApi } = require("openai");

const configuration = new Configuration({
  apiKey: "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",
});

const openai = new OpenAIApi(configuration);

const generateImg = async ()=>{
try{
    const imgData = await openai.createImage({
        prompt:"a admin panel ui",
        n: 1,
        size:"1024x1024",
    });
    
    const dataURL= imgData.data.data[0].url;
    console.log(dataURL)

}
catch(error){
    throw new Error(error)
}
}

generateImg();
```