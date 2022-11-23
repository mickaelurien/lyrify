<script>
    import { step } from '../store.js';
    import Wrapper from './Wrapper.svelte';
</script>

<div>
    <Wrapper>
        <h1>Bienvenue sur Lyrify !</h1>

        <p class="mt">Lyrify est un générateur de "lyrics".</p>
        <p>Choisissez un artiste parmi la liste,<br>
            puis un couplet sera généré dans son style
        </p>

        <button on:click|once={() => $step++}>Commencer</button>
    </Wrapper>
</div>

<style>
    p {
        text-align: center;
    }
</style>