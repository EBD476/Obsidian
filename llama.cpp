Ran an LLM on Android Phone with LLaMA.cpp

- Download termux [https://f-droid.org/packages/com.termux/]
  $ termux-setup-storage
  $ apt update && upgrade -y
  $ pkg install clang wget cmake
  
- Download llama.cpp [https://github.com/ggerganov/llama.cp]
  release : b2144
  $ mv llma.cpp-b2144 llma.cpp
  $ make
  

- Download TinyLLaMA.GGUF (Recommended for 4 GB RAM): https://huggingface.co/TheBloke/TinyL.
  $ wget https://huggingface.co/TheBloke/TinyLlama1-1.1B-Chat-v1.0-GGUF/resolve/main/tinylama-1.1b-chat-v1.0.Q5 ...
  $ cd models/7B
  $ mv tinylama-1.1b-chat-v1.0.Q5_K_M.gguf ggml-model-f16.gguf
  $ ./server
  
- Web server on http://127.0.0.1:8080

------------------------------------------------
whisper.cpp

$ git clone https://github.com/ggerganov/whisper.cpp.git
$ ./models/download-ggml-model.sh base.en
$ make
$ ./main -f samples/jfk.wav
$ make command 

# Run with default arguments and small model
& ./command -m ./models/ggml-base.en.bin -t 8 

# On Raspberry Pi, use tiny or base models + "-ac 768" for better performance
./command -m ./models/ggml-tiny.en.bin -ac 768 -t 3 -c 0

# Run in guided mode, the list of allowed commands is in commands.txt
./command -m ./models/ggml-base.en.bin -cmd ./examples/command/commands.txt

# On Raspberry Pi, in guided mode you can use "-ac 128" for extra performance
./command -m ./models/ggml-tiny.en.bin -cmd ./examples/command/commands.txt -ac 128 -t 3 -c 0
