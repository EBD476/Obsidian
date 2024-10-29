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
