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
Although we have provided the first steps towards improving algorithm analysis for $\SG$s, 
there are still many fields of our work that act as a base for further improvements.

The model features we analyze at the moment helped us to draw some conclusions, but there are still many questions unanswered that would require
additional structural concepts and features that we track.
These questions are, for example, when to use Gauss-Seidel optimization or whether there is a model structure that consistently makes $\OVI$ faster than $\WP$.

In addition, there are still many data analysis techniques we did not implement yet, like stochastic tests or artificial intelligence algorithms
that can cluster features and find correlations between them. 

We believe that more research on the correlation between algorithm performance and structural properties gives way to a portfolio solver, which could first
analyze important structural features, and then pick heuristically the most adequate algorithm to solve the problem.
With enough models, the decision of which algorithm to use may be made by a neural network.
Also, combinations of algorithms like $\OVI$ and $\WP$ could be used effectively in a fitting scenario.
The user would have to pay the overhead for computing more vectors but may converge faster.

Since algorithm performance may change drastically depending on the models' size,
we need to resolve the issue that our random generation process creates large explicit files which PRISM cannot handle.
The next step would be to create an optimization system for our random generation algorithm that takes advantage of the PRISM language and holds chunks of the data in 
implicit blocks or uses modules to make the files easier parsable.

Furthermore, at the moment, our random generation algorithm enforces a tendency of states with smaller indices to have more actions than states with higher indices.
Ideally, the user should be able to remove this restriction.
This could be addressed by introducing mechanisms like, for example, that a state $\stateMac_i$ can only be connected to states $\stateMac_{j}$ with $j \in [i-50, i+50]$.
Another way to improve the random generation algorithm is to find a method of reducing the models' numbers of states that can be computed trivially.

Ultimately, improving random algorithm generation and learning more about model structure are the basis for what could become a uniform benchmarking set that could be used by everyone creating algorithms for $\SGs$ to 
test and improve their algorithms.

In conclusion, we have taken the first step towards improving algorithm analysis for SGs, 
and we have provided many promising directions for improvements of the algorithm analysis, the random model generation, and the algorithms themselves.
""" 

#pyperclip.copy(strip(inp))
print(strip(inp))