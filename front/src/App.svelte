<script>
  import { step, artist_choose } from './store.js';
  import Welcome from './lib/Welcome.svelte';
  import Artists from './lib/Artists.svelte';
  import Loading from './lib/Loading.svelte';
  import Generated from './lib/Generated.svelte';

  $: verifyStep($step);

  function verifyStep(step) {
    if (step === 2) {
      // TODO : Request python api with artist_choose and set result in $lyrics
      // $step = 3;
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

<style>
  
</style>
