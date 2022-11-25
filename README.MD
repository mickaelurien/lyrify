

# Lyrify

<h1 align="center">
  <br>
  <a href="https://mickaelurien.fr/projexts/lyrify"><img src="https://mickaelurien.fr/projects/lyrify/logo.png" alt="Lyrify" width="200"></a>
  <br>
  Lyrify
</h1>

<h4 align="center">A lyrics generator based on an artist's style.</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#acknowledgments">Acknowledgements</a>
</p>

## Key Features
- Scrape lyrics from a website with the artist name
	- Scrape proxies from a [free proxy list](https://free-proxy-list.net/)
	- Each request use a random proxy, header and user-agent
	- Store the content of each song in a [artist].txt file
- Generate lyrics from the .txt file with the help of [markovify](https://github.com/jsvine/markovify)
- Endpoint with [FastApi](https://fastapi.tiangolo.com) who return the lyrics from an artist name
- Pretty interface for user pleasure with [Svelte](https://svelte.dev/)



## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Node.js](https://nodejs.org/en/download/) (which comes with [npm](http://npmjs.com)) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/amitmerchant1990/electron-markdownify

# Go into the repository
$ cd electron-markdownify

# Install dependencies
$ npm install

# Run the app
$ npm start
```

## Acknowledgments

- https://gitlab.com/random-dude for personal help and tips 😉

- https://www.youtube.com/watch?v=dT1aKuUsKUE (On code un générateur de texte ! (avec Python et des chaînes de Markov))

- https://www.youtube.com/watch?v=HfGH28j2TbA (Apprendre le Web Scraping avec Python Français)

- https://www.youtube.com/watch?v=hHgY40rRGQg (Web Scraping - Éviter la détection ! (Python))

---
