# ***Extração de sentimentos com python***

 **Introdução**

Esse repositório foi criado para o estudo de automatizações de extração de sentimentos utilizando python e a biblioteca NLTK que possui a ferramenta chamada VADER (Valence Aware Dictionary and Sentiment Reasoner) é uma ferramenta de análise de sentimento especialmente projetada para lidar com textos informais, como postagens em redes sociais, comentários, e outros tipos de comunicação digital. É parte da biblioteca nltk (Natural Language Toolkit) e é amplamente utilizada para análise de sentimento devido à sua eficiência e precisão.

Nos dias atuais, de grandes empresas a pequenos comercios na internet, precisamos lidar com grandes volumes de dados, e necesitamos de ferramentas que otimizem o nosso tempo, pois não é possível analisar comentário a comentário para chegar a uma decisão, de forma eficaz e rápida.

**Explicação**

Inicialmente descobri como a ferramenta funciona, utilizando uma frase pré estabelecida: 

*Você pode acessar o código no link: [Analise.py](https://github.com/lethiciaasevedo1999/analise-sentimento-python/blob/main/analise.py)*

<div align= "center">
<img src="/Assets/testedeextracao.png" alt="Código e resultado do teste">
</div>

Acima podemos ver como foi simples trabalhar com a biblioteca. Neste explo fiz o import da mesma, logo em seguida importei o analizador de sentimentos. Chamei a ferramenta VADER e iniciei o processo.   

No terminal podemos ver o resultado, sendo :    
- **neg** : para comentários negativos.   
- **neu** : para comentários neutros.  
- **pos** : para comentários positivos.   
- **compound** : índice geral, sendo resultado acima de 0 significa positivo e resultado abaixo de 0 negativo.

A análise chegou a conclusão de que meu comentário era positivo, com índice geral acima de 0. 

# ***Testando com base de dados reais***

Em seguida, procurei testar a ferramenta com dados reais, que pode ser acessada no link : [Análise com base de dados reais](https://github.com/lethiciaasevedo1999/analise-sentimento-python/blob/main/An%C3%A1lise%20com%20base%20real/analise.ipynb)

Após análise automatizada da base de dados importada, chegamos á conclusão que os parques possuem boas avaliações em sua maioria, já que o número do índice geral ficou positivo, e os comentários positivos possuem uma proporção bem maior aos negativos.

<img src="/Assets/dados-reais.png" alt="Resultado da análise utilizando dados reais">


# ***Conclusão***

O projeto mostrou como com poucas linhas de código, conseguimos automatizar um processo que poderiam durar dias, sendo necessário aumento de mão de obra para realizar a tarefa no modo manual, também pudemos ver o quão precisa foi a biblioteca utlizada no processo.

### **Fontes** : 🔎

Base de dados utilizada: 📂[Disneyland Reviews](https://www.kaggle.com/datasets/arushchillar/disneyland-reviews)  
Fonte: 📂[Kaggle](https://www.kaggle.com/)

### **Ferramentas utilizadas no projeto :**

- 📌Python versão 3.12.6 [Documentação](https://devdocs.io/python~3.12/)
- 📌Biblioteca NLTK versão 3.9.1 [Documentação](https://www.nltk.org/)
- 📌Extensão Jupyter Notebook versão 4.9.1 [Documentação](https://docs.jupyter.org/en/latest/)

### **Me sigam nas redes sociais :**

- 🔗[Linkedin](https://www.linkedin.com/in/lethiciaasevedo/)
- 🔗[Github](https://github.com/lethiciaasevedo1999)