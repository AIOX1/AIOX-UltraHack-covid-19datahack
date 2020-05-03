# Intro

Here is the link for our video:

https://drive.google.com/file/d/1nik6CoDbA9lz_JCek2fXpkeANetvJQMj/view

### Context

This repository contains information about what was developed by AIOX during the UltraHack challenge Data against Covid19.

We describe here what problems we had to solve and how we solved them. Some of the solutions include pieces of code from our operations, which we couldn't include here due to IP reasons.

AIOX develops an automated news analysis solution for investment banking sector, thanks to machine learning algorithms.
We crawl relevant media sources, find trending topics and news circulation patterns, to provide insights to our prospects and customers.

### Objective

Here, our objective is to track the economic impact of the Covid crisis. Tracking the economic impact of the Covid crisis is critical for decision-makers from public and private sector alike. Policy makers need to understand where is public support most needed, to optimize capital allocation. Private sector decision makers need to understand what's going on to improve their restart plans. For many organizations (ex: airports), a bad timing for their recovery plan can change their losses by the millions and job losses by the thousands.

### The Problem

Tracking the economic impact of Covid19 requires changes to our tech, since the problem is more open ended than what we usually do (insights limited to investment banking sector).

When we want to extract insights from the press, we use a 3-steps pipeline:
1- we select relevant media sources
2- we filter the noise (we can't apply algorithms to raw text from web pages)
3- we mine for patterns

Concretely, we need to adapt each of those steps to the Covid19 context.

# The code

### News sources selection

For step 1 (media sources selection), there is no particular challenge. We increase the size of our usual media corpus to include more generic, non-financial sources.

### Noise filtering

We have a web crawling infrastructure that we use to crawl the web. We fetch text from web pages, which contains many unwanted stuff (text from all ads etc).
In order to apply NLP (natural language processing), we need to filter out the noise. This is heavily sector-specific, since we use a lot context to find out which text is an ad, a journalist typo, etc.
We rely heavily on deep learning classification networks. For the UltraHack challenge, we were
able to widen our training datasets and finetune those networks to work in a Covid news analysis
context.
Thanks to this transfer learning, the deep neural networks we usually use now manage to perform
accurate predictions on non-finance only news.

Some functions descriptions can be found in the filter.py "placeholder" code file.

### Pattern mining

We use a mix of TF IDF analysis, and articles vectorization techniques to compute distances between articles, and perform clustering analysis (for instance, when outliers start becoming their own cluster, it means a new topic is emerging).
We also analyze news propagation pattern, eg sudden changes in propagation speed.

Some functions descriptions can be found in the mine.py "placeholder" code file.

### Web Viz

We set up a basic AngularJS web application to visualize data from our Hackathon analysis.

# Questions?

Feel free to contact fruty@aiox.io
