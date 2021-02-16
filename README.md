# Text classification with graph neural networks

This project is about using graph neural networks (GNNs) as a method to improve text representation in classification task.

## Dataset
In the project problem of classification polish Wikipedia pages to science fields was considered. Pages were parsed from polish Wikipedia dump and labelled by matching their categories to the closest of the seven choosen main categories related with science fields based on scrapped Wikipedia categories tree. Also links between pages were saved during dump parsing.

## Graphs
Two types of graphs have been used.

**Articles graph** - node represent pages ang edges between nodes represent links between articles.

**Articles and words graph** - this graph is articles graph extended by nodes representing words and edges between word nodes and article nodes created if word appears in article. In this approache as word nodes were considered only some number of most common specific nouns from each category.

## Methods
Few approaches have been combined and compared in the project.

Initial text representaion:
- one-hot encoding of selected most common and specific nouns for article nodes,
- [HerBERT](https://github.com/allegro/HerBERT) embedding for article nodes,
- [fastText](https://github.com/sdadas/polish-nlp-resources) embedding for word nodes,
- [Word2Vec](https://github.com/sdadas/polish-nlp-resources) embedding for word nodes.

Classification models:
- MLP as a baseline model,
- [GCN](https://stellargraph.readthedocs.io/en/stable/api.html#stellargraph.layer.GCN) + MLP,
- [GAT](https://stellargraph.readthedocs.io/en/stable/api.html#stellargraph.layer.GAT) + MLP.

## Results
Pipelines visualisation and all results are available in this [presentation](https://docs.google.com/presentation/d/18CCJkarKveK2ipv39uiDpUuNiH2JJqEgfQjidMj1Pyg/edit?usp=sharing).

Conducted experiments showed that acquired pages can be proper classified using HerBERT embeddings and simple MLP. In this scenario GNNs didn't improve the results. But using poorer (also faster to calcualte) representation, like one-hot encoding of selected nouns, GNNs gave significant improve (equaled the results to HerBERT scenario).

## Project structure
**Articles** - fixed and modified version of this Wikipedia dump [parser](https://github.com/alvations/rubyslippers). Customized to work with polish dump, read categories and save annotations as list of edges.

**Categories** - celery based Wikipedia categories tree scraper.

**Experiments** - folder with additional data processing and conducted experiments:
- **gcn_1.ipynb** - HerBERT embeddings preparation,
- **gcn_2.ipynb** - MLP and GNNs models on articles graph with HerBERT embeddings,
- **gcn_3.ipynb** - MLP and GNNs models on articles graph with one-hot representation,
- **gcn_4.ipynb** - Word2Vec and fastText embeddings preparation,
- **gcn_5_ft.ipynb** - GNNs models on articles and words (140 selected nouns) graph with fastText embeddings for word nodes,
- **gcn_5.ipynb** - GNNs models on articles and words (140 selected nouns) graph with Word2Vec embeddings for word nodes,
- **gcn_6_ft.ipynb** - GNNs models on articles and words (280 selected nouns) graph with fastText embeddings for word nodes,
- **gcn_6.ipynb** - GNNs models on articles and words (280 selected nouns) graph with Word2Vec embeddings for word nodes.

**Network** - pages graph creation and exploration.