import ollama


class CompletionEngine:
    def __init__(self, model: str, options={}, fill_in_middle: bool = False):
        self.model = model
        self.client = ollama.Client("http://localhost:11434")
        self.options = options
        self.fim = fill_in_middle

    def complete(self, lines, line, character) -> ollama.GenerateResponse:
        context = ""
        if self.fim:
            lines[0] = "<|fim_prefix|>" + lines[0]
            lines[line] = lines[line][:character] + \
                "<|fim_suffix|>" + lines[line][character:]

            context = "\n".join(lines) + "<|fim_middle|>"
        else:
            context = "\n".join(
                lines[:line]) + "\n" + lines[line][:character]

        return self.client.generate(
            model=self.model,
            prompt=context,
            stream=True,
            options=self.options
        )
