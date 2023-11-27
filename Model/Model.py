import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Encoding
def encode(list_of_strings, tokenizer, pad_token_id=0):
    max_length = max([len(string) for string in list_of_strings])

    # create empty tensors
    attention_masks = torch.zeros((len(list_of_strings), max_length), dtype=torch.long)
    input_ids = torch.full((len(list_of_strings), max_length), pad_token_id, dtype=torch.long)

    for idx, string in enumerate(list_of_strings):
        # tokenize the string
        encoded = tokenizer.encode(string, add_special_tokens=True)

        input_ids[idx, :len(encoded)] = torch.tensor(encoded)
        attention_masks[idx, :len(encoded)] = 1

    return input_ids, attention_masks
    
# Decoding
def decode(outputs_ids, tokenizer):
    decoded_outputs = []
    for output_ids in outputs_ids.tolist():
        # transform id back to string
        decoded_outputs.append(tokenizer.decode(output_ids, skip_special_tokens=True))
    return decoded_outputs

def generate_dynamic_story(prompt, control_input=None, max_length=100):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    encoded, attention_masks = encode(prompt, tokenizer)
    
    if control_input is not None:
        # Include control input in the input_ids
        control_input_ids, _ = encode(control_input, tokenizer)
        input_ids = torch.cat([control_input_ids, encoded], dim=1)
        attention_masks = torch.cat([torch.ones_like(control_input_ids), attention_masks], dim=1)

    outputs = model.generate(input_ids, attention_mask=attention_masks, do_sample=True, max_length=max_length)
    decoded_output = decode(outputs, tokenizer)
    
    return decoded_output
    
def plug_and_play(prompt, max_length=100):
    # Users can plug in their own control input
    control_input = [input("Enter control input: ")]
    generated_story = generate_dynamic_story(prompt, control_input, max_length)
    print("Generated Story:")
    print(generated_story)

# Example usage:
prompt = ["A long time ago"]
plug_and_play(prompt)
