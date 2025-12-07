# Lab exercise

For this lab I programmatically queried the Mistral LLM with three sets of questions in Spanish, the code can be found in a notebook called [questions.ipynb](questions.ipynb). The first set of questions is composed of the questions in English, the second set is composed of the basic questions translated into Spanish. The third set of questions are localised versions of the basic ones in Spanish. Finally, the third set is composed of a more localised an contextualised version of the third one.

As expected the answers to the general questions are very correct and they are acceptable in most cultures, using neutral dialect (although with some regional words such as using "saco" as "sweater"). As an observation, in the second question all prices are in Euros, which is an interesting choice given that most Spanish speaking countries do not use that currency. The prices also change from one answer to another.

* Is there a difference between responses in two languages? In how many questions?

In question #7 there was a noticeable cultural/religious difference just by changing the language of the question. The question refers to the traditional easter meals and in the one written in Spanish the LLM writes about the *cuaresma* and how in some religious settings no meat is eaten during these days (in my experience this is not usual) so it mentions mostly non-meat based meals. In contrast, in the English written questions this is not mentioned and lamb dishes are listed as the traditional easter meal. This might be due to religious differences, given that Spanish speaking countries are catholic, whilst English speaking countries lean more towards reformist branches of christianism.

Question #11 also displays some differences, as tipping culture is different in USA (the answer seems to focus mostly in USA without mentioning other English speaking countries) and the Spanish speaking world, although the Spanish written question is answered with a more global response, mentioning USA, Canada and other countries in Europe.

I'd say there's difference in about 3-4 questions.

* Is there less difference if the questions are localised? In how many questions?

When we compare with the localized questions we usually see more specific information. I'd say about 33% of the answers comment on the Spanish values and/or traditions. It's funny how in the third question the localised version recommends *botellon*, which will be commented on the last question. Questions also include information regarding Spanish law, although some non localised questions in Spanish also assumed a Spanish localisation. These Spanish specific laws are mentioned in answers #2, #5, #6, #7, #12. The localised version also mention Spanish institutions such as *guardia civil*.

* Were there some entertaining responses or differences worth noting?

In the second question the LLM suggests *botellon* as a good event to meet new people, which strictly speaking is not a false statement. For context, *botellon* means that a group of people meet in a public place (a square, the street, a park, etc) generally to drink alcohol. This is generally frowned upon in Spain and it's, except for specific zones during local festivities, illegal. I don't think it's false information but suggesting *botellon* without commenting the risks (you can get a substantial fine) is not adequate.

There are some words that are translated literally from English such as "Azúcar libre" which sounds very funny because it means "free sugar" instead of "sugar free".