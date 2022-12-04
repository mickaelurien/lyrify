<script>
    import Wrapper from './Wrapper.svelte';
    import { artist_choose, step } from '../store.js';

    const artists = [
        {
            name : 'Damso', slug: 'damso', img: 'damso.jpg'
        },
        {
            name : 'Pnl', slug: 'pnl', img: 'pnl.jpg'
        },
        {
            name : 'Alpha Wann', slug: 'alphawann', img: 'alphawann.jpg'
        },
        {
            name : 'Booba', slug: 'booba', img: 'booba.jpg'
        },
        // {
        //     name : 'Angèle', slug: 'angle', img: 'angele.png'
        // },
        {
            name : 'Orelsan', slug: 'orelsan', img: 'orelsan.jpg'
        }
    ]

    const getArtistImg = (img) => `./artists/${img}`;
</script>

<div>
    <Wrapper>
        <h1>Choisissez un artiste</h1>

        <div class="artists-container">
            {#each artists as {name, slug, img}}
                <div class="artist" class:choose={$artist_choose == slug} on:click={() => $artist_choose = slug}>
                    <div class="img-wrapper">
                        <img src="{getArtistImg(img)}" alt="{slug}">
                    </div>
                    <p>{name}</p>
                </div>
            {/each}
        </div>

        <button class:disabled={$artist_choose == ''} on:click|once={() => $step++}>Générer</button>
    </Wrapper>
</div>


<style>
    .artists-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        margin: 2.5em;
    }
    .artist {
        cursor: pointer;
        margin: 0 2em;
        text-align: center;
    }

    .artist > .img-wrapper {
        border: 2px solid rgba(255,255,255,0.5);
        width: 150px;
        height: 150px;
        border-radius: 5px;
        transition: border 0.2s ease;
    }
    .artist.choose > .img-wrapper {
        border-color: white;
    }

    .artist > .img-wrapper > img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 5px;
        opacity: 0.5;
        transition: opacity 0.2s ease;
    }
    .artist.choose > .img-wrapper > img {
        opacity: 1;
    }

    .disabled {
        opacity: 0.5;
        pointer-events: none;
    }

    @media screen and (max-width: 768px) {
        .artists-container {
            margin: 0 1em;
        }
        .artist {
            margin: 0 1em;
        }
        .artist > .img-wrapper {
            height: 120px;
            width: 120px;
        }
    }
    @media screen and (max-width: 400px) {
        .artist {
            margin: 0 0.5em;
        }
        .artist > p {
            margin-top: 8px;
        }
        .artist > .img-wrapper {
            height: 80px;
            width: 80px;
        }
    }
</style>
