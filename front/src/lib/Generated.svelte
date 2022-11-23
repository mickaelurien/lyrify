<script>
    import { step, lyrics } from '../store.js';
    import Wrapper from './Wrapper.svelte';
</script>

<div>
    <Wrapper>
        <h1>Génération terminée</h1>

        <div class="lyrics-container">
            <p>
                {$lyrics}
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum officia saepe quidem quasi cum sunt necessitatibus, dolorum dolores vel, cumque deleniti.
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum officia saepe quidem quasi cum sunt necessitatibus, dolorum dolores vel, cumque deleniti.
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum officia saepe quidem quasi cum sunt necessitatibus, dolorum dolores vel, cumque deleniti.
            </p>
        </div>

        <button on:click|once={() => $step = 0}>Recommencer</button>
    </Wrapper>
</div>

<style>
    .lyrics-container {
        margin: 2.5em;
        border: 2px solid white;
        padding: 1em;
    }
    .lyrics-container > * {
        text-align: left;
    }
</style>