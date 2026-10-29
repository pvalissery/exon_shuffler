**Exon** **Shuffler**

https://pvalissery.github.io/exon_shuffler/

Exon Shuffler is a simple web tool designed to illustrate how biological complexity emerges from simple modular building blocks. By simulating the evolutionary mechanism of exon shuffling, the application lets users generate novel chimeric proteins from a curated library of established protein domains.

I've always been hooked on the idea of designing custom proteins from scratch. After spending years working in molecular biology, you realize how much of nature's complexity just boils down to mixing and matching a few structural Lego bricks. To explore the sheer breadth of what can be created, I built this 'recombination engine'.

First, I wrote a Python scraper to pull domain data from InterPro, mapping them to Gene Ontology (GO) terms to infer their baseline functions. The engine then takes these domains and shuffles them together at random. You can use the slider to control the number of domains, and the tool spits out a completely unique protein that probably wouldn't exist in nature right now. Ultimately, this app is a sandbox for creativity and a demonstration of the extreme versatility of molecular recombination.

**Features**

- **Interactive Shuffling** : Slider-controlled generation of chimeric proteins containing 2 to 10 distinct domains.
- **Curated Domain Library** : Runs completely in the browser using a bundled JSON dataset of protein domains and their associated biological functions.
- **Heuristic Function Prediction** : Procedurally generates natural language descriptions of what the resulting chimera might actually do in a cell based on keyword analysis of its constituent parts.
- **Zero Dependencies** : Built entirely with vanilla JavaScript and Tailwind CSS. No backend or database required. However, you can choose to use the included Python script to pull more domains from InterPro or plug in domains of your choice. 

**What's Next:** Directed Evolution

I am currently building a much more elaborate tool tailored for directed evolution. Instead of relying on random recombination, the focus is on targeted, industrial application-driven design.

You will be able to define a specific commercial or therapeutic use-case such as a highly stable industrial enzyme, a novel biosensor, or a specialized therapeutic and the tool will leverage a custom-built LLM to generate custom protein building blocks optimized for that exact niche. The platform will then map these domains together and output the codon-optimized nucleotide sequences required for scalable expression in standard heterologous biomanufacturing systems. Ultimately, the goal is to bridge the gap between prompt-driven design and commercial production, giving researchers a streamlined pipeline for rapid protein prototyping.
