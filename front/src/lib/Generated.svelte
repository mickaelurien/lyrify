<script>
    import { step, lyrics } from '../store.js';
    import Wrapper from './Wrapper.svelte';
</script>

<div>
    <Wrapper>
        <h1>Génération terminée</h1>

        <div class="lyrics-container">
            {$lyrics}
        </div>

        <button on:click|once={() => $step = 0}>Recommencer</button>
    </Wrapper>
</div>

<style>
    .lyrics-container {
        margin: 2.5em;
        border: 2px solid white;
        padding: 1em;
        white-space: pre-line;
    }

    @media screen and (max-width: 768px) {
        .lyrics-container {
            margin: 0;
            padding: 0 0.5em;
            line-height: 1.2;
        }
    }
</style>