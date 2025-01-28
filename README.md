# olly.nvim

olly.nvim is a generative AI code completion plugin like GitHub Copilot. It is based on [Ollama-Copilot](https://github.com/Jacob411/Ollama-Copilot).
To date, most of the plugin code is by Jacob411. Obviously, huge thanks to Jacob411.
Ollama-Copilot is licensed under MIT.

This is a fork with the intention of going my own direction with the plugin.
My immediate focus was on finishing up the existing fill-in-the-middle completion.
Second, I aim to select a few models that I believe will work best, rather than opening it up for any model.
This is because I believe the current best small coding model is Qwen2.5-coder, offering model sizes down to a mere half a billion parameters, allowing it to be run on devices such as a raspberry pi.
Qwen2.5-coder has a specific FIM template which isn't compatible with other models.

Some additional planned improvements include the name of the file, the content in other files, etc. for more context-aware completions.
Qwen2.5-coder comes with builtin templating options for these features.
Additionally, I plan to look into YaRN, something that will help expand the context length and understanding of these Qwen models, hopefully allowing it to handle more than 32k tokens worth of data.

This project is deeply under construction and not ready so listen to the readme with caution.

One frustrating known issue is losing access to the tab button :(.
This is being worked on.

## Overview
### Copilot-like Tab Completion for NeoVim
olly.nvim allows users to integrate their Ollama code completion models into Neovim, giving GitHub Copilot-like tab completions.  
  
Offers **Suggestion Streaming** which will stream the completions into your editor as they are generated from the model.

### Optimizations:
- [x] Debouncing for subsequent completion requests to avoid overflows of Ollama requests which lead to CPU over-utilization.
- [x] Full control over triggers, using textChange events instead of Neovim client requests.
### Features
- [x] Language server which can provide code completions from an Ollama model
- [x] Ghost text completions which can be inserted into the editor
- [x] Streamed ghost text completions which populate in real-time


## Install
### Requires
To use olly.nvim, you need to have Ollama installed [github.com/ollama/ollama](https://github.com/ollama/ollama):  
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
Also, the language server runs on Python, and requires two libraries (Can also be found in python/requirements.txt)
```bash
pip install pygls ollama
```
Make sure you have the model you want to use installed, a catalog can be found here: [ollama.com/library](https://ollama.com/library?q=code)
```
# To view your available models:
ollama ls

# To pull a new model
ollama pull <Model name>
```
### Using a plugin manager
Lazy:
```lua
-- Default configuration
{"trevin-j/olly.nvim", opts={}}
```
```lua
-- Custom configuration (defaults shown)
{
  'trevin-j/olly.nvim',
  opts = {
    model_name = "deepseek-coder:base",
    stream_suggestion = false,
    python_command = "python3",
    filetypes = {'python', 'lua','vim', "markdown"},
    ollama_model_opts = {
        num_predict = 40,
        temperature = 0.1,
    },
    keymaps = {
        suggestion = '<leader>os',
        reject = '<leader>or',
        insert_accept = '<Tab>',
    },
    fill_in_middle = false,
}
},
```
For more Ollama customization, see [github.com/ollama/ollama/blob/main/docs/modelfile.md](https://github.com/ollama/ollama/blob/main/docs/modelfile.md)

## Usage
olly.nvim language server will attach when you enter a buffer and can be viewed using:
```lua
:LspInfo
```
### Recomendations
Smaller models (<3 billion parameters) work best for tab completion tasks, providing low latency and minimal CPU usage.
- [deepseek-coder](https://ollama.com/library/deepseek-coder:1.3b) - 1.3B
- [starcoder](https://ollama.com/library/starcoder:1b) - 1B
- [codegemma](https://ollama.com/library/codegemma:2b) - 2B
- [starcoder2](https://ollama.com/library/starcoder2:3b) - 3B

