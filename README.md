This script allows you to use OpenAI's GPT-3 language model to calculate the probability of a target word appearing after a given sentence fragment.
For example, to calculate the cloze probability of the word "baby" following the sentence context "In the crib, there is a sleeping".
It also gives the cloze probability of the most probable five words following the context.

To use this script, you will need to have an OpenAI API key and the openai Python package installed.
Once you have installed the package and obtained your API key, you can use the gpt_cloze_probability.py script to calculate the probability of a target word appearing after a given sentence context.

You need o provide the script with the following arguments:

--api_key: Your OpenAI API key.

--csv file that contains a column of 'Context' and column of 'Target'. See ExampleInput.csv for example of layout.

--num_words: The number of words for which you want to calculate the cloze probability. The script will return the probability for the top num_words words that follow the given context.

Note
Please note that using the OpenAI GPT-3 API may incur charges to your OpenAI account. It is your responsibility to ensure that you have sufficient funds in your account to cover any charges incurred by using this script.

Also, please ensure that you comply with the OpenAI API terms of service when using this script.
