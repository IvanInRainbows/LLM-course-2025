# Using LLMs and Prompting-based approaches

## Lecture

Slides can be found here: [Week 2 Slides](https://github.com/Helsinki-NLP/LLM-course-2024/blob/main/week-2/LLM-Course%20Lecture%202.pdf).


## Preparation for the lab

**Gemini API Key**
* Use your existing google account or create a new free account
* Go to https://aistudio.google.com/apikey
* Get your API key and store it in a safe place

**Create a HuggingFace account**
* https://huggingface.co/join

**Set up Python & Jupyter environment**
* I use Python 3.12 for running code locally
* For inference or fine-tuning requiring GPU, I use Google Colab: https://colab.research.google.com/


## Lab Exercise

For this exercise use the gemini-chatbot and/or prompting-notebook found in GitHub under week-2 folder. 
Select a domain (e.g. finance, sports, cooking), tone of voice, style and persona (e.g. a pirate) and a question/task you want to accomplish (e.g. write a blog post)
* Modify the gemini-chatbot and test the different prompting approaches discussed in the lecture to achieve the task.
* Do the same for prompting-notebook (run this in Google Colab using a T4 GPU backend)
* Write a section to your report explaining what you did and what were your findings. Which prompting approach worked the best and why? 

Modify the in-context-learning notebook (you can run this locally or in Google Colab)
* Modify the prompt to change the style of the output to be a table with strengths and weaknesses in separate columns. (Markdown printing should show the table correctly. If you have time, modify the html printing to show the updated style as a table).
* If you have time: modify the notebook to use an open source model from Hugging Face instead of Gemini

### Exercise

I tried both the chatbot python script and the prompting jupyter notebook. I made most of this part in the notebook because the output suited better the task, as the output was written in markdown. For the task I asked Gemini to generate a law that forbids the emission of violent content in the Spanish public television written in formal and academical Spanish and no longer than 4000 characters. For this, three prompting techniques were tested: Zero-shot, One-shot (using the text in a webpage as reference) and, finally, chain of thought (still using the reference from the one-shot). I found all answers to be adequate and well written but with some minor differences:

1. Zero-Shot: The promt was "Can you write a law that forbids the emmission of violent content in the Spanish public television? The text should be no longer than 4000 characters. It should also be written in formal and academical Spanish.". The answer was very well written but with some caveats:

    * Lacking signatures of authorities: It is expected that published and enforced laws are signed by the authorities, which in the case of Spain most of the time include the king and the president. These were not present in this first answer.

    * Structure: Although the structure was adequate it did not completely resemble a true published law, as these have different chapters which contain the articles. The answer also lacks the date and number of the law.

2. Few-shot/One-Shot: The prompt was "Can you write a law that forbids the emmission of violent content in the Spanish public television? The text should be no longer than 4000 characters. It should also be written in formal and academical Spanish. The structure should mimic the one found here: https://www.boe.es/buscar/act.php?id=BOE-A-2015-3442". The result using this prompting technique improved vastly, now containing the signatures of both the king and president (this one was a placeholder), date, law number and such. The structure also resembles the reference that was given, which was a real law. The only caveat is that the king's signature is from pre previous one, which makes it a bit outdated.

3. Chain of Thought: The prompt was "Can you write a law that forbids the emmission of violent content in the Spanish public television? The text should be no longer than 4000 characters. It should also be written in formal and academical Spanish. The structure should mimic the one found here: https://www.boe.es/buscar/act.php?id=BOE-A-2015-3442. Expose some reasons that led to this legislation in the preamble. Some articles should refer to these reasons by explaining how they affect them. Replace al the placeholders with actual values, for example, the law should be written using today's date and signed by the current president and king of Spain. Make up the law number." The result is very similar to the previous one but with some differences. The structure does not completely resembles the reference and some protocol things are missing but in this one the placeholders are replaced with the current data for the king and president.

Overall I would say that the prompt technique that offered the best result was the second one, Few-Shot/One-Shot.

Regarding the second part of the exercise the in-context-learning notebook has been changed to display the table. Despite this, given that each table is a different prompt, the sometimes have different styles. The table works both in HTML and in Markdown.