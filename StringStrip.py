import re
import pyperclip

def strip(s : str):
    s = s.replace('\\emph', '')
    s = s.replace('\\item', '')
    s = s.replace('\texttt', '')
    s = s.replace('\f', '\\f')
    s = s.replace('\a', '\\a')
    s = s.replace('\b', '\\b')
    s = s.replace('\t', '')
    s = s.replace('    ', '')
    
    
    s = re.sub(r'\\cite{.*?}', 'CITATION', s)
    s = re.sub(r'\\ref{.*?}', 'A', s)
    s = re.sub(r'\ref{.*?}', 'A', s)
    s = re.sub(r'\\begin{.*?}', '', s)
    s = re.sub(r'\\end{.*?}', '', s)
    s = re.sub(r'\\label{.*?}', '', s)
    s = s.replace('mathbf', '')    
    s = s.replace('{', '')
    s = s.replace('}', '')
    s = s.replace('\\', '')
    s = s.replace('$', '')
    return s

inp = '' + \
"""

Table \ref{tab:genTime} provides an overview of the algorithm needs to generate models with 10000, 100000, and 1000000 states and 1, 10, or 100 actions.
Clearly, the generation process is becoming significantly slower for large models. This is mostly due to way we generate actions (as described in Algorithm \ref{alg:FillActions}). 
When selecting a random state the action should lead into, we have to ensure this state has is not yet included in $\post$ of current state-action pair. 
Thus, we subtract the states we already reach in the state-action pair from all the possible states. 
Subtracting the sets for every transition poses the bottleneck in our generation process.
To fix this issue, we provide the \texttt{--fastTransitions} switch. 
When used, we hold a stack of shuffled state indices that we pop whenever we need to generate a new transition. 
The switch makes the generation slightly more predictable, but decreases the time required considerably as \ref{tab:genTime} shows.
Lastly, since PRISM requires more time to parse a model every time an algorithm must solve it than we need to generate the model, 
and since due to PRISM we are bound to using randomly generated models of size no larger than 50000 states, 
we conclude that the time performance is not an issue for now.
""" 

pyperclip.copy(strip(inp))
print(strip(inp))