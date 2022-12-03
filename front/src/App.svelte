<script>
  import { step, artist_choose, lyrics } from './store.js';
  import Welcome from './lib/Welcome.svelte';
  import Artists from './lib/Artists.svelte';
  import Loading from './lib/Loading.svelte';
  import Generated from './lib/Generated.svelte';
  import Footer from './lib/Footer.svelte';

  $: $step, verifyStep();

  async function verifyStep() {
    if ($step === 2) {
      const response = await fetch(import.meta.env.VITE_API_URL + `${$artist_choose}`);
      $lyrics = await response.json();
      $lyrics.replaceAll('\n', '<br>');
      console.log({$lyrics})
      $step++;
    }
  }
</script>

<main>
  <!-- TODO : Transition betweens each steps -->
  {#if $step === 0}
    <Welcome />
  {:else if $step === 1}
    <Artists />
  {:else if $step === 2}
    <Loading />
  {:else if $step === 3}
    <Generated />
  {/if}
</main>
<Footer />

<style>
  main {
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 1fr;
  }
  :global(main > *) {
    grid-column: 1;
    grid-row: 1;
  }
</style>
