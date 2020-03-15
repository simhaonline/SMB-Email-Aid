# https://github.com/minimaxir/gpt-2-simple

import gpt_2_simple as gpt2
import os
import requests

def gpt_2_simple_train(file_name: str):

    model_name = "124M"

    # model is saved into current directory under /models/124M/
    if not os.path.isdir(os.path.join("models", model_name)):
        print(f"Downloading {model_name} model...")
        gpt2.download_gpt2(model_name=model_name)

    sess = gpt2.start_tf_sess()
    gpt2.finetune(sess,
                  file_name,
                  model_name=model_name,
                  steps=1000)    # steps is max number of training steps

    gpt2.generate(sess)

gpt_2_simple_train("marketing_phrases.txt")
