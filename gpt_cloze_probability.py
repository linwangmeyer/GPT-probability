import openai
import pandas as pd
import math
import numpy as np
import itertools

openai.api_key = "YOUR-KEY" #get it from your openai account

def get_top_nword_completions(prompt, num_words):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=0,
        top_p=1,
        logprobs = num_words, 
        frequency_penalty=0,
        presence_penalty=0, 
        echo=True
    )
    top_logprobs = completions["choices"][0]["logprobs"]['top_logprobs'][-1] #for the last token
    words = []
    probs = []
    for word, logprob in top_logprobs.items():
        print(f"Word: {word}, Log Probability: {np.e**logprob}")
        words.append(word.strip())
        probs.append(np.e**logprob)
    # save the data to a dictionary
    x = {word:prob for word, prob in zip(words,probs)}
    return x
    
#############################################
## start from here
#############################################
# Load the data from the CSV file
df = pd.read_csv('orthoRep_stim_forGPT3_PretargetWords.csv')
contexts = df['Context'].tolist()
target_word = df['Target'].tolist()

# Set up an empty list to store the results
results = []
for i,context in enumerate(contexts):
    print(context)
    
    # Get the top 5 completions for the prompt
    top_5_completions = get_top_nword_completions(context,5)
    
    #check if target is in the top 5, and get the cloze value
    if target_word[i] in top_5_completions.keys():
        target_cloze = top_5_completions[target_word[i]]
    else:
        target_cloze = min(top_5_completions.values())
    
    #get the cloze for all top 5 continuations
    row = list(itertools.chain.from_iterable((k, v) for k, v in top_5_completions.items()))  
    
    #combine with the target word and cloze values
    row.insert(0, target_word[i])
    row.insert(1, target_cloze)
    
    results.append(row)  
    

# Convert the results to a DataFrame
col_names = ['Target','Target_cloze',
             'top1','top1_cloze',
             'top2','top2_cloze',
             'top3','top3_cloze',
             'top4','top4_cloze',
             'top5','top5_cloze']
results_df = pd.DataFrame(results,columns=col_names)

#combine the cloze outputs with the other part of the table
output = pd.concat([df.iloc[:, :df.columns.get_loc('Context')+1],results_df],axis=1)

# Save the results to a CSV file
output.to_csv('gpt3_cloze_results.csv', index=False)
